# realtime_pipeline.py
# Consumes AppsFlyer-like events from Kafka, processes and stores to MongoDB

from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import time
from datetime import datetime

# MongoDB setup
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["streaming_db"]
hourly_collection = db["hourly_events"]
daily_collection = db["daily_events"]

# Kafka consumer setup
consumer = KafkaConsumer(
    'appsflyer-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True
)

# Buffer for aggregations
hourly_buffer = {}
daily_buffer = {}

def aggregate_event(event):
    event_time = datetime.strptime(event['timestamp'], "%Y-%m-%dT%H:%M:%S")
    campaign = event.get('campaign', 'unknown')

    hour_key = event_time.strftime("%Y-%m-%d %H:00")
    day_key = event_time.strftime("%Y-%m-%d")

    # Hourly aggregation
    if hour_key not in hourly_buffer:
        hourly_buffer[hour_key] = {}
    if campaign not in hourly_buffer[hour_key]:
        hourly_buffer[hour_key][campaign] = 0
    hourly_buffer[hour_key][campaign] += 1

    # Daily aggregation
    if day_key not in daily_buffer:
        daily_buffer[day_key] = {}
    if campaign not in daily_buffer[day_key]:
        daily_buffer[day_key][campaign] = 0
    daily_buffer[day_key][campaign] += 1

def flush_to_mongo():
    # Insert hourly aggregates
    for hour, campaigns in hourly_buffer.items():
        hourly_collection.update_one(
            {"hour": hour},
            {"$set": {"campaigns": campaigns}},
            upsert=True
        )
    hourly_buffer.clear()

    # Insert daily aggregates
    for day, campaigns in daily_buffer.items():
        daily_collection.update_one(
            {"day": day},
            {"$set": {"campaigns": campaigns}},
            upsert=True
        )
    daily_buffer.clear()

print("[INFO] Starting real-time data consumer...")
flush_interval = 60  # seconds
last_flush_time = time.time()

for message in consumer:
    event = message.value
    aggregate_event(event)

    if time.time() - last_flush_time > flush_interval:
        flush_to_mongo()
        last_flush_time = time.time()

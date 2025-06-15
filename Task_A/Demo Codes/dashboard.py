# dashboard.py

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from pymongo import MongoClient
import pandas as pd
import plotly.express as px
from datetime import datetime

# Khởi tạo ứng dụng Dash
app = Dash(__name__)
server = app.server

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["streaming_db"]
daily_collection = db["daily_events"]
hourly_collection = db["hourly_events"]

# Layout giao diện
app.layout = html.Div([
    html.H1("📊 Real-Time Marketing Campaign Dashboard", style={"textAlign": "center"}),

    dcc.Interval(id='interval', interval=30 * 1000, n_intervals=0),  # Auto-refresh mỗi 30 giây

    html.Div([
        html.Div(id='total-daily-installs', className='kpi-box'),
        html.Div(id='top-daily-campaign', className='kpi-box'),
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin': '20px'}),

    html.Div([
        html.H3("🕒 Hourly Campaign Installs"),
        dcc.Graph(id='hourly-graph'),
    ]),

    html.Div([
        html.H3("📆 Daily Campaign Summary"),
        dcc.Graph(id='daily-graph'),
    ]),

    html.Div(id='last-updated', style={"textAlign": "right", "fontStyle": "italic", "marginTop": "10px"})
])


@app.callback(
    Output('total-daily-installs', 'children'),
    Output('top-daily-campaign', 'children'),
    Output('hourly-graph', 'figure'),
    Output('daily-graph', 'figure'),
    Output('last-updated', 'children'),
    Input('interval', 'n_intervals')
)
def update_dashboard(n):
    try:
        # Fetch data từ MongoDB
        daily_docs = list(daily_collection.find())
        hourly_docs = list(hourly_collection.find())

        # Format dữ liệu Daily
        daily_data = []
        for doc in daily_docs:
            day = doc["day"]
            for campaign, count in doc["campaigns"].items():
                daily_data.append({"day": day, "campaign": campaign, "count": count})
        df_daily = pd.DataFrame(daily_data)
        df_daily["day"] = pd.to_datetime(df_daily["day"])

        # Format dữ liệu Hourly
        hourly_data = []
        for doc in hourly_docs:
            hour = doc["hour"]
            for campaign, count in doc["campaigns"].items():
                hourly_data.append({"hour": hour, "campaign": campaign, "count": count})
        df_hourly = pd.DataFrame(hourly_data)
        df_hourly["hour"] = pd.to_datetime(df_hourly["hour"])

        # KPI: tổng cài đặt hôm nay
        total_installs = int(df_daily["count"].sum())
        top_campaign = df_daily.groupby("campaign")["count"].sum().idxmax()

        kpi1 = html.H4(f"📦 Total Daily Installs: {total_installs:,}")
        kpi2 = html.H4(f"🏆 Top Campaign: {top_campaign}")

        # Biểu đồ Daily
        fig_daily = px.bar(
            df_daily.groupby(["day", "campaign"])["count"].sum().reset_index(),
            x="day", y="count", color="campaign",
            title="📆 Daily Campaign Performance"
        )

        # Biểu đồ Hourly
        fig_hourly = px.line(
            df_hourly.groupby(["hour", "campaign"])["count"].sum().reset_index(),
            x="hour", y="count", color="campaign",
            title="🕒 Hourly Installs per Campaign", markers=True
        )

        return (
            kpi1, kpi2,
            fig_hourly, fig_daily,
            f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

    except Exception as e:
        return html.H4("❌ No data available"), html.H4(""), {}, {}, str(e)


# Khởi chạy ứng dụng
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

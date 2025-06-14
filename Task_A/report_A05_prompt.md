---
title: real_time_streaming_data_pipeline_prompt
---

## Project Requirements Summary
<details - open>
<summary>Summarize the overall project requirements</summary>
---
- What are the key business and technical requirements for the real-time streaming data pipeline?
- Provide a formatted summary of these requirements.
---
</details>

## System Architecture Description
<details - open>
<summary>Describe the system architecture by layers</summary>
---
- Describe the Ingestion Layer including AppsFlyer API and Apache NiFi roles.
- Detail the Streaming Layer with Kafka topics `raw_events` and `enriched_events`.
- Explain the Processing Layer using Spark Streaming for sentiment analysis and aggregation.
- Outline the Storage Layer with MongoDB collections for enriched events and aggregated metrics.
- Summarize the Visualization Layer using Dash for real-time KPI dashboards.
- Describe the Infrastructure Layer with AWS EC2 and Docker Compose container orchestration.
---
</details>

## Component APIs and Data Flow
<details - open>
<summary>Explain APIs and data interactions for each component</summary>
---
- How does Apache NiFi use InvokeHTTP processor to fetch data and send to Kafka?
- What are the Kafka topic structures and message formats?
- How does Spark Streaming consume, process, and produce data streams?
- How is MongoDB structured for storing processed and aggregated data?
- How does Dash query MongoDB and present real-time visualizations?
---
</details>

## Documentation Compliance and Improvement
<details - open>
<summary>Evaluate current markdown documentation and suggest improvements</summary>
---
- Does the current markdown file meet all project requirements and documentation style guidelines?
- What percentage of requirements does it cover?
- What areas need improvement (e.g., Docker Compose config, sample API schemas, monitoring, alerting)?
- Suggest next steps for validation using Perplexity AI or similar tools.
---
</details>

## Project Customization and Similar Projects
<details - open>
<summary>Request similar projects and customization advice</summary>
---
- Provide examples of similar real-time streaming data pipeline projects.
- Suggest how to customize the current project to specific business needs.
- Recommend best practices for deployment, scaling, and monitoring.
---
</details>

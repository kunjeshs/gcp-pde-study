<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_13.json  (just the JSON, no backticks).
4. Repeat for every batch file, then run:  python tools/chatgpt-htt/ingest.py
Each batch is self-contained: you do not need previous batches in the same chat.
-->

You are a staff data engineer who coaches candidates through the GCP Professional Data Engineer exam. You write "How to Think" markdown that teaches the reasoning, not just the answer.
Output ONLY a JSON object mapping each question id to {"how_to_think": {"markdown": "..."}}.
No prose outside JSON. No code fences. No commentary. No trailing text.

Markdown structure per entry (match exactly, include EVERY section below):

## How to Think

This question is really asking:

- "<one-line plain-English rephrase>"

### Step 1: Spot the main clue

- The key clue is: <decisive phrases from stem, bold decisive words>.
- That points toward <GCP concept/service category>.

### Step 2: Match the clue to the GCP service/concept

- The concept is **<exact GCP service/feature>**.
- Exam angle: <one sentence why GCP picks this over alternatives>.

### Step 3: Eliminate traps

- **Option A** is tempting because <surface appeal> - but fails because <concrete GCP limitation: cost / latency / scale / IAM scope / consistency / region / batch-vs-stream>.
- **Option B** ... - but fails because ...
- **Option C** ... - but fails because ...
- (Skip the correct option.)

### Step 4: Choose the answer

- <one bullet naming the correct option's chosen service/feature and the single decisive reason it wins>.
- <one bullet tying it back to every requirement in the stem so it clearly satisfies all of them>.

### Exam shortcut

If you see:
- <distinctive signal 1 from the stem>
- <distinctive signal 2 from the stem>
- <distinctive signal 3 from the stem>

Think: **<exact GCP service/feature>**

**Tiny mental image:** <one vivid, concrete real-world analogy in a single sentence that makes the concept stick>.

**Final answer:** <letter>. <correct option text, verbatim from input>

Hard rules:
- Name real GCP services exact: BigQuery, Dataflow, Pub/Sub, Cloud Storage, Bigtable, Spanner, Composer, Dataproc, Dataplex, Cloud SQL, Memorystore, Vertex AI, Looker, Data Fusion.
- Every trap reason cites a concrete GCP limit, not generic advice.
- ALL of the sections above are mandatory: How to Think, Step 1, Step 2, Step 3, Step 4, Exam shortcut, Tiny mental image, Final answer.
- The "Exam shortcut" signals must be reusable pattern cues (the kind that recur across questions), not a paraphrase of this one stem.
- The "Tiny mental image" must be a relatable analogy, max one sentence, not a restatement of the service definition.
- "Final answer" must use the correct option's letter and text verbatim from the input.
- Max 280 words per entry.
- No "in conclusion" filler. No content after the Final answer line.
- Use option letters and text from input verbatim.


Generate how_to_think for the 20 questions below. Return a SINGLE JSON object mapping each id -> {"how_to_think": {"markdown": "..."}}. Include an entry for every one of these ids and nothing else:
test_13_q22, test_13_q27, test_13_q33, test_13_q35, test_13_q40, test_13_q41, test_13_q43, test_13_q45, test_13_q47, test_13_q51, test_13_q54, test_13_q55, test_13_q57, test_13_q59, test_14_q4, test_14_q8, test_14_q11, test_14_q21, test_14_q29, test_14_q30

Questions:

[
 {
  "id": "test_13_q22",
  "q": "Scenario: A SQL pipeline needs to be set up to perform an aggregate SQL transformation on a BigQuery table every two hours, appending the result to another existing BigQuery table. The pipeline should be configured to retry in case of errors, and an email notification should be sent after three consecutive failures. How should you configure the SQL pipeline to retry in case of errors and send an email notification after three consecutive failures?",
  "opts": {
   "A": "Use the BigQueryUpsertTableOperator in Cloud Composer, set the retry parameter to three, and set the email_on_failure parameter to true.",
   "B": "Use the BigQueryInsertJobOperator in Cloud Composer, set the retry parameter to three, and set the email_on_failure parameter to true.",
   "C": "Create a BigQuery scheduled query to run the SQL transformation with schedule options that repeats every two hours, and enable email notifications.",
   "D": "Create a BigQuery scheduled query to run the SQL transformation with schedule options that repeats every two hours, and enable notification to Pub/Sub topic. Use Pub/Sub and Cloud Functions to send an email after three failed executions."
  },
  "correct": "D",
  "correct_text": "Create a BigQuery scheduled query to run the SQL transformation with schedule options that repeats every two hours, and enable notification to Pub/Sub topic. Use Pub/Sub and Cloud Functions to send an email after three…",
  "base": "Let’s analyze each option to determine the best approach for configuring the SQL pipeline with retries and email notifications: Use the BigQueryUpsertTableOperator in Cloud Composer, set the retry parameter to three, and set the email_on_failure parameter to true. While Cloud Composer is a powerful…"
 },
 {
  "id": "test_13_q27",
  "q": "Scenario: Your organization currently stores customer data in an on-premises Apache Hadoop cluster in Apache Parquet format. The data is processed daily by Apache Spark jobs running on the cluster. You are planning to migrate the Spark jobs and Parquet data to Google Cloud. As BigQuery will be utilized in future transformation pipelines, you aim to have the data available in BigQuery. Your goal is to leverage managed services, reduce ETL data processing modifications, and minimize overhead costs. What steps should be taken to achieve this objective?",
  "opts": {
   "A": "Migrate your data to Cloud Storage and migrate the metadata to Dataproc Metastore (DPMS). Refactor Spark pipelines to write and read data on Cloud Storage, and run them on Dataproc Serverless.",
   "B": "Migrate your data to Cloud Storage and register the bucket as a Dataplex asset. Refactor Spark pipelines to write and read data on Cloud Storage, and run them on Dataproc Serverless.",
   "C": "Migrate your data to BigQuery. Refactor Spark pipelines to write and read data on BigQuery, and run them on Dataproc Serverless.",
   "D": "Migrate your data to BigLake. Refactor Spark pipelines to write and read data on Cloud Storage, and run them on Dataproc on Compute Engine."
  },
  "correct": "C",
  "correct_text": "Migrate your data to BigQuery. Refactor Spark pipelines to write and read data on BigQuery, and run them on Dataproc Serverless.",
  "base": "Correct Option C. Migrate your data to BigQuery. Refactor Spark pipelines to write and read data on BigQuery, and run them on Dataproc Serverless Correct because: BigQuery natively supports Parquet ingestion and provides ANSI SQL for analysis. Migrating directly to BigQuery minimizes ETL modificati…"
 },
 {
  "id": "test_13_q33",
  "q": "Scenario: You are constructing a streaming Dataflow pipeline to collect noise level data from numerous sensors near construction sites in a city. The sensors transmit noise level readings every ten seconds to the pipeline when the levels exceed 70 dBA. What steps should you take to calculate the average noise level from a sensor when data is available for over 30 minutes, but the window closes if no data is received for 15 minutes?",
  "opts": {
   "A": "Use session windows with a 15-minute gap duration.",
   "B": "Use session windows with a 30-minute gap duration.",
   "C": "Use hopping windows with a 15-minute window, and a thirty-minute period.",
   "D": "Use tumbling windows with a 15-minute window and a fifteen-minute .withAllowedLateness operator."
  },
  "correct": "A",
  "correct_text": "Use session windows with a 15-minute gap duration.",
  "base": "A. Use session windows with a 15-minute gap duration.Explanation why A is correct:– Using session windows with a 15-minute gap duration is the correct approach for this scenario because it allows you to define windows based on periods of activity (data being received) and inactivity (no data being…"
 },
 {
  "id": "test_13_q35",
  "q": "Scenario: You have developed an updated version of a Dataflow streaming data ingestion pipeline that extracts data from Pub/Sub and loads it into BigQuery. The current production pipeline operates on a 5-minute window for processing. How can you implement the deployment of the new pipeline version without risking data loss, inconsistencies, or a processing latency increase exceeding 10 minutes?",
  "opts": {
   "A": "Update the old pipeline with the new pipeline code.",
   "B": "Snapshot the old pipeline, stop the old pipeline, and then start the new pipeline from the snapshot.",
   "C": "Drain the old pipeline, then start the new pipeline.",
   "D": "Cancel the old pipeline, then start the new pipeline."
  },
  "correct": "C",
  "correct_text": "Drain the old pipeline, then start the new pipeline.",
  "base": "C. Drain the old pipeline, then start the new pipeline.Draining the old pipeline involves allowing all the existing data to be processed and ensuring that no new data is being ingested before starting the new pipeline. This ensures that all the data in the existing pipeline is processed before swit…"
 },
 {
  "id": "test_13_q40",
  "q": "Scenario: You have set up an analytics environment on Google Cloud to enable your data scientist team to analyze data without disrupting the on-premises Apache Hadoop system. The data in the on-premises Hadoop Distributed File System (HDFS) cluster is stored in Optimized Row Columnar (ORC) formatted files with multiple columns of Hive partitioning. What is the most cost-effective storage and processing solution for allowing the data scientist team to explore the data similarly to how they did on the on-premises HDFS cluster with SQL on the Hive query engine?",
  "opts": {
   "A": "Import the ORC files to Bigtable tables for the data scientist team.",
   "B": "Import the ORC files to BigQuery tables for the data scientist team.",
   "C": "Copy the ORC files on Cloud Storage, then deploy a Dataproc cluster for the data scientist team.",
   "D": "Copy the ORC files on Cloud Storage, then create external BigQuery tables for the data scientist team."
  },
  "correct": "D",
  "correct_text": "Copy the ORC files on Cloud Storage, then create external BigQuery tables for the data scientist team.",
  "base": "The correct answer is D. Copy the ORC files on Cloud Storage, then create external BigQuery tables for the data scientist team.– Since the data in the on-premises HDFS cluster is in ORC format with Hive partitioning, copying these ORC files to Cloud Storage would be a suitable solution as Cloud Sto…"
 },
 {
  "id": "test_13_q41",
  "q": "Scenario: When designing a Dataflow pipeline for a batch processing job, you aim to address potential zonal failures during job submission. What steps should be taken to mitigate multiple zonal failures at job submission time in the Dataflow pipeline?",
  "opts": {
   "A": "Submit duplicate pipelines in two different zones by using the --zone flag.",
   "B": "Set the pipeline staging location as a regional Cloud Storage bucket.",
   "C": "Specify a worker region by using the --region flag.",
   "D": "Create an Eventarc trigger to resubmit the job in case of zonal failure when submitting the job."
  },
  "correct": "C",
  "correct_text": "Specify a worker region by using the --region flag.",
  "base": "The correct answer is C. Specify a worker region by using the –region flag.By specifying a worker region using the –region flag, you ensure that the Dataflow job‘s worker instances are created in the specified region. This helps mitigate multiple zonal failures at job submission time because the wo…"
 },
 {
  "id": "test_13_q43",
  "q": "Scenario: Your car factory is pushing machine measurements as messages into a Pub/Sub topic in your Google Cloud project. A Dataflow streaming job, created using the Apache Beam SDK, processes these messages, sends acknowledgments to Pub/Sub, applies custom business logic in a DoFn instance, and stores the results in BigQuery. How can you set up a mechanism to route messages to a specific Pub/Sub topic for alerting if the custom business logic fails during processing?",
  "opts": {
   "A": "Enable retaining of acknowledged messages in your Pub/Sub pull subscription. Use Cloud Monitoring to monitor the subscription/num_retained_acked_messages metric on this subscription.",
   "B": "Use an exception handling block in your Dataflows DoFn code to push the messages that failed to be transformed through a side output and to a new Pub/Sub topic. Use Cloud Monitoring to monitor the topic/num_unacked_messages_by_region metric on this new topic.",
   "C": "Enable dead lettering in your Pub/Sub pull subscription, and specify a new Pub/Sub topic as the dead letter topic. Use Cloud Monitoring to monitor the subscription/dead_letter_message_count metric on your pull subscription.",
   "D": "Create a snapshot of your Pub/Sub pull subscription. Use Cloud Monitoring to monitor the snapshot/num_messages metric on this snapshot."
  },
  "correct": "B",
  "correct_text": "Use an exception handling block in your Dataflows DoFn code to push the messages that failed to be transformed through a side output and to a new Pub/Sub topic. Use Cloud Monitoring to monitor the topic/num_unacked_mes…",
  "base": "The correct answer is B. Here‘s an explanation of why option B is the correct choice and why the other options are incorrect:B. Use an exception handling block in your Dataflows DoFn code to push the messages that failed to be transformed through a side output and to a new Pub/Sub topic. Use Cloud…"
 },
 {
  "id": "test_13_q45",
  "q": "Scenario: You are running a streaming pipeline with Dataflow and are utilizing hopping windows to group the data as it arrives. Some data is arriving late but is not being identified as late data, leading to incorrect aggregations downstream. What steps should you take to address this issue and capture the late data in the correct window?",
  "opts": {
   "A": "Use watermarks to define the expected data arrival window. Allow late data as it arrives.",
   "B": "Change your windowing function to tumbling windows to avoid overlapping window periods.",
   "C": "Change your windowing function to session windows to define your windows based on certain activity.",
   "D": "Expand your hopping window so that the late data has more time to arrive within the grouping."
  },
  "correct": "A",
  "correct_text": "Use watermarks to define the expected data arrival window. Allow late data as it arrives.",
  "base": "A. Use watermarks to define the expected data arrival window. Allow late data as it arrives.Using watermarks in Dataflow allows you to define the expected data arrival window. Watermarks are timestamps that represent the progress of event time in your data. By setting watermarks, you can specify th…"
 },
 {
  "id": "test_13_q47",
  "q": "Scenario: A Dataflow streaming job reads messages from a message bus lacking exactly-once delivery support, applies transformations, and loads the result into BigQuery. How can you ensure that data is streamed into BigQuery with exactly-once delivery semantics at an ingestion throughput of approximately 1.5 GB per second?",
  "opts": {
   "A": "Use the BigQuery Storage Write API and ensure that your target BigQuery table is regional.",
   "B": "Use the BigQuery Storage Write API and ensure that your target BigQuery table is multiregional.",
   "C": "Use the BigQuery Streaming API and ensure that your target BigQuery table is regional.",
   "D": "Use the BigQuery Streaming API and ensure that your target BigQuery table is multiregional."
  },
  "correct": "A",
  "correct_text": "Use the BigQuery Storage Write API and ensure that your target BigQuery table is regional.",
  "base": "A. Use the BigQuery Storage Write API and ensure that your target BigQuery table is regional.– The BigQuery Storage Write API allows you to stream data into BigQuery with exactly-once delivery semantics. By using this API, you can ensure that each record is written to BigQuery exactly once.– Choosi…"
 },
 {
  "id": "test_13_q51",
  "q": "Scenario: You have numerous Apache Spark jobs running on your on-premises Apache Hadoop cluster. You are looking to transition these jobs to Google Cloud and opt for managed services to handle job execution instead of managing a persistent Hadoop cluster. With a limited timeframe and the goal to minimize code modifications, you seek guidance on the best course of action. What steps should be taken to efficiently migrate Apache Spark jobs from an on-premises Apache Hadoop cluster to Google Cloud using managed services, while minimizing code alterations within a tight timeline?",
  "opts": {
   "A": "Move your data to BigQuery. Convert your Spark scripts to a SQL-based processing approach.",
   "B": "Rewrite your jobs in Apache Beam. Run your jobs in Dataflow.",
   "C": "Copy your data to Compute Engine disks. Manage and run your jobs directly on those instances.",
   "D": "Move your data to Cloud Storage. Run your jobs on Dataproc."
  },
  "correct": "D",
  "correct_text": "Move your data to Cloud Storage. Run your jobs on Dataproc.",
  "base": "The correct answer is D. Move your data to Cloud Storage and run your jobs on Dataproc.Moving data to Cloud Storage: Cloud Storage is a scalable and durable object storage service provided by Google Cloud. It is highly available and can handle large amounts of data. By moving your data to Cloud Sto…"
 },
 {
  "id": "test_13_q54",
  "q": "Scenario: Data in BigQuery is used to generate reports for your company, but some fields in the weekly executive reports do not adhere to company standards, such as varying telephone formats and country code identifiers. How can you create a recurring job to normalize the data without requiring any coding for a quick solution?",
  "opts": {
   "A": "Use Cloud Data Fusion and Wrangler to normalize the data, and set up a recurring job.",
   "B": "Use Dataflow SQL to create a job that normalizes the data, and that after the first run of the job, schedule the pipeline to execute recurrently.",
   "C": "Create a Spark job and submit it to Dataproc Serverless.",
   "D": "Use BigQuery and GoogleSQL to normalize the data, and schedule recurring queries in BigQuery."
  },
  "correct": "A",
  "correct_text": "Use Cloud Data Fusion and Wrangler to normalize the data, and set up a recurring job.",
  "base": "A. Use Cloud Data Fusion and Wrangler to normalize the data, and set up a recurring job.– Cloud Data Fusion is a fully managed, cloud-native data integration service that helps to efficiently build and manage ETL/ELT data pipelines. It provides a visual interface for building data pipelines without…"
 },
 {
  "id": "test_13_q55",
  "q": "Scenario: You are setting up a messaging system using Pub/Sub for processing clickstream data with an event-driven consumer app that uses a push subscription. The system needs to be reliable during temporary downtime of the consumer app and store unprocessed messages. It should also retry failed messages gradually and store them in a topic after a maximum of 10 retries. How should the Pub/Sub subscription be configured to meet the system requirements described above?",
  "opts": {
   "A": "Increase the acknowledgement deadline to 10 minutes.",
   "B": "Use immediate redelivery as the subscription retry policy, and configure dead lettering to a different topic with maximum delivery attempts set to 10.",
   "C": "Use exponential backoff as the subscription retry policy, and configure dead lettering to the same source topic with maximum delivery attempts set to 10.",
   "D": "Use exponential backoff as the subscription retry policy, and configure dead lettering to a different topic with maximum delivery attempts set to 10."
  },
  "correct": "D",
  "correct_text": "Use exponential backoff as the subscription retry policy, and configure dead lettering to a different topic with maximum delivery attempts set to 10.",
  "base": "The correct answer is D. Use exponential backoff as the subscription retry policy, and configure dead lettering to a different topic with maximum delivery attempts set to 10.1. Using exponential backoff as the subscription retry policy ensures that failed messages are retried with increasing time i…"
 },
 {
  "id": "test_13_q57",
  "q": "Scenario: You have terabytes of customer behavioral data streaming from Google Analytics into BigQuery daily. Your customers information, such as their preferences, is hosted on a Cloud SQL for MySQL database. Your CRM database is hosted on a Cloud SQL for PostgreSQL instance. The marketing team wants to use your customers information from the two databases and the customer behavioral data to create marketing campaigns for yearly active customers. You need to ensure that the marketing team can run the campaigns over 100 times a day on typical days and up to 300 during sales. At the same time, you want to keep the load on the Cloud SQL databases to a minimum. What should you do?",
  "opts": {
   "A": "Create BigQuery connections to both Cloud SQL databases. Use BigQuery federated queries on the two databases and the Google Analytics data on BigQuery to run these queries.",
   "B": "Create a job on Apache Spark with Dataproc Serverless to query both Cloud SQL databases and the Google Analytics data on BigQuery for these queries.",
   "C": "Create streams in Datastream to replicate the required tables from both Cloud SQL databases to BigQuery for these queries.",
   "D": "Create a Dataproc cluster with Trino to establish connections to both Cloud SQL databases and BigQuery, to execute the queries."
  },
  "correct": "C",
  "correct_text": "Create streams in Datastream to replicate the required tables from both Cloud SQL databases to BigQuery for these queries.",
  "base": "The correct answer is C. Create streams in Datastream to replicate the required tables from both Cloud SQL databases to BigQuery for these queries.By using Datastream to replicate the required tables from both Cloud SQL databases to BigQuery, you can create a centralized location for the data that…"
 },
 {
  "id": "test_13_q59",
  "q": "Scenario: Your infrastructure team has established an interconnect link connecting Google Cloud and the on-premises network. You are tasked with creating a high-throughput streaming pipeline to continuously ingest data from an Apache Kafka cluster located on-premises. How can you efficiently store the streaming data in BigQuery with minimal latency?",
  "opts": {
   "A": "Setup a Kafka Connect bridge between Kafka and Pub/Sub. Use a Google-provided Dataflow template to read the data from Pub/Sub, and write the data to BigQuery.",
   "B": "Use a proxy host in the VPC in Google Cloud connecting to Kafka. Write a Dataflow pipeline, read data from the proxy host, and write the data to BigQuery.",
   "C": "Use Dataflow, write a pipeline that reads the data from Kafka, and writes the data to BigQuery.",
   "D": "Setup a Kafka Connect bridge between Kafka and Pub/Sub. Write a Dataflow pipeline, read the data from Pub/Sub, and write the data to BigQuery."
  },
  "correct": "C",
  "correct_text": "Use Dataflow, write a pipeline that reads the data from Kafka, and writes the data to BigQuery.",
  "base": "The correct answer is C. Use Dataflow, write a pipeline that reads the data from Kafka, and writes the data to BigQuery.– Using Dataflow to read data directly from Kafka and write it to BigQuery is the most efficient approach in this scenario to achieve minimal latency. Dataflow is a fully managed…"
 },
 {
  "id": "test_14_q4",
  "q": "Scenario: You have created an Apache Beam processing pipeline that reads from a Pub/Sub topic with a one-day message retention duration and writes to a Cloud Storage bucket. What actions should you take to choose a bucket location and processing strategy that can avoid data loss during a regional outage with a Recovery Point Objective (RPO) of 15 minutes?",
  "opts": {
   "A": "1. Use a dual-region Cloud Storage bucket. 2. Monitor Dataflow metrics with Cloud Monitoring to determine when an outage occurs. 3. Seek the subscription back in time by 15 minutes to recover the acknowledged messages. 4. Start the Dataflow job in a secondary region.",
   "B": "1. Use a multi-regional Cloud Storage bucket. 2. Monitor Dataflow metrics with Cloud Monitoring to determine when an outage occurs. 3. Seek the subscription back in time by 60 minutes to recover the acknowledged messages. 4. Start the Dataflow job in a secondary region.",
   "C": "1. Use a regional Cloud Storage bucket. 2. Monitor Dataflow metrics with Cloud Monitoring to determine when an outage occurs. 3. Seek the subscription back in time by one day to recover the acknowledged messages. 4. Start the Dataflow job in a secondary region and write in a bucket in the same region.",
   "D": "1. Use a dual-region Cloud Storage bucket with turbo replication enabled. 2. Monitor Dataflow metrics with Cloud Monitoring to determine when an outage occurs. 3. Seek the subscription back in time by 60 minutes to recover the acknowledged messages. 4. Start the Dataflow job in a secondary region."
  },
  "correct": "D",
  "correct_text": "1. Use a dual-region Cloud Storage bucket with turbo replication enabled. 2. Monitor Dataflow metrics with Cloud Monitoring to determine when an outage occurs. 3. Seek the subscription back in time by 60 minutes to reco…",
  "base": "The correct answer is D. Here‘s why: 1. Use a dual-region Cloud Storage bucket with turbo replication enabled: A dual-region Cloud Storage bucket provides redundancy across two regions, which helps in preventing data loss in case of a regional outage. Enabling turbo replication ensures that data is…"
 },
 {
  "id": "test_14_q8",
  "q": "Scenario: CSV files are being loaded from Cloud Storage to BigQuery. The files contain known data quality issues, like mixed data types within the same column and inconsistent formatting of values like phone numbers or addresses. What steps should be taken to create a data pipeline that ensures data quality, and performs the necessary cleansing and transformation?",
  "opts": {
   "A": "Use Data Fusion to transform the data before loading it into BigQuery.",
   "B": "Use Data Fusion to convert the CSV files to a self-describing data format, such as AVRO, before loading the data to BigQuery.",
   "C": "Load the CSV files into a staging table with the desired schema, perform the transformations with SQL, and then write the results to the final destination table.",
   "D": "Create a table with the desired schema, load the CSV files into the table, and perform the transformations in place using SQL."
  },
  "correct": "A",
  "correct_text": "Use Data Fusion to transform the data before loading it into BigQuery.",
  "base": "A. Use Data Fusion to transform the data before loading it into BigQuery.Using Data Fusion to transform the data before loading it into BigQuery is the correct approach in this scenario for the following reasons:1. Data Fusion is a fully managed, cloud-native data integration service that enables y…"
 },
 {
  "id": "test_14_q11",
  "q": "Scenario: An aerospace company utilizes a unique data format to store its flight data. The task is to link this new data source to BigQuery and stream the data into the platform. How can you effectively import the data into BigQuery while minimizing resource consumption?",
  "opts": {
   "A": "Write a shell script that triggers a Cloud Function that performs periodic ETL batch jobs on the new data source.",
   "B": "Use a standard Dataflow pipeline to store the raw data in BigQuery, and then transform the format later when the data is used.",
   "C": "Use Apache Hive to write a Dataproc job that streams the data into BigQuery in CSV format.",
   "D": "Use an Apache Beam custom connector to write a Dataflow pipeline that streams the data into BigQuery in Avro format."
  },
  "correct": "D",
  "correct_text": "Use an Apache Beam custom connector to write a Dataflow pipeline that streams the data into BigQuery in Avro format.",
  "base": "The correct answer is D. Use an Apache Beam custom connector to write a Dataflow pipeline that streams the data into BigQuery in Avro format.Using an Apache Beam custom connector to write a Dataflow pipeline is the most efficient way to import the proprietary flight data into BigQuery while consumi…"
 },
 {
  "id": "test_14_q21",
  "q": "Scenario: You aim to develop a machine learning model with BigQuery ML and establish an endpoint for hosting the model with Vertex AI. This setup will facilitate the handling of continuous streaming data in near-real time from various vendors, which might include invalid values. What steps should be taken in this scenario to address the presence of potentially invalid values in the data stream?",
  "opts": {
   "A": "Create a new BigQuery dataset and use streaming inserts to land the data from multiple vendors. Configure your BigQuery ML model to use the “ingestion“ dataset as the framing data.",
   "B": "Use BigQuery streaming inserts to land the data from multiple vendors where your BigQuery dataset ML model is deployed.",
   "C": "Create a Pub/Sub topic and send all vendor data to it. Connect a Cloud Function to the topic to process the data and store it in BigQuery.",
   "D": "Create a Pub/Sub topic and send all vendor data to it. Use Dataflow to process and sanitize the Pub/Sub data and stream it to BigQuery."
  },
  "correct": "D",
  "correct_text": "Create a Pub/Sub topic and send all vendor data to it. Use Dataflow to process and sanitize the Pub/Sub data and stream it to BigQuery.",
  "base": "The correct answer is D. Create a Pub/Sub topic and send all vendor data to it. Use Dataflow to process and sanitize the Pub/Sub data and stream it to BigQuery.Explanation of why option D is correct:– Creating a Pub/Sub topic allows for decoupling the data ingestion from the processing, enabling as…"
 },
 {
  "id": "test_14_q29",
  "q": "Scenario: You need to schedule a series of sequential load and transformation jobs. Data files are uploaded to a Cloud Storage bucket unpredictably by an upstream process. Subsequently, a Dataproc job is initiated to execute transformations and store the data in BigQuery. Following this, multiple distinct transformation jobs need to be run in BigQuery, with varying durations. Your goal is to establish an effective and sustainable workflow to process numerous tables and deliver up‑to‑date data to end users. How can you efficiently and reliably manage the workflow for processing hundreds of tables and ensuring the freshest data for end users?",
  "opts": {
   "A": "1. Create an Apache Airflow directed acyclic graph (DAG) in Cloud Composer with sequential tasks by using the Cloud Storage, Dataproc, and BigQuery operators. 2. Use a single shared DAG for all tables that need to go through the pipeline. 3. Schedule the DAG to run hourly.",
   "B": "1. Create an Apache Airflow directed acyclic graph (DAG) in Cloud Composer with sequential tasks by using the Cloud Storage, Dataproc, and BigQuery operators. 2. Create a separate DAG for each table that needs to go through the pipeline. 3. Schedule the DAGs to run hourly.",
   "C": "1. Create an Apache Airflow directed acyclic graph (DAG) in Cloud Composer with sequential tasks by using the Dataproc and BigQuery operators. 2. Use a single shared DAG for all tables that need to go through the pipeline. 3. Use a Cloud Storage object trigger to launch a Cloud Function that triggers the DAG.",
   "D": "1. Create an Apache Airflow directed acyclic graph (DAG) in Cloud Composer with sequential tasks by using the Dataproc and BigQuery operators. 2. Create a separate DAG for each table that needs to go through the pipeline. 3. Use a Cloud Storage object trigger to launch a Cloud Function that triggers the DAG."
  },
  "correct": "D",
  "correct_text": "1. Create an Apache Airflow directed acyclic graph (DAG) in Cloud Composer with sequential tasks by using the Dataproc and BigQuery operators. 2. Create a separate DAG for each table that needs to go through the pipelin…",
  "base": "Correct Option D. Create an Apache Airflow directed acyclic graph (DAG) in Cloud Composer with sequential tasks by using the Dataproc and BigQuery operators. Create a separate DAG for each table that needs to go through the pipeline. Use a Cloud Storage object trigger to launch a Cloud Function tha…"
 },
 {
  "id": "test_14_q30",
  "q": "Scenario: You have a streaming pipeline that is currently ingesting data from Pub/Sub in production. You are required to enhance the business logic of this streaming pipeline. It is essential to make sure that the updated pipeline can reprocess the Pub/Sub messages delivered in the last two days. What steps should you take to achieve this? (Select two options.)",
  "opts": {
   "A": "Use the Pub/Sub subscription clear-retry-policy flag",
   "B": "Use Pub/Sub Snapshot capture two days before the deployment.",
   "C": "Create a new Pub/Sub subscription two days before the deployment.",
   "D": "Use the Pub/Sub subscription retain-acked-messages flag.",
   "E": "Use Pub/Sub Seek with a timestamp."
  },
  "correct": "D",
  "correct_text": "Use the Pub/Sub subscription retain-acked-messages flag.",
  "base": "Correct Option D. Use the Pub/Sub subscription retain‑acked‑messages flag This is correct. By enabling the retain-acked-messages flag, Pub/Sub will retain acknowledged messages for a defined retention period (up to 7 days). This allows you to reprocess messages that were already delivered and ackno…"
 }
]

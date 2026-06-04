<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_08.json  (just the JSON, no backticks).
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
test_3_q29, test_3_q30, test_3_q31, test_3_q34, test_3_q36, test_3_q37, test_3_q41, test_3_q44, test_3_q46, test_3_q47, test_3_q48, test_3_q50, test_4_q2, test_4_q3, test_4_q4, test_4_q8, test_4_q15, test_4_q23, test_4_q24, test_4_q25

Questions:

[
 {
  "id": "test_3_q29",
  "q": "How can you speed up a Dataflow pipeline that ingests and transforms compressed gzip text files, uses SideInputs to join data, and writes errors to a dead-letter queue?",
  "opts": {
   "A": "Change to using compressed Avro files instead of gzip",
   "B": "Decrease the batch size used in the pipeline.",
   "C": "Implement a retry mechanism for records that encounter errors",
   "D": "Replace the SideInput with CoGroupByKey to improve performance."
  },
  "correct": "D",
  "correct_text": "Replace the SideInput with CoGroupByKey to improve performance.",
  "base": "The CoGroupByKey transform is a core Beam transform that merges (flattens) multiple PCollection objects and groups elements that have a common key. Unlike a side input, which makes the entire side input data available to each worker, CoGroupByKey performs a shuffle (grouping) operation to distribut…"
 },
 {
  "id": "test_3_q30",
  "q": "Your organization is looking to optimize its batch pipeline for processing structured data on Google Cloud. Currently, you are using PySpark for data transformations, but your pipelines are taking more than 12 hours to run. You need a serverless solution that can support SQL syntax to expedite development and pipeline run time. Your raw data is already stored in Cloud Storage. Which approach should you take to build your pipeline on Google Cloud while meeting your performance and processing requirements?",
  "opts": {
   "A": "Convert your PySpark commands into SparkSQL queries to transform the data and use Dataproc to write the data into BigQuery.",
   "B": "Ingest your data into Cloud SQL, convert your PySpark commands into SparkSQL queries to transform the data, and then use federated queries from BigQuery for machine learning",
   "C": "Ingest your data into BigQuery from Cloud Storage, convert your PySpark commands into BigQuery SQL queries to transform the data, and then write the transformations to a new table",
   "D": "Use the Apache Beam Python SDK to build the transformation pipelines and write the data into BigQuery."
  },
  "correct": "C",
  "correct_text": "Ingest your data into BigQuery from Cloud Storage, convert your PySpark commands into BigQuery SQL queries to transform the data, and then write the transformations to a new table",
  "base": "BigQuery is an option to meet the performance and processing requirements. Ref: https://medium.com/paypal-tech/comparing-bigquery-processing-and-spark-dataproc-4c90c10e31ac"
 },
 {
  "id": "test_3_q31",
  "q": "You are managing an Apache Kafka-based IoT pipeline that receives 5000 messages per second. You need to set up an alert that will notify you if the moving average over one hour falls below 4000 messages per second. Which approach should you take using Google Cloud Platform?",
  "opts": {
   "A": "Consume the stream of data in Dataflow using Kafka IO, set a sliding time window of 1 hour every 5 minutes, compute the average when the window closes, and send an alert if the average is less than 4000 messages per second",
   "B": "Consume the stream of data in Dataflow using Kafka IO, set a fixed time window of 1 hour, compute the average when the window closes, and send an alert if the average is less than 4000 messages per second.",
   "C": "Use Kafka Connect to link Kafka to Pub/Sub, write messages to Bigtable using a Dataflow template, use Cloud Scheduler to count the number of rows in Bigtable created in the last hour, and send an alert if the count is less than 4000.",
   "D": "Use Kafka Connect to link Kafka to Pub/Sub, write messages to BigQuery using a Dataflow template, use Cloud Scheduler to count the number of rows in BigQuery created in the last hour, and send an alert if the count is less than 4000."
  },
  "correct": "A",
  "correct_text": "Consume the stream of data in Dataflow using Kafka IO, set a sliding time window of 1 hour every 5 minutes, compute the average when the window closes, and send an alert if the average is less than 4000 messages per sec…",
  "base": "Option A is the best approach for this scenario. Using Dataflow with Kafka IO, you can consume the stream of data and set a sliding time window of 1 hour every 5 minutes to compute the moving average. When the window closes, if the average is less than 4000 messages per second, an alert can be sent…"
 },
 {
  "id": "test_3_q34",
  "q": "How can you address a disk I/O intensive Hadoop job running slowly with Cloud Dataproc in a managed Hadoop system that uses Cloud Storage connector for storing input, output, and intermediary data?",
  "opts": {
   "A": "Increase the memory allocation of the Hadoop cluster to hold the intermediary data of the slow Hadoop job in memory",
   "B": "Allocate enough persistent disk space to the Hadoop cluster and store the intermediate data of the slow Hadoop job on native Hadoop Distributed File System (HDFS)",
   "C": "Increase the CPU cores of the virtual machine instances of the Hadoop cluster to scale up networking bandwidth for each instance",
   "D": "Allocate additional network interface cards (NICs), and set up link aggregation in the operating system to use the combined throughput while working with Cloud Storage."
  },
  "correct": "B",
  "correct_text": "Allocate enough persistent disk space to the Hadoop cluster and store the intermediate data of the slow Hadoop job on native Hadoop Distributed File System (HDFS)",
  "base": "Allocate sufficient persistent disk space to the Hadoop cluster, and store the intermediate data of that particular Hadoop job on native HDFS: This option could work if the issue is related to the Cloud Storage connector being slow or not optimized for the specific workload. By storing the intermed…"
 },
 {
  "id": "test_3_q36",
  "q": "What service should you use to manage several batch jobs that have interdependent steps to be executed in a specific order and involve running shell scripts, Hadoop jobs, and BigQuery queries. These jobs are expected to run for many minutes up to several hours, and if the steps fail, they must be retried a fixed number of times. Choose the correct option?",
  "opts": {
   "A": "Use Cloud Scheduler to schedule and run the batch jobs",
   "B": "Use Cloud Dataflow to manage the execution of the batch jobs",
   "C": "Use Cloud Functions to manage the execution of the batch jobs",
   "D": "Use Cloud Composer to orchestrate and manage the execution of the batch jobs"
  },
  "correct": "D",
  "correct_text": "Use Cloud Composer to orchestrate and manage the execution of the batch jobs",
  "base": "Option D (Cloud Composer) is a Fully managed workflow orchestration service that allows you to define, schedule, and monitor complex workflows consisting of multiple tasks with dependencies and retries. It is a suitable option for managing the execution of batch jobs with many interdependent steps…"
 },
 {
  "id": "test_3_q37",
  "q": "You are migrating an on-premises Hadoop system that uses ORC data format and Hive as the primary tool to Cloud Dataproc. You have successfully copied all ORC files to a Cloud Storage bucket, and you need to replicate some data to the cluster‘s local Hadoop Distributed File System (HDFS) to improve performance. Which of the following are two ways to start using Hive in Cloud Dataproc (Choose two)?",
  "opts": {
   "A": "Transfer all ORC files from the Cloud Storage bucket to HDFS using the gsutil utility, and mount the Hive tables locally.",
   "B": "Transfer all ORC files from the Cloud Storage bucket to any node of the Dataproc cluster using the gsutil utility, and mount the Hive tables locally.",
   "C": "Transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster using the gsutil utility, run the Hadoop utility to copy them to HDFS, and mount the Hive tables from HDFS.",
   "D": "Use the Cloud Storage connector for Hadoop to mount the ORC files as external Hive tables, and replicate the external Hive tables to the native ones",
   "E": "Load the ORC files into BigQuery, use the BigQuery connector for Hadoop to mount the BigQuery tables as external Hive tables, and replicate the external Hive tables to the native ones."
  },
  "correct": "C",
  "correct_text": "Transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster using the gsutil utility, run the Hadoop utility to copy them to HDFS, and mount the Hive tables from HDFS.",
  "base": "Option C is a valid solution, but it involves extra steps, such as manually copying the files to HDFS, that can be avoided. Option D is a valid solution because it leverages the Cloud Storage connector for Hadoop to mount the ORC files as external Hive tables and then replicates the external Hive t…"
 },
 {
  "id": "test_3_q41",
  "q": "You have a Dataflow pipeline that writes time series metrics to Bigtable. However, you have noticed that the data is slow to update in Bigtable, which is used to feed a dashboard with thousands of concurrent users. You need to support more concurrent users while reducing the time it takes to write the data. What are two actions you should take?",
  "opts": {
   "A": "Use Cloud Dataflow service to execute the pipeline",
   "B": "Increase the maximum number of workers by setting maxNumWorkers in PipelineOptions",
   "C": "Increase the number of nodes in the Bigtable cluster",
   "D": "Modify the pipeline to use the Flatten transform before writing to Bigtable",
   "E": "Modify the pipeline to use the CoGroupByKey transform before writing to Bigtable"
  },
  "correct": "B",
  "correct_text": "Increase the maximum number of workers by setting maxNumWorkers in PipelineOptions",
  "base": "The two actions to take to improve the performance of the pipeline and reduce the time it takes to write data to Bigtable are B and C. Increasing the maximum number of workers by setting maxNumWorkers in PipelineOptions can help the pipeline process data faster by distributing the workload among mo…"
 },
 {
  "id": "test_3_q44",
  "q": "You are using Dataflow to process data from a Pub/Sub topic and write it to a BigQuery dataset located in the EU. However, during peak periods, your pipeline is experiencing delays due to all three n1-standard-1 workers being at maximum CPU utilization. Which two actions can you take to increase your pipeline‘s performance?",
  "opts": {
   "A": "Increase the maximum number of workers in your pipeline",
   "B": "Use a larger instance type for your Dataflow workers",
   "C": "Change the zone of your Dataflow pipeline to run in us-central1",
   "D": "Create a temporary buffer table in Bigtable to write to before transferring to BigQuery",
   "E": "Create a temporary buffer table in Cloud Spanner to write to before transferring to BigQuery"
  },
  "correct": "A",
  "correct_text": "Increase the maximum number of workers in your pipeline",
  "base": "A: Increasing the maximum number of workers can help distribute the workload and prevent CPU utilization from becoming the bottleneck. B: Using a larger instance type for the Dataflow workers can also provide more CPU and memory resources to handle the increased workload. C: Changing the zone of th…"
 },
 {
  "id": "test_3_q46",
  "q": "How can you efficiently process and load application events published to a Pub/Sub topic into BigQuery, ensuring scalability for large volumes of events, and aggregating them across hourly intervals?",
  "opts": {
   "A": "Use a Cloud Function triggered by Pub/Sub to perform data processing every time a new message is published.",
   "B": "Schedule a Cloud Function to run hourly, pulling available messages from the Pub/Sub topic and performing the necessary aggregations",
   "C": "Schedule a batch Dataflow job to run hourly, pulling available messages from the Pub/Sub topic and performing the necessary aggregations",
   "D": "Use a streaming Dataflow job that reads continuously from the Pub/Sub topic and performs the necessary aggregations using tumbling windows."
  },
  "correct": "D",
  "correct_text": "Use a streaming Dataflow job that reads continuously from the Pub/Sub topic and performs the necessary aggregations using tumbling windows.",
  "base": "Ref: https://cloud.google.com/dataflow/docs/concepts/streaming-pipelines#tumbling-windows"
 },
 {
  "id": "test_3_q47",
  "q": "How should you set up a windowed pipeline in DataFlow to compute a moving average of a company‘s stock price every 5 seconds using the past 30 seconds‘ worth of data from Pub/Sub?",
  "opts": {
   "A": "Use a fixed window with a duration of 5 seconds and emit results using a trigger of AfterProcessingTime.pastFirstElementInPane().plusDelayOf(Duration.standardSeconds(30))",
   "B": "Use a fixed window with a duration of 30 seconds and emit results using a trigger of AfterWatermark.pastEndOfWindow().plusDelayOf(Duration.standardSeconds(5)).",
   "C": "Use a sliding window with a duration of 5 seconds and emit results using a trigger of AfterProcessingTime.pastFirstElementInPane().plusDelayOf(Duration.standardSeconds(30)).",
   "D": "Use a sliding window with a duration of 30 seconds and a period of 5 seconds and emit results using a trigger of AfterWatermark.pastEndOfWindow()."
  },
  "correct": "D",
  "correct_text": "Use a sliding window with a duration of 30 seconds and a period of 5 seconds and emit results using a trigger of AfterWatermark.pastEndOfWindow().",
  "base": "You set the following windows with the Apache Beam SDK or Dataflow SQL streaming extensions: Hopping windows (called sliding windows in Apache Beam) A hopping window represents a consistent time interval in the data stream. Hopping windows can overlap, whereas tumbling windows are disjoint. For exa…"
 },
 {
  "id": "test_3_q48",
  "q": "You are tasked with building a new application that requires scalable collection of continuously arriving data, expected to generate approximately 150 GB of JSON data per day by the end of the year. Your requirements include decoupling the producer from the consumer, cost-efficient storage of raw ingested data which should be stored indefinitely, near real-time SQL query capability, and maintaining at least 2 years of historical data that will be queried with SQL. Which pipeline should you use to meet these requirements?",
  "opts": {
   "A": "Develop an application with an API and a tool to poll the API and write data to Cloud Storage as gzipped JSON files.",
   "B": "Build an application that writes to a Cloud SQL database to store the data, with periodic exports of the database to write to Cloud Storage and load into BigQuery.",
   "C": "Create an application that publishes events to Cloud Pub/Sub, and set up Spark jobs on Cloud Dataproc to convert the JSON data to Avro format, stored on HDFS on Persistent Disk",
   "D": "Create an application that publishes events to Cloud Pub/Sub, and set up a Cloud Dataflow pipeline that transforms the JSON event payloads to Avro, writing the data to Cloud Storage and BigQuery"
  },
  "correct": "D",
  "correct_text": "Create an application that publishes events to Cloud Pub/Sub, and set up a Cloud Dataflow pipeline that transforms the JSON event payloads to Avro, writing the data to Cloud Storage and BigQuery",
  "base": "Create an application that publishes events to Cloud Pub/Sub and create a Cloud Dataflow pipeline that transforms the JSON event payloads to Avro, writing the data to Cloud Storage and BigQuery. This option uses Cloud Pub/Sub to decouple the producer from the consumer, ensuring that the application…"
 },
 {
  "id": "test_3_q50",
  "q": "You are updating the code for a subscriber to a Pub/Sub feed and want to ensure that message loss does not occur due to erroneous message acknowledgments after deployment. Which of the following options should you choose?",
  "opts": {
   "A": "Test the new subscriber logic on the Pub/Sub emulator on your local machine before deploying it to production.",
   "B": "Create a Pub/Sub snapshot before deploying new subscriber code, and use a Seek operation to re-deliver messages that became available after the snapshot was created if errors occur",
   "C": "Use Cloud Build for your deployment, and locate a timestamp logged by Cloud Build at the start of the deployment if errors occur",
   "D": "Enable dead-lettering on the Pub/Sub topic to capture unacknowledged messages, and re-deliver any messages captured by the dead-letter queue if errors occur"
  },
  "correct": "B",
  "correct_text": "Create a Pub/Sub snapshot before deploying new subscriber code, and use a Seek operation to re-deliver messages that became available after the snapshot was created if errors occur",
  "base": "Create a Pub/Sub snapshot before deploying new subscriber code. Use a Seek operation to re-deliver messages that became available after the snapshot was created. According to the second reference in the list below (Refer second link below ) a concern with deploying new subscriber code is that the n…"
 },
 {
  "id": "test_4_q2",
  "q": "As the operator of a logistics company, you are seeking to improve the reliability of event delivery for vehicle-based sensors. Currently, you have small data centers located in various parts of the world to capture these events. However, the leased lines connecting your event collection infrastructure to the event processing infrastructure are unreliable, resulting in unpredictable latency. You need to find a cost-effective solution to address this issue. Which of the following options would be the best course of action?",
  "opts": {
   "A": "Implement small Kafka clusters in your data centers to buffer events.",
   "B": "Configure the data acquisition devices to publish data to Cloud Pub/Sub.",
   "C": "Establish a Cloud Interconnect between all remote data centers and Google.",
   "D": "Develop a Cloud Dataflow pipeline that aggregates all data in session windows."
  },
  "correct": "B",
  "correct_text": "Configure the data acquisition devices to publish data to Cloud Pub/Sub.",
  "base": "Option A suggests deploying small Kafka clusters in data centers to buffer events. While Kafka can help buffer events and improve reliability, it requires additional infrastructure and maintenance costs, which may not be the most cost-effective solution. Option C suggests establishing a Cloud Inter…"
 },
 {
  "id": "test_4_q3",
  "q": "You have a large amount of historical data in BigQuery and a daily data pipeline that continuously adds new data to the table. The Data Science team runs SQL queries on this data, but they are noticing that queries filtered on a date column and limited to 30-90 days of data are scanning the entire table. Additionally, you have observed that your billing is increasing more quickly than expected. What is the most cost-effective solution to resolve this issue while maintaining the ability to conduct SQL queries?",
  "opts": {
   "A": "Use DDL to recreate the tables and partition them by a column containing a TIMESTAMP or DATE type",
   "B": "Recommend that the Data Science team export the table to a CSV file on Cloud Storage and use Cloud Datalab to explore the data by reading the files directly.",
   "C": "Create two separate tables, one for the last 30-90 days of data and another for the longer history, to minimize full table scans over the entire history.",
   "D": "Write an Apache Beam pipeline that creates a new BigQuery table every day and advise the Data Science team to use wildcards on the table name suffixes to select the data they need."
  },
  "correct": "A",
  "correct_text": "Use DDL to recreate the tables and partition them by a column containing a TIMESTAMP or DATE type",
  "base": "The correct answer is option A: Create new tables using DDL and partition them by a column containing a TIMESTAMP or DATE type. Partitioning the tables in BigQuery is an efficient way to handle large amounts of data by organizing them into smaller, more manageable sections based on a specific colum…"
 },
 {
  "id": "test_4_q4",
  "q": "You are working on a new Google Cloud pipeline to stream IoT data from Cloud Pub/Sub to BigQuery via Cloud Dataflow. While previewing the data, you noticed that approximately 2% of the data is corrupt. To filter out this corrupt data, what modification should you make to the Cloud Dataflow pipeline (Consider the following options)?",
  "opts": {
   "A": "Incorporate a SideInput that returns a Boolean value for corrupt elements.",
   "B": "Add a ParDo transform within the Cloud Dataflow to discard corrupt elements.",
   "C": "Implement a Partition transform in Cloud Dataflow to separate corrupt data from valid data",
   "D": "Add a GroupByKey transform to Cloud Dataflow to group valid data together and discard corrupt data."
  },
  "correct": "B",
  "correct_text": "Add a ParDo transform within the Cloud Dataflow to discard corrupt elements.",
  "base": "The ParDo transform in Cloud Dataflow can be used to filter out corrupt elements by adding a DoFn that checks each element and filters out the corrupt ones. This is the most efficient way to remove corrupt elements from the data stream, as it allows the pipeline to continue processing only the vali…"
 },
 {
  "id": "test_4_q8",
  "q": "How can you optimize the performance of a complicated analytical Spark job with shuffling operations and initial data in parquet format (average size of 200-400 MB each) after migrating it from an on-prem Hadoop cluster to Dataproc on GCS, while keeping in mind the cost sensitivity of your organization. The Spark job is currently running on preemptible VMs with only two non-preemptible workers?",
  "opts": {
   "A": "Ensure that the parquet files are at least 1 GB in size.",
   "B": "Switch from using parquet files to TFRecords formats, which are approximately 200 MB per file.",
   "C": "Change from using HDDs to SSDs, copy initial data from GCS to HDFS, run the Spark job, and copy the results back to GCS.",
   "D": "Change from using HDDs to SSDs and modify the configuration of preemptible VMs to increase the boot disk size."
  },
  "correct": "A",
  "correct_text": "Ensure that the parquet files are at least 1 GB in size.",
  "base": "A. Ensure that the parquet files are at least 1 GB in size. Spark performs best when processing larger files. With files in the 200-400 MB range, Spark might spend more time in task scheduling and metadata management compared to actual data processing. Increasing the Parquet file size to around 1 G…"
 },
 {
  "id": "test_4_q15",
  "q": "As part of your data pipeline, you are loading CSV files from Cloud Storage to BigQuery. However, these files have known data quality issues, such as mismatched data types and inconsistent formatting. You want to ensure data quality is maintained and perform the required cleansing and transformation. Which approach should you take?",
  "opts": {
   "A": "Use Data Fusion to transform the data before loading it into BigQuery",
   "B": "Use Data Fusion to convert the CSV files to a self-describing data format, such as AVRO, before loading the data to BigQuery.",
   "C": "Load the CSV files into a staging table with the desired schema, perform the transformations with SQL, and then write the results to the final destination table.",
   "D": "Create a table with the desired schema, load the CSV files into the table, and perform the transformations in place using SQL"
  },
  "correct": "A",
  "correct_text": "Use Data Fusion to transform the data before loading it into BigQuery",
  "base": "Correct Option A. Use Data Fusion to transform the data before loading it into BigQuery Cloud Data Fusion is a fully managed ETL/ELT service on Google Cloud. It allows you to build pipelines that cleanse, validate, and transform data before loading into BigQuery. This is the best approach when deal…"
 },
 {
  "id": "test_4_q23",
  "q": "How can you compare the output of the original ETL job with the output of the migrated job after migrating them to run on BigQuery, given that the tables do not have a primary key column to join them together for comparison, but you have loaded a table containing the output of the original job?",
  "opts": {
   "A": "Select random samples from the tables using the RAND() function and compare the samples.",
   "B": "Select random samples from the tables using the HASH() function and compare the samples",
   "C": "Use a Dataproc cluster and the BigQuery Hadoop connector to read the data from each table and calculate a hash from non-timestamp columns of the table after sorting. Compare the hashes of each table.",
   "D": "Create stratified random samples using the OVER() function and compare equivalent samples from each table"
  },
  "correct": "C",
  "correct_text": "Use a Dataproc cluster and the BigQuery Hadoop connector to read the data from each table and calculate a hash from non-timestamp columns of the table after sorting. Compare the hashes of each table.",
  "base": "Correct Option C. Use a Dataproc cluster and the BigQuery Hadoop connector to read the data from each table and calculate a hash from non‑timestamp columns of the table after sorting. Compare the hashes of each table. This is the correct approach because: Without a primary key, you cannot join rows…"
 },
 {
  "id": "test_4_q24",
  "q": "Your company wants to upload their historical data to Cloud Storage, but the security rules in place do not allow external IPs to access their on-premises resources. They plan to add new data from existing on-premises applications daily after an initial upload. What should they do to transfer the data securely?",
  "opts": {
   "A": "Use “gsutil rsync“ command to sync the on-premises servers with Cloud Storage",
   "B": "Use Dataflow to write the data directly to Cloud Storage",
   "C": "Write a Dataproc job template to perform the data transfer.",
   "D": "Install an FTP server on a Compute Engine VM to receive the files and move them to Cloud Storage."
  },
  "correct": "A",
  "correct_text": "Use “gsutil rsync“ command to sync the on-premises servers with Cloud Storage",
  "base": "Correct Option A. Use “gsutil rsync” command to sync the on‑premises servers with Cloud Storage gsutil rsync is the recommended tool for secure synchronization between local storage and Cloud Storage. It uses HTTPS for secure transfer and supports incremental updates (only new or changed files are…"
 },
 {
  "id": "test_4_q25",
  "q": "Your team is responsible for the development and maintenance of ETL pipelines in your company. One of your Dataflow jobs is failing due to errors in the input data, and you need to improve the pipeline‘s reliability, including the ability to reprocess all failing data. What is the recommended approach?",
  "opts": {
   "A": "Include a filtering step to avoid these types of errors in the future, extract erroneous rows from logs",
   "B": "Include a try...catch block in your DoFn that transforms the data, extract erroneous rows from logs",
   "C": "Include a try...catch block in your DoFn that transforms the data, write erroneous rows directly to Pub/Sub from the DoFn",
   "D": "Include a try...catch block in your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to Pub/Sub later"
  },
  "correct": "D",
  "correct_text": "Include a try...catch block in your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to Pub/Sub later",
  "base": "Correct Option D: Include a try…catch block in your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to Pub/Sub later. The Logic: A robust pipeline should never simply “fail” on bad input. By wrapping transformation logic in a try...catch block, you can cat…"
 }
]

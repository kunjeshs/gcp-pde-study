<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_10.json  (just the JSON, no backticks).
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
test_5_q38, test_5_q44, test_5_q45, test_6_q2, test_6_q3, test_6_q4, test_6_q5, test_6_q7, test_6_q8, test_6_q9, test_6_q14, test_6_q18, test_6_q19, test_6_q24, test_6_q29, test_6_q32, test_6_q33, test_6_q34, test_6_q36, test_6_q38

Questions:

[
 {
  "id": "test_5_q38",
  "q": "Your analytics team wants to build a simple statistical model to determine which customers are most likely to work with your company again, based on a few different metrics. They want to run the model on Apache Spark, using data housed in Google Cloud Storage, and you have recommended using Google CloudDataproc to execute this job. Testing has shown that this workload can run in approximately 30 minutes on a 15-node cluster, outputting the results into GoogleBigQuery. The plan is to run this workload weekly. How should you optimize the cluster for cost?",
  "opts": {
   "A": "Migrate the workload to Google Cloud Dataflow",
   "B": "Use pre-emptible virtual machines (VMs) for the cluster",
   "C": "Use a higher-memory node so that the job runs faster",
   "D": "Use SSDs on the worker nodes so that the job can run faster"
  },
  "correct": "B",
  "correct_text": "Use pre-emptible virtual machines (VMs) for the cluster",
  "base": "https://cloud.google.com/dataproc/docs/concepts/compute/preemptible-vms"
 },
 {
  "id": "test_5_q44",
  "q": "You need to store and analyze social media postings in Google BigQuery at a rate of 10,000 messages per minute in near real-time. Initially, design the application to use streaming inserts for individual postings. Your application also performs data aggregations right after the streaming inserts. You discover that the queries after streaming inserts do not exhibit strong consistency, and reports from the queries might miss in-flight data. How can you adjust your application design?",
  "opts": {
   "A": "Re-write the application to load accumulated data every 2 minutes.",
   "B": "Convert the streaming insert code to batch load for individual messages.",
   "C": "Load the original message to Google Cloud SQL, and export the table every hour to BigQuery via streaming inserts.",
   "D": "Estimate the average latency for data availability after streaming inserts, and always run queries after waiting twice as long."
  },
  "correct": "D",
  "correct_text": "Estimate the average latency for data availability after streaming inserts, and always run queries after waiting twice as long.",
  "base": "Answer: D Description: The data is first comes to buffer and then written to Storage. If we are running queries in buffer we will face above mentioned issues. If we wait for the bigquery to write the data to storage then we wont face the issue. So We need to wait till its written tio storage"
 },
 {
  "id": "test_5_q45",
  "q": "You work for a car manufacturer and have set up a data pipeline using Google Cloud Pub/Sub to capture anomalous sensor events. You are using a push subscription in Cloud Pub/Sub that calls a custom HTTPS endpoint that you have created to take action of these anomalous events as they occur. Your customHTTPS endpoint keeps getting an inordinate amount of duplicate messages. What is the most likely cause of these duplicate messages?",
  "opts": {
   "A": "The message body for the sensor event is too large.",
   "B": "Your custom endpoint has an out-of-date SSL certificate.",
   "C": "The Cloud Pub/Sub topic has too many messages published to it.",
   "D": "Your custom endpoint is not acknowledging messages within the acknowledgement deadline."
  },
  "correct": "D",
  "correct_text": "Your custom endpoint is not acknowledging messages within the acknowledgement deadline.",
  "base": "https://cloud.google.com/pubsub/docs/troubleshooting#dupes"
 },
 {
  "id": "test_6_q2",
  "q": "You have an Apache Kafka cluster on-prem with topics containing web application logs. You need to replicate the data to Google Cloud for analysis in BigQuery and Cloud Storage. The preferred replication method is mirroring to avoid deployment of Kafka Connect plugins.What should you do?",
  "opts": {
   "A": "Deploy a Kafka cluster on GCE VM Instances. Configure your on-prem cluster to mirror your topics to the cluster running in GCE. Use a Dataproc cluster or Dataflow job to read from Kafka and write to GCS.",
   "B": "Deploy a Kafka cluster on GCE VM Instances with the PubSub Kafka connector configured as a Sink connector. Use a Dataproc cluster or Dataflow job to read from Kafka and write to GCS.",
   "C": "Deploy the PubSub Kafka connector to your on-prem Kafka cluster and configure PubSub as a Source connector. Use a Dataflow job to read from PubSub and write to GCS.",
   "D": "Deploy the PubSub Kafka connector to your on-prem Kafka cluster and configure PubSub as a Sink connector. Use a Dataflow job to read from PubSub and write to GCS."
  },
  "correct": "A",
  "correct_text": "Deploy a Kafka cluster on GCE VM Instances. Configure your on-prem cluster to mirror your topics to the cluster running in GCE. Use a Dataproc cluster or Dataflow job to read from Kafka and write to GCS.",
  "base": "A. https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=27846330 The solution specifically mentions mirroring and minimizing the use of Kafka Connect plugin. D would be the more Google Cloud-native way of implementing the same, but the requirement is better met by A."
 },
 {
  "id": "test_6_q3",
  "q": "Your company receives both batch- and stream-based event data. You want to process the data using Google Cloud Dataflow over a predictable time period.However, you realize that in some instances data can arrive late or out of order. How should you design your Cloud Dataflow pipeline to handle data that is late or out of order?",
  "opts": {
   "A": "Set a single global window to capture all the data.",
   "B": "Set sliding windows to capture all the lagged data.",
   "C": "Use watermarks and timestamps to capture the lagged data.",
   "D": "Ensure every datasource type (stream or batch) has a timestamp, and use the timestamps to define the logic for lagged data."
  },
  "correct": "C",
  "correct_text": "Use watermarks and timestamps to capture the lagged data.",
  "base": "Answer: C Description: A watermark is a threshold that indicates when Dataflow expects all of the data in a window to have arrived. If new data arrives with a timestamp that‘s in the window but older than the watermark, the data is considered late data."
 },
 {
  "id": "test_6_q4",
  "q": "You are planning to migrate your current on-premises Apache Hadoop deployment to the cloud. You need to ensure that the deployment is as fault-tolerant and cost-effective as possible for long-running batch jobs. You want to use a managed service. What should you do?",
  "opts": {
   "A": "Deploy a Cloud Dataproc cluster. Use a standard persistent disk and 50% preemptible workers. Store data in Cloud Storage, and change references in scripts from hdfs:// to gs://",
   "B": "Deploy a Cloud Dataproc cluster. Use an SSD persistent disk and 50% preemptible workers. Store data in Cloud Storage, and change references in scripts from hdfs:// to gs://",
   "C": "Install Hadoop and Spark on a 10-node Compute Engine instance group with standard instances. Install the Cloud Storage connector, and store the data in Cloud Storage. Change references in scripts from hdfs:// to gs://",
   "D": "Install Hadoop and Spark on a 10-node Compute Engine instance group with preemptible instances. Store data in HDFS. Change references in scripts from hdfs:// to gs://"
  },
  "correct": "A",
  "correct_text": "Deploy a Cloud Dataproc cluster. Use a standard persistent disk and 50% preemptible workers. Store data in Cloud Storage, and change references in scripts from hdfs:// to gs://",
  "base": "A. Deploy a Cloud Dataproc cluster. Use a standard persistent disk and 50% preemptible workers. Store data in Cloud Storage, and change references in scripts from hdfs:// to gs:// Let‘s break down why this approach is ideal: Managed Service: Cloud Dataproc is a Google Cloud managed Hadoop and Spark…"
 },
 {
  "id": "test_6_q5",
  "q": "You receive data files in CSV format monthly from a third party. You need to cleanse this data, but every third month the schema of the files changes. Your requirements for implementing these transformations include:? Executing the transformations on a schedule? Enabling non-developer analysts to modify transformations? Providing a graphical tool for designing transformationsWhat should you do?",
  "opts": {
   "A": "Use Cloud Dataprep to build and maintain the transformation recipes, and execute them on a scheduled basis",
   "B": "Load each month‘s CSV data into BigQuery, and write a SQL query to transform the data to a standard schema. Merge the transformed tables together with a SQL query",
   "C": "Help the analysts write a Cloud Dataflow pipeline in Python to perform the transformation. The Python code should be stored in a revision control system and modified as the incoming data‘s schema changes",
   "D": "Use Apache Spark on Cloud Dataproc to infer the schema of the CSV file before creating a Dataframe. Then implement the transformations in Spark SQL before writing the data out to Cloud Storage and loading into BigQuery"
  },
  "correct": "A",
  "correct_text": "Use Cloud Dataprep to build and maintain the transformation recipes, and execute them on a scheduled basis",
  "base": "A. Use Cloud Dataprep to build and maintain the transformation recipes, and execute them on a scheduled basis Here‘s why Cloud Dataprep aligns well with your requirements: Scheduled Transformations: Cloud Dataprep allows you to design data cleaning and transformation workflows visually. These workf…"
 },
 {
  "id": "test_6_q7",
  "q": "You are operating a streaming Cloud Dataflow pipeline. Your engineers have a new version of the pipeline with a different windowing algorithm and triggering strategy. You want to update the running pipeline with the new version. You want to ensure that no data is lost during the update. What should you do?",
  "opts": {
   "A": "Update the Cloud Dataflow pipeline inflight by passing the --update option with the --jobName set to the existing job name",
   "B": "Update the Cloud Dataflow pipeline inflight by passing the --update option with the --jobName set to a new unique job name",
   "C": "Stop the Cloud Dataflow pipeline with the Cancel option. Create a new Cloud Dataflow job with the updated code",
   "D": "Stop the Cloud Dataflow pipeline with the Drain option. Create a new Cloud Dataflow job with the updated code"
  },
  "correct": "D",
  "correct_text": "Stop the Cloud Dataflow pipeline with the Drain option. Create a new Cloud Dataflow job with the updated code",
  "base": "D. Stop the Cloud Dataflow pipeline with the Drain option. Create a new Cloud Dataflow job with the updated code. This approach ensures that no data is lost during the update process: Stop with Drain: This option allows the pipeline to finish processing all currently buffered data before shutting d…"
 },
 {
  "id": "test_6_q8",
  "q": "You architect a system to analyze seismic data. Your extract, transform, and load (ETL) process runs as a series of MapReduce jobs on an Apache Hadoop cluster. The ETL process takes days to process a data set because some steps are computationally expensive. Then you discover that a sensor calibration step has been omitted. How should you change your ETL process to carry out sensor calibration systematically in the future?",
  "opts": {
   "A": "Modify the transformMapReduce jobs to apply sensor calibration before they do anything else.",
   "B": "Introduce a new MapReduce job to apply sensor calibration to raw data, and ensure all other MapReduce jobs are chained after this.",
   "C": "Add sensor calibration data to the output of the ETL process, and document that all users need to apply sensor calibration themselves.",
   "D": "Develop an algorithm through simulation to predict variance of data output from the last MapReduce job based on calibration factors, and apply the correction to all data."
  },
  "correct": "B",
  "correct_text": "Introduce a new MapReduce job to apply sensor calibration to raw data, and ensure all other MapReduce jobs are chained after this.",
  "base": "B. Introduce a new MapReduce job to apply sensor calibration to raw data, and ensure all other MapReduce jobs are chained after this. This approach offers several advantages: Systematic Calibration: A dedicated MapReduce job ensures that sensor calibration is applied consistently to all data, preve…"
 },
 {
  "id": "test_6_q9",
  "q": "Your team is responsible for developing and maintaining ETLs in your company. One of your Dataflow jobs is failing because of some errors in the input data, and you need to improve reliability of the pipeline (incl. being able to reprocess all failing data).What should you do?",
  "opts": {
   "A": "Add a filtering step to skip these types of errors in the future, extract erroneous rows from logs. that transforms the data, extract erroneous rows from logs. . that can be stored to PubSub later.",
   "B": "Add a try catch block to your DoFn that transforms the data, extract erroneous rows from logs.",
   "C": "Add a try catch block to your DoFn that transforms the data, write erroneous rows to PubSub directly from the DoFn.",
   "D": "Add a try catch block to your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to PubSub later."
  },
  "correct": "D",
  "correct_text": "Add a try catch block to your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to PubSub later.",
  "base": "The best solution for improving the reliability of the Dataflow job and reprocessing failing data is: D. Add a try…catch block to your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to PubSub later. Here’s why: try…catch block: This allows you to handle e…"
 },
 {
  "id": "test_6_q14",
  "q": "You are creating a new pipeline in Google Cloud to stream IoT data from Cloud Pub/Sub through Cloud Dataflow to BigQuery. While previewing the data, you notice that roughly 2% of the data appears to be corrupt. You need to modify the Cloud Dataflow pipeline to filter out this corrupt data. What should you do?",
  "opts": {
   "A": "Add a SideInput that returns a Boolean if the element is corrupt.",
   "B": "Add a ParDo transform in Cloud Dataflow to discard corrupt elements.",
   "C": "Add a Partition transform in Cloud Dataflow to separate valid data from corrupt data.",
   "D": "Add a GroupByKey transform in Cloud Dataflow to group all of the valid data together and discard the rest."
  },
  "correct": "B",
  "correct_text": "Add a ParDo transform in Cloud Dataflow to discard corrupt elements.",
  "base": "vote B :https://beam.apache.org/documentation/programming-guide/#pardo Filtering a data set. You can use ParDo to consider each element in a PCollection and either output that element to a new collection or discard it. Formatting or type-converting each element in a data set. If your input PCollect…"
 },
 {
  "id": "test_6_q18",
  "q": "You decided to use Cloud Datastore to ingest vehicle telemetry data in real time. You want to build a storage system that will account for the long-term data growth, while keeping the costs low. You also want to create snapshots of the data periodically, so that you can make a point-in-time (PIT) recovery, or clone a copy of the data for Cloud Datastore in a different environment. You want to archive these snapshots for a long time. Which two methods can accomplish this?(Choose two.)",
  "opts": {
   "A": "Use managed export, and store the data in a Cloud Storage bucket using Nearline or Coldline class.",
   "B": "Use managed export, and then import to Cloud Datastore in a separate project under a unique namespace reserved for that export.",
   "C": "Use managed export, and then import the data into a BigQuery table created just for that export, and delete temporary export files.",
   "D": "Write an application that uses Cloud Datastore client libraries to read all the entities. Treat each entity as a BigQuery table row via BigQuery streaming insert. Assign an export timestamp for each export, and attach it as an extra column for each row. Make sure that the BigQuery table is partitioned using the export timestamp column.",
   "E": "Write an application that uses Cloud Datastore client libraries to read all the entities. Format the exported data into a JSON file. Apply compression before storing the data in Cloud Source Repositories."
  },
  "correct": "A",
  "correct_text": "Use managed export, and store the data in a Cloud Storage bucket using Nearline or Coldline class.",
  "base": "Correct option A. Managed export to Nearline/Coldline Low-cost archival; import for PIT. option B. Export + import to new project/namespace Clones for recovery/DR. Incorrect option C. BigQuery import + delete No Datastore-native restore. option D. Streaming to BigQuery No snapshots; custom app. opt…"
 },
 {
  "id": "test_6_q19",
  "q": "You store historic data is in Cloud Storage. You need to perform analytics on the historic data. You want to use a solution to detect invalid data entries and perform data transformations that will not require programming or knowledge of SQL.What should you do?",
  "opts": {
   "A": "Use Cloud Dataflow with Beam to detect errors and perform transformations.",
   "B": "Use Cloud Dataprep with recipes to detect errors and perform transformations.",
   "C": "Use Cloud Dataproc with a Hadoop job to detect errors and perform transformations.",
   "D": "Use federated tables in BigQuery with queries to detect errors and perform transformations."
  },
  "correct": "B",
  "correct_text": "Use Cloud Dataprep with recipes to detect errors and perform transformations.",
  "base": "Correct Option B. Use Cloud Dataprep with recipes to detect errors and perform transformations. Cloud Dataprep provides a visual, no-code interface for data profiling, automatic anomaly detection, data validation, and transformations through reusable recipes. It connects directly to Cloud Storage,…"
 },
 {
  "id": "test_6_q24",
  "q": "Your company‘s customer and order databases are often under heavy load. This makes performing analytics against them difficult without harming operations.The databases are in a MySQL cluster, with nightly backups taken using mysqldump. You want to perform analytics with minimal impact on operations. What should you do?",
  "opts": {
   "A": "Add a node to the MySQL cluster and build an OLAP cube there.",
   "B": "Use an ETL tool to load the data from MySQL into Google BigQuery.",
   "C": "Connect an on-premises Apache Hadoop cluster to MySQL and perform ETL.",
   "D": "Mount the backups to Google Cloud SQL, and then process the data using Google Cloud Dataproc."
  },
  "correct": "D",
  "correct_text": "Mount the backups to Google Cloud SQL, and then process the data using Google Cloud Dataproc.",
  "base": "Correct Option D. “Mount the backups to Google Cloud SQL, and then process the data using Google Cloud Dataproc.” This is correct because using Cloud SQL allows you to restore the MySQL backups without impacting the production cluster. From there, you can offload analytics workloads to Dataproc (Ha…"
 },
 {
  "id": "test_6_q29",
  "q": "You operate an IoT pipeline built around Apache Kafka that normally receives around 5000 messages per second. You want to use Google Cloud Platform to create an alert as soon as the moving average over 1 hour drops below 4000 messages per second. What should you do?",
  "opts": {
   "A": "Consume the stream of data in Cloud Dataflow using Kafka IO. Set a sliding time window of 1 hour every 5 minutes. Compute the average when the window closes, and send an alert if the average is less than 4000 messages.",
   "B": "Consume the stream of data in Cloud Dataflow using Kafka IO. Set a fixed time window of 1 hour. Compute the average when the window closes, and send an alert if the average is less than 4000 messages.",
   "C": "Use Kafka Connect to link your Kafka message queue to Cloud Pub/Sub. Use a Cloud Dataflow template to write your messages from Cloud Pub/Sub to Cloud Bigtable. Use Cloud Scheduler to run a script every hour that counts the number of rows created in Cloud Bigtable in the last hour. If that number falls below 4000, send an alert.",
   "D": "Use Kafka Connect to link your Kafka message queue to Cloud Pub/Sub. Use a Cloud Dataflow template to write your messages from Cloud Pub/Sub to BigQuery. Use Cloud Scheduler to run a script every five minutes that counts the number of rows created in BigQuery in the last hour. If that number falls below 4000, send an alert."
  },
  "correct": "A",
  "correct_text": "Consume the stream of data in Cloud Dataflow using Kafka IO. Set a sliding time window of 1 hour every 5 minutes. Compute the average when the window closes, and send an alert if the average is less than 4000 messages.",
  "base": "Option A is the correct answer. Reasons:- a) Kafka IO and Dataflow is a valid option for interconnect (needless where Kafka is located – On Prem/Google Cloud/Other cloud) b) Sliding Window will help to calculate average. Option C and D are overkill and complex, considering the scenario in the quest…"
 },
 {
  "id": "test_6_q32",
  "q": "You are developing a software application using Google‘s Dataflow SDK, and want to use conditional, for loops and other complex programming structures to create a branching pipeline. Which component will be used for the data processing operation?",
  "opts": {
   "A": "PCollection",
   "B": "Transform",
   "C": "Pipeline",
   "D": "Sink API"
  },
  "correct": "B",
  "correct_text": "Transform",
  "base": "In Google Cloud, the Dataflow SDK provides a transform component. It is responsible for the data processing operation. You can use conditional, for loops, and other complex programming structure to create a branching pipeline. Reference: https://cloud.google.com/dataflow/model/programming-model"
 },
 {
  "id": "test_6_q33",
  "q": "You want to build a managed Hadoop system as your data lake. The data transformation process is composed of a series of Hadoop jobs executed in sequence.To accomplish the design of separating storage from compute, you decided to use the Cloud Storage connector to store all input data, output data, and intermediary data. However, you noticed that one Hadoop job runs very slowly with Cloud Dataproc, when compared with the on-premises bare-metal Hadoop environment (8-core nodes with 100-GB RAM). Analysis shows that this particular Hadoop job is disk I/O intensive. You want to resolve the issue. What should you do?",
  "opts": {
   "A": "Allocate sufficient memory to the Hadoop cluster, so that the intermediary data of that particular Hadoop job can be held in memory",
   "B": "Allocate sufficient persistent disk space to the Hadoop cluster, and store the intermediate data of that particular Hadoop job on native HDFS",
   "C": "Allocate more CPU cores of the virtual machine instances of the Hadoop cluster so that the networking bandwidth for each instance can scale up",
   "D": "Allocate additional network interface card (NIC), and configure link aggregation in the operating system to use the combined throughput when working with Cloud Storage"
  },
  "correct": "B",
  "correct_text": "Allocate sufficient persistent disk space to the Hadoop cluster, and store the intermediate data of that particular Hadoop job on native HDFS",
  "base": "Correct: B Local HDFS storage is a good option if: Your jobs require a lot of metadata operationsfor example, you have thousands of partitions and directories, and each file size is relatively small. You modify the HDFS data frequently or you rename directories. (Cloud Storage objects are immutabl…"
 },
 {
  "id": "test_6_q34",
  "q": "You currently have a single on-premises Kafka cluster in a data center in the us-east region that is responsible for ingesting messages from IoT devices globally.Because large parts of globe have poor internet connectivity, messages sometimes batch at the edge, come in all at once, and cause a spike in load on yourKafka cluster. This is becoming difficult to manage and prohibitively expensive. What is the Google-recommended cloud native architecture for this scenario?",
  "opts": {
   "A": "Edge TPUs as sensor devices for storing and transmitting the messages.",
   "B": "Cloud Dataflow connected to the Kafka cluster to scale the processing of incoming messages.",
   "C": "An IoT gateway connected to Cloud Pub/Sub, with Cloud Dataflow to read and process the messages from Cloud Pub/Sub.",
   "D": "A Kafka cluster virtualized on Compute Engine in us-east with Cloud Load Balancing to connect to the devices around the world."
  },
  "correct": "C",
  "correct_text": "An IoT gateway connected to Cloud Pub/Sub, with Cloud Dataflow to read and process the messages from Cloud Pub/Sub.",
  "base": "C. An IoT gateway connected to Cloud Pub/Sub, with Cloud Dataflow to read and process the messages from Cloud Pub/Sub This architecture leverages several Google Cloud Platform services for a scalable and cost-effective solution: IoT gateway: Deploy an IoT gateway at the edge near your sensor device…"
 },
 {
  "id": "test_6_q36",
  "q": "You work for a manufacturing plant that batches application log files together into a single log file once a day at 2:00 AM. You have written a Google CloudDataflow job to process that log file. You need to make sure the log file in processed once per day as inexpensively as possible. What should you do?",
  "opts": {
   "A": "Change the processing job to use Google Cloud Dataproc instead.",
   "B": "Manually start the Cloud Dataflow job each morning when you get into the office.",
   "C": "Create a cron job with Google App Engine Cron Service to run the Cloud Dataflow job.",
   "D": "Configure the Cloud Dataflow job as a streaming job so that it processes the log data immediately."
  },
  "correct": "C",
  "correct_text": "Create a cron job with Google App Engine Cron Service to run the Cloud Dataflow job.",
  "base": "Answer is C. https://cloud.google.com/appengine/docs/flexible/nodejs/scheduling-jobs-with-cron-yaml"
 },
 {
  "id": "test_6_q38",
  "q": "You want to use a BigQuery table as a data sink. In which writing mode(s) can you use BigQuery as a sink?",
  "opts": {
   "A": "Both batch and streaming",
   "B": "BigQuery cannot be used as a sink",
   "C": "Only batch",
   "D": "Only streaming"
  },
  "correct": "A",
  "correct_text": "Both batch and streaming",
  "base": "When you apply a BigQueryIO.Write transform in batch mode to write to a single table, Dataflow invokes a BigQuery load job. When you apply a BigQueryIO.Write transform in streaming mode or in batch mode using a function to specify the destination table, Dataflow uses BigQuery‘s streaming inserts Re…"
 }
]

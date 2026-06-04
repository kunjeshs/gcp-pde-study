<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_05.json  (just the JSON, no backticks).
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
test_14_q58, test_15_q36, test_16_q38, test_1_q47, test_2_q43, test_6_q22, test_13_q21, test_13_q29, test_1_q26, test_2_q7, test_2_q26, test_2_q34, test_2_q55, test_3_q4, test_3_q5, test_3_q8, test_3_q16, test_3_q24, test_4_q21, test_4_q34

Questions:

[
 {
  "id": "test_14_q58",
  "q": "Scenario: You are migrating a MySQL database workload to Cloud SQL. The database needs to scale to accommodate multiple readers from different geographic locations and maintain high availability with low RTO and RPO, especially during a regional outage. How can you minimize interruptions for readers during a database failover in this scenario?",
  "opts": {
   "A": "Create a highly available Cloud SQL instance in region Create a highly available read replica in region B. Scale up read workloads by creating cascading read replicas in multiple regions. Backup the Cloud SQL instances to a multi-regional Cloud Storage bucket. Restore the Cloud SQL backup to a new instance in another region when Region A is down.",
   "B": "Create a highly available Cloud SQL instance in region A. Scale up read workloads by creating read replicas in multiple regions. Promote one of the read replicas when region A is down.",
   "C": "Create a highly available Cloud SQL instance in region A. Create a highly available read replica in region B. Scale up read workloads by creating cascading read replicas in multiple regions. Promote the read replica in region B when region A is down.",
   "D": "Create a highly available Cloud SQL instance in region A. Scale up read workloads by creating read replicas in the same region. Failover to the standby Cloud SQL instance when the primary instance fails."
  },
  "correct": "C",
  "correct_text": "Create a highly available Cloud SQL instance in region A. Create a highly available read replica in region B. Scale up read workloads by creating cascading read replicas in multiple regions. Promote the read replica in…",
  "base": "The correct answer is C: Create a highly available Cloud SQL instance in region A. Create a highly available read replica in region B. Scale up read workloads by creating cascading read replicas in multiple regions. Promote the read replica in region B when region A is down.1. Creating a highly ava…"
 },
 {
  "id": "test_15_q36",
  "q": "Scenario: You have uploaded 5 years of log data to Cloud Storage. A user reported that some data points in the log data are outside of their expected ranges, which indicates errors. What steps should you take to address the issue of log data errors and ensure the ability to rerun the process in the future while maintaining the original data for compliance purposes?",
  "opts": {
   "A": "Import the data from Cloud Storage into BigQuery. Create a new BigQuery table, and skip the rows with errors.",
   "B": "Create a Compute Engine instance and create a new copy of the data in Cloud Storage. Skip the rows with errors.",
   "C": "Create a Dataflow workflow that reads the data from Cloud Storage, checks for values outside the expected range, sets the value to an appropriate default, and writes the updated records to a new dataset in Cloud Storage.",
   "D": "Create a Dataflow workflow that reads the data from Cloud Storage, checks for values outside the expected range, sets the value to an appropriate default, and writes the updated records to the same dataset in Cloud Storage."
  },
  "correct": "C",
  "correct_text": "Create a Dataflow workflow that reads the data from Cloud Storage, checks for values outside the expected range, sets the value to an appropriate default, and writes the updated records to a new dataset in Cloud Storage.",
  "base": "The correct answer is C: Create a Dataflow workflow that reads the data from Cloud Storage, checks for values outside the expected range, sets the value to an appropriate default, and writes the updated records to a new dataset in Cloud Storage.Creating a Dataflow workflow allows for a scalable and…"
 },
 {
  "id": "test_16_q38",
  "q": "Scenario: You are preparing to implement Cloud SQL with MySQL, aiming to guarantee high availability in case of a zone failure. What steps should you take to achieve this goal?",
  "opts": {
   "A": "Create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region.",
   "B": "Create a Cloud SQL instance in one zone, and create a read replica in another zone within the same region.",
   "C": "Create a Cloud SQL instance in one zone, and configure an external read replica in a zone in a different region.",
   "D": "Create a Cloud SQL instance in a region, and configure automatic backup to a Cloud Storage bucket in the same region."
  },
  "correct": "A",
  "correct_text": "Create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region.",
  "base": "A. Create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region.Creating a Cloud SQL instance in one zone and setting up a failover replica in another zone within the same region is the correct approach to ensure high availability in the event of a z…"
 },
 {
  "id": "test_1_q47",
  "q": "You have to migrate a large volume of data from an on-premises data store to Cloud Storage. You want to add metadata tags to objects with personally identifiable information. What two Google Cloud managed services could you use to accomplish this?",
  "opts": {
   "A": "Compute Engine and Data Catalog",
   "B": "Data Catalog and Cloud Firestore",
   "C": "Data Loss Prevention and Compute Engine",
   "D": "Data Loss Prevention and Data Catalog"
  },
  "correct": "D",
  "correct_text": "Data Loss Prevention and Data Catalog",
  "base": "Data Loss Prevention can identify personal identifiable information and Data Catalog can assign and store metadata tags to objects. Compute Engine could be used with custom applications but it is not a managed service. Cloud Firestore is a document database and could be used for storage but Data Ca…"
 },
 {
  "id": "test_2_q43",
  "q": "You are developing a distributed system and want to decouple two services. You want to ensure messages use a standard format and you plan to use Cloud Pub/Sub. What schema types are supported by Cloud Pub/Sub? (Choose 2)",
  "opts": {
   "A": "Parquet",
   "B": "Protocol Buffer",
   "C": "CSV",
   "D": "Thrift",
   "E": "Avro"
  },
  "correct": "B",
  "correct_text": "Protocol Buffer",
  "base": "Cloud Pub/Sub supports Avro and Protocol Buffer schemas. Thrift is an alternative to Protocol Buffers but is not supported for schemas. Parquet is an open source file format used in Hadoop. CSV is a file format often used when sharing data between applications. See https://cloud.google.com/pubsub/d…"
 },
 {
  "id": "test_6_q22",
  "q": "Which of these statements about exporting data from BigQuery is false?",
  "opts": {
   "A": "To export more than 1 GB of data, you need to put a wildcard in the destination filename.",
   "B": "The only supported export destination is Google Cloud Storage.",
   "C": "Data can only be exported in JSON or Avro format.",
   "D": "The only compression option available is GZIP."
  },
  "correct": "C",
  "correct_text": "Data can only be exported in JSON or Avro format.",
  "base": "Correct (False Statement) Option C. Data can only be exported in JSON or Avro format Correct (this is the false statement) because: BigQuery supports exporting data in CSV, JSON, and Avro formats. Saying “only JSON or Avro” is incorrect since CSV is also supported. Therefore, this statement is fals…"
 },
 {
  "id": "test_13_q21",
  "q": "Scenario: Your organization‘s data assets are spread across BigQuery, Pub/Sub, and a PostgreSQL instance on Compute Engine. Due to the variety of domains and teams accessing the data, it is challenging for teams to locate the existing data assets. How can you enhance data discoverability across different platforms in your organization with minimal development and configuration efforts?",
  "opts": {
   "A": "Use Data Catalog to automatically catalog BigQuery datasets. Use Data Catalog APIs to manually catalog Pub/Sub topics and PostgreSQL tables.",
   "B": "Use Data Catalog to automatically catalog BigQuery datasets and Pub/Sub topics. Use Data Catalog APIs to manually catalog PostgreSQL tables.",
   "C": "Use Data Catalog to automatically catalog BigQuery datasets and Pub/Sub topics. Use custom connectors to manually catalog PostgreSQL tables.",
   "D": "Use customer connectors to manually catalog BigQuery datasets, Pub/Sub topics, and PostgreSQL tables."
  },
  "correct": "B",
  "correct_text": "Use Data Catalog to automatically catalog BigQuery datasets and Pub/Sub topics. Use Data Catalog APIs to manually catalog PostgreSQL tables.",
  "base": "Let’s analyze each option to determine the most efficient way to enhance data discoverability with minimal effort: Use Data Catalog to automatically catalog BigQuery datasets. Use Data Catalog APIs to manually catalog Pub/Sub topics and PostgreSQL tables. This is partially correct. Data Catalog doe…"
 },
 {
  "id": "test_13_q29",
  "q": "In a Dataplex environment with raw and curated zones, the data engineering team is uploading JSON and CSV files to a bucket asset in the curated zone, but the files are not being automatically discovered by Dataplex. What steps should be taken to ensure that the files are discovered by Dataplex?",
  "opts": {
   "A": "Move the JSON and CSV files to the raw zone.",
   "B": "Enable auto-discovery of files for the curated zone.",
   "C": "Use the bg command-line tool to load the JSON and CSV files into BigQuery tables.",
   "D": "Grant object level access to the CSV and JSON files in Cloud Storage."
  },
  "correct": "A",
  "correct_text": "Move the JSON and CSV files to the raw zone.",
  "base": "Correct Option A. Move the JSON and CSV files to the raw zone. This is correct. In Dataplex, automatic discovery is enabled for raw zones where files are ingested. Curated zones are typically used for structured, processed data (often in BigQuery or other curated formats). Uploading raw files like…"
 },
 {
  "id": "test_1_q26",
  "q": "How can you design a solution to transfer log data from your set of YouTube channels into Google Cloud for analysis? Your design should allow global marketing teams to perform ANSI SQL and other types of analysis on the latest YouTube channel log data.",
  "opts": {
   "A": "Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination",
   "B": "Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Regional bucket as a final destination.",
   "C": "Use BigQuery Data Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination.",
   "D": "Use BigQuery Data Transfer Service to transfer the offsite backup files to a Cloud Storage Regional storage bucket as a final destination"
  },
  "correct": "A",
  "correct_text": "Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination",
  "base": "Correct Option A. Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi‑Regional storage bucket as a final destination Correct because the Storage Transfer Service is designed to move large volumes of log or backup data into Cloud Storage. Using a Multi‑Regional…"
 },
 {
  "id": "test_2_q7",
  "q": "A team of researchers is running a high performance distributed computing platform on premises but wants to migrate to Google Cloud. The platform uses virtual machines. The researchers want to be able to scale up the number of virtual machines in the cluster based on CPU load. What would you recommend they use?",
  "opts": {
   "A": "Kubernetes cluster",
   "B": "Managed instance groups",
   "C": "Unmanaged instance groups",
   "D": "Cloud Run"
  },
  "correct": "B",
  "correct_text": "Managed instance groups",
  "base": "The correct answer is managed instance groups, which is a way of deploying Compute Engine instances basesed on a template. Kubernetes is used for running containers, not virtual machines. Cloud Run is also used to run containers not virtual machines. Unmanaged instance groups run virtual machines b…"
 },
 {
  "id": "test_2_q26",
  "q": "You have been tasked with ensuring the successful transfer of 100 TB of data from the AWS S3 object storage system. This is a one time transfer. A complete and reliable transfer of all data is a top priority. How would you recommend loading this data into Cloud Storage?",
  "opts": {
   "A": "gsutil cp",
   "B": "Cloud Dataflow",
   "C": "Cloud Storage Transfer Service",
   "D": "Transfer Appliance"
  },
  "correct": "C",
  "correct_text": "Cloud Storage Transfer Service",
  "base": "Correct Option C – Cloud Storage Transfer Service This is the recommended solution for a large, one‑time transfer (100 TB) from AWS S3 to Google Cloud Storage. It is designed for reliability, scale, and completeness, ensuring all data is transferred successfully. Provides built‑in error handling, r…"
 },
 {
  "id": "test_2_q34",
  "q": "A group of analysts is migrating a Hadoop cluster from on premises to GCP. They want to follow Google Cloud recommended best practices. What should they do as part of the migration?",
  "opts": {
   "A": "Use ephemeral clusters and Cloud Storage instead of HDFS on local storage.",
   "B": "Use ephemeral clusters and use HDFS on local storage.",
   "C": "Continually run clusters and use Cloud Storage instead of HDFS on local storage.",
   "D": "Continually run clusters and use HDFS on local storage."
  },
  "correct": "A",
  "correct_text": "Use ephemeral clusters and Cloud Storage instead of HDFS on local storage.",
  "base": "Google Cloud recommends using ephemeral clusters. Since clusters start quickly you do not need to keep clusters running to avoid long startup time. Google Cloud also recommends using Cloud Storage to store persistent data so data does not have to be copied from a cluster before shutting down and th…"
 },
 {
  "id": "test_2_q55",
  "q": "Your company is migrating an on-premises long-term storage archive to Google Cloud. The archived files are accessed on average about once every 30 days. You would like to minimize the cost of storage. What storage option would you recommend?",
  "opts": {
   "A": "Nearline Storage",
   "B": "Coldline Storage",
   "C": "Multi-regional storage",
   "D": "Persistent Disks"
  },
  "correct": "A",
  "correct_text": "Nearline Storage",
  "base": "Nearline Storage is a class of Cloud Storage designed for objects that will be accessed at most once every 30 days. Coldline Storage is suitable for objects accessed at most once per 90 days. Multi-regional storage is best suited for objects that should have low latency access from multiple regions…"
 },
 {
  "id": "test_3_q4",
  "q": "You have a platform on your on-premises environment that generates millions of structured JSON text files totaling 100 GB daily. However, the on-premises environment cannot be accessed from the public internet. You want to explore and query the platform data using Google Cloud products. What is the recommended solution?",
  "opts": {
   "A": "Use Cloud Scheduler to transfer the data daily to Cloud Storage, then import the data into BigQuery using the BigQuery Data Transfer Service.",
   "B": "Use a Transfer Appliance to transfer the data to Cloud Storage, then import the data into BigQuery using the BigQuery Data Transfer Service.",
   "C": "Use Transfer Service for on-premises data to transfer the data to Cloud Storage, then import the data into BigQuery using the BigQuery Data Transfer Service.",
   "D": "Use the BigQuery Data Transfer Service dataset copy feature to directly transfer all data into BigQuery."
  },
  "correct": "C",
  "correct_text": "Use Transfer Service for on-premises data to transfer the data to Cloud Storage, then import the data into BigQuery using the BigQuery Data Transfer Service.",
  "base": "The Transfer Service for on-premises data is designed specifically for securely transferring large volumes of data from on-premises environments to Google Cloud Storage. Since the on-premises environment cannot be accessed from the public internet, this service can be used to establish a secure con…"
 },
 {
  "id": "test_3_q5",
  "q": "How can you migrate a Redis database from an on-premises data center to a Memorystore for Redis instance while following Google-recommended practices and minimizing cost, time, and effort. Which option is the best?",
  "opts": {
   "A": "Backup the Redis database as an RDB file, copy the file to a Cloud Storage bucket using the gsutil utility, and import the file into the Memorystore for Redis instance",
   "B": "Create a secondary instance of the Redis database on a Compute Engine instance, then perform a live cutover.",
   "C": "Use Dataflow to read the Redis database from the on-premises data center and write the data to a Memorystore for Redis instance",
   "D": "Write a shell script to migrate the Redis data and create a new Memorystore for Redis instance."
  },
  "correct": "A",
  "correct_text": "Backup the Redis database as an RDB file, copy the file to a Cloud Storage bucket using the gsutil utility, and import the file into the Memorystore for Redis instance",
  "base": "Option A is the best choice. The recommended practice for migrating a Redis database to Memorystore for Redis is to create an RDB backup of the database, copy the RDB file to Cloud Storage, and then import it into the Memorystore instance. This method is quick and easy to implement and provides min…"
 },
 {
  "id": "test_3_q8",
  "q": "Your organization has 15 TB of data stored in a POSIX-compliant source in your on-premises data center that you need to transfer to Google Cloud. The data changes weekly and your network operations team has granted you 500 Mbps bandwidth to the public internet. You want to follow Google‘s recommended practices for a reliable weekly data transfer. What should you do?",
  "opts": {
   "A": "Use Cloud Scheduler to schedule a weekly transfer of the data using gsutil with the -m parameter for optimal parallelism.",
   "B": "Use Transfer Appliance to transfer the data into a Google Kubernetes Engine cluster and then configure a weekly transfer job.",
   "C": "Install Storage Transfer Service agents on-premises in your data center and configure a weekly transfer job.",
   "D": "Install Storage Transfer Service on a Google Cloud virtual machine and configure a weekly transfer job."
  },
  "correct": "C",
  "correct_text": "Install Storage Transfer Service agents on-premises in your data center and configure a weekly transfer job.",
  "base": "Install Storage Transfer Service agents (for on-premises data in your data center) and then configure a weekly transfer job. Storage Transfer Service is a fully managed and cost-effective service that can handle transferring large amounts of data from on-premises data centers to Google Cloud. With…"
 },
 {
  "id": "test_3_q16",
  "q": "The company currently runs a large on-premises cluster using Spark, Hive, and HDFS and is planning to move to the cloud to benefit from cost savings and to modernize their infrastructure. They have only 2 months for their initial migration due to the timing of their contract renewal with the colocation facility. Which migration strategy should they adopt to maximize cost savings while completing the migration on time?",
  "opts": {
   "A": "Migrate the workloads to Dataproc plus HDFS; modernize later: This option suggests moving the workloads to Dataproc plus HDFS without modernizing and doing so at a later time.",
   "B": "Migrate the workloads to Dataproc plus Cloud Storage; modernize later: This option suggests moving the workloads to Dataproc plus Cloud Storage without modernizing and doing so at a later time",
   "C": "Migrate the Spark workload to Dataproc plus HDFS and modernize the Hive workload for BigQuery: This option suggests migrating the Spark workload to Dataproc plus HDFS and modernizing the Hive workload for BigQuery",
   "D": "Modernize the Spark workload for Dataflow and the Hive workload for BigQuery: This option suggests modernizing the Spark workload for Dataflow and the Hive workload for BigQuery",
   "E": "Migrate the workloads to Dataproc plus Cloud Storage; modernize later: This option provides a good balance between speed and cost savings, allowing the company to meet its deadline while still achieving some cost optimization."
  },
  "correct": "B",
  "correct_text": "Migrate the workloads to Dataproc plus Cloud Storage; modernize later: This option suggests moving the workloads to Dataproc plus Cloud Storage without modernizing and doing so at a later time",
  "base": "Correct Option B. Migrate the workloads to Dataproc plus Cloud Storage; modernize later. Correct because: Cloud Storage is a cost-effective and scalable replacement for HDFS. Migrating Spark and Hive workloads to Dataproc with Cloud Storage allows the company to quickly move off-premises, meet the…"
 },
 {
  "id": "test_3_q24",
  "q": "You need to migrate 2 PB of historical data from an on-premises storage appliance to Cloud Storage within six months. Your outbound network capacity is limited to 20 Mb/sec. How should you perform this migration?",
  "opts": {
   "A": "Use Transfer Appliance to copy the data to Cloud Storage",
   "B": "Compress the content using gsutil cp -J before uploading to Cloud Storage",
   "C": "Create a private URL for the historical data and use Storage Transfer Service to copy the data to Cloud Storage",
   "D": "Use a tool like trickle or ionice with gsutil cp to limit the bandwidth utilization to less than 20 Mb/sec to avoid interfering with production traffic"
  },
  "correct": "A",
  "correct_text": "Use Transfer Appliance to copy the data to Cloud Storage",
  "base": "Correct Option A. Use Transfer Appliance to copy the data to Cloud Storage This is the correct answer. With 2 PB of data and only 20 Mb/sec outbound bandwidth, transferring over the network would take far longer than six months. Google’s Transfer Appliance is specifically designed for large-scale m…"
 },
 {
  "id": "test_4_q21",
  "q": "You have the task of copying millions of sensitive patient records from a relational database with a total size of 10 TB to BigQuery. Your solution must be secure and time-efficient. Which option is the best solution?",
  "opts": {
   "A": "Export the records from the database as an Avro file, upload the file to Google Cloud Storage (GCS) using gsutil, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console",
   "B": "Export the records from the database as an Avro file, copy the file onto a Transfer Appliance, send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.",
   "C": "Export the records from the database into a CSV file, create a public URL for the CSV file, use Storage Transfer Service to move the file to Cloud Storage, and then load the CSV file into BigQuery using the BigQuery web UI in the GCP Console.",
   "D": "Export the records from the database as an Avro file, create a public URL for the Avro file, use Storage Transfer Service to move the file to Cloud Storage, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console."
  },
  "correct": "B",
  "correct_text": "Export the records from the database as an Avro file, copy the file onto a Transfer Appliance, send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.",
  "base": "Correct Option B: Export the records from the database as an Avro file, copy the file onto a Transfer Appliance, send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console. For large datasets (10 TB), Google’s Transfer Appliance is the recommended solu…"
 },
 {
  "id": "test_4_q34",
  "q": "Can you recommend tools for migrating a data warehouse to Google Cloud and ensuring real-time updates to the warehouse from transactional systems. The files being transferred are not large in number but are each 90 GB in size?",
  "opts": {
   "A": "Use Storage Transfer Service for the migration; Pub/Sub and Cloud Data Fusion for real-time updates",
   "B": "Use BigQuery Data Transfer Service for the migration; Pub/Sub and Dataproc for real-time updates",
   "C": "Use gsutil for the migration; Pub/Sub and Dataflow for real-time updates",
   "D": "Use gsutil for both the migration and real-time updates"
  },
  "correct": "C",
  "correct_text": "Use gsutil for the migration; Pub/Sub and Dataflow for real-time updates",
  "base": "The gsutil tool is the standard tool for small- to medium-sized transfers (less than 1 TB) over a typical enterprise-scale network, from a private data center to Google Cloud. Use Gsutil when there is enough bandwidth to meet your project deadline for less than 1 TB of data. Storage Transfer Servic…"
 }
]

<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_06.json  (just the JSON, no backticks).
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
test_4_q44, test_5_q22, test_6_q30, test_7_q46, test_11_q17, test_11_q29, test_13_q7, test_13_q16, test_13_q32, test_14_q6, test_14_q7, test_14_q13, test_14_q19, test_16_q43, test_1_q48, test_5_q39, test_7_q45, test_8_q36, test_15_q53, test_16_q51

Questions:

[
 {
  "id": "test_4_q44",
  "q": "You are tasked with migrating 1 PB of data from an on-premises data center to Google Cloud, with the goal of minimizing transfer time and following Google-recommended best practices for a secure connection. Which option should you choose?",
  "opts": {
   "A": "Use the Storage Transfer Service after establishing a Cloud Interconnect connection between the on-premises data center and Google Cloud",
   "B": "Use a Transfer Appliance and have engineers manually encrypt, decrypt, and verify the data",
   "C": "Establish a Cloud VPN connection, transfer the data using gcloud compute scp jobs in parallel, and run checksums to verify the data.",
   "D": "Transfer the data using gsutil in 3 TB batches, and run checksums to verify the data."
  },
  "correct": "A",
  "correct_text": "Use the Storage Transfer Service after establishing a Cloud Interconnect connection between the on-premises data center and Google Cloud",
  "base": "To transfer a large amount of data (1 PB) within a few hours, it is recommended to use a dedicated network connection like Cloud Interconnect, which can provide higher bandwidth and lower latency compared to using the public internet. The Storage Transfer Service can be used to transfer data betwee…"
 },
 {
  "id": "test_5_q22",
  "q": "You need to copy millions of sensitive patient records from a relational database to BigQuery. The total size of the database is 10 TB. You need to design a solution that is secure and time-efficient. What should you do?",
  "opts": {
   "A": "Export the records from the database as an Avro file. Upload the file to GCS using gsutil, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.",
   "B": "Export the records from the database as an Avro file. Copy the file onto a Transfer Appliance and send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.",
   "C": "Export the records from the database into a CSV file. Create a public URL for the CSV file, and then use Storage Transfer Service to move the file to Cloud Storage. Load the CSV file into BigQuery using the BigQuery web UI in the GCP Console.",
   "D": "Export the records from the database as an Avro file. Create a public URL for the Avro file, and then use Storage Transfer Service to move the file to Cloud Storage. Load the Avro file into BigQuery using the BigQuery web UI in the GCP Console."
  },
  "correct": "B",
  "correct_text": "Export the records from the database as an Avro file. Copy the file onto a Transfer Appliance and send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.",
  "base": "Correct Option B: Export the records from the database as an Avro file. Copy the file onto a Transfer Appliance and send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console. Why it is correct: * Transfer Appliance: For 10 TB of data, a physical Trans…"
 },
 {
  "id": "test_6_q30",
  "q": "You want to migrate an on-premises Hadoop system to Cloud Dataproc. Hive is the primary tool in use, and the data format is Optimized Row Columnar (ORC).All ORC files have been successfully copied to a Cloud Storage bucket. You need to replicate some data to the cluster‘s local Hadoop Distributed File System(HDFS) to maximize performance. What are two ways to start using Hive in Cloud Dataproc? (Choose two.)",
  "opts": {
   "A": "Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to HDFS. Mount the Hive tables locally.",
   "B": "Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to any node of the Dataproc cluster. Mount the Hive tables locally.",
   "C": "Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster. Then run the Hadoop utility to copy them do HDFS. Mount the Hive tables from HDFS.",
   "D": "Leverage Cloud Storage connector for Hadoop to mount the ORC files as external Hive tables. Replicate external Hive tables to the native ones.",
   "E": "Load the ORC files into BigQuery. Leverage BigQuery connector for Hadoop to mount the BigQuery tables as external Hive tables. Replicate external Hive tables to the native ones."
  },
  "correct": "C",
  "correct_text": "Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster. Then run the Hadoop utility to copy them do HDFS. Mount the Hive tables from HDFS.",
  "base": "C. Run the gsutil utility to transfer some ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster. Then run the Hadoop utility to copy them do HDFS. Mount the Hive tables from HDFS. This method leverages a combination of tools: * **gsutil**: The Google Cloud Storage comm…"
 },
 {
  "id": "test_7_q46",
  "q": "You need to move 2 PB of historical data from an on-premises storage appliance to Cloud Storage within six months, and your outbound network capacity is constrained to 20 Mb/sec. How should you migrate this data to Cloud Storage?",
  "opts": {
   "A": "Use Transfer Appliance to copy the data to Cloud Storage",
   "B": "Use gsutil cp ““J to compress the content being uploaded to Cloud Storage",
   "C": "Create a private URL for the historical data, and then use Storage Transfer Service to copy the data to Cloud Storage",
   "D": "Use trickle or ionice along with gsutil cp to limit the amount of bandwidth gsutil utilizes to less than 20 Mb/sec so it does not interfere with the production traffic"
  },
  "correct": "A",
  "correct_text": "Use Transfer Appliance to copy the data to Cloud Storage",
  "base": "Vote for A A – Correct , Transfer Appliance for moving offline data, large data sets, or data from a source with limited bandwidth https://cloud.google.com/storage-transfer/docs/overview B – Eliminated (Not recommended for large storage). recommended for < 1TB C - Its ONLINE, but we have bandwidth…"
 },
 {
  "id": "test_11_q17",
  "q": "A data engineer needs to load data stored in Avro files in Cloud Storage into Bigtable. They would like to have a reliable, easily monitored process for copying the data. What would you recommend they use to copy the data?",
  "opts": {
   "A": "Custom Python 3 program",
   "B": "Storage Transfer Service",
   "C": "Cloud Dataflow, starting with a Cloud Storage Avro to Bigtable template.",
   "D": "gsutil"
  },
  "correct": "C",
  "correct_text": "Cloud Dataflow, starting with a Cloud Storage Avro to Bigtable template.",
  "base": "The correct answer is to use Cloud Dataflow with a Cloud Storage Avro to Bigtable template. Using Python 3 would require more work than necessary. Gsutil is used to load data into Cloud Storage, not Bigtable. Storage Transfer Service is for copying data into Cloud Storage from other object storage…"
 },
 {
  "id": "test_11_q29",
  "q": "How can you design a solution to transfer log data from your set of YouTube channels into Google Cloud for analysis. Your design should allow your global marketing teams to perform ANSI SQL and other types of analysis on the latest YouTube channel log data.?",
  "opts": {
   "A": "Use BigQuery Data Transfer Service to transfer the offsite backup files to a Cloud Storage Regional storage bucket as a final destination",
   "B": "Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination",
   "C": "Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Regional bucket as a final destination.",
   "D": "Use BigQuery Data Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination."
  },
  "correct": "B",
  "correct_text": "Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination",
  "base": "Correct Option B. Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi‑Regional storage bucket as a final destination Correct because: Storage Transfer Service is designed to move large datasets (including logs/backups) into Cloud Storage. Using a Multi‑Regiona…"
 },
 {
  "id": "test_13_q7",
  "q": "Scenario: You are transferring a large number of files from a public HTTPS endpoint to Cloud Storage. The files are secured with signed URLs to prevent unauthorized access. After creating a TSV file containing the object URLs, you initiated a transfer job using Storage Transfer Service. However, the job failed after running for a considerable time. Upon reviewing the logs, you discovered that the job was progressing smoothly until it encountered HTTP 403 errors on the remaining files. You confirmed that there were no modifications made to the source system. What steps should you take to address the issue and continue the migration process smoothly?",
  "opts": {
   "A": "Set up Cloud Storage FUSE, and mount the Cloud Storage bucket on a Compute Engine instance. Remove the completed files from the TSV file. Use a shell script to iterate through the TSV file and download the remaining URLs to the FUSE mount point.",
   "B": "Renew the TLS certificate of the HTTPS endpoint. Remove the completed files from the TSV file and rerun the Storage Transfer Service job.",
   "C": "Create a new TSV file for the remaining files by generating signed URLs with a longer validity period. Split the TSV file into multiple smaller files and submit them as separate Storage Transfer Service jobs in parallel.",
   "D": "Update the file checksums in the TSV file from using MD5 to SHA256. Remove the completed files from the TSV file and rerun the Storage Transfer Service job."
  },
  "correct": "C",
  "correct_text": "Create a new TSV file for the remaining files by generating signed URLs with a longer validity period. Split the TSV file into multiple smaller files and submit them as separate Storage Transfer Service jobs in parallel.",
  "base": "The correct answer is C.– The issue of the HTTP 403 errors on the remaining files is likely due to the expiration of the signed URLs used for accessing the files from the public HTTPS endpoint. Signed URLs have an expiration time after which they become invalid for access.– By creating a new TSV fi…"
 },
 {
  "id": "test_13_q16",
  "q": "Scenario: You have an upstream process that writes data to Cloud Storage. This data is then read by an Apache Spark job that runs on Dataproc. These jobs are run in the us-central1 region, but the data could be stored anywhere in the United States. You need to have a recovery process in place in case of a catastrophic single region failure. What steps should be taken to ensure a maximum of 15 minutes of data loss (RPO=15 mins) and minimal latency when reading the data?",
  "opts": {
   "A": "1. Create two regional Cloud Storage buckets, one in the us-central1 region and one in the us-south1 region. 2. Have the upstream process write data to the us-central1 bucket. Use the Storage Transfer Service to copy data hourly from the us-central1 bucket to the us-south1 bucket. 3. Run the Dataproc cluster in a zone in the us-central1 region, reading from the bucket in that region. 4. In case of regional failure, redeploy your Dataproc clusters to the us-south1 region and read from the bucket in that region instead.",
   "B": "1. Create a Cloud Storage bucket in the US multi-region. 2. Run the Dataproc cluster in a zone in the us-central1 region, reading data from the US multi-region bucket. 3. In case of a regional failure, redeploy the Dataproc cluster to the us-central2 region and continue reading from the same bucket.",
   "C": "1. Create a dual-region Cloud Storage bucket in the us-central1 and us-south1 regions. 2. Enable turbo replication. 3. Run the Dataproc cluster in a zone in the us-central1 region, reading from the bucket in the us-south1 region. 4. In case of a regional failure, redeploy your Dataproc cluster to the us-south1 region and continue reading from the same bucket.",
   "D": "1. Create a dual-region Cloud Storage bucket in the us-central1 and us-south1 regions. 2. Enable turbo replication. 3. Run the Dataproc cluster in a zone in the us-central1 region, reading from the bucket in the same region. 4. In case of a regional failure, redeploy the Dataproc clusters to the us-south1 region and read from the same bucket."
  },
  "correct": "D",
  "correct_text": "1. Create a dual-region Cloud Storage bucket in the us-central1 and us-south1 regions. 2. Enable turbo replication. 3. Run the Dataproc cluster in a zone in the us-central1 region, reading from the bucket in the same re…",
  "base": "The correct answer is Option D:1. Create a dual-region Cloud Storage bucket in the us-central1 and us-south1 regions.2. Enable turbo replication.3. Run the Dataproc cluster in a zone in the us-central1 region, reading from the bucket in the same region.4. In case of a regional failure, redeploy the…"
 },
 {
  "id": "test_13_q32",
  "q": "Scenario: You are creating a fault-tolerant architecture for storing data in a regional BigQuery dataset. Your goal is to enable your application to recover from a corruption event in your tables that happened in the last seven days. What steps should you take to implement a managed service solution with the lowest RPO and cost-effectiveness?",
  "opts": {
   "A": "Access historical data by using time travel in BigQuery.",
   "B": "Export the data from BigQuery into a new table that excludes the corrupted data",
   "C": "Create a BigQuery table snapshot on a daily basis.",
   "D": "Migrate your data to multi-region BigQuery buckets."
  },
  "correct": "A",
  "correct_text": "Access historical data by using time travel in BigQuery.",
  "base": "A. Access historical data by using time travel in BigQuery.– Time travel in BigQuery allows you to query data stored in a table at any point in the past within the past seven days. This feature is helpful in recovering from a corruption event as you can access the historical data before the corrupt…"
 },
 {
  "id": "test_14_q6",
  "q": "Scenario: To migrate a Redis database from an on-premises data center to a Memorystore for Redis instance while adhering to Google-recommended practices and ensuring minimal cost, time, and effort. What steps should be taken to achieve this migration effectively and efficiently?",
  "opts": {
   "A": "Make an RDB backup of the Redis database, use the gsutil utility to copy the RDB file into a Cloud Storage bucket, and then import the RDB file into the Memorystore for Redis instance.",
   "B": "Make a secondary instance of the Redis database on a Compute Engine instance and then perform a live cutover.",
   "C": "Create a Dataflow job to read the Redis database from the on-premises data center and write the data to a Memorystore for Redis instance.",
   "D": "Write a shell script to migrate the Redis data and create a new Memorystore for Redis instance."
  },
  "correct": "A",
  "correct_text": "Make an RDB backup of the Redis database, use the gsutil utility to copy the RDB file into a Cloud Storage bucket, and then import the RDB file into the Memorystore for Redis instance.",
  "base": "A. Make an RDB backup of the Redis database, use the gsutil utility to copy the RDB file into a Cloud Storage bucket, and then import the RDB file into the Memorystore for Redis instance.– Making an RDB backup of the Redis database ensures that the data is backed up in a suitable format for migrati…"
 },
 {
  "id": "test_14_q7",
  "q": "Scenario: You are tasked with transferring 1 PB of data from an on-premises data center to Google Cloud within a few hours while following Google-recommended practices for a secure connection. What steps should be taken to facilitate the secure and efficient transfer of such a large amount of data to Google Cloud within a short timeframe?",
  "opts": {
   "A": "Establish a Cloud Interconnect connection between the on-premises data center and Google Cloud, and then use the Storage Transfer Service.",
   "B": "Use a Transfer Appliance and have engineers manually encrypt, decrypt, and verify the data.",
   "C": "Establish a Cloud VPN connection, start gcloud compute scp jobs in parallel, and run checksums to verify the data.",
   "D": "Reduce the data into 3 TB batches, transfer the data using gsutil, and run checksums to verify the data."
  },
  "correct": "A",
  "correct_text": "Establish a Cloud Interconnect connection between the on-premises data center and Google Cloud, and then use the Storage Transfer Service.",
  "base": "A. Establish a Cloud Interconnect connection between the on-premises data center and Google Cloud, and then use the Storage Transfer Service.– Cloud Interconnect provides a dedicated, high-throughput, low-latency connection between on-premises networks and Google Cloud. This ensures a secure and ef…"
 },
 {
  "id": "test_14_q13",
  "q": "Scenario: You have 15 TB of data in your on-premises data center that needs to be transferred to Google Cloud. The data changes weekly and is stored in a POSIX-compliant source. Your network operations team has provided you with 500 Mbps bandwidth to the public internet. How can you follow Google-recommended practices to reliably transfer your 15 TB of data to Google Cloud on a weekly basis?",
  "opts": {
   "A": "Use Cloud Scheduler to trigger the gsutil command. Use the -m parameter for optimal parallelism.",
   "B": "Use Transfer Appliance to migrate your data into a Google Kubernetes Engine cluster, and then configure a weekly transfer job.",
   "C": "Install Storage Transfer Service for on-premises data in your data center, and then configure a weekly transfer job.",
   "D": "Install Storage Transfer Service for on-premises data on a Google Cloud virtual machine, and then configure a weekly transfer job."
  },
  "correct": "C",
  "correct_text": "Install Storage Transfer Service for on-premises data in your data center, and then configure a weekly transfer job.",
  "base": "The correct answer is C. Install Storage Transfer Service for on-premises data in your data center, and then configure a weekly transfer job.Using Storage Transfer Service for on-premises data in your data center is the recommended approach for transferring data from an on-premises environment to G…"
 },
 {
  "id": "test_14_q19",
  "q": "Scenario: Your on-premises environment generates 100 GB of data daily, consisting of millions of structured JSON text files. This environment is not accessible from the public internet. How can you leverage Google Cloud products to query and explore the data from your on-premises platform?",
  "opts": {
   "A": "Use Cloud Scheduler to copy data daily from your on-premises environment to Cloud Storage. Use the BigQuery Data Transfer Service to import data into BigQuery.",
   "B": "Use a Transfer Appliance to copy data from your on-premises environment to Cloud Storage. Use the BigQuery Data Transfer Service to import data into BigQuery.",
   "C": "Use Transfer Service for on-premises data to copy data from your on-premises environment to Cloud Storage. Use the BigQuery Data Transfer Service to import data into BigQuery.",
   "D": "Use the BigQuery Data Transfer Service dataset copy to transfer all data into BigQuery."
  },
  "correct": "C",
  "correct_text": "Use Transfer Service for on-premises data to copy data from your on-premises environment to Cloud Storage. Use the BigQuery Data Transfer Service to import data into BigQuery.",
  "base": "The correct answer is C: Use Transfer Service for on-premises data to copy data from your on-premises environment to Cloud Storage. Use the BigQuery Data Transfer Service to import data into BigQuery.1. Transfer Service for on-premises data allows you to securely transfer data from your on-premises…"
 },
 {
  "id": "test_16_q43",
  "q": "Scenario: You have 2 PB of historical data stored in an on-premises storage appliance that needs to be moved to Cloud Storage within six months. Your outbound network capacity is limited to 20 Mb/sec. What is the best approach to migrate this data to Cloud Storage considering the network constraints and timeframe?",
  "opts": {
   "A": "Use Transfer Appliance to copy the data to Cloud Storage",
   "B": "Use gsutil cp ?“J to compress the content being uploaded to Cloud Storage",
   "C": "Create a private URL for the historical data, and then use Storage Transfer Service to copy the data to Cloud Storage",
   "D": "Use trickle or ionice along with gsutil cp to limit the amount of bandwidth gsutil utilizes to less than 20 Mb/sec so it does not interfere with the production traffic"
  },
  "correct": "A",
  "correct_text": "Use Transfer Appliance to copy the data to Cloud Storage",
  "base": "A. Use Transfer Appliance to copy the data to Cloud Storage.Using Transfer Appliance is the best option for moving 2 PB of historical data within six months when the outbound network capacity is constrained to 20 Mb/sec. Transfer Appliance is a physical storage appliance provided by Google Cloud th…"
 },
 {
  "id": "test_1_q48",
  "q": "A data warehouse team is concerned that some data sources may have poor quality controls. They do not want to bring incorrect or invalid data into the data warehouse. What could they do to understand the scope of the problem before starting to write ETL code?",
  "opts": {
   "A": "Have administrators of the source systems produce a data quality verification before exporting the data.",
   "B": "Load all source data into a data lake and then load it to the data warehouse.",
   "C": "Perform a data quality assessment on the source data after it is extracted from the source system. These should include checks for ranges of values in each attribute, distribution of values in each attribute, counts of the number of invalid and missing values, and other checks on source data.",
   "D": "Load the data into the data warehouse and log any records that fail integrity or consistency checks."
  },
  "correct": "C",
  "correct_text": "Perform a data quality assessment on the source data after it is extracted from the source system. These should include checks for ranges of values in each attribute, distribution of values in each attribute, counts of…",
  "base": "The correct answer is performing a data quality assessment on data extracted from the source system. Loading data from a data lake to a data warehouse will not provide an assessment of the range of the problem. Loading data into the data warehouse and logging failed checks is less efficient because…"
 },
 {
  "id": "test_5_q39",
  "q": "You work for an economic consulting firm that helps companies identify economic trends as they happen. As part of your analysis, you use Google BigQuery to correlate customer data with the average prices of the 100 most common goods sold, including bread, gasoline, milk, and others. The average prices of these goods are updated every 30 minutes. You want to make sure this data stays up to date so you can combine it with other data in BigQuery as cheaply as possible.What should you do?",
  "opts": {
   "A": "Load the data every 30 minutes into a new partitioned table in BigQuery.",
   "B": "Store and update the data in a regional Google Cloud Storage bucket and create a federated data source in BigQuery",
   "C": "Store the data in Google Cloud Datastore. Use Google Cloud Dataflow to query BigQuery and combine the data programmatically with the data stored in Cloud Datastore",
   "D": "Store the data in a file in a regional Google Cloud Storage bucket. Use Cloud Dataflow to query BigQuery and combine the data programmatically with the data stored in Google Cloud Storage."
  },
  "correct": "B",
  "correct_text": "Store and update the data in a regional Google Cloud Storage bucket and create a federated data source in BigQuery",
  "base": "B is correct. This is one of the use cases for external (federated) data sources in BigQuery: “Small amount of frequently changing data to join with other tables in BigQuery“. https://cloud.google.com/blog/products/gcp/accessing-external-federated-data-sources-with-bigquerys-data-access-layer"
 },
 {
  "id": "test_7_q45",
  "q": "You are planning to use Google‘s Dataflow SDK to analyze customer data such as displayed below. Your project requirement is to extract only the customer name from the data source and then write to an output PCollection.Tom,555 X street -Tim,553 Y street -Sam, 111 Z street -Which operation is best suited for the above data processing requirement?",
  "opts": {
   "A": "ParDo",
   "B": "Sink API",
   "C": "Source API",
   "D": "Data extraction"
  },
  "correct": "A",
  "correct_text": "ParDo",
  "base": "In Google Cloud dataflow SDK, you can use the ParDo to extract only a customer name of each element in your PCollection. Reference: https://cloud.google.com/dataflow/model/par-do"
 },
 {
  "id": "test_8_q36",
  "q": "When running a pipeline that has a BigQuery source, on your local machine, you continue to get permission denied errors. What could be the reason for that?",
  "opts": {
   "A": "Your gcloud does not have access to the BigQuery resources",
   "B": "BigQuery cannot be accessed from local machines",
   "C": "You are missing gcloud on your machine",
   "D": "Pipelines cannot be run locally"
  },
  "correct": "A",
  "correct_text": "Your gcloud does not have access to the BigQuery resources",
  "base": "When reading from a Dataflow source or writing to a Dataflow sink using DirectPipelineRunner, the Cloud Platform account that you configured with the gcloud executable will need access to the corresponding source/sink Reference: https://cloud.google.com/dataflow/java-sdk/JavaDoc/com/google/cloud/da…"
 },
 {
  "id": "test_15_q53",
  "q": "Scenario: New website users need to be assigned a globally unique identifier (GUID) by a service that generates GUIDs based on data points from internal and external systems. The data is obtained through HTTP calls made via microservices within the pipeline, with tens of thousands of messages per second being processed in a multi-threaded environment. What pipeline design should be implemented to reduce backpressure on the system under these circumstances?",
  "opts": {
   "A": "Call out to the service via HTTP.",
   "B": "Create the pipeline statically in the class definition.",
   "C": "Create a new object in the startBundle method of DoFn.",
   "D": "Batch the job into ten-second increments."
  },
  "correct": "D",
  "correct_text": "Batch the job into ten-second increments.",
  "base": "The correct option is D. Batch the job into ten-second increments.By batching the job into ten-second increments, you can limit the number of HTTP calls made to the service for generating GUIDs. This approach allows you to process a batch of data points at once, reducing the frequency of HTTP calls…"
 },
 {
  "id": "test_16_q51",
  "q": "Analysts are using Cloud Data Studio for analyzing data sets. They would like to improve the performance of the time required to update tables and charts when working with the data. What would you recommend they try to improve performance?",
  "opts": {
   "A": "Use a live data source",
   "B": "Use an imported data source",
   "C": "Use an extracted data source",
   "D": "Use a blended data source"
  },
  "correct": "C",
  "correct_text": "Use an extracted data source",
  "base": "Extracted data sources are snapshots and can provide better performance than live data sources. Blended data sources are used to combine data from multiple data sources. There is no imported data source. See https://cloud.google.com/bigquery/external-data-sources"
 }
]

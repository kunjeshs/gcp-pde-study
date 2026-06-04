<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_04.json  (just the JSON, no backticks).
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
test_15_q35, test_15_q40, test_15_q51, test_15_q59, test_16_q26, test_16_q41, test_1_q11, test_3_q7, test_5_q18, test_7_q34, test_8_q10, test_10_q19, test_11_q11, test_11_q28, test_13_q11, test_13_q19, test_13_q24, test_13_q58, test_14_q14, test_14_q39

Questions:

[
 {
  "id": "test_15_q35",
  "q": "Scenario: You are troubleshooting a Dataflow pipeline that transfers data from Cloud Storage to BigQuery. The Dataflow worker nodes are unable to communicate with each other. Your networking team uses Google Cloud network tags for defining firewall rules. What steps should you take to identify the issue while adhering to Google-recommended networking security practices?",
  "opts": {
   "A": "Determine whether your Dataflow pipeline has a custom network tag set.",
   "B": "Determine whether there is a firewall rule set to allow traffic on TCP ports 12345 and 12346 for the Dataflow network tag.",
   "C": "Determine whether there is a firewall rule set to allow traffic on TCP ports 12345 and 12346 on the subnet used by Dataflow workers.",
   "D": "Determine whether your Dataflow pipeline is deployed with the external IP address option enabled."
  },
  "correct": "B",
  "correct_text": "Determine whether there is a firewall rule set to allow traffic on TCP ports 12345 and 12346 for the Dataflow network tag.",
  "base": "The correct answer is B. Determine whether there is a firewall rule set to allow traffic on TCP ports 12345 and 12346 for the Dataflow network tag.In this scenario, the issue is that the Dataflow worker nodes cannot communicate with each other. To allow communication between the Dataflow worker nod…"
 },
 {
  "id": "test_15_q40",
  "q": "Scenario: You work for a financial institution that allows customers to register online. As new customers register, their user data is sent to Pub/Sub before being ingested into BigQuery. For security purposes, you need to redact customers‘ Government issued Identification Numbers while enabling customer service representatives to view the original values when required. What steps should you take to achieve this?",
  "opts": {
   "A": "Use BigQuery‘s built-in AEAD encryption to encrypt the SSN column. Save the keys to a new table that is only viewable by permissioned users.",
   "B": "Use BigQuery column-level security. Set the table permissions so that only members of the Customer Service user group can see the SSN column.",
   "C": "Before loading the data into BigQuery, use Cloud Data Loss Prevention (DLP) to replace input values with a cryptographic hash.",
   "D": "Before loading the data into BigQuery, use Cloud Data Loss Prevention (DLP) to replace input values with a cryptographic format-preserving encryption token."
  },
  "correct": "D",
  "correct_text": "Before loading the data into BigQuery, use Cloud Data Loss Prevention (DLP) to replace input values with a cryptographic format-preserving encryption token.",
  "base": "The correct answer is D. Before loading the data into BigQuery, use Cloud Data Loss Prevention (DLP) to replace input values with a cryptographic format-preserving encryption token.By using Cloud Data Loss Prevention (DLP) to replace input values with a cryptographic format-preserving encryption to…"
 },
 {
  "id": "test_15_q51",
  "q": "Scenario: Building a real-time prediction engine that streams files, potentially containing PII data, into Cloud Storage and then into BigQuery. Priority is to mask sensitive data while maintaining referential integrity, as names and emails are common join keys. How can the Cloud Data Loss Prevention API (DLP API) be utilized to prevent unauthorized access to PII data in this scenario?",
  "opts": {
   "A": "Create a pseudonym by replacing the PII data with cryptogenic tokens, and store the non-tokenized data in a locked-down button.",
   "B": "Redact all PII data, and store a version of the unredacted data in a locked-down bucket.",
   "C": "Scan every table in BigQuery, and mask the data it finds that has PII.",
   "D": "Create a pseudonym by replacing PII data with a cryptographic format-preserving token."
  },
  "correct": "D",
  "correct_text": "Create a pseudonym by replacing PII data with a cryptographic format-preserving token.",
  "base": "The correct answer is D. Create a pseudonym by replacing PII data with a cryptographic format-preserving token.Using a cryptographic format-preserving token to replace PII data ensures that sensitive information is masked while still maintaining referential integrity. This method allows you to pres…"
 },
 {
  "id": "test_15_q59",
  "q": "Scenario: The Development and External teams have the project viewer Identity and Access Management (IAM) role in a folder named Visualization. How can you allow the Development Team to read data from both Cloud Storage and BigQuery, while restricting the External Team to only read data from BigQuery?",
  "opts": {
   "A": "Remove Cloud Storage IAM permissions to the External Team on the acme-raw-data project.",
   "B": "Create Virtual Private Cloud (VPC) firewall rules on the acme-raw-data project that deny all ingress traffic from the External Team CIDR range.",
   "C": "Create a VPC Service Controls perimeter containing both projects and BigQuery as a restricted API. Add the External Team users to the perimeter‘s Access Level.",
   "D": "Create a VPC Service Controls perimeter containing both projects and Cloud Storage as a restricted API. Add the Development Team users to the perimeter‘s Access Level."
  },
  "correct": "D",
  "correct_text": "Create a VPC Service Controls perimeter containing both projects and Cloud Storage as a restricted API. Add the Development Team users to the perimeter‘s Access Level.",
  "base": "The correct answer is D. Create a VPC Service Controls perimeter containing both projects and Cloud Storage as a restricted API. Add the Development Team users to the perimeter’s Access Level. – By creating a VPC Service Controls perimeter containing both projects and Cloud Storage as a restricted…"
 },
 {
  "id": "test_16_q26",
  "q": "Scenario: You need to store data in Cloud Storage and wish to encrypt it using the ′Trust No One′ (TNO) approach to ensure the security of sensitive information. What steps should you take to prevent the cloud provider staff from decrypting your data while using the ′Trust No One′ approach for encryption?",
  "opts": {
   "A": "Use gcloud kms keys create to create a symmetric key. Then use gcloud kms encrypt to encrypt each archival file with the key and unique additional authenticated data (AAD). Use gsutil cp to upload each encrypted file to the Cloud Storage bucket, and keep the AAD outside of Google Cloud.",
   "B": "Use gcloud kms keys create to create a symmetric key. Then use gcloud kms encrypt to encrypt each archival file with the key. Use gsutil cp to upload each encrypted file to the Cloud Storage bucket. Manually destroy the key previously used for encryption, and rotate the key once.",
   "C": "Specify customer-supplied encryption key (CSEK) in the .boto configuration file. Use gsutil cp to upload each archival file to the Cloud Storage bucket. Save the CSEK in Cloud Memorystore as permanent storage of the secret.",
   "D": "Specify customer-supplied encryption key (CSEK) in the .boto configuration file. Use gsutil cp to upload each archival file to the Cloud Storage bucket. Save the CSEK in a different project that only the security team can access."
  },
  "correct": "A",
  "correct_text": "Use gcloud kms keys create to create a symmetric key. Then use gcloud kms encrypt to encrypt each archival file with the key and unique additional authenticated data (AAD). Use gsutil cp to upload each encrypted file to…",
  "base": "Correct Option A. Reasoning: The Trust No One approach requires that Google Cloud staff cannot decrypt your data. By encrypting files before uploading with your own symmetric key and keeping AAD outside Google Cloud, you ensure that only you can decrypt the data. This aligns with TNO principles: en…"
 },
 {
  "id": "test_16_q41",
  "q": "Scenario: In order to deploy additional dependencies to all nodes of a Cloud Dataproc cluster at startup, you need to use an existing initialization action. However, the company‘s security policies dictate that Cloud Dataproc nodes must not have Internet access for fetching resources. What steps should be taken to address this issue?",
  "opts": {
   "A": "Deploy the Cloud SQL Proxy on the Cloud Dataproc master",
   "B": "Use an SSH tunnel to give the Cloud Dataproc cluster access to the Internet",
   "C": "Copy all dependencies to a Cloud Storage bucket within your VPC security perimeter",
   "D": "Use Resource Manager to add the service account used by the Cloud Dataproc cluster to the Network User role"
  },
  "correct": "C",
  "correct_text": "Copy all dependencies to a Cloud Storage bucket within your VPC security perimeter",
  "base": "The correct answer is C. Copy all dependencies to a Cloud Storage bucket within your VPC security perimeter.By copying all dependencies to a Cloud Storage bucket within your VPC security perimeter, you can ensure that the Cloud Dataproc nodes can access the required dependencies during startup with…"
 },
 {
  "id": "test_1_q11",
  "q": "You are tasked with selecting a NoSQL database to handle telemetry data from millions of IoT devices. The volume of data is increasing at a rate of 100 TB per year, and each data entry has approximately 100 attributes. The data processing pipeline does not require ACID compliance, but high availability and low latency are crucial. You need to query individual fields in the data for analysis. Which three databases are suitable for this purpose. (Choose three from the following options)?",
  "opts": {
   "A": "Redis",
   "B": "HBase",
   "C": "MySQL",
   "D": "MongoDB",
   "E": "Cassandra",
   "F": "HDFS with Hive"
  },
  "correct": "B",
  "correct_text": "HBase",
  "base": "The three NoSQL databases suitable for handling telemetry data from millions of IoT devices, given the volume, attributes, and requirements, are: MongoDB: Flexible schema: MongoDB’s flexible schema model allows for easy addition and modification of attributes, which is crucial for handling evolving…"
 },
 {
  "id": "test_3_q7",
  "q": "How can you design an ACID-compliant database system that requires minimal human intervention in the event of a failure. (Choose one option from the following:)?",
  "opts": {
   "A": "Configure a Cloud SQL for MySQL instance with point-in-time recovery enabled.",
   "B": "Configure a Cloud SQL for PostgreSQL instance with high availability enabled.",
   "C": "Configure a Bigtable instance with more than one cluster.",
   "D": "Configure a BigQuery table with a multi-region configuration."
  },
  "correct": "B",
  "correct_text": "Configure a Cloud SQL for PostgreSQL instance with high availability enabled.",
  "base": "Configuring a Cloud SQL for PostgreSQL instance with high availability ensures minimal human intervention in case of a failure as it provides automatic failover to a standby replica instance in a different zone. This option also ensures that the database remains ACID-compliant. The other options do…"
 },
 {
  "id": "test_5_q18",
  "q": "You have a data stored in BigQuery. The data in the BigQuery dataset must be highly available. You need to define a storage, backup, and recovery strategy of this data that minimizes cost. How should you configure the BigQuery table?",
  "opts": {
   "A": "Set the BigQuery dataset to be regional. In the event of an emergency, use a point-in-time snapshot to recover the data.",
   "B": "Set the BigQuery dataset to be regional. Create a scheduled query to make copies of the data to tables suffixed with the time of the backup. In the event of an emergency, use the backup copy of the table.",
   "C": "Set the BigQuery dataset to be multi-regional. In the event of an emergency, use a point-in-time snapshot to recover the data.",
   "D": "Set the BigQuery dataset to be multi-regional. Create a scheduled query to make copies of the data to tables suffixed with the time of the backup. In the event of an emergency, use the backup copy of the table."
  },
  "correct": "C",
  "correct_text": "Set the BigQuery dataset to be multi-regional. In the event of an emergency, use a point-in-time snapshot to recover the data.",
  "base": "Correct Option C. Set the BigQuery dataset to be multi-regional. In the event of an emergency, use a point-in-time snapshot to recover the data. Correct because: Multi-regional datasets in BigQuery automatically replicate data across multiple regions, ensuring high availability and disaster recover…"
 },
 {
  "id": "test_7_q34",
  "q": "You are choosing a NoSQL database to handle telemetry data submitted from millions of Internet-of-Things (IoT) devices. The volume of data is growing at 100TB per year, and each data entry has about 100 attributes. The data processing pipeline does not require atomicity, consistency, isolation, and durability (ACID).However, high availability and low latency are required.You need to analyze the data by querying against individual fields. Which three databases meet your requirements? (Choose three.)",
  "opts": {
   "A": "Redis",
   "B": "HBase",
   "C": "MySQL",
   "D": "MongoDB",
   "E": "Cassandra",
   "F": "HDFS with Hive"
  },
  "correct": "B",
  "correct_text": "HBase",
  "base": "Answer is BDE – A. Redis – Redis is an in-memory non-relational key-value store. Redis is a great choice for implementing a highly available in-memory cache to decrease data access latency, increase throughput, and ease the load off your relational or NoSQL database and application. Since the quest…"
 },
 {
  "id": "test_8_q10",
  "q": "What is the recommended way to ensure high availability in the event of a zone failure when deploying Cloud SQL using MySQL?",
  "opts": {
   "A": "Create a Cloud SQL instance in one zone, and create a read replica in another zone within the same region",
   "B": "Create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region.",
   "C": "Create a Cloud SQL instance in one zone, and configure an external read replica in a zone in a different region",
   "D": "Create a Cloud SQL instance in a region, and configure automatic backup to a Cloud Storage bucket in the same region."
  },
  "correct": "B",
  "correct_text": "Create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region.",
  "base": "The recommended way to ensure high availability in the event of a zone failure when deploying Cloud SQL using MySQL is to create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region (Option A). T his provides automatic failover to the replica instan…"
 },
 {
  "id": "test_10_q19",
  "q": "You have uploaded 5 years of log data to Cloud Storage. A user reported that some data points in the log data are outside of their expected ranges, indicating errors. You need to fix this issue and ensure that the original data is retained for compliance reasons. What should you do?",
  "opts": {
   "A": "Use a Dataflow workflow to read the data from Cloud Storage, identify and correct values outside the expected range, and write the updated data to a new dataset in Cloud Storage",
   "B": "Import the data from Cloud Storage to BigQuery, create a new table, and remove the rows with errors",
   "C": "Use a Dataflow workflow to read the data from Cloud Storage, identify and correct values outside the expected range, and overwrite the original dataset in Cloud Storage.",
   "D": ". Create a new copy of the data in Cloud Storage using a Compute Engine instance, and remove the rows with errors"
  },
  "correct": "A",
  "correct_text": "Use a Dataflow workflow to read the data from Cloud Storage, identify and correct values outside the expected range, and write the updated data to a new dataset in Cloud Storage",
  "base": "The correct answer is: Use a Dataflow workflow to read the data from Cloud Storage, identify and correct values outside the expected range, and write the updated data to a new dataset in Cloud Storage. Here’s why: Dataflow workflow: This is a scalable and managed service that can efficiently proces…"
 },
 {
  "id": "test_11_q11",
  "q": "As a database administrator, you are finding that a Cloud SQL database using PostgreSQL is not meeting read operation SLAs. You want to improve performance with minimal changes to database applications. What would you try first to improve read performance?",
  "opts": {
   "A": "Use Cloud Memorystore to cache data to be read.",
   "B": "Use change data capture to keep a second database in a different region in synch with the primary database while having read operations sent to the secondary database.",
   "C": "Use PostgreSQL‘s explain plan feature to analyze queries and rewrite them to improve performance.",
   "D": "Create a read replica."
  },
  "correct": "D",
  "correct_text": "Create a read replica.",
  "base": "The correct answer is to create a read replica for read operations. Using a cache could improve read performance but would require changes to database applications. Using a secondary database would require changes to the application to read from the secondary database instead of the primary. Using…"
 },
 {
  "id": "test_11_q28",
  "q": "As the architect of a seismic data analysis system that utilizes an Apache Hadoop cluster for its ETL process, you encounter an issue where the ETL process takes several days to process a data set due to the computational complexity of some steps. After investigating the issue, you discover that the sensor calibration step has been omitted. To ensure that sensor calibration is carried out systematically in the future, which of the following actions should you take?",
  "opts": {
   "A": "Develop an algorithm that uses simulation to predict the variance of the data output from the last MapReduce job based on calibration factors, and then apply the correction to all data",
   "B": "Append sensor calibration data to the output of the ETL process, and provide documentation for users to apply sensor calibration themselves",
   "C": "Modify the existing MapReduce jobs to apply sensor calibration before anything else is done.",
   "D": "Add a new MapReduce job to apply sensor calibration to the raw data, and ensure that all other MapReduce jobs are chained after this step."
  },
  "correct": "D",
  "correct_text": "Add a new MapReduce job to apply sensor calibration to the raw data, and ensure that all other MapReduce jobs are chained after this step.",
  "base": "Correct Option D: text Add a new MapReduce job to apply sensor calibration to the raw data, and ensure that all other MapReduce jobs are chained after this step. Explanation: This is the best practice. Calibration should be applied up front to raw data so that all downstream jobs operate on correct…"
 },
 {
  "id": "test_13_q11",
  "q": "Scenario: In a production environment, there is a Standard Tier Memorystore for Redis instance deployed. What steps should be taken to simulate a Redis instance failover in a disaster recovery situation accurately without impacting production data?",
  "opts": {
   "A": "Create a Standard Tier Memorystore for Redis instance in the development environment. Initiate a manual failover by using the limited-data-loss data protection mode.",
   "B": "Create a Standard Tier Memorystore for Redis instance in a development environment. Initiate a manual failover by using the force-data-loss data protection mode.",
   "C": "Increase one replica to Redis instance in production environment. Initiate a manual failover by using the force-data-loss data protection mode.",
   "D": "Initiate a manual failover by using the limited-data-loss data protection mode to the Memorystore for Redis instance in the production environment."
  },
  "correct": "B",
  "correct_text": "Create a Standard Tier Memorystore for Redis instance in a development environment. Initiate a manual failover by using the force-data-loss data protection mode.",
  "base": "The correct answer is B: Create a Standard Tier Memorystore for Redis instance in a development environment. Initiate a manual failover by using the force-data-loss data protection mode.– Creating a Standard Tier Memorystore for Redis instance in a development environment allows you to simulate a f…"
 },
 {
  "id": "test_13_q19",
  "q": "Scenario: You have a Cloud SQL for PostgreSQL instance in Region‘ with one read replica in Region2 and another read replica in Region3. An unexpected event in Region‘ requires that you perform disaster recovery by promoting a read replica in Region2. What steps should you take to ensure that your application has the same database capacity available before switching over the connections?",
  "opts": {
   "A": "Enable zonal high availability on the primary instance. Create a new read replica in a new region.",
   "B": "Create a cascading read replica from the existing read replica in Region3.",
   "C": "Create two new read replicas from the new primary instance, one in Region3 and one in a new region.",
   "D": "Create a new read replica in Region1, promote the new read replica to be the primary instance, and enable zonal high availability."
  },
  "correct": "C",
  "correct_text": "Create two new read replicas from the new primary instance, one in Region3 and one in a new region.",
  "base": "The correct answer is C. Create two new read replicas from the new primary instance, one in Region3 and one in a new region.To ensure that your application has the same database capacity available before switching over the connections, you need to create new read replicas from the promoted read rep…"
 },
 {
  "id": "test_13_q24",
  "q": "Scenario – You are tasked with designing a highly available and fault-tolerant architecture for a web application on Google Cloud Platform. Which architectural choices should you consider to achieve these goals?",
  "opts": {
   "A": "Deploy the web application on a single Compute Engine instance in a single zone.",
   "B": "Use Cloud Load Balancing to distribute incoming traffic across multiple Compute Engine instances in the same zone.",
   "C": "Utilize Cloud CDN to cache and deliver content closer to users, reducing latency and improving availability.",
   "D": "Store application data in a single Cloud SQL instance with automated backups enabled."
  },
  "correct": "B",
  "correct_text": "Use Cloud Load Balancing to distribute incoming traffic across multiple Compute Engine instances in the same zone.",
  "base": "Deploy the web application on a single Compute Engine instance in a single zone. This is not highly available or fault tolerant because if that instance or zone fails, the application goes down. Incorrect for HA/FT. Use Cloud Load Balancing to distribute incoming traffic across multiple Compute Eng…"
 },
 {
  "id": "test_13_q58",
  "q": "Scenario: Working for a large ecommerce company, you use Pub/Sub to ingest clickstream data to Google Cloud for analytics. You notice that new subscribers connecting to an existing topic cannot subscribe to older data. With an upcoming yearly sale event in two months, you require a solution that allows new subscribers to access the last 30 days of data once implemented. What steps should be taken to enable any new subscriber to read the last 30 days of data for the upcoming yearly sale event in two months, considering the issue with existing subscribers not being able to subscribe to older data?",
  "opts": {
   "A": "Create a new topic, and publish the last 30 days of data each time a new subscriber connects to an existing topic.",
   "B": "Set the topic retention policy to 30 days.",
   "C": "Set the subscriber retention policy to 30 days.",
   "D": "Ask the source system to re-push the data to Pub/Sub, and subscribe to it."
  },
  "correct": "B",
  "correct_text": "Set the topic retention policy to 30 days.",
  "base": "The correct answer is B. Set the topic retention policy to 30 days.By setting the topic retention policy to 30 days, Pub/Sub will retain messages in the topic for 30 days. This means that any new subscriber connecting to the topic will be able to read the last 30 days of data. This solution ensures…"
 },
 {
  "id": "test_14_q14",
  "q": "Scenario: You are developing a system that necessitates an ACID-compliant database. It is crucial that the system minimizes the need for human intervention in the event of a failure. What steps should be taken to achieve this goal?",
  "opts": {
   "A": "Configure a Cloud SQL for MySQL instance with point-in-time recovery enabled.",
   "B": "Configure a Cloud SQL for PostgreSQL instance with high availability enabled.",
   "C": "Configure a Bigtable instance with more than one cluster.",
   "D": "Configure a BigQuery table with a multi-region configuration."
  },
  "correct": "B",
  "correct_text": "Configure a Cloud SQL for PostgreSQL instance with high availability enabled.",
  "base": "The correct answer is B. Configure a Cloud SQL for PostgreSQL instance with high availability enabled.1. ACID-compliance: ACID stands for Atomicity, Consistency, Isolation, and Durability. PostgreSQL is known for its robust support for ACID compliance, making it a suitable choice for systems that r…"
 },
 {
  "id": "test_14_q39",
  "q": "Scenario: You have important legal hold documents stored in a Cloud Storage bucket. What steps should you take to prevent these documents from being deleted or modified?",
  "opts": {
   "A": "Set a retention policy. Lock the retention policy.",
   "B": "Set a retention policy. Set the default storage class to Archive for long-term digital preservation.",
   "C": "Enable the Object Versioning feature. Add a lifecycle rule.",
   "D": "Enable the Object Versioning feature. Create a copy in a bucket in a different region."
  },
  "correct": "A",
  "correct_text": "Set a retention policy. Lock the retention policy.",
  "base": "A. Set a retention policy. Lock the retention policy.Setting a retention policy on the Cloud Storage bucket ensures that the documents are not deleted or modified for a specific period of time. Locking the retention policy prevents any changes or deletions to the documents until the retention perio…"
 }
]

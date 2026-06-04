<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_20.json  (just the JSON, no backticks).
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
test_6_q25, test_6_q43, test_7_q11, test_7_q16, test_7_q33, test_7_q40, test_8_q31, test_8_q43, test_9_q16, test_12_q26, test_13_q8, test_13_q12, test_13_q17, test_13_q25, test_14_q23, test_14_q28, test_14_q47, test_14_q52, test_15_q4, test_15_q6

Questions:

[
 {
  "id": "test_6_q25",
  "q": "You are migrating your data warehouse to BigQuery. You have migrated all of your data into tables in a dataset. Multiple users from your organization will be using the data. They should only see certain tables based on their team membership. How should you set user permissions?",
  "opts": {
   "A": "Assign the users/groups data viewer access at the table level for each table",
   "B": "Create SQL views for each team in the same dataset in which the data resides, and assign the users/groups data viewer access to the SQL views",
   "C": "Create authorized views for each team in the same dataset in which the data resides, and assign the users/groups data viewer access to the authorized views",
   "D": "Create authorized views for each team in datasets created for each team. Assign the authorized views data viewer access to the dataset in which the data resides. Assign the users/groups data viewer access to the datasets in which the authorized views reside"
  },
  "correct": "C",
  "correct_text": "Create authorized views for each team in the same dataset in which the data resides, and assign the users/groups data viewer access to the authorized views",
  "base": "Correct Option C: Create authorized views for each team in the same dataset in which the data resides, and assign the users/groups data viewer access to the authorized views The Logic: An Authorized View allows you to restrict access at a granular level (rows or columns) or to specific tables withi…"
 },
 {
  "id": "test_6_q43",
  "q": "Which SQL keyword can be used to reduce the number of columns processed by BigQuery?",
  "opts": {
   "A": "BETWEEN",
   "B": "WHERE",
   "C": "SELECT",
   "D": "LIMIT"
  },
  "correct": "C",
  "correct_text": "SELECT",
  "base": "SELECT allows you to query specific columns rather than the whole table. LIMIT, BETWEEN, and WHERE clauses will not reduce the number of columns processed by BigQuery. Reference: https://cloud.google.com/bigquery/launch-checklist#architecture_design_and_development_checklist"
 },
 {
  "id": "test_7_q11",
  "q": "You launched a new gaming app almost three years ago. You have been uploading log files from the previous day to a separate Google BigQuery table with the table name format LOGS_yyyymmdd. You have been using table wildcard functions to generate daily and monthly reports for all time ranges. Recently, you discovered that some queries that cover long date ranges are exceeding the limit of 1,000 tables and failing. How can you resolve this issue?",
  "opts": {
   "A": "Convert all daily log tables into date-partitioned tables",
   "B": "Convert the sharded tables into a single partitioned table",
   "C": "Enable query caching so you can cache data from previous months",
   "D": "Create separate views to cover each month, and query from these views"
  },
  "correct": "B",
  "correct_text": "Convert the sharded tables into a single partitioned table",
  "base": "Let’s analyze each option to determine the best solution: A. Convert all daily log tables into date-partitioned tables: This is a strong option. By converting the daily tables into a single date-partitioned table, you eliminate the need to query numerous separate tables. BigQuery’s partitioning all…"
 },
 {
  "id": "test_7_q16",
  "q": "You are designing storage for 20 TB of text files as part of deploying a data pipeline on Google Cloud. Your input data is in CSV format. You want to minimize the cost of querying aggregate values for multiple users who will query the data in Cloud Storage with multiple engines. Which storage service and schema design should you use?",
  "opts": {
   "A": "Use Cloud Bigtable for storage. Install the HBase shell on a Compute Engine instance to query the Cloud Bigtable data.",
   "B": "Use Cloud Bigtable for storage. Link as permanent tables in BigQuery for query.",
   "C": "Use Cloud Storage for storage. Link as permanent tables in BigQuery for query.",
   "D": "Use Cloud Storage for storage. Link as temporary tables in BigQuery for query."
  },
  "correct": "C",
  "correct_text": "Use Cloud Storage for storage. Link as permanent tables in BigQuery for query.",
  "base": "Correct Option C. Use Cloud Storage for storage. Link as permanent tables in BigQuery for query. Correct because storing the 20 TB of CSV files in Cloud Storage is cost‑effective, and linking them as permanent external tables in BigQuery allows multiple users and engines to query aggregate values e…"
 },
 {
  "id": "test_7_q33",
  "q": "You designed a database for patient records as a pilot project to cover a few hundred patients in three clinics. Your design used a single database table to represent all patients and their visits, and you used self-joins to generate reports. The server resource utilization was at 50%. Since then, the scope of the project has expanded. The database must now store 100 times more patient records. You can no longer run the reports, because they either take too long or they encounter errors with insufficient compute resources. How should you adjust the database design?",
  "opts": {
   "A": "Add capacity (memory and disk space) to the database server by the order of 200.",
   "B": "Shard the tables into smaller ones based on date ranges, and only generate reports with prespecified date ranges.",
   "C": "Normalize the master patient-record table into the patient table and the visits table, and create other necessary tables to avoid self-join.",
   "D": "Partition the table into smaller tables, with one for each clinic. Run queries against the smaller table pairs, and use unions for consolidated reports."
  },
  "correct": "C",
  "correct_text": "Normalize the master patient-record table into the patient table and the visits table, and create other necessary tables to avoid self-join.",
  "base": "C is correct because this option provides the least amount of inconvenience over using pre-specified date ranges or one table per clinic while also increasing performance due to avoiding self-joins. A is not correct because adding additional compute resources is not a recommended way to resolve dat…"
 },
 {
  "id": "test_7_q40",
  "q": "What are two of the benefits of using denormalized data structures in BigQuery?",
  "opts": {
   "A": "Reduces the amount of data processed, reduces the amount of storage required",
   "B": "Increases query speed, makes queries simpler",
   "C": "Reduces the amount of storage required, increases query speed",
   "D": "Reduces the amount of data processed, increases query speed"
  },
  "correct": "B",
  "correct_text": "Increases query speed, makes queries simpler",
  "base": "Denormalization increases query speed for tables with billions of rows because BigQuery‘s performance degrades when doing JOINs on large tables, but with a denormalized data structure, you don‘t have to use JOINs, since all of the data has been combined into one table. Denormalization also makes qu…"
 },
 {
  "id": "test_8_q31",
  "q": "Which of these is not a supported method of putting data into a partitioned table?",
  "opts": {
   "A": "If you have existing data in a separate file for each day, then create a partitioned table and upload each file into the appropriate partition.",
   "B": "Run a query to get the records for a specific day from an existing table and for the destination table, specify a partitioned table ending with the day in the format “$YYYYMMDD“.",
   "C": "Create a partitioned table and stream new records to it every day.",
   "D": "Use ORDER BY to put a table‘s rows into chronological order and then change the table‘s type to “Partitioned“."
  },
  "correct": "D",
  "correct_text": "Use ORDER BY to put a table‘s rows into chronological order and then change the table‘s type to “Partitioned“.",
  "base": "You cannot change an existing table into a partitioned table. You must create a partitioned table from scratch. Then you can either stream data into it every day and the data will automatically be put in the right partition, or you can load data into a specific partition by using “$YYYYMMDD“ at the…"
 },
 {
  "id": "test_8_q43",
  "q": "What are two methods that can be used to denormalize tables in BigQuery?",
  "opts": {
   "A": "1) Split table into multiple tables; 2) Use a partitioned table",
   "B": "1) Join tables into one table; 2) Use nested repeated fields",
   "C": "1) Use a partitioned table; 2) Join tables into one table",
   "D": "1) Use nested repeated fields; 2) Use a partitioned table"
  },
  "correct": "B",
  "correct_text": "1) Join tables into one table; 2) Use nested repeated fields",
  "base": "The conventional method of denormalizing data involves simply writing a fact, along with all its dimensions, into a flat table structure. For example, if you are dealing with sales transactions, you would write each individual fact to a record, along with the accompanying dimensions such as order a…"
 },
 {
  "id": "test_9_q16",
  "q": "You have a table in BigQuery containing information about purchases made across several store locations. You need to choose the best data model for optimal query performance. The table includes information such as the time of the transaction, items purchased, the store ID, and the city and state in which the store is located. You often run queries to view the sales of each item over the past 30 days and to analyze purchasing trends by state, city, and individual store. How would you model this table for the best query performance?",
  "opts": {
   "A": "Cluster the table by state, city, and then store ID without partitioning",
   "B": "Cluster the table by store ID, city, and then state without partitioning",
   "C": "Partition the table by transaction time and cluster it by state, city, and then store ID",
   "D": "Partition the table by transaction time and cluster it by store ID, city, and then state"
  },
  "correct": "C",
  "correct_text": "Partition the table by transaction time and cluster it by state, city, and then store ID",
  "base": "Partitioning by transaction time will help with filtering data by the date of the transaction, which is a common use case. Clustering by state, city, and store ID in that order will help with grouping data by geographic regions and allow for efficient filtering and aggregation. This approach will a…"
 },
 {
  "id": "test_12_q26",
  "q": "A BigQuery data warehouse needs to access some data in Cloud Storage using external tables. Which of the following is not a supported file format for external tables based on files in Cloud Storage?",
  "opts": {
   "A": "Avro",
   "B": "ORC",
   "C": "Firestore export files",
   "D": "Excel xlsx format"
  },
  "correct": "D",
  "correct_text": "Excel xlsx format",
  "base": "The Excel xlsx file format is not supported for files stored in Cloud Storage. Avro, CSV, newline-delimited JSON, Datastore export files, Firestore export files, ORC, and Parquet files are supported. See https://cloud.google.com/bigquery/external-data-sources"
 },
 {
  "id": "test_13_q8",
  "q": "Scenario: You need to access data from a large BigQuery table multiple times daily. The table is several petabytes in size, but you want to streamline your queries for faster results and simpler aggregations for other users. How can you optimize your BigQuery queries to improve query speed and provide more timely insights?",
  "opts": {
   "A": "Run a scheduled query to pull the necessary data at specific intervals dally.",
   "B": "Use a cached query to accelerate time to results.",
   "C": "Limit the query columns being pulled in the final result.",
   "D": "Create a materialized view based off of the query being run."
  },
  "correct": "D",
  "correct_text": "Create a materialized view based off of the query being run.",
  "base": "D. Create a materialized view based off of the query being run:Creating a materialized view is the best option in this scenario because materialized views store the results of a query in a separate table, which can be queried much faster than running the original query each time. This approach is i…"
 },
 {
  "id": "test_13_q12",
  "q": "Scenario: Your company’s customer_order table in BigQuery stores the order history for 10 million customers, with a table size of 10 PB. You need to create a dashboard for the support team to view the order history. Question: How should you redesign the BigQuery table to support faster access for the dashboard with country_name and username filters?",
  "opts": {
   "A": "Cluster the table by country and username fields.",
   "B": "Cluster the table by country field, and partition by username field.",
   "C": "Partition the table by country and username fields.",
   "D": "Partition the table by _PARTITIONTIME."
  },
  "correct": "A",
  "correct_text": "Cluster the table by country and username fields.",
  "base": "A. Cluster the table by country and username fields. Clustering the table by the country and username fields is the correct approach to support faster access for the given scenario. Clustering in BigQuery helps organize the data within the table based on the values of one or more columns. By cluste…"
 },
 {
  "id": "test_13_q17",
  "q": "Scenario: You are transitioning your on-premises data warehouse to BigQuery. One of the data sources is a MySQL database located in your on-premises data center without public IP addresses. How can you securely ingest data from this MySQL database into BigQuery without using the public internet?",
  "opts": {
   "A": "Update your existing on-premises ETL tool to write to BigQuery by using the BigQuery Open Database Connectivity (ODBC) driver. Set up the proxy parameter in the simba.googlebigqueryodbc.ini file to point to your data centers NAT gateway.",
   "B": "Use Datastream to replicate data from your on-premises MySQL database to BigQuery. Set up Cloud Interconnect between your on-premises data center and Google Cloud. Use Private connectivity as the connectivity method and allocate an IP address range within your VPC network to the Datastream connectivity configuration. Use Server-only as the encryption type when setting up the connection profile in Datastream.",
   "C": "Use Datastream to replicate data from your on-premises MySQL database to BigQuery. Use Forward-SSH tunnel as the connectivity method to establish a secure tunnel between Datastream and your on-premises MySQL database through a tunnel server in your on-premises data center. Use None as the encryption type when setting up the connection profile in Datastream.",
   "D": "Use Datastream to replicate data from your on-premises MySQL database to BigQuery. Gather Datastream public IP addresses of the Google Cloud region that will be used to set up the stream. Add those IP addresses to the firewall allowlist of your on-premises data center. Use IP Allowlisting as the connectivity method and Server-only as the encryption type when setting up the connection profile in Datastream."
  },
  "correct": "B",
  "correct_text": "Use Datastream to replicate data from your on-premises MySQL database to BigQuery. Set up Cloud Interconnect between your on-premises data center and Google Cloud. Use Private connectivity as the connectivity method and…",
  "base": "The correct answer is B.Option B suggests using Datastream to replicate data from the on-premises MySQL database to BigQuery. By setting up Cloud Interconnect between the on-premises data center and Google Cloud, you can establish a private connection that does not go through the public internet. U…"
 },
 {
  "id": "test_13_q25",
  "q": "Scenario: You work for a farming company that has a BigQuery table named sensors, which is 500 MB in size and holds information on 5000 sensors, including id, name, and location. The table is updated hourly, and each sensor produces a metric every 30 seconds with a timestamp that needs to be stored in BigQuery. To monitor the data weekly and reduce costs, you need to determine the appropriate data model. What data model would be most suitable for storing sensor metrics in BigQuery to allow for weekly analytical queries while minimizing costs?",
  "opts": {
   "A": "1. Create a metrics column in the sensors table. 2. Set RECORD type and REPEATED mode for the metrics column. 3. Use an UPDATE statement every 30 seconds to add new metrics.",
   "B": "1. Create a metrics column in the sensors table. 2. Set RECORD type and REPEATED mode for the metrics column. 3. Use an INSERT statement every 30 seconds to add new metrics.",
   "C": "1. Create a metrics table partitioned by timestamp. 2. Create a sensorId column in the metrics table, that points to the id column in the sensors table. 3. Use an INSERT statement every 30 seconds to append new metrics to the metrics table. 4. Join the two tables, if needed, when running the analytical query.",
   "D": "1. Create a metrics table partitioned by timestamp. 2. Create a sensorId column in the metrics table, which points to the id column in the sensors table. 3. Use an UPDATE statement every 30 seconds to append new metrics to the metrics table. 4. Join the two tables, if needed, when running the analytical query."
  },
  "correct": "C",
  "correct_text": "1. Create a metrics table partitioned by timestamp. 2. Create a sensorId column in the metrics table, that points to the id column in the sensors table. 3. Use an INSERT statement every 30 seconds to append new metrics…",
  "base": "Correct Option C. Create a metrics table partitioned by timestamp, include sensorId, and use INSERT statements This is the best practice for time-series data in BigQuery. Partitioning by timestamp ensures queries only scan relevant weekly partitions, reducing cost and improving performance. Separat…"
 },
 {
  "id": "test_14_q23",
  "q": "Scenario: You need ads data for AI models and historical data for analytics. Identifying longtail and outlier data points is crucial. The data must be cleansed in near-real time before being used in AI models. What steps should be taken to cleanse the data before running it through AI models?",
  "opts": {
   "A": "Use Cloud Storage as a data warehouse, shell scripts for processing, and BigQuery to create views for desired datasets.",
   "B": "Use Dataflow to identify longtail and outlier data points programmatically, with BigQuery as a sink.",
   "C": "Use BigQuery to ingest, prepare, and then analyze the data, and then run queries to create views.",
   "D": "Use Cloud Composer to identify longtail and outlier data points, and then output a usable dataset to BigQuery."
  },
  "correct": "B",
  "correct_text": "Use Dataflow to identify longtail and outlier data points programmatically, with BigQuery as a sink.",
  "base": "The correct answer is B. Use Dataflow to identify longtail and outlier data points programmatically, with BigQuery as a sink.– Dataflow is a service on Google Cloud that allows for real-time data processing and analysis. It can be used to programmatically identify longtail and outlier data points i…"
 },
 {
  "id": "test_14_q28",
  "q": "Scenario: You are looking to transfer your current Teradata data warehouse to BigQuery. The goal is to transfer the historical data to BigQuery using the most efficient method with minimal programming. However, your existing data warehouse has limited local storage space. What steps should you take in this situation?",
  "opts": {
   "A": "Use BigQuery Data Transfer Service by using the Java Database Connectivity (JDBC) driver with FastExport connection.",
   "B": "Create a Teradata Parallel Transporter (TPT) export script to export the historical data, and import to BigQuery by using the bq command-line tool.",
   "C": "Use BigQuery Data Transfer Service with the Teradata Parallel Transporter (TPT) tbuild utility.",
   "D": "Create a script to export the historical data, and upload in batches to Cloud Storage. Set up a BigQuery Data Transfer Service instance from Cloud Storage to BigQuery."
  },
  "correct": "A",
  "correct_text": "Use BigQuery Data Transfer Service by using the Java Database Connectivity (JDBC) driver with FastExport connection.",
  "base": "Correct Option A. Use BigQuery Data Transfer Service by using the JDBC driver with FastExport connection. Correct because the BigQuery Data Transfer Service (DTS) supports Teradata migration using JDBC and FastExport. This method avoids the need for large local storage, streams data efficiently, an…"
 },
 {
  "id": "test_14_q47",
  "q": "Scenario: Your business users, who are not very tech-savvy, require a user-friendly tool to clean and prepare data for analysis using graphical interfaces. They also prefer to conduct analysis directly in a spreadsheet after data transformation. What solution would you recommend for your less technically savvy business users to clean, prepare data, and perform analysis directly in a spreadsheet?",
  "opts": {
   "A": "Use Dataprep to clean the data, and write the results to BigQuery. Analyze the data by using Connected Sheets.",
   "B": "Use Dataprep to clean the data, and write the results to BigQuery. Analyze the data by using Looker Studio.",
   "C": "Use Dataflow to clean the data, and write the results to BigQuery. Analyze the data by using Connected Sheets.",
   "D": "Use Dataflow to clean the data, and write the results to BigQuery. Analyze the data by using Looker Studio."
  },
  "correct": "A",
  "correct_text": "Use Dataprep to clean the data, and write the results to BigQuery. Analyze the data by using Connected Sheets.",
  "base": "A. Use Dataprep to clean the data, and write the results to BigQuery. Analyze the data by using Connected Sheets.– Dataprep is a data preparation tool that allows users to visually explore, clean, and prepare data without needing to write code. This is suitable for business users who are less techn…"
 },
 {
  "id": "test_14_q52",
  "q": "Scenario: You use a SQL-based tool to visualize data stored in BigQuery, requiring outer joins and analytic functions. The visualizations need to be based on data at least 4 hours old. Business users are unhappy with the slow generation of visualizations. How can you enhance the performance of visualization queries while reducing the maintenance burden of the data preparation pipeline?",
  "opts": {
   "A": "Create materialized views with the allow_non_incremental_definition option set to true for the visualization queries. Specify the max_staleness parameter to 4 hours and the enable_refresh parameter to true. Reference the materialized views in the data visualization tool.",
   "B": "Create views for the visualization queries. Reference the views in the data visualization tool.",
   "C": "Create a Cloud Function instance to export the visualization query results as parquet files to a Cloud Storage bucket. Use Cloud Scheduler to trigger the Cloud Function every 4 hours. Reference the parquet files in the data visualization tool.",
   "D": "Create materialized views for the visualization queries. Use the incremental updates capability of BigQuery materialized views to handle changed data automatically. Reference the materialized views in the data visualization tool."
  },
  "correct": "A",
  "correct_text": "Create materialized views with the allow_non_incremental_definition option set to true for the visualization queries. Specify the max_staleness parameter to 4 hours and the enable_refresh parameter to true. Reference th…",
  "base": "A. Create materialized views with the allow_non_incremental_definition option set to true for the visualization queries. Specify the max_staleness parameter to 4 hours and the enable_refresh parameter to true. Reference the materialized views in the data visualization tool.Creating materialized vie…"
 },
 {
  "id": "test_15_q4",
  "q": "Scenario: Your company is transitioning from on-premises data warehousing solutions to BigQuery. The current data warehouse utilizes trigger-based change data capture (CDC) to incorporate updates from various transactional databases daily. The goal now is to enhance CDC processes in BigQuery, allowing real-time access to changes from source systems through log-based CDC streams. The objective is to optimize performance in applying these changes to the data warehouse. To achieve minimal latency in making changes available in the BigQuery reporting table and reduce compute overhead, what are the two recommended steps that should be implemented? (Choose two.)",
  "opts": {
   "A": "Perform a DML INSERT, UPDATE, or DELETE to replicate each individual CDC record in real time directly on the reporting table.",
   "B": "Insert each new CDC record and corresponding operation type to a staging table in real time.",
   "C": "Periodically DELETE outdated records from the reporting table.",
   "D": "Periodically use a DML MERGE to perform several DML INSERT, UPDATE, and DELETE operations at the same time on the reporting table.",
   "E": "Insert each new CDC record and corresponding operation type in real time to the reporting table, and use a materialized view to expose only the newest version of each unique record."
  },
  "correct": "B",
  "correct_text": "Insert each new CDC record and corresponding operation type to a staging table in real time.",
  "base": "BD is the correct answer for the question.– Option B: Inserting each new CDC record and corresponding operation type to a staging table in real time allows for minimal latency as changes are captured immediately. This approach helps reduce compute overhead by processing changes in batches rather th…"
 },
 {
  "id": "test_15_q6",
  "q": "Scenario: You are tasked with setting access to BigQuery for various departments in your company. The solution should adhere to specific criteria: – Each department should access only their data. – Each department will have one or more leads who can create and update tables for their team. – Each department includes data analysts who can query data but not modify it. How would you configure access to the data in BigQuery to meet the specified requirements?",
  "opts": {
   "A": "Create a dataset for each department. Assign the department leads the role of OWNER, and assign the data analysts the role of WRITER on their dataset.",
   "B": "Create a dataset for each department. Assign the department leads the role of WRITER, and assign the data analysts the role of READER on their dataset.",
   "C": "Create a table for each department. Assign the department leads the role of Owner, and assign the data analysts the role of Editor on the project the table is in.",
   "D": "Create a table for each department. Assign the department leads the role of Editor, and assign the data analysts the role of Viewer on the project the table is in."
  },
  "correct": "B",
  "correct_text": "Create a dataset for each department. Assign the department leads the role of WRITER, and assign the data analysts the role of READER on their dataset.",
  "base": "The correct answer is option B: Create a dataset for each department. Assign the department leads the role of WRITER, and assign the data analysts the role of READER on their dataset.1. Creating a dataset for each department allows you to segregate the data and provide access control at a more gran…"
 }
]

<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_18.json  (just the JSON, no backticks).
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
test_8_q39, test_11_q19, test_11_q22, test_13_q23, test_13_q49, test_14_q18, test_14_q26, test_14_q56, test_15_q7, test_15_q12, test_15_q17, test_15_q22, test_15_q23, test_15_q38, test_15_q46, test_16_q23, test_16_q27, test_16_q42, test_10_q2, test_1_q44

Questions:

[
 {
  "id": "test_8_q39",
  "q": "Your company is running their first dynamic campaign, serving different offers by analyzing real-time data during the holiday season. The data scientists are collecting terabytes of data that rapidly grows every hour during their 30-day campaign. They are using Google Cloud Dataflow to preprocess the data and collect the feature (signals) data that is needed for the machine learning model in Google Cloud Bigtable. The team is observing suboptimal performance with reads and writes of their initial load of 10 TB of data. They want to improve this performance while minimizing cost. What should they do?",
  "opts": {
   "A": "Redefine the schema by evenly distributing reads and writes across the row space of the table.",
   "B": "The performance issue should be resolved over time as the site of the BigDate cluster is increased.",
   "C": "Redesign the schema to use a single row key to identify values that need to be updated frequently in the cluster.",
   "D": "Redesign the schema to use row keys based on numeric IDs that increase sequentially per user viewing the offers."
  },
  "correct": "A",
  "correct_text": "Redefine the schema by evenly distributing reads and writes across the row space of the table.",
  "base": "A as the schema needs to be redesigned to distribute the reads and writes evenly across each table. Refer GCP documentation – Bigtable Performance: https://cloud.google.com/bigtable/docs/performance The table‘s schema is not designed correctly. To get good performance from Cloud Bigtable, it‘s esse…"
 },
 {
  "id": "test_11_q19",
  "q": "You have a latency-sensitive application that uses Bigtable. You want to follow Google Cloud recommended best practices. What would you do?",
  "opts": {
   "A": "Use a service account for all read operations",
   "B": "Keep storage utilization per node below 60%",
   "C": "Use a global load balancer in front of Bigtable",
   "D": "Use HDD storage instead of SSD storage"
  },
  "correct": "B",
  "correct_text": "Keep storage utilization per node below 60%",
  "base": "For low latency applications, Google Cloud recommends keeping storage utilization below 60%. Using service accounts for read operations will not affect latency of write operations. HDD storage is less performant than SSD storage. A load balancer is not needed to distribute workload within a Bigtabl…"
 },
 {
  "id": "test_11_q22",
  "q": "How should you design storage for 20 TB of text files when deploying a data pipeline on Google Cloud in order to minimize the cost of querying aggregate values for multiple users who will query the data in Cloud Storage with multiple engines, given that your input data is in CSV format. (Which storage service and schema design should be utilized)?",
  "opts": {
   "A": "Use Cloud Bigtable for storage and link the data as permanent tables in BigQuery for querying",
   "B": "Use Cloud Bigtable for storage and install the HBase shell on a Compute Engine instance to query the data.",
   "C": "Use Cloud Storage for storage and link the data as temporary tables in BigQuery for querying.",
   "D": "Use Cloud Storage for storage and link the data as permanent tables in BigQuery for querying."
  },
  "correct": "D",
  "correct_text": "Use Cloud Storage for storage and link the data as permanent tables in BigQuery for querying.",
  "base": "The recommended solution for storing 20 TB of text files for a data pipeline on Google Cloud in order to minimize the cost of querying aggregate values for multiple users who will query the data in Cloud Storage with multiple engines, given that the input data is in CSV format, is to use Cloud Stor…"
 },
 {
  "id": "test_13_q23",
  "q": "Scenario: You have transactional data stored on-premises in a PostgreSQL database and want to modernize your data environment by running transactional workloads and supporting analytics needs with a single database. You aim to move to Google Cloud without changing database management systems, while minimizing cost and complexity. What steps should you take to achieve this goal?",
  "opts": {
   "A": "Migrate and modernize your database with Cloud Spanner.",
   "B": "Migrate your workloads to AlloyDB for PostgreSQL.",
   "C": "Migrate to BigQuery to optimize analytics.",
   "D": "Migrate your PostgreSQL database to Cloud SQL for PostgreSQL."
  },
  "correct": "D",
  "correct_text": "Migrate your PostgreSQL database to Cloud SQL for PostgreSQL.",
  "base": "The best approach to achieve your goal is to: Migrate your PostgreSQL database to Cloud SQL for PostgreSQL. Here’s why: Maintaining PostgreSQL: Cloud SQL for PostgreSQL allows you to migrate your existing PostgreSQL database to Google Cloud without changing the database management system, meeting y…"
 },
 {
  "id": "test_13_q49",
  "q": "Scenario: You have a network of 1000 sensors generating time series data at a rate of one metric per sensor per second, each with a timestamp. Currently, you have 1 TB of data, and the data is expected to increase by 1 GB daily. How should you store this data to ensure that you can access the data efficiently for both retrieving a specific sensor‘s metric at a specific timestamp with low latency and running complex analytic queries once a day?",
  "opts": {
   "A": "Store your data in BigQuery. Concatenate the sensor ID and timestamp, and use it as the primary key.",
   "B": "Store your data in Bigtable. Concatenate the sensor ID and timestamp and use it as the row key. Perform an export to BigQuery every day.",
   "C": "Store your data in Bigtable. Concatenate the sensor ID and metric, and use it as the row key. Perform an export to BigQuery every day.",
   "D": "Store your data in BigQuery. Use the metric as a primary key."
  },
  "correct": "B",
  "correct_text": "Store your data in Bigtable. Concatenate the sensor ID and timestamp and use it as the row key. Perform an export to BigQuery every day.",
  "base": "The correct answer is B: Store your data in Bigtable. Concatenate the sensor ID and timestamp and use it as the row key. Perform an export to BigQuery every day.1. Bigtable is a NoSQL database designed for storing large amounts of data with low latency. By using Bigtable and concatenating the senso…"
 },
 {
  "id": "test_14_q18",
  "q": "Scenario: Your startup operates a web application that caters to customers in a single region in Asia. Seeking funding to expand globally, you aim to optimize for cost initially and later for global presence and performance. Requirement: Utilize a native JDBC driver. How should you proceed in order to achieve your goals?",
  "opts": {
   "A": "Use Cloud Spanner to configure a single region instance initially, and then configure multi-region Cloud Spanner instances after securing funding.",
   "B": "Use a Cloud SQL for PostgreSQL highly available instance first, and Bigtable with US, Europe, and Asia replication after securing funding.",
   "C": "Use a Cloud SQL for PostgreSQL zonal instance first, and Bigtable with US, Europe, and Asia after securing funding.",
   "D": "Use a Cloud SQL for PostgreSQL zonal instance first, and Cloud SQL for PostgreSQL with highly available configuration after securing funding."
  },
  "correct": "A",
  "correct_text": "Use Cloud Spanner to configure a single region instance initially, and then configure multi-region Cloud Spanner instances after securing funding.",
  "base": "A. Use Cloud Spanner to configure a single region instance initially, and then configure multi-region Cloud Spanner instances after securing funding.– Cloud Spanner is a globally distributed, horizontally scalable, and strongly consistent database service provided by Google Cloud Platform. It is a…"
 },
 {
  "id": "test_14_q26",
  "q": "Scenario: Your company needs to extract and store large result sets of medical information from a database with over 10 TBs. The new tables must support further queries and have a low-maintenance architecture accessible via SQL. What cost-effective solution should be implemented to support data analytics for large result sets in this scenario?",
  "opts": {
   "A": "Use Cloud SQL, but first organize the data into tables. Use JOIN in queries to retrieve data.",
   "B": "Use BigQuery as a data warehouse. Set output destinations for caching large queries.",
   "C": "Use a MySQL cluster installed on a Compute Engine managed instance group for scalability.",
   "D": "Use Cloud Spanner to replicate the data across regions. Normalize the data in a series of tables."
  },
  "correct": "B",
  "correct_text": "Use BigQuery as a data warehouse. Set output destinations for caching large queries.",
  "base": "Correct Option B. Use BigQuery as a data warehouse. Set output destinations for caching large queries Correct because BigQuery is Google Cloud’s serverless, highly scalable, low-maintenance data warehouse. It is designed for large datasets (10 TBs and beyond) and supports SQL queries directly. BigQ…"
 },
 {
  "id": "test_14_q56",
  "q": "Scenario: You migrated a data backend for an application that serves 10 PB of historical product data for analytics. Only the last known state for a product, which is about 10 GB of data, needs to be served through an API to other applications. What cost-effective persistent storage solution should you choose to accommodate the analytics requirements and the API performance of up to 1000 queries per second (QPS) with less than 1 second latency?",
  "opts": {
   "A": "1. Store the historical data in BigQuery for analytics. 2. Use a materialized view to precompute the last state of a product. 3. Serve the last state data directly from BigQuery to the API.",
   "B": "1. Store the products as a collection in Firestore with each product having a set of historical changes. 2. Use simple and compound queries for analytics. 3. Serve the last state data directly from Firestore to the API.",
   "C": "1. Store the historical data in Cloud SQL for analytics. 2. In a separate table, store the last state of the product after every product change. 3. Serve the last state data directly from Cloud SQL to the API.",
   "D": "1. Store the historical data in BigQuery for analytics. 2. In a Cloud SQL table, store the last state of the product after every product change. 3. Serve the last state data directly from Cloud SQL to the API."
  },
  "correct": "D",
  "correct_text": "1. Store the historical data in BigQuery for analytics. 2. In a Cloud SQL table, store the last state of the product after every product change. 3. Serve the last state data directly from Cloud SQL to the API.",
  "base": "The correct answer is option D. Let‘s break down why D is the correct choice and why the other options are incorrect:Option D:1. Store the historical data in BigQuery for analytics: BigQuery is a cost-effective solution for storing and analyzing large datasets. It is designed for handling massive a…"
 },
 {
  "id": "test_15_q7",
  "q": "Scenario: You run a database storing stock trades and an application that calculates the average stock price for a specific company within a customizable timeframe. The data is kept in Cloud Bigtable, with the trade datetime at the start of the row key. With a growing number of stocks being added and thousands of concurrent users, the application‘s performance is deteriorating. How can you enhance the performance of your application under these circumstances?",
  "opts": {
   "A": "Change the row key syntax in your Cloud Bigtable table to begin with the stock symbol.",
   "B": "Change the row key syntax in your Cloud Bigtable table to begin with a random number per second.",
   "C": "Change the data pipeline to use BigQuery for storing stock trades, and update your application.",
   "D": "Use Cloud Dataflow to write a summary of each day‘s stock trades to an Avro file on Cloud Storage. Update your application to read from Cloud Storage and Cloud Bigtable to compute the responses."
  },
  "correct": "A",
  "correct_text": "Change the row key syntax in your Cloud Bigtable table to begin with the stock symbol.",
  "base": "A. Change the row key syntax in your Cloud Bigtable table to begin with the stock symbol.By changing the row key syntax in the Cloud Bigtable table to begin with the stock symbol, you can improve the performance of your application. This is because storing data with the stock symbol at the beginnin…"
 },
 {
  "id": "test_15_q12",
  "q": "Scenario: You have a petabyte of analytics data and need to create a storage and processing platform for it. You must support data warehouse-style analytics on the data in Google Cloud and make the dataset accessible as files for batch analysis tools in other cloud providers. What steps should be taken to achieve this?",
  "opts": {
   "A": "Store and process the entire dataset in BigQuery.",
   "B": "Store and process the entire dataset in Bigtable.",
   "C": "Store the full dataset in BigQuery, and store a compressed copy of the data in a Cloud Storage bucket.",
   "D": "Store the warm data as files in Cloud Storage, and store the active data in BigQuery. Keep this ratio as 80% warm and 20% active."
  },
  "correct": "C",
  "correct_text": "Store the full dataset in BigQuery, and store a compressed copy of the data in a Cloud Storage bucket.",
  "base": "The correct answer is C: Store the full dataset in BigQuery, and store a compressed copy of the data in a Cloud Storage bucket.1. Storing the full dataset in BigQuery allows you to perform data warehouse-style analytics on the data in Google Cloud. BigQuery is a fully managed, serverless, and highl…"
 },
 {
  "id": "test_15_q17",
  "q": "Scenario: A United States-based company has developed an application that evaluates and handles user actions. The main table of the application experiences a data volume increase of 250,000 records per second. Various third parties utilize the company‘s APIs to integrate the application‘s features into their frontend applications. The APIs of the application must adhere to specific requirements, including a single global endpoint, ANSI SQL support, and consistent access to the latest data. What steps should be taken to meet the specified requirements for the company‘s application APIs?",
  "opts": {
   "A": "Implement BigQuery with no region selected for storage or processing.",
   "B": "Implement Cloud Spanner with the leader in North America and read-only replicas in Asia and Europe.",
   "C": "Implement Cloud SQL for PostgreSQL with the master in North America and read replicas in Asia and Europe.",
   "D": "Implement Bigtable with the primary cluster in North America and secondary clusters in Asia and Europe."
  },
  "correct": "B",
  "correct_text": "Implement Cloud Spanner with the leader in North America and read-only replicas in Asia and Europe.",
  "base": "The correct answer is B. Implement Cloud Spanner with the leader in North America and read-only replicas in Asia and Europe.– Cloud Spanner is a globally distributed, horizontally scalable, strongly consistent database service provided by Google Cloud Platform. It meets the requirements of having a…"
 },
 {
  "id": "test_15_q22",
  "q": "Scenario: You are tasked with creating a new data pipeline to facilitate data exchange between jobs generators and job runners. The solution should be scalable to handle increased usage and adaptable to incorporate new applications without impacting the performance of current ones. How would you approach this task to ensure the data pipeline meets the scalability requirements and can seamlessly integrate new applications while maintaining the performance of existing ones?",
  "opts": {
   "A": "Create an API using App Engine to receive and send messages to the applications",
   "B": "Use a Cloud Pub/Sub topic to publish jobs, and use subscriptions to execute them",
   "C": "Create a table on Cloud SQL, and insert and delete rows with the job information",
   "D": "Create a table on Cloud Spanner, and insert and delete rows with the job information"
  },
  "correct": "B",
  "correct_text": "Use a Cloud Pub/Sub topic to publish jobs, and use subscriptions to execute them",
  "base": "The correct answer is option B: Use a Cloud Pub/Sub topic to publish jobs, and use subscriptions to execute them.Using Cloud Pub/Sub for data pipeline between job generators and job runners is a scalable and efficient solution. Cloud Pub/Sub is a messaging service that allows asynchronous messaging…"
 },
 {
  "id": "test_15_q23",
  "q": "Scenario: A new transaction table needs to be created in Cloud Spanner to store product sales data. From a performance perspective, which strategy should be chosen for the primary key?",
  "opts": {
   "A": "The current epoch time",
   "B": "A concatenation of the product name and the current epoch time",
   "C": "A random universally unique identifier number (version 4 UUID)",
   "D": "The original order identification number from the sales system, which is a monotonically increasing integer"
  },
  "correct": "C",
  "correct_text": "A random universally unique identifier number (version 4 UUID)",
  "base": "From a performance perspective, the best strategy to choose as a primary key for the new transaction table in Cloud Spanner that stores product sales data is option C – a random universally unique identifier number (version 4 UUID).Explanation of why option C is correct:1. Random universally unique…"
 },
 {
  "id": "test_15_q38",
  "q": "Scenario: You are employed by a large bank with operations across North America. You are in the process of establishing a data storage system for managing bank account transactions that must adhere to ACID compliance and allow data access through SQL. Which solution would be suitable for this data storage system setup?",
  "opts": {
   "A": "Store transaction data in Cloud Spanner. Enable stale reads to reduce latency.",
   "B": "Store transaction in Cloud Spanner. Use locking read-write transactions.",
   "C": "Store transaction data in BigQuery. Disabled the query cache to ensure consistency.",
   "D": "Store transaction data in Cloud SQL. Use a federated query BigQuery for analysis."
  },
  "correct": "B",
  "correct_text": "Store transaction in Cloud Spanner. Use locking read-write transactions.",
  "base": "The correct answer is B. Store transaction data in Cloud Spanner and use locking read-write transactions.– Cloud Spanner is a fully managed, scalable, relational database service that offers strong consistency and ACID compliance. It is designed to handle large-scale transactional workloads across…"
 },
 {
  "id": "test_15_q46",
  "q": "Scenario: A live TV show is requesting viewers to vote via mobile phones, generating a significant amount of data in just 3 minutes. As the person responsible for the “Voting infrastructure,” you need to guarantee that the system can manage the influx of data and process all votes. Additionally, you are required to show interim results during the voting period and accurately tally the votes once voting concludes. Question: What steps should you take to ensure the voting infrastructure can handle the load, display partial results while voting is ongoing, and efficiently count the votes only once to minimize costs?",
  "opts": {
   "A": "Create a Memorystore instance with a high availability (HA) configuration.",
   "B": "Create a Cloud SQL for PostgreSQL database with high availability (HA) configuration and multiple read replicas.",
   "C": "Write votes to a Pub/Sub topic and have Cloud Functions subscribe to it and write votes to BigQuery.",
   "D": "Write votes to a Pub/Sub topic and load into both Bigtable and BigQuery via a Dataflow pipeline. Query Bigtable for real-time results and BigQuery for later analysis. Shut down the Bigtable instance when voting concludes."
  },
  "correct": "D",
  "correct_text": "Write votes to a Pub/Sub topic and load into both Bigtable and BigQuery via a Dataflow pipeline. Query Bigtable for real-time results and BigQuery for later analysis. Shut down the Bigtable instance when voting conclude…",
  "base": "The correct answer is D. Write votes to a Pub/Sub topic and load into both Bigtable and BigQuery via a Dataflow pipeline. Query Bigtable for real-time results and BigQuery for later analysis. Shut down the Bigtable instance when voting concludes. – By writing the votes to a Pub/Sub topic, you decou…"
 },
 {
  "id": "test_16_q23",
  "q": "Scenario: You are tasked with selecting a database for a new project that must meet the following criteria: fully managed, capable of automatic scaling, transactionally consistent, able to scale up to 6 TB, and queryable using SQL. Which database would you recommend for this project?",
  "opts": {
   "A": "Cloud SQL",
   "B": "Cloud Bigtable",
   "C": "Cloud Spanner",
   "D": "Cloud Datastore"
  },
  "correct": "C",
  "correct_text": "Cloud Spanner",
  "base": "Cloud Spanner would be the most suitable database for this project based on the given criteria. Here’s why: Fully Managed: Cloud Spanner is a fully managed, globally distributed, and scalable database service provided by Google Cloud. Automatic Scaling: Cloud Spanner automatically scales horizontal…"
 },
 {
  "id": "test_16_q27",
  "q": "Scenario: You work for a mid-sized enterprise that needs to transfer its operational system transaction data from an on-premises database to GCP. The database is approximately 20 TB in size. Which database should you choose for this data transfer?",
  "opts": {
   "A": "Cloud SQL",
   "B": "Cloud Bigtable",
   "C": "Cloud Spanner",
   "D": "Cloud Datastore"
  },
  "correct": "C",
  "correct_text": "Cloud Spanner",
  "base": "Correct Option C. Cloud Spanner Cloud Spanner is the correct choice for this scenario. It is a horizontally scalable, globally distributed, strongly consistent relational database service. It is designed to handle large datasets (tens of terabytes and beyond) while supporting transactional workload…"
 },
 {
  "id": "test_16_q42",
  "q": "Scenario: A database is required to store time series CPU and memory usage for millions of computers, with data being recorded in one-second interval samples. Analysts will be conducting real-time, ad hoc analytics on the database. It is essential to prevent charges for each query executed and ensure scalability of the dataset in the future. What database and data model would be the best choice for this scenario?",
  "opts": {
   "A": "Create a table in BigQuery, and append the new samples for CPU and memory to the table",
   "B": "Create a wide table in BigQuery, create a column for the sample value at each second, and update the row with the interval for each second",
   "C": "Create a narrow table in Bigtable with a row key that combines the Computer Engine computer identifier with the sample time at each second",
   "D": "Create a wide table in Bigtable with a row key that combines the computer identifier with the sample time at each minute, and combine the values for each second as column data."
  },
  "correct": "C",
  "correct_text": "Create a narrow table in Bigtable with a row key that combines the Computer Engine computer identifier with the sample time at each second",
  "base": "C. Create a narrow table in Bigtable with a row key that combines the Computer Engine computer identifier with the sample time at each second.– Bigtable is a good choice for storing time series data for millions of computers with one-second interval samples because it is designed for high-performan…"
 },
 {
  "id": "test_10_q2",
  "q": "A manufacturer has successfully migrated several data warehouses to BigQuery and is using Cloud Storage for machine learning data. ML engineers and data analysts are having difficulty finding data sets they need. The CTO of the company has asked for your advice on how to reduce the workload on ML engineers and analysts when they need to find data sets. What would you recommend?",
  "opts": {
   "A": "Use Cloud Logging to track files uploaded to Cloud Storage and data sets to BigQuery.",
   "B": "Use Cloud Fusion to tracking both files uploaded to Cloud Storage and data sets loaded into BigQuery.",
   "C": "Use Cloud Data Catalog to automatically extract metadata from Cloud Storage objects and BigQuery data.",
   "D": "Query the metadata catalog of BigQuery and Cloud Storage and write the results to a BigQuery table where the ML engineers and data analysts can query the data with SQL."
  },
  "correct": "C",
  "correct_text": "Use Cloud Data Catalog to automatically extract metadata from Cloud Storage objects and BigQuery data.",
  "base": "The correct answer is to use Cloud Data Catalog, which can automatically extract metadata from sources including Cloud Storage, BigQuery, Cloud Bigtable, Cloud Pub/Sub, and Google Sheets. Cloud Logging is used for recording data about events and is not the best way to collect metadata. Cloud Fusion…"
 },
 {
  "id": "test_1_q44",
  "q": "You use materialized views in BigQuery. You are incurring higher than expected charges for BigQuery and suspect it may be related to materialized views. What materialized view characteristic could increase your BigQuery costs? (Choose 2)",
  "opts": {
   "A": "The datatypes used in materialized views",
   "B": "The frequency of materialized view refresh",
   "C": "The total volume of data stored in materialized views",
   "D": "The number of users with read access to the materialized view"
  },
  "correct": "B",
  "correct_text": "The frequency of materialized view refresh",
  "base": "The amount of data stored and the frequency of refresh jobs can increase the cost of maintaining materialized views. The data types used in the materialized view do not affect the cost. The number of users reading a materialized view does not affect cost but the total amount of data scanned would i…"
 }
]

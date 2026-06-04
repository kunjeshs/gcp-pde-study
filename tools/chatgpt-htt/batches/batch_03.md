<!--
HOW TO USE THIS FILE
1. Open a ChatGPT conversation (GPT-5 / o-series recommended).
2. Paste this ENTIRE file as one message.
3. ChatGPT replies with ONE JSON object. Save that reply verbatim as
   tools/chatgpt-htt/outputs/batch_03.json  (just the JSON, no backticks).
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
test_10_q20, test_13_q5, test_13_q6, test_13_q20, test_13_q26, test_13_q37, test_13_q44, test_13_q56, test_13_q60, test_14_q5, test_14_q17, test_14_q27, test_14_q33, test_14_q38, test_14_q46, test_14_q50, test_14_q54, test_14_q60, test_15_q24, test_15_q26

Questions:

[
 {
  "id": "test_10_q20",
  "q": "A team of analysts working with healthcare data have analyzed data in a BigQuery dataset for personally identifiable information. They want to store the results of the analysis in a managed service that will make it easy for them to retrieving information about the PII analysis at later times. What service would you recommend?",
  "opts": {
   "A": "Data Catalog",
   "B": "BigQuery",
   "C": "Data Loss Prevention",
   "D": "Cloud Spanner"
  },
  "correct": "A",
  "correct_text": "Data Catalog",
  "base": "I would recommend Data Catalog. Here’s why: Data Catalog is specifically designed for discovering, classifying, and managing metadata about data assets in Google Cloud, including BigQuery datasets. Storing the results of the PII analysis (e.g., what PII was found, where it was found, any remediatio…"
 },
 {
  "id": "test_13_q5",
  "q": "Scenario: You are tasked with preparing an organization-wide dataset by preprocessing customer data stored in a restricted bucket in Cloud Storage. The data is intended for creating consumer analyses, and you must ensure compliance with data privacy requirements. What steps should you take in this situation?",
  "opts": {
   "A": "Use Dataflow and the Cloud Data Loss Prevention API to mask sensitive data. Write the processed data in BigQuery.",
   "B": "Use customer-managed encryption keys (CMEK) to directly encrypt the data in Cloud Storage. Use federated queries from BigQuery. Share the encryption key by following the principle of least privilege.",
   "C": "Use the Cloud Data Loss Prevention API and Dataflow to detect and remove sensitive fields from the data in Cloud Storage. Write the filtered data in BigQuery.",
   "D": "Use Dataflow and Cloud KMS to encrypt sensitive fields and write the encrypted data in BigQuery. Share the encryption key by following the principle of least privilege."
  },
  "correct": "A",
  "correct_text": "Use Dataflow and the Cloud Data Loss Prevention API to mask sensitive data. Write the processed data in BigQuery.",
  "base": "A. Use Dataflow and the Cloud Data Loss Prevention API to mask sensitive data. Write the processed data in BigQuery.This option is the correct approach because it involves using Dataflow, which is a managed service for executing a wide range of data processing patterns, and the Cloud Data Loss Prev…"
 },
 {
  "id": "test_13_q6",
  "q": "Scenario: You need to connect several applications with dynamic public IP addresses to a Cloud SQL instance. Users have been configured with strong passwords and SSL connection has been enforced for the Cloud SQL instance. What steps should you take to utilize the Cloud SQL public IP and establish secure connections?",
  "opts": {
   "A": "Add CIDR 0.0.0.0/0 network to Authorized Network. Use Identity and Access Management (IAM) to add users.",
   "B": "Add all application networks to Authorized Network and regularly update them.",
   "C": "Leave the Authorized Network empty. Use Cloud SQL Auth proxy on all applications.",
   "D": "Add CIDR 0.0.0.0/0 network to Authorized Network. Use Cloud SQL Auth proxy on all applications."
  },
  "correct": "C",
  "correct_text": "Leave the Authorized Network empty. Use Cloud SQL Auth proxy on all applications.",
  "base": "The correct answer is C. Leave the Authorized Network empty. Use Cloud SQL Auth proxy on all applications.By leaving the Authorized Network empty, you are not allowing any specific IP address or range to access your Cloud SQL instance directly, which helps in enhancing the security. Instead, you ca…"
 },
 {
  "id": "test_13_q20",
  "q": "Scenario: When designing the architecture for processing data from Cloud Storage to BigQuery using Dataflow, the network team has offered a Shared VPC network and subnetwork for pipeline utilization. How can you enable the deployment of the pipeline on the Shared VPC network?",
  "opts": {
   "A": "Assign the compute.networkUser role to the Dataflow service agent.",
   "B": "Assign the compute.networkUser role to the service account that executes the Dataflow pipeline.",
   "C": "Assign the dataflow.admin role to the Dataflow service agent.",
   "D": "Assign the dataflow.admin role to the service account that executes the Dataflow pipeline."
  },
  "correct": "B",
  "correct_text": "Assign the compute.networkUser role to the service account that executes the Dataflow pipeline.",
  "base": "Let’s analyze the scenario and each option: Scenario: Dataflow pipeline processing data from Cloud Storage to BigQuery. Using a Shared VPC network and subnetwork. Requirement: Enable the Dataflow pipeline to deploy on the Shared VPC network. Analysis: Dataflow Service Agent: The Dataflow service ag…"
 },
 {
  "id": "test_13_q26",
  "q": "Scenario: An encryption key stored in Cloud Key Management Service (Cloud KMS) has been compromised, requiring re-encryption of all CMEK-protected Cloud Storage data using that key and deletion of the compromised key. Additionally, measures need to be taken to prevent objects from being written without customer-managed encryption key (CMEK) protection in the future. What steps should be taken to address the compromised encryption key, re-encrypt the data, and enhance future protection of objects with CMEK encryption?",
  "opts": {
   "A": "Rotate the Cloud KMS key version. Continue to use the same Cloud Storage bucket.",
   "B": "Create a new Cloud KMS key. Set the default CMEK key on the existing Cloud Storage bucket to the new one.",
   "C": "Create a new Cloud KMS key. Create a new Cloud Storage bucket. Copy all objects from the old bucket to the new one bucket while specifying the new Cloud KMS key in the copy command.",
   "D": "Create a new Cloud KMS key. Create a new Cloud Storage bucket configured to use the new key as the default CMEK key. Copy all objects from the old bucket to the new bucket without specifying a key."
  },
  "correct": "D",
  "correct_text": "Create a new Cloud KMS key. Create a new Cloud Storage bucket configured to use the new key as the default CMEK key. Copy all objects from the old bucket to the new bucket without specifying a key.",
  "base": "Correct Option D: Create a new Cloud KMS key. Create a new Cloud Storage bucket configured to use the new key as the default CMEK key. Copy all objects from the old bucket to the new bucket without specifying a key. This is the best practice when a CMEK key is compromised. By creating a new Cloud K…"
 },
 {
  "id": "test_13_q37",
  "q": "Scenario: In the BigQuery dataset named “customers“, all tables are tagged using a Data Catalog tag template called “gdpr“. The template includes a mandatory field, “has_sensitive_data“, which has a boolean value. All employees should have the ability to search for tables in the dataset based on whether the “has_sensitive_data“ field is true or false. However, only the Human Resources (HR) group should have access to view the data within tables where “has_sensitive_data“ is true. The all employees group has been granted the bigquery.metadataViewer and bigquery.connectionUser roles on the dataset. Considering the need to minimize configuration overhead, what should be the next step to achiev…",
  "opts": {
   "A": "Create the gdpr tag template with private visibility. Assign the bigquery.dataViewer role to the HR group on the tables that contain sensitive data.",
   "B": "Create the gdpr tag template with private visibility. Assign the datacatalog.tagTemplateViewer role on this tag to the all employees group, and assign the bigquery.dataViewer role to the HR group on the tables that contain sensitive data.",
   "C": "Create the gdpr tag template with public visibility. Assign the bigquery.dataViewer role to the HR group on the tables that contain sensitive data.",
   "D": "Create the gdpr tag template with public visibility. Assign the datacatalog.tagTemplateViewer role on this tag to the all employees group, and assign the bigquery.dataViewer role to the HR group on the tables that contain sensitive data."
  },
  "correct": "C",
  "correct_text": "Create the gdpr tag template with public visibility. Assign the bigquery.dataViewer role to the HR group on the tables that contain sensitive data.",
  "base": "The correct answer is C: Create the gdpr tag template with public visibility. Assign the bigquery.dataViewer role to the HR group on the tables that contain sensitive data.1. Creating the “gdpr“ tag template with public visibility allows all employees to view the tag template and search for table…"
 },
 {
  "id": "test_13_q44",
  "q": "Scenario: You aim to centralize your team‘s shared tables in a single dataset for convenient access by different analysts. You intend to ensure that this data is viewable but not editable by analysts. Additionally, you wish to grant analysts separate workspaces within the project to create and store tables for personal use, ensuring privacy from other team members. What steps should you take to achieve these objectives effectively?",
  "opts": {
   "A": "Give analysts the BigQuery Data Viewer role at the project level. Create one other dataset, and give the analysts the BigQuery Data Editor role on that dataset.",
   "B": "Give analysts the BigQuery Data Viewer role at the project level. Create a dataset for each analyst, and give each analyst the BigQuery Data Editor role at the project level.",
   "C": "Give analysts the BigQuery Data Viewer role on the shared dataset. Create a dataset for each analyst, and give each analyst the BigQuery Data Editor role at the dataset level for their assigned dataset.",
   "D": "Give analysts the BigQuery Data Viewer role on the shared dataset. Create one other dataset and give the analysts the BigQuery Data Editor role on that dataset."
  },
  "correct": "C",
  "correct_text": "Give analysts the BigQuery Data Viewer role on the shared dataset. Create a dataset for each analyst, and give each analyst the BigQuery Data Editor role at the dataset level for their assigned dataset.",
  "base": "The correct answer is C. Give analysts the BigQuery Data Viewer role on the shared dataset. Create a dataset for each analyst, and give each analyst the BigQuery Data Editor role at the dataset level for their assigned dataset.– By giving analysts the BigQuery Data Viewer role on the shared dataset…"
 },
 {
  "id": "test_13_q56",
  "q": "Scenario: You have created a data warehouse in BigQuery for analyzing sales data. How can you efficiently share the sales dataset with other business units in your organization while ensuring it is self-serving, low-maintenance, and cost-effective?",
  "opts": {
   "A": "Create an Analytics Hub private exchange, and publish the sales dataset.",
   "B": "Enable the other business units projects to access the authorized views of the sales dataset.",
   "C": "Create and share views with the users in the other business units.",
   "D": "Use the BigQuery Data Transfer Service to create a schedule that copies the sales dataset to the other business units projects."
  },
  "correct": "A",
  "correct_text": "Create an Analytics Hub private exchange, and publish the sales dataset.",
  "base": "A. Create an Analytics Hub private exchange, and publish the sales dataset.Creating an Analytics Hub private exchange in BigQuery is the most suitable option for sharing the sales dataset with other business units in a self-serving, low-maintenance, and cost-effective manner. An Analytics Hub allow…"
 },
 {
  "id": "test_13_q60",
  "q": "Scenario: You have migrated your on-premises Apache Hadoop Distributed File System (HDFS) data lake to Cloud Storage. The data scientist team requires processing the data with Apache Spark and SQL while enforcing security policies at the column level. You aim to implement a cost-effective solution that can scale into a data mesh. What steps should you take to achieve this objective?",
  "opts": {
   "A": "1. Deploy a long-living Dataproc cluster with Apache Hive and Ranger enabled. 2. Configure Ranger for column level security. 3. Process with Dataproc Spark or Hive SQL.",
   "B": "1. Define a BigLake table. 2. Create a taxonomy of policy tags in Data Catalog. 3. Add policy tags to columns. 4. Process with the Spark-BigQuery connector or BigQuery SQL.",
   "C": "1. Load the data to BigQuery tables. 2. Create a taxonomy of policy tags in Data Catalog. 3. Add policy tags to columns. 4. Process with the Spark-BigQuery connector or BigQuery SQL.",
   "D": "1. Apply an Identity and Access Management (IAM) policy at the file level in Cloud Storage. 2. Define a BigQuery external table for SQL processing. 3. Use Dataproc Spark to process the Cloud Storage files."
  },
  "correct": "B",
  "correct_text": "1. Define a BigLake table. 2. Create a taxonomy of policy tags in Data Catalog. 3. Add policy tags to columns. 4. Process with the Spark-BigQuery connector or BigQuery SQL.",
  "base": "The correct answer is option B. Here‘s why:1. Define a BigLake table: This step involves defining a table in BigQuery to store the data migrated from the HDFS data lake to Cloud Storage. This allows for structured data storage and processing in BigQuery.2. Create a taxonomy of policy tags in Data C…"
 },
 {
  "id": "test_14_q5",
  "q": "Scenario: Different teams in your organization store customer and performance data in BigQuery. Each team needs to maintain full control of their collected data, query data within their projects, and exchange data with other teams. How can you implement an organization-wide solution that minimizes operational tasks and costs?",
  "opts": {
   "A": "Ask each team to create authorized views of their data. Grant the biquery.jobUser role to each team.",
   "B": "Create a BigQuery scheduled query to replicate all customer data into team projects.",
   "C": "Ask each team to publish their data in Analytics Hub. Direct the other teams to subscribe to them.",
   "D": "Enable each team to create materialized views of the data they need to access in their projects."
  },
  "correct": "C",
  "correct_text": "Ask each team to publish their data in Analytics Hub. Direct the other teams to subscribe to them.",
  "base": "The correct answer is C. Ask each team to publish their data in Analytics Hub and direct the other teams to subscribe to them.– By asking each team to publish their data in Analytics Hub, you are centralizing the data exchange process and allowing each team to maintain control of their collected da…"
 },
 {
  "id": "test_14_q17",
  "q": "Scenario: Government regulations in the banking industry dictate the safeguarding of clients‘ personally identifiable information (PII). Your company mandates that PII must be access controlled, encrypted, and compliant with key data protection standards. In line with this, you are utilizing Cloud Data Loss Prevention (Cloud DLP) and aim to adhere to Google‘s recommended practices by employing service accounts to manage access to PII. What steps should you take in this situation?",
  "opts": {
   "A": "Assign the required Identity and Access Management (IAM) roles to every employee, and create a single service account to access project resources.",
   "B": "Use one service account to access a Cloud SQL database, and use separate service accounts for each human user.",
   "C": "Use Cloud Storage to comply with major data protection standards. Use one service account shared by all users.",
   "D": "Use Cloud Storage to comply with major data protection standards. Use multiple service accounts attached to IAM groups to grant the appropriate access to each group."
  },
  "correct": "D",
  "correct_text": "Use Cloud Storage to comply with major data protection standards. Use multiple service accounts attached to IAM groups to grant the appropriate access to each group.",
  "base": "Explanation of why option D is correct:D is the correct answer because using multiple service accounts attached to IAM groups is a recommended practice for controlling access to Personally Identifiable Information (PII) in Google Cloud. By using IAM groups and multiple service accounts, you can ens…"
 },
 {
  "id": "test_14_q27",
  "q": "Scenario: You have a BigQuery table containing customer data, including sensitive information like names and addresses. Your goal is to securely share this data with your data analytics and consumer support teams. The data analytics team should view all customer data but not access the sensitive information. The consumer support team should have access to all columns except for customers with inactive contracts. To achieve this, you utilized an authorized dataset and policy tags. After setting up these measures, the data analytics team still has access to the sensitive columns. What steps should you take to ensure the data analytics team cannot access restricted data? (Choose two.)",
  "opts": {
   "A": "Create two separate authorized datasets; one for the data analytics team and another for the consumer support team.",
   "B": "Ensure that the data analytics team members do not have the Data Catalog Fine-Grained Reader role for the policy tags.",
   "C": "Replace the authorized dataset with an authorized view. Use row-level security and apply filter_expression to limit data access.",
   "D": "Remove the bigquery.dataViewer role from the data analytics team on the authorized datasets.",
   "E": "Enforce access control in the policy tag taxonomy."
  },
  "correct": "B",
  "correct_text": "Ensure that the data analytics team members do not have the Data Catalog Fine-Grained Reader role for the policy tags.",
  "base": "Correct Option B. Ensure that the data analytics team members do not have the Data Catalog Fine‑Grained Reader role for the policy tags. Explanation: Policy tags in BigQuery are managed through Data Catalog. If users have the Fine‑Grained Reader role, they can bypass restrictions and view sensitive…"
 },
 {
  "id": "test_14_q33",
  "q": "Scenario: You have a BigQuery dataset containing customers‘ street addresses. How can you retrieve all instances of street addresses from the dataset?",
  "opts": {
   "A": "Write a SQL query in BigQuery by using REGEXP_CONTAINS on all tables in your dataset to find rows where the word street appears.",
   "B": "Create a deep inspection job on each table in your dataset with Cloud Data Loss Prevention and create an inspection template that includes the STREET_ADDRESS infoType.",
   "C": "Create a discovery scan configuration on your organization with Cloud Data Loss Prevention and create an inspection template that includes the STREET_ADDRESS infoType.",
   "D": "Create a de-identification job in Cloud Data Loss Prevention and use the masking transformation."
  },
  "correct": "B",
  "correct_text": "Create a deep inspection job on each table in your dataset with Cloud Data Loss Prevention and create an inspection template that includes the STREET_ADDRESS infoType.",
  "base": "The correct answer is B: Create a deep inspection job on each table in your dataset with Cloud Data Loss Prevention and create an inspection template that includes the STREET_ADDRESS infoType.When dealing with sensitive data like customers‘ street addresses, it is essential to use a solution that c…"
 },
 {
  "id": "test_14_q38",
  "q": "Scenario: Your company‘s data platform receives CSV file dumps of booking and user profile data from upstream sources and stores them in Cloud Storage. The data analyst team aims to combine these datasets based on the email field present in both, for analysis. However, it is crucial that personally identifiable information (PII) remains protected from the analysts. Therefore, you are required to de-identify the email field in both datasets before uploading them to BigQuery for analysis. What steps should you take to de-identify the email field in the datasets prior to loading them into BigQuery for the analysts‘ analysis?",
  "opts": {
   "A": "1. Create a pipeline to de-identify the email field by using recordTransformations in Cloud Data Loss Prevention (Cloud DLP) with masking as the de-identification transformations type. 2. Load the booking and user profile data into a BigQuery table.",
   "B": "1. Create a pipeline to de-identify the email field by using recordTransformations in Cloud DLP with format-preserving encryption with FFX as the de-identification transformation type. 2. Load the booking and user profile data into a BigQuery table.",
   "C": "1. Load the CSV files from Cloud Storage into a BigQuery table, and enable dynamic data masking. 2. Create a policy tag with the email mask as the data masking rule. 3. Assign the policy to the email field in both tables. 4. Assign the Identity and Access Management bigquerydatapolicy.maskedReader role for the BigQuery tables to the analysts.",
   "D": "1. Load the CSV files from Cloud Storage into a BigQuery table, and enable dynamic data masking. 2. Create a policy tag with the default masking value as the data masking rule. 3. Assign the policy to the email field in both tables. 4. Assign the Identity and Access Management bigquerydatapolicy.maskedReader role for the BigQuery tables to the analysts"
  },
  "correct": "B",
  "correct_text": "1. Create a pipeline to de-identify the email field by using recordTransformations in Cloud DLP with format-preserving encryption with FFX as the de-identification transformation type. 2. Load the booking and user profi…",
  "base": "The correct answer is option B. Here‘s why:Option B is correct because it suggests using format-preserving encryption with FFX as the de-identification transformation type. Format-preserving encryption allows you to encrypt sensitive data (such as email addresses) while preserving the format and le…"
 },
 {
  "id": "test_14_q46",
  "q": "Scenario: You are developing an Apache Beam pipeline to extract data from a Cloud SQL instance using JdbcIO. The pipeline will be deployed and executed on Dataflow in Project A, while the Cloud SQL instance is in Project B without a public IP address. VPC Service Controls and shared VPC are not utilized in these projects. How can you resolve the connection failure error in the pipeline while ensuring that the data does not traverse the public internet?",
  "opts": {
   "A": "Set up VPC Network Peering between Project A and Project B. Add a firewall rule to allow the peered subnet range to access all instances on the network.",
   "B": "Turn off the external IP addresses on the Dataflow worker. Enable Cloud NAT in Project A.",
   "C": "Add the external IP addresses of the Dataflow worker as authorized networks in the Cloud SQL instance.",
   "D": "Set up VPC Network Peering between Project A and Project B. Create a Compute Engine instance without external IP address in Project B on the peered subnet to serve as a proxy server to the Cloud SQL database."
  },
  "correct": "D",
  "correct_text": "Set up VPC Network Peering between Project A and Project B. Create a Compute Engine instance without external IP address in Project B on the peered subnet to serve as a proxy server to the Cloud SQL database.",
  "base": "The correct answer is D: Set up VPC Network Peering between Project A and Project B. Create a Compute Engine instance without an external IP address in Project B on the peered subnet to serve as a proxy server to the Cloud SQL database.– Setting up VPC Network Peering between Project A and Project…"
 },
 {
  "id": "test_14_q50",
  "q": "Scenario: Your organization has two Google Cloud projects, project A and project B. In project A, there is a Pub/Sub topic that receives data from confidential sources. Only resources within project A should have access to the data in that topic. How can you ensure that project B and any future projects are prevented from accessing data in the project A topic?",
  "opts": {
   "A": "Add firewall rules in project A so only traffic from the VPC in project A is permitted.",
   "B": "Configure VPC Service Controls in the organization with a perimeter around project A.",
   "C": "Use Identity and Access Management conditions to ensure that only users and service accounts in project A. can access resources in project A.",
   "D": "Configure VPC Service Controls in the organization with a perimeter around the VPC of project A."
  },
  "correct": "B",
  "correct_text": "Configure VPC Service Controls in the organization with a perimeter around project A.",
  "base": "The correct answer is B. Configure VPC Service Controls in the organization with a perimeter around project A.– VPC Service Controls allow you to define a security perimeter around specific resources in your Google Cloud projects. By configuring VPC Service Controls with a perimeter around project…"
 },
 {
  "id": "test_14_q54",
  "q": "Scenario: You are a member of the data governance team responsible for implementing security requirements for deploying resources. Your goal is to restrict resources to the europe-west3 region while adhering to Google‘s recommended practices. What steps should you take to achieve this goal?",
  "opts": {
   "A": "Set the constraints/gcp.resourceLocations organization policy constraint to in:europe-west3-locations.",
   "B": "Deploy resources with Terraform and implement a variable validation rule to ensure that the region is set to the europe-west3 region for all resources.",
   "C": "Set the constraints/gcp.resourceLocations organization policy constraint to in:eu-locations.",
   "D": "Create a Cloud Function to monitor all resources created and automatically destroy the ones created outside the europe-west3 region."
  },
  "correct": "A",
  "correct_text": "Set the constraints/gcp.resourceLocations organization policy constraint to in:europe-west3-locations.",
  "base": "A. Set the constraints/gcp.resourceLocations organization policy constraint to in:europe-west3-locations.Setting the constraints/gcp.resourceLocations organization policy constraint to in:europe-west3-locations is the correct approach to ensure that resources are limited to only the europe-west3 re…"
 },
 {
  "id": "test_14_q60",
  "q": "Scenario: In order to enhance data security, you need to encrypt the customer data stored in BigQuery and implement per-user crypto-deletion on the data in your tables. How can you leverage native features in Google Cloud to achieve per-user crypto-deletion for the encrypted customer data stored in BigQuery?",
  "opts": {
   "A": "Implement Authenticated Encryption with Associated Data (AEAD) BigQuery functions while storing your data in BigQuery.",
   "B": "Create a customer-managed encryption key (CMEK) in Cloud KMS. Associate the key to the table while creating the table.",
   "C": "Create a customer-managed encryption key (CMEK) in Cloud KMS. Use the key to encrypt data before storing in BigQuery.",
   "D": "Encrypt your data during ingestion by using a cryptographic library supported by your ETL pipeline."
  },
  "correct": "A",
  "correct_text": "Implement Authenticated Encryption with Associated Data (AEAD) BigQuery functions while storing your data in BigQuery.",
  "base": "A. Implement Authenticated Encryption with Associated Data (AEAD) BigQuery functions while storing your data in BigQuery.– Authenticated Encryption with Associated Data (AEAD) provides both encryption and authentication of the data, ensuring its confidentiality and integrity.– By using AEAD functio…"
 },
 {
  "id": "test_15_q24",
  "q": "Scenario: Data Analysts in your company have the Cloud IAM Owner role assigned to them in their projects to work with various GCP products. Your organization mandates retention of BigQuery data access logs for 6 months. Only audit personnel should access the data access logs for all projects. What steps should be taken to ensure that only audit personnel in your company can access the data access logs for all projects while complying with the requirement to retain logs for 6 months?",
  "opts": {
   "A": "Enable data access logs in each Data Analyst‘s project. Restrict access to Stackdriver Logging via Cloud IAM roles.",
   "B": "Export the data access logs via a project-level export sink to a Cloud Storage bucket in the Data Analysts‘ projects. Restrict access to the Cloud Storage bucket.",
   "C": "Export the data access logs via a project-level export sink to a Cloud Storage bucket in a newly created projects for audit logs. Restrict access to the project with the exported logs.",
   "D": "Export the data access logs via an aggregated export sink to a Cloud Storage bucket in a newly created project for audit logs. Restrict access to the project that contains the exported logs."
  },
  "correct": "D",
  "correct_text": "Export the data access logs via an aggregated export sink to a Cloud Storage bucket in a newly created project for audit logs. Restrict access to the project that contains the exported logs.",
  "base": "The correct answer is D. Export the data access logs via an aggregated export sink to a Cloud Storage bucket in a newly created project for audit logs. Restrict access to the project that contains the exported logs.By setting up an aggregated export sink, you can export all BigQuery data access log…"
 },
 {
  "id": "test_15_q26",
  "q": "Scenario: A data scientist has developed a BigQuery ML model and requests your assistance in setting up an ML pipeline for serving predictions. Your REST API application needs to provide predictions for a single user ID with a latency of less than 100 milliseconds. The prediction query used is: SELECT predicted_label, user_id FROM ML.PREDICT (MODEL ‘dataset.model‘, table user_features). How can you establish the ML pipeline to meet the requirements of serving predictions for an individual user ID within 100 milliseconds using the given prediction query?",
  "opts": {
   "A": "Add a WHERE clause to the query, and grant the BigQuery Data Viewer role to the application service account.",
   "B": "Create an Authorized View with the provided query. Share the dataset that contains the view with the application service account.",
   "C": "Create a Dataflow pipeline using BigQueryIO to read results from the query. Grant the Dataflow Worker role to the application service account.",
   "D": "Create a Dataflow pipeline using BigQueryIO to read predictions for all users from the query. Write the results to Bigtable using BigtableIO. Grant the Bigtable Reader role to the application service account so that the application can read predictions for individual users from Bigtable."
  },
  "correct": "D",
  "correct_text": "Create a Dataflow pipeline using BigQueryIO to read predictions for all users from the query. Write the results to Bigtable using BigtableIO. Grant the Bigtable Reader role to the application service account so that the…",
  "base": "Correct Option D: BigQuery ML.PREDICT queries have high latency unsuitable for <100ms real-time predictions. Pre-compute all predictions via Dataflow pipeline, store in Bigtable (low-latency NoSQL), and serve individual user predictions instantly from Bigtable with Reader role. Incorrect Option A:…"
 }
]

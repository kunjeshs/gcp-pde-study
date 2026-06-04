from lib import append_entries

E = {}

E["test_13_q17"] = '''### Step 4: Choose the answer

- Datastream with Cloud Interconnect and private connectivity replicates the no-public-IP MySQL database to BigQuery entirely over private networking.
- It satisfies both: serverless CDC into BigQuery and ingestion that never traverses the public internet.

### Exam shortcut

If you see:
- replicate on-prem database (no public IP) to BigQuery
- must avoid the public internet
- Datastream + private connectivity over Interconnect

Think: **Datastream + Interconnect + private connectivity**

**Tiny mental image:** a managed sync pipe running through your own private tunnel, never the open web.

**Final answer:** B. Use Datastream to replicate data from your on-premises MySQL database to BigQuery. Set up Cloud Interconnect between your on-premises data center and Google Cloud. Use Private connectivity as the connectivity method and allocate an IP address range within your VPC network to the Datastream connectivity configuration. Use Server-only as the encryption type when setting up the connection profile in Datastream.'''

E["test_13_q25"] = '''### Step 4: Choose the answer

- A separate metrics table partitioned by timestamp, with a sensorId foreign key and append-only INSERTs (joined to the small sensors table when needed), keeps high-frequency writes cheap and weekly queries efficient.
- It satisfies both: low-cost append ingestion and partition-pruned weekly analytics.

### Exam shortcut

If you see:
- high-frequency metrics + a small dimension table, weekly analytics, minimize cost
- append (INSERT), not UPDATE, in BigQuery
- partition the fact table by time, reference the dimension

Think: **separate time-partitioned metrics table, INSERT-append, join to dimension**

**Tiny mental image:** stream readings into a dated log table and join to the sensor list only when reporting.

**Final answer:** C. 1. Create a metrics table partitioned by timestamp. 2. Create a sensorId column in the metrics table, that points to the id column in the sensors table. 3. Use an INSERT statement every 30 seconds to append new metrics to the metrics table. 4. Join the two tables, if needed, when running the analytical query.'''

E["test_14_q23"] = '''### Step 4: Choose the answer

- A Dataflow pipeline programmatically identifies longtail and outlier points and cleanses the data in near-real time, writing the result to BigQuery.
- It satisfies both: near-real-time custom cleansing before the AI models and a BigQuery sink for analytics.

### Exam shortcut

If you see:
- near-real-time cleansing, detect outliers/longtail programmatically
- custom logic before ML
- land in BigQuery

Think: **Dataflow (programmatic cleansing) → BigQuery**

**Tiny mental image:** a live filter that spots the weird data points before they reach the model.

**Final answer:** B. Use Dataflow to identify longtail and outlier data points programmatically, with BigQuery as a sink.'''

E["test_14_q28"] = '''### Step 4: Choose the answer

- BigQuery Data Transfer Service with the JDBC driver and FastExport moves the Teradata history efficiently with minimal coding and without needing local staging storage.
- It satisfies the constraints: managed transfer, minimal programming, and no reliance on scarce local disk.

### Exam shortcut

If you see:
- migrate Teradata to BigQuery, minimal programming
- limited local storage (can't stage exports)
- managed transfer service

Think: **BigQuery Data Transfer Service (JDBC + FastExport)**

**Tiny mental image:** a managed pipe pulling Teradata straight into BigQuery, no local warehouse needed.

**Final answer:** A. Use BigQuery Data Transfer Service by using the Java Database Connectivity (JDBC) driver with FastExport connection.'''

E["test_14_q47"] = '''### Step 4: Choose the answer

- Dataprep lets non-technical users clean/prepare data visually into BigQuery, and Connected Sheets lets them analyze it directly in a spreadsheet.
- It satisfies both: graphical data prep and familiar spreadsheet-based analysis over BigQuery.

### Exam shortcut

If you see:
- non-technical users, graphical data cleaning
- analyze in a spreadsheet
- Dataprep + Connected Sheets

Think: **Dataprep (clean) → BigQuery → Connected Sheets (analyze)**

**Tiny mental image:** click-to-clean the data, then explore it in a familiar spreadsheet.

**Final answer:** A. Use Dataprep to clean the data, and write the results to BigQuery. Analyze the data by using Connected Sheets.'''

E["test_14_q52"] = '''### Step 4: Choose the answer

- Non-incremental materialized views (allow_non_incremental_definition) support outer joins/analytic functions, and max_staleness=4h with enable_refresh serves fast, low-maintenance results within the 4-hour freshness window.
- It satisfies both: accelerated visualization queries and reduced pipeline maintenance via managed refresh.

### Exam shortcut

If you see:
- materialized view with outer joins / analytic functions
- data can be a few hours stale (max_staleness)
- speed up viz, cut pipeline maintenance

Think: **non-incremental materialized view + max_staleness + enable_refresh**

**Tiny mental image:** a managed precomputed cache that's allowed to be up to 4 hours old, refreshed for you.

**Final answer:** A. Create materialized views with the allow_non_incremental_definition option set to true for the visualization queries. Specify the max_staleness parameter to 4 hours and the enable_refresh parameter to true. Reference the materialized views in the data visualization tool.'''

E["test_15_q4"] = '''### Step 4: Choose the answer

- Inserting each CDC record (with its operation type) into a staging table in real time, then periodically MERGE-ing into the reporting table, minimizes latency while cutting compute.
- It satisfies both: near-real-time availability via streamed staging and efficient batched application via MERGE.

### Exam shortcut

If you see:
- log-based CDC into BigQuery, low latency + low compute
- stream to staging, then batch-apply
- DML MERGE instead of per-record DML

Think: **stream CDC to a staging table + periodic MERGE into the reporting table**

**Tiny mental image:** collect the changes in an inbox, then apply them all at once in one efficient sweep.

**Final answer:** B. Insert each new CDC record and corresponding operation type to a staging table in real time.'''

E["test_15_q6"] = '''### Step 4: Choose the answer

- A dataset per department with leads as WRITER (create/update tables) and analysts as READER (query only) maps roles exactly to duties.
- It satisfies all three rules: per-department isolation, leads who can modify, analysts who can only read.

### Exam shortcut

If you see:
- per-team data isolation in BigQuery
- some users edit tables, others only query
- map roles to dataset, not project

Think: **dataset per team; WRITER for editors, READER for query-only**

**Tiny mental image:** each department's cabinet - leads have the edit key, analysts a read-only window.

**Final answer:** B. Create a dataset for each department. Assign the department leads the role of WRITER, and assign the data analysts the role of READER on their dataset.'''

E["test_15_q41"] = '''### Step 4: Choose the answer

- Partitioning by transaction time serves the "last 30 days" filter, and clustering by state, then city, then store ID matches the geographic drill-down.
- It satisfies both access patterns: date pruning plus coarse-to-fine geographic clustering.

### Exam shortcut

If you see:
- date-range filter + drill-down by a geographic hierarchy
- partition on time, cluster on the filter hierarchy
- order clustering coarse → fine (state → city → store)

Think: **partition by date, cluster state → city → store**

**Tiny mental image:** file by day, then sort within each day by state, then city, then store.

**Final answer:** A. Partition by transaction time; cluster by state first, then city, then store ID.'''

E["test_15_q47"] = '''### Step 4: Choose the answer

- Partitioning the table by transaction date lets the last-30-days queries prune to those partitions, speeding them up with no extra storage cost.
- It satisfies the goal: faster date-filtered queries via partition pruning.

### Exam shortcut

If you see:
- BigQuery date-range queries slow, don't want more storage
- partition pruning on a date column
- star schema migrated to BigQuery

Think: **partition by transaction date**

**Tiny mental image:** file sales by day so a 30-day query opens only 30 drawers.

**Final answer:** D. Partition the data by transaction date.'''

E["test_15_q52"] = '''### Step 4: Choose the answer

- Nesting the author fields inside an author column (a nested/repeated record) denormalizes the data the BigQuery-recommended way, speeding author-related queries.
- It satisfies the goal: a single table with nested structures, avoiding costly joins.

### Exam shortcut

If you see:
- BigQuery schema best practice for related entities
- avoid joins, denormalize
- nested/repeated (STRUCT/ARRAY) fields

Think: **nest related fields (nested/repeated records)**

**Tiny mental image:** tuck the author's details inside each book's record instead of a separate table to join.

**Final answer:** C. Create a table that includes information about the books and authors, but nest the author fields inside the author column.'''

E["test_15_q56"] = '''### Step 4: Choose the answer

- Moving staged data into the production table and clearing staging every few hours keeps a single master dataset without impacting ingestion or reporting.
- It satisfies the goal: one authoritative table, with periodic promotion that avoids contention.

### Exam shortcut

If you see:
- streaming into staging then promoting to production
- one master dataset, no ingestion/reporting impact
- periodic move-and-clear

Think: **promote staging → production and clear staging on an interval**

**Tiny mental image:** empty the inbox into the master file every few hours so neither pile grows messy.

**Final answer:** C. Have a staging table that moves the staged data over to the production table and deletes the contents of the staging table every three hours.'''

E["test_15_q58"] = '''### Step 4: Choose the answer

- Exporting Cloud Logging data daily to BigQuery and building views filtered by project, log type, resource, and user produces the daily consumption-and-user reports efficiently.
- It satisfies the goal: SQL-queryable, filterable daily reports from the audit/usage logs.

### Exam shortcut

If you see:
- daily reports on resource consumption + who used them
- source is Cloud Logging / audit logs
- export to BigQuery and build views

Think: **Cloud Logging → BigQuery export + filtered views**

**Tiny mental image:** pour the logs into the warehouse each day and slice them with saved views.

**Final answer:** A. Do daily exports of Cloud Logging data to BigQuery. Create views filtering by project, log type, resource, and user.'''

E["test_16_q28"] = '''### Step 4: Choose the answer

- Creating an authorized view per team in the same dataset, and granting each team data-viewer access to its view, exposes only the tables/rows that team should see.
- It satisfies the goal: per-team visibility without granting access to the base tables.

### Exam shortcut

If you see:
- teams should see only certain tables/data in BigQuery
- expose filtered results, hide base tables
- per-group sharing

Think: **authorized views per team**

**Tiny mental image:** a tailored window for each team showing only their slice of the warehouse.

**Final answer:** C. Create authorized views for each team in the same dataset in which the data resides, and assign the users/groups data viewer access to the authorized views'''

E["test_1_q7"] = '''### Step 4: Choose the answer

- Cloud Storage lifecycle conditions include Age, Is Live, and Matches Storage Class (among others) - not file size or file type.
- It satisfies the question: those three are valid lifecycle conditions.

### Exam shortcut

If you see:
- Cloud Storage Object Lifecycle Management conditions
- Age, Is Live, Matches Storage Class, Number of newer versions, Created before
- file size/type are NOT conditions

Think: **Age, Is Live, Matches Storage Class**

**Tiny mental image:** rules trigger on how old, whether current, and which class - not on the file's size or extension.

**Final answer:** B. Age'''

E["test_1_q43"] = '''### Step 4: Choose the answer

- An intermittent FetchFailedException on an autoscaling Dataproc cluster typically means the policy scaled down and shuffle data was lost when a node was decommissioned.
- It satisfies the diagnosis: aggressive scale-down removes nodes still holding shuffle data.

### Exam shortcut

If you see:
- Dataproc autoscaling + intermittent FetchFailedException
- shuffle data lost on node removal
- scale-down too aggressive

Think: **autoscaler decommissioned a node holding shuffle data**

**Tiny mental image:** a worker leaves mid-task carrying the half-done parts the next stage needed.

**Final answer:** A. The autoscaling policy is scaling down and shuffle data is lost when a node is decommissioned.'''

E["test_2_q18"] = '''### Step 4: Choose the answer

- gsutil rsync is resumable by design: re-running the same command syncs only the files that didn't upload, skipping the ones already there.
- It satisfies the goal: resume without re-uploading completed files, no special flag needed.

### Exam shortcut

If you see:
- resume a failed gsutil rsync, don't re-upload completed files
- rsync compares source and destination
- no special resume flag

Think: **just re-run the same rsync command (it resumes)**

**Tiny mental image:** rsync looks at what's already there and only ships what's missing.

**Final answer:** A. The same command that was used initially. Gsutil rsynch will automatically resume.'''

E["test_3_q23"] = '''### Step 4: Choose the answer

- Clustering the ingest-date-partitioned table on the package-tracking ID co-locates each package's records, speeding the geospatial trend queries that follow a package's lifecycle.
- It satisfies the goal: better performance via clustering on the high-cardinality query key, no re-partitioning.

### Exam shortcut

If you see:
- partitioned table, queries filter/group by a high-cardinality ID
- improve performance by clustering
- cluster on the queried entity, not the partition column

Think: **cluster on the package-tracking ID**

**Tiny mental image:** group each package's events together so its lifecycle query reads one tight block.

**Final answer:** B. Use clustering in BigQuery on the package-tracking ID column.'''

E["test_5_q6"] = '''### Step 4: Choose the answer

- Clustering the ingest-date-partitioned table on the package-tracking ID co-locates each package's records, speeding the geospatial lifecycle queries as data grows.
- It satisfies the goal: improved performance via clustering on the query key, without re-partitioning.

### Exam shortcut

If you see:
- partitioned table slowing over time, queries by a high-cardinality ID
- improve performance with clustering
- cluster on the queried entity

Think: **cluster on the package-tracking ID**

**Tiny mental image:** group each package's events so its lifecycle query reads one tight block.

**Final answer:** B. Implement clustering in BigQuery on the package-tracking ID column.'''

E["test_7_q12"] = '''### Step 4: Choose the answer

- Transforming the text files to compressed Avro with Dataflow and storing in BigQuery gives ANSI SQL, compression, and parallel loading per Google's best practices.
- It satisfies all: SQL queryability, compression, and splittable Avro for parallel loads.

### Exam shortcut

If you see:
- large text files, ANSI SQL + compression + parallel load
- self-describing, splittable format
- Avro into BigQuery

Think: **Dataflow → compressed Avro → BigQuery**

**Tiny mental image:** repackage the bulky text into compact, parallel-loadable Avro crates for the SQL warehouse.

**Final answer:** A. Transform text files to compressed Avro using Cloud Dataflow. Use BigQuery for storage and query.'''

append_entries(E)

from lib import append_entries

E = {}

E["test_6_q35"] = '''### Step 4: Choose the answer

- Cloud SQL hosts the 2 TB relational database with minimal refactoring at the lowest operating cost.
- It satisfies the goal: drop-in managed relational storage where cost, not extreme scale, is the priority.

### Exam shortcut

If you see:
- migrate a moderate relational DB, minimal app changes
- cost is the primary concern
- no global/Spanner scale needed

Think: **Cloud SQL**

**Tiny mental image:** the same database, just managed - the budget-friendly relational choice.

**Final answer:** D. Cloud SQL'''

E["test_6_q46"] = '''### Step 4: Choose the answer

- A narrow Bigtable table keyed by computer ID plus per-second timestamp handles millions of high-frequency time-series writes, real-time reads, future growth, and no per-query charges.
- It satisfies all: scalable low-latency time-series, ad hoc real-time analytics, and flat pricing.

### Exam shortcut

If you see:
- high-frequency time-series for millions of sources, real-time
- avoid per-query billing (rules out BigQuery)
- scalable wide-column, room to grow

Think: **Bigtable narrow table, row key = entity + timestamp**

**Tiny mental image:** a fast ticker ledger keyed by machine-and-second, not a pay-per-search warehouse.

**Final answer:** C. Create a narrow table in Cloud Bigtable with a row key that combines the Computer Engine computer identifier with the sample time at each second'''

E["test_7_q9"] = '''### Step 4: Choose the answer

- Year of birth and income are continuous numeric values, while country is categorical - so 2 continuous and 1 categorical.
- It satisfies the question: count numeric (continuous) vs discrete-label (categorical) columns.

### Exam shortcut

If you see:
- classify features as continuous vs categorical
- numbers on a scale = continuous; labels/groups = categorical
- year/income vs country

Think: **continuous = numeric scale, categorical = labels**

**Tiny mental image:** numbers you can average (birth year, income) vs buckets you sort into (country).

**Final answer:** D. 2 continuous and 1 categorical'''

E["test_7_q15"] = '''### Step 4: Choose the answer

- Cloud Datastore is the serverless, automatically scaling database for transactional point-of-sale data with exponential user growth and no infrastructure to manage.
- It satisfies the goal: managed, autoscaling NoSQL with transactions and zero scaling ops.

### Exam shortcut

If you see:
- exponential growth, "don't manage scaling"
- transactional app data, serverless
- autoscaling NoSQL (Datastore/Firestore)

Think: **Cloud Datastore (serverless autoscaling)**

**Tiny mental image:** a database that grows itself as the crowd doubles, no knobs to turn.

**Final answer:** D. Cloud Datastore'''

E["test_7_q26"] = '''### Step 4: Choose the answer

- Cloud Spanner is the managed, horizontally scalable relational database suited to a 20 TB operational (transactional) system.
- It satisfies the goal: SQL OLTP at large scale with strong consistency.

### Exam shortcut

If you see:
- large operational/transactional system at TB scale
- relational + scalable + strongly consistent
- beyond a single Cloud SQL instance

Think: **Cloud Spanner**

**Tiny mental image:** a relational engine that grows sideways to hold the whole transaction system.

**Final answer:** C. Cloud Spanner'''

E["test_7_q39"] = '''### Step 4: Choose the answer

- Retrying the query with exponential backoff, capped at the 15-minute refresh interval, handles the database failure gracefully without hammering it.
- It satisfies the goal: resilient frontend behavior that backs off and recovers without overload.

### Exam shortcut

If you see:
- handle a backend/database failure from a high-traffic frontend
- avoid retry storms, recover gracefully
- transient-error pattern

Think: **retry with exponential backoff (capped)**

**Tiny mental image:** knock, then wait longer and longer between knocks instead of pounding the door.

**Final answer:** B. Retry the query with exponential backoff, up to a cap of 15 minutes.'''

E["test_7_q41"] = '''### Step 4: Choose the answer

- BigQuery loads from file upload, Google Drive, and Cloud Storage, but not directly from Cloud SQL, so Cloud SQL is the source you cannot load from.
- It satisfies the "cannot" framing: Cloud SQL isn't a native load source (it's reached via federated queries instead).

### Exam shortcut

If you see:
- "which source can you NOT load into BigQuery from?"
- valid: file upload, Drive, Cloud Storage
- Cloud SQL is the odd one out

Think: **not a direct load source: Cloud SQL**

**Tiny mental image:** the loading dock accepts uploads, Drive, and GCS crates - the Cloud SQL truck has to use a different door (federation).

**Final answer:** D. Google Cloud SQL'''

E["test_8_q32"] = '''### Step 4: Choose the answer

- Cloud Spanner gives horizontally scalable transactions at 10 TB, and secondary indexes optimize the range queries on non-key columns.
- It satisfies both: scale-out relational transactions plus index support for the query patterns.

### Exam shortcut

If you see:
- relational + horizontally scalable transactions at large scale
- range/secondary-column query patterns
- global consistency

Think: **Cloud Spanner + secondary indexes**

**Tiny mental image:** a relational database that grows sideways, with extra indexes for fast range lookups.

**Final answer:** C. Use Cloud Spanner for storage. Add secondary indexes to support query patterns.'''

E["test_8_q39"] = '''### Step 4: Choose the answer

- Redefining the schema so reads and writes spread evenly across the row-key space removes the hot-spotting that's throttling Bigtable, with no added cost.
- It satisfies the goal: better performance through key/schema design rather than more nodes.

### Exam shortcut

If you see:
- Bigtable suboptimal reads/writes, minimize cost
- load concentrated on part of the key space
- fix via schema/row-key design

Think: **redesign the schema to distribute load across the row space**

**Tiny mental image:** spread the customers across all the registers instead of crowding one.

**Final answer:** A. Redefine the schema by evenly distributing reads and writes across the row space of the table.'''

E["test_11_q19"] = '''### Step 4: Choose the answer

- Keeping storage utilization per node below ~60% is the Bigtable best practice that preserves low-latency performance.
- It satisfies the goal: headroom per node so latency-sensitive reads/writes stay fast.

### Exam shortcut

If you see:
- latency-sensitive Bigtable, best practices
- per-node storage/utilization guidance
- keep headroom (~60%)

Think: **keep per-node storage utilization below ~60%**

**Tiny mental image:** don't pack each warehouse shelf past 60% or retrieval slows down.

**Final answer:** B. Keep storage utilization per node below 60%'''

E["test_11_q22"] = '''### Step 4: Choose the answer

- Storing the CSV in Cloud Storage and linking it as permanent BigQuery external tables lets multiple engines query the same files cheaply, with aggregate queries served by BigQuery.
- It satisfies the goal: low-cost shared storage plus SQL query access over the external data.

### Exam shortcut

If you see:
- large CSV in Cloud Storage queried by multiple engines
- minimize cost, query aggregates with SQL
- external/permanent tables over the bucket

Think: **Cloud Storage + BigQuery permanent external tables**

**Tiny mental image:** keep the files in the shared warehouse and put a permanent SQL window over them.

**Final answer:** D. Use Cloud Storage for storage and link the data as permanent tables in BigQuery for querying.'''

E["test_13_q23"] = '''### Step 4: Choose the answer

- Migrating to Cloud SQL for PostgreSQL keeps the same DBMS, supports the transactional workloads, and minimizes cost and complexity.
- It satisfies the goal: a managed PostgreSQL move with no engine change and the least overhead.

### Exam shortcut

If you see:
- migrate PostgreSQL "without changing the DBMS", minimize cost/complexity
- transactional workloads, managed
- simplest lift

Think: **Cloud SQL for PostgreSQL**

**Tiny mental image:** same Postgres, now managed by Google - the lowest-friction move.

**Final answer:** D. Migrate your PostgreSQL database to Cloud SQL for PostgreSQL.'''

E["test_13_q49"] = '''### Step 4: Choose the answer

- Bigtable with a sensor-ID + timestamp row key serves single-sensor-at-a-time lookups with low latency, and a daily export to BigQuery powers the complex analytic queries.
- It satisfies both access patterns: fast point reads plus once-a-day heavy analytics.

### Exam shortcut

If you see:
- time-series: low-latency point lookups + periodic heavy analytics
- key by entity + timestamp
- Bigtable for serving, BigQuery for analysis

Think: **Bigtable (entity+timestamp key) + daily export to BigQuery**

**Tiny mental image:** a fast ticker for instant lookups, dumped nightly into the analytics warehouse.

**Final answer:** B. Store your data in Bigtable. Concatenate the sensor ID and timestamp and use it as the row key. Perform an export to BigQuery every day.'''

E["test_14_q18"] = '''### Step 4: Choose the answer

- Starting with a single-region Cloud Spanner instance is cheaper now, and switching to multi-region Spanner later delivers global presence with native JDBC.
- It satisfies the phased goal: cost first, then global performance, on one relational engine that supports JDBC.

### Exam shortcut

If you see:
- start cost-optimized, later go global, native JDBC
- relational, single engine throughout
- single-region Spanner → multi-region Spanner

Think: **Cloud Spanner single-region now → multi-region later**

**Tiny mental image:** open one regional branch, then flip the switch to worldwide once funded.

**Final answer:** A. Use Cloud Spanner to configure a single region instance initially, and then configure multi-region Cloud Spanner instances after securing funding.'''

E["test_14_q26"] = '''### Step 4: Choose the answer

- BigQuery is the low-maintenance SQL data warehouse for 10 TB+; setting destination tables persists the large query results for further querying.
- It satisfies the goal: cost-effective SQL retrieval at scale with results written to new tables.

### Exam shortcut

If you see:
- large result sets from TB-scale data, store results in new tables
- low-maintenance, SQL-accessible warehouse
- analytical, not OLTP

Think: **BigQuery with destination/output tables**

**Tiny mental image:** run the big search and save the answers onto a fresh shelf.

**Final answer:** B. Use BigQuery as a data warehouse. Set output destinations for caching large queries.'''

E["test_14_q56"] = '''### Step 4: Choose the answer

- Keeping the 10 PB of history in BigQuery for analytics and serving the small last-state (in a Cloud SQL table) gives 1000 QPS sub-second API reads cost-effectively.
- It satisfies both: heavy analytics in BigQuery and low-latency key lookups from Cloud SQL.

### Exam shortcut

If you see:
- huge history for analytics + tiny "current state" served at high QPS, low latency
- split analytics store from serving store
- BigQuery (analytics) + Cloud SQL (serving)

Think: **history in BigQuery, last-state in Cloud SQL for the API**

**Tiny mental image:** the giant archive sits in the warehouse; the current snapshot sits at the fast service counter.

**Final answer:** D. 1. Store the historical data in BigQuery for analytics. 2. In a Cloud SQL table, store the last state of the product after every product change. 3. Serve the last state data directly from Cloud SQL to the API.'''

E["test_15_q7"] = '''### Step 4: Choose the answer

- Leading the row key with the datetime concentrates load on sequential rows; starting the key with the stock symbol spreads it and speeds per-company queries.
- It satisfies the fix: a key that distributes data and aligns with the per-company access pattern.

### Exam shortcut

If you see:
- Bigtable performance degrading, time-based row-key prefix
- queries are per-entity (per stock/company)
- redesign the key

Think: **lead the row key with the entity (stock symbol), not the timestamp**

**Tiny mental image:** file by company-then-time so each company's trades sit together and load spreads out.

**Final answer:** A. Change the row key syntax in your Cloud Bigtable table to begin with the stock symbol.'''

E["test_15_q12"] = '''### Step 4: Choose the answer

- Storing the full dataset in BigQuery enables warehouse-style analytics, while a compressed copy in Cloud Storage makes the data available as files for other clouds' batch tools.
- It satisfies both: in-warehouse SQL analytics and portable file access across providers.

### Exam shortcut

If you see:
- warehouse SQL analytics AND files accessible to other clouds' tools
- one platform can't serve both as-is
- BigQuery + a Cloud Storage file copy

Think: **BigQuery (analytics) + compressed copy in Cloud Storage (files)**

**Tiny mental image:** keep the searchable warehouse and also box up a portable copy other tools can pick up.

**Final answer:** C. Store the full dataset in BigQuery, and store a compressed copy of the data in a Cloud Storage bucket.'''

E["test_15_q17"] = '''### Step 4: Choose the answer

- Cloud Spanner with a North American leader and read-only replicas in Asia and Europe gives a single global endpoint, ANSI SQL, and consistent access to the latest data at high write volume.
- It satisfies all three requirements: global endpoint, SQL, and strong consistency.

### Exam shortcut

If you see:
- single global endpoint + ANSI SQL + always-current (strong consistency)
- very high write throughput, global readers
- relational at global scale

Think: **Cloud Spanner (leader + read-only replicas)**

**Tiny mental image:** one worldwide SQL front door always serving the freshest, agreed-upon data.

**Final answer:** B. Implement Cloud Spanner with the leader in North America and read-only replicas in Asia and Europe.'''

E["test_15_q22"] = '''### Step 4: Choose the answer

- A Pub/Sub topic decouples job generators (publishers) from job runners (subscribers), scaling with usage and letting new apps subscribe without affecting existing ones.
- It satisfies the goal: scalable, loosely-coupled data exchange that's easy to extend.

### Exam shortcut

If you see:
- decouple producers and consumers, scalable
- add new apps without impacting current ones
- publish/subscribe

Think: **Cloud Pub/Sub topic + subscriptions**

**Tiny mental image:** a bulletin board anyone can post to or subscribe from, independently.

**Final answer:** B. Use a Cloud Pub/Sub topic to publish jobs, and use subscriptions to execute them'''

append_entries(E)

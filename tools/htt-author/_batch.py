from lib import append_entries

E = {}

E["test_2_q39"] = '''### Step 4: Choose the answer

- Cloud SQL is the managed PostgreSQL service, so the team migrates with minimal application changes.
- It satisfies the goal: a drop-in managed PostgreSQL for a regional research team.

### Exam shortcut

If you see:
- migrate PostgreSQL/MySQL with minimal changes
- regional, moderate scale
- managed relational

Think: **Cloud SQL**

**Tiny mental image:** the same Postgres, just run and patched by Google.

**Final answer:** B. Cloud SQL'''

E["test_2_q40"] = '''### Step 4: Choose the answer

- Cloud Firestore is the managed document database that replaces MongoDB while cutting maintenance cost.
- It satisfies the goal: a managed NoSQL document store for player game data.

### Exam shortcut

If you see:
- replace MongoDB / document database, reduce maintenance
- flexible JSON/document model
- managed NoSQL

Think: **Cloud Firestore**

**Tiny mental image:** the same flexible document drawers, now maintained for you.

**Final answer:** B. Cloud Firestore'''

E["test_2_q42"] = '''### Step 4: Choose the answer

- Cloud Bigtable is the managed database built on the sparse multidimensional sorted-map model the company already uses.
- It satisfies the goal: a managed service matching that data structure (with HBase/Cassandra as the open-source equivalents).

### Exam shortcut

If you see:
- "sparse multidimensional array/map" data structure
- managed, wide-column at scale
- (open-source equivalents: HBase, Cassandra)

Think: **Cloud Bigtable**

**Tiny mental image:** a giant sparse grid where most cells are empty - Bigtable's native shape.

**Final answer:** B. Cloud Bigtable'''

E["test_2_q48"] = '''### Step 4: Choose the answer

- Cloud Spanner offers strong consistency, SQL, and horizontal global scale across North America, Asia, and Europe.
- It satisfies all: a globally distributed, strongly-consistent relational database with SQL.

### Exam shortcut

If you see:
- strong consistency + SQL + global scale
- relational across multiple continents
- transactional at scale

Think: **Cloud Spanner**

**Tiny mental image:** one SQL database that spans the globe yet always agrees with itself.

**Final answer:** A. Cloud Spanner'''

E["test_2_q50"] = '''### Step 4: Choose the answer

- Cloud Spanner provides strong global consistency, normalized relational modeling, and multi-region scale for the expanding financial service.
- It satisfies all: strongly-consistent transactions, normalized schema, and worldwide growth.

### Exam shortcut

If you see:
- strong consistency for global transactions
- normalized relational model
- multi-continent expansion

Think: **Cloud Spanner**

**Tiny mental image:** a single ledger the whole planet shares with no disagreements.

**Final answer:** A. Cloud Spanner'''

E["test_3_q9"] = '''### Step 4: Choose the answer

- BigQuery is the low-maintenance SQL data warehouse for 10 TB+; setting destination tables lets you persist large query results for further querying.
- It satisfies the goal: cost-effective SQL retrieval at scale with results written to new tables.

### Exam shortcut

If you see:
- large result sets from TB-scale data, store results in new tables
- low-maintenance, SQL-accessible warehouse
- analytical, not OLTP

Think: **BigQuery with destination/output tables**

**Tiny mental image:** run the big search and save the answers into a fresh shelf for next time.

**Final answer:** B. Use BigQuery as a data warehouse and set output destinations for caching large queries'''

E["test_3_q15"] = '''### Step 4: Choose the answer

- A narrow Bigtable table keyed by computer ID plus per-second timestamp handles millions of high-frequency time-series writes with real-time reads and no per-query charges.
- It satisfies all: scalable low-latency time-series storage, ad hoc real-time analytics, and flat (not per-query) pricing.

### Exam shortcut

If you see:
- high-frequency time-series for millions of sources, real-time
- avoid per-query billing (rules out BigQuery)
- scalable wide-column

Think: **Bigtable narrow table, row key = entity + timestamp**

**Tiny mental image:** a fast ticker ledger keyed by machine-and-second, not a pay-per-search warehouse.

**Final answer:** C. Create a narrow table in Bigtable with a row key that combines the Computer Engine computer identifier with the sample time at each second.'''

E["test_3_q21"] = '''### Step 4: Choose the answer

- Cloud Spanner is the managed, horizontally scalable relational database suited to a 20 TB operational (transactional) system.
- It satisfies the goal: SQL OLTP at large scale with strong consistency.

### Exam shortcut

If you see:
- large operational/transactional (OLTP) system at TB scale
- relational + scalable + strongly consistent
- beyond a single Cloud SQL instance

Think: **Cloud Spanner**

**Tiny mental image:** a relational engine that grows sideways to hold the whole transaction system.

**Final answer:** C. Cloud Spanner'''

E["test_3_q26"] = '''### Step 4: Choose the answer

- Cloud Spanner is fully managed, autoscaling, transactionally consistent, scales past 6 TB, and is queried with SQL.
- It satisfies every listed requirement in one managed relational service.

### Exam shortcut

If you see:
- managed + autoscale + transactional consistency + SQL + large scale
- relational beyond a single instance
- the classic Spanner checklist

Think: **Cloud Spanner**

**Tiny mental image:** the relational database that ticks every box: managed, consistent, SQL, and elastic.

**Final answer:** C. Cloud Spanner'''

E["test_3_q39"] = '''### Step 4: Choose the answer

- A Pub/Sub topic decouples job generators (publishers) from job runners (subscribers), scaling without touching existing applications.
- It satisfies the goal: asynchronous, scalable job distribution via publish/subscribe.

### Exam shortcut

If you see:
- decouple producers and consumers of jobs/messages
- scalable, no impact on existing apps
- publish/subscribe distribution

Think: **Cloud Pub/Sub topic + subscriptions**

**Tiny mental image:** a bulletin board where generators post jobs and runners pick them up independently.

**Final answer:** B. Utilize a Cloud Pub/Sub topic to publish jobs and execute them through subscriptions'''

E["test_3_q51"] = '''### Step 4: Choose the answer

- Cloud Spanner with locking read-write transactions gives ACID guarantees and SQL access for the bank's transaction data.
- It satisfies the goal: strongly-consistent, locking transactions over a scalable SQL database.

### Exam shortcut

If you see:
- ACID-compliant transactions + SQL at scale
- strong consistency (not stale reads)
- locking read-write transactions

Think: **Cloud Spanner (locking read-write transactions)**

**Tiny mental image:** a teller who locks the ledger line while updating it, so no two edits collide.

**Final answer:** B. Use Cloud Spanner to store transaction data and utilize locking read-write transactions'''

E["test_4_q10"] = '''### Step 4: Choose the answer

- Cloud SQL is the managed relational service that hosts the 3 TB database with minimal application changes at the lowest operating cost.
- It satisfies the goal: drop-in managed relational storage where cost, not extreme scale, is the priority.

### Exam shortcut

If you see:
- migrate a moderate relational DB, minimal app changes
- cost is the primary concern
- no need for global/Spanner scale

Think: **Cloud SQL**

**Tiny mental image:** the same database, just managed - the budget-friendly relational choice.

**Final answer:** D. Cloud SQL'''

E["test_4_q26"] = '''### Step 4: Choose the answer

- Adding a second Bigtable cluster with multi-cluster routing, plus separate live-traffic and batch-analytics app profiles, isolates the hourly analytics from the production workload.
- It satisfies both: production reliability and a place to run the analytical job without contention.

### Exam shortcut

If you see:
- Bigtable serving + periodic analytics on the same data
- protect production while running batch
- app profiles for workload isolation

Think: **second cluster + separate app profiles (live vs batch)**

**Tiny mental image:** give the analysts their own synced copy so they never slow the live cash registers.

**Final answer:** B. Add a second cluster to an existing instance with multi-cluster routing. Configure a live-traffic app profile to handle your regular workload, and a batch-analytics profile to handle the analytical workload'''

E["test_4_q29"] = '''### Step 4: Choose the answer

- Starting on a zonal Cloud SQL for PostgreSQL is cheapest now, and moving to Cloud Spanner later delivers global scale with native JDBC.
- It satisfies the phased goal: minimal cost initially, then global presence/performance after funding.

### Exam shortcut

If you see:
- start cheap/regional, later go global + high-performance
- relational + native JDBC
- phased: Cloud SQL now → Spanner later

Think: **Cloud SQL (zonal) now → Cloud Spanner later**

**Tiny mental image:** open one small shop first, then scale to a worldwide chain once funded.

**Final answer:** C. Start with a zonal instance of Cloud SQL for PostgreSQL, and then use Cloud Spanner after securing funding.'''

E["test_4_q39"] = '''### Step 4: Choose the answer

- Keeping raw posts in Cloud Storage (cheap archive) and the API-extracted data in BigQuery (for analysis) is the most cost-effective split.
- It satisfies both: durable low-cost archiving and SQL-queryable analytics, with minimal steps.

### Exam shortcut

If you see:
- archive raw data cheaply + analyze structured results
- SQL/dashboards on extracted data
- cost-effective, minimal steps

Think: **raw → Cloud Storage, analytics → BigQuery**

**Tiny mental image:** keep the original letters in cheap storage; file the summarized notes in the searchable index.

**Final answer:** C. Store the raw social media posts in Cloud Storage, and write the extracted data from the API into BigQuery'''

E["test_4_q46"] = '''### Step 4: Choose the answer

- Cloud Spanner with a North American leader and read-only replicas in Asia and Europe gives a single global endpoint, ANSI SQL, and consistent access to the latest data at 200K writes/sec.
- It satisfies all three requirements: global endpoint, SQL, and strong consistency under heavy write load.

### Exam shortcut

If you see:
- single global endpoint + ANSI SQL + always-current (strong consistency)
- very high write throughput, global readers
- relational at global scale

Think: **Cloud Spanner (leader + read-only replicas)**

**Tiny mental image:** one worldwide SQL front door that always serves the freshest, agreed-upon data.

**Final answer:** B. Use Cloud Spanner with the master located in North America and read-only replicas located in Asia and Europe'''

E["test_5_q10"] = '''### Step 4: Choose the answer

- Cloud Spanner is fully managed, autoscaling, transactionally consistent, scales past 6 TB, and is queried with SQL.
- It satisfies every listed requirement in one managed relational service.

### Exam shortcut

If you see:
- managed + autoscale + transactional consistency + SQL + large scale
- relational beyond a single instance
- the classic Spanner checklist

Think: **Cloud Spanner**

**Tiny mental image:** the relational database that ticks every box: managed, consistent, SQL, and elastic.

**Final answer:** C. Cloud Spanner'''

E["test_6_q16"] = '''### Step 4: Choose the answer

- Cloud Spanner with a North American leader and read-only replicas in Asia and Europe gives a single global endpoint, ANSI SQL, and consistent access to the latest data at high write volume.
- It satisfies all three requirements: global endpoint, SQL, and strong consistency under heavy load.

### Exam shortcut

If you see:
- single global endpoint + ANSI SQL + always-current (strong consistency)
- very high write throughput, global readers
- relational at global scale

Think: **Cloud Spanner (leader + read-only replicas)**

**Tiny mental image:** one worldwide SQL front door always serving the freshest, agreed-upon data.

**Final answer:** B. Implement Cloud Spanner with the leader in North America and read-only replicas in Asia and Europe.'''

E["test_6_q23"] = '''### Step 4: Choose the answer

- Adding a second Bigtable cluster with multi-cluster routing, plus separate live-traffic and batch-analytics app profiles, isolates the hourly analytics from production traffic.
- It satisfies both: production reliability and a place to run the analytical job without contention.

### Exam shortcut

If you see:
- Bigtable serving + periodic analytics on the same data
- protect production while running batch
- app profiles for workload isolation

Think: **second cluster + separate app profiles (live vs batch)**

**Tiny mental image:** give the analysts their own synced copy so they never slow the live registers.

**Final answer:** B. Add a second cluster to an existing instance with a multi-cluster routing, use live-traffic app profile for your regular workload and batch-analytics profile for the analytics workload.'''

E["test_6_q27"] = '''### Step 4: Choose the answer

- Leading the row key with the datetime concentrates writes/reads on sequential rows; starting the key with the stock symbol spreads load and speeds per-company queries.
- It satisfies the fix: a key that distributes data and aligns with the access pattern (by company).

### Exam shortcut

If you see:
- Bigtable performance degrading, time-based row-key prefix
- queries are per-entity (per stock/company)
- redesign the key to avoid hot-spotting

Think: **lead the row key with the entity (stock symbol), not the timestamp**

**Tiny mental image:** file by company-then-time so each company's trades sit together and load spreads out.

**Final answer:** A. Change the row key syntax in your Cloud Bigtable table to begin with the stock symbol.'''

append_entries(E)

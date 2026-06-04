from lib import append_entries

E = {}

E["test_15_q23"] = '''### Step 4: Choose the answer

- A random version-4 UUID primary key spreads writes evenly across Spanner's key space, avoiding the hot-spotting that sequential or time-based keys cause.
- It satisfies the goal: balanced write distribution and good insert performance.

### Exam shortcut

If you see:
- choosing a Spanner/Bigtable primary/row key for performance
- avoid monotonically increasing or timestamp-led keys
- spread writes evenly

Think: **random UUID (v4) key, not a sequential/epoch key**

**Tiny mental image:** hand out randomly-numbered tickets so the queue spreads across every window.

**Final answer:** C. A random universally unique identifier number (version 4 UUID)'''

E["test_15_q38"] = '''### Step 4: Choose the answer

- Cloud Spanner with locking read-write transactions gives ACID guarantees and SQL access for the bank's account transactions.
- It satisfies the goal: strongly-consistent, locking transactions over a scalable SQL database.

### Exam shortcut

If you see:
- ACID transactions + SQL at scale
- strong consistency (not stale reads)
- locking read-write transactions

Think: **Cloud Spanner (locking read-write transactions)**

**Tiny mental image:** a teller who locks the ledger line while updating it, so no two edits collide.

**Final answer:** B. Store transaction in Cloud Spanner. Use locking read-write transactions.'''

E["test_15_q46"] = '''### Step 4: Choose the answer

- Writing votes to Pub/Sub and a Dataflow pipeline that loads both Bigtable (real-time interim results) and BigQuery (final analysis), then shutting Bigtable down after voting, handles the burst cost-effectively.
- It satisfies all: absorb the spike, show live partial results, tally accurately, and minimize cost by releasing Bigtable when done.

### Exam shortcut

If you see:
- huge short burst of events, show live interim results + final tally
- real-time serving + later analytics
- minimize cost after the event

Think: **Pub/Sub → Dataflow → Bigtable (live) + BigQuery (final), tear down Bigtable after**

**Tiny mental image:** a live scoreboard (Bigtable) during the show and an archive (BigQuery) after - then unplug the scoreboard.

**Final answer:** D. Write votes to a Pub/Sub topic and load into both Bigtable and BigQuery via a Dataflow pipeline. Query Bigtable for real-time results and BigQuery for later analysis. Shut down the Bigtable instance when voting concludes.'''

E["test_16_q23"] = '''### Step 4: Choose the answer

- Cloud Spanner is fully managed, autoscaling, transactionally consistent, scales past 6 TB, and is queried with SQL.
- It satisfies every listed requirement in one managed relational service.

### Exam shortcut

If you see:
- managed + autoscale + transactional consistency + SQL + large scale
- relational beyond a single instance
- the classic Spanner checklist

Think: **Cloud Spanner**

**Tiny mental image:** the relational database that ticks every box: managed, consistent, SQL, elastic.

**Final answer:** C. Cloud Spanner'''

E["test_16_q27"] = '''### Step 4: Choose the answer

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

E["test_16_q42"] = '''### Step 4: Choose the answer

- A narrow Bigtable table keyed by computer ID plus per-second timestamp handles millions of high-frequency time-series writes, real-time reads, future growth, and no per-query charges.
- It satisfies all: scalable low-latency time-series, ad hoc real-time analytics, and flat pricing.

### Exam shortcut

If you see:
- high-frequency time-series for millions of sources, real-time
- avoid per-query billing (rules out BigQuery)
- scalable wide-column, room to grow

Think: **Bigtable narrow table, row key = entity + timestamp**

**Tiny mental image:** a fast ticker ledger keyed by machine-and-second, not a pay-per-search warehouse.

**Final answer:** C. Create a narrow table in Bigtable with a row key that combines the Computer Engine computer identifier with the sample time at each second'''

E["test_10_q2"] = '''### Step 4: Choose the answer

- Cloud Data Catalog automatically extracts and indexes metadata from Cloud Storage and BigQuery, so engineers and analysts can search and find datasets quickly.
- It satisfies the goal: a managed discovery/metadata layer that cuts the effort of locating data.

### Exam shortcut

If you see:
- users can't find datasets across GCS/BigQuery
- need search/discovery, metadata catalog
- reduce data-hunting workload

Think: **Data Catalog (auto metadata + search)**

**Tiny mental image:** a library catalog that auto-indexes every shelf so nobody wanders the stacks.

**Final answer:** C. Use Cloud Data Catalog to automatically extract metadata from Cloud Storage objects and BigQuery data.'''

E["test_1_q44"] = '''### Step 4: Choose the answer

- Materialized view costs rise with how often they refresh (each refresh scans/processes data) and the volume of data they store.
- It satisfies the question: refresh frequency (and stored volume) are the cost drivers, not datatypes or reader count.

### Exam shortcut

If you see:
- unexpected materialized-view costs
- what drives the bill: refresh frequency + stored data volume
- not datatypes / reader count

Think: **refresh frequency (and data volume) drive MV cost**

**Tiny mental image:** the more often you re-bake the cached cake - and the bigger it is - the higher the bill.

**Final answer:** B. The frequency of materialized view refresh'''

E["test_1_q49"] = '''### Step 4: Choose the answer

- BigQuery BI Engine is the in-memory analysis layer that delivers fast, interactive, in-memory query performance comparable to on-prem in-memory analytics.
- It satisfies the goal: sub-second, in-memory acceleration directly over BigQuery.

### Exam shortcut

If you see:
- want fast in-memory/interactive analytics on BigQuery
- comparable to on-prem in-memory tools
- acceleration layer

Think: **BigQuery BI Engine**

**Tiny mental image:** a built-in in-memory turbo for BigQuery dashboards.

**Final answer:** B. BigQuery BI Engine'''

E["test_2_q20"] = '''### Step 4: Choose the answer

- Avoiding SELECT * (read only needed columns) and estimating bytes with a dry run before running queries cut BigQuery's bytes-scanned cost.
- It satisfies the goal: reduce data scanned per query, the main BigQuery cost lever.

### Exam shortcut

If you see:
- reduce BigQuery query cost
- column pruning (no SELECT *) + estimate bytes first
- pay per bytes scanned

Think: **avoid SELECT \\*, dry-run estimate bytes (and partition/cluster)**

**Tiny mental image:** ask only for the columns you need and check the meter before running the search.

**Final answer:** A. Avoid using SELECT *'''

E["test_2_q28"] = '''### Step 4: Choose the answer

- The narrowly-scoped predefined role that adds only materialized-view refresh permission on top of dataViewer is the right least-privilege grant.
- It satisfies the goal: enable refresh without granting broader editor/owner/admin rights.

### Exam shortcut

If you see:
- add only the ability to refresh a materialized view
- keep least privilege (not dataEditor/dataOwner/admin)
- predefined, narrowly-scoped role

Think: **the minimal MV-refresh predefined role, not a broad editor/admin role**

**Tiny mental image:** hand over just the "press refresh" button, not the keys to edit the data.

**Final answer:** D. bigquery.mvUpdater'''

E["test_3_q32"] = '''### Step 4: Choose the answer

- BigQuery natively supports geospatial (GIS) functions and ML predictions over the 40 TB dataset, and pairs with a dashboard to show at-risk ships by region.
- It satisfies all: storage at scale, native prediction (BigQuery ML), geospatial processing (GeoJSON/GIS), and BI dashboards.

### Exam shortcut

If you see:
- large analytics dataset needing native prediction (ML) + geospatial (GIS)
- dashboard/reporting on top
- SQL at TB+ scale

Think: **BigQuery (BigQuery ML + GIS)**

**Tiny mental image:** one warehouse that maps the ships, predicts delays, and feeds the dashboard.

**Final answer:** A. BigQuery'''

E["test_3_q43"] = '''### Step 4: Choose the answer

- Partitioning the table by transaction date lets queries over the past 30 days prune to those partitions, speeding them up with no extra storage cost.
- It satisfies the goal: faster date-filtered queries via partition pruning.

### Exam shortcut

If you see:
- BigQuery date-range queries slow, don't want more storage
- partition pruning on a date column
- star schema migrated to BigQuery

Think: **partition by transaction date**

**Tiny mental image:** file sales by day so a 30-day query opens only 30 drawers.

**Final answer:** D. Partition the data by transaction date.'''

E["test_4_q22"] = '''### Step 4: Choose the answer

- Streaming inventory changes into a daily movement table and computing balances in a view joined to the historical balances (refreshed nightly) keeps the dashboard near-real-time, accurate, and fast.
- It satisfies both: live accuracy via streamed deltas and high performance by avoiding constant table updates.

### Exam shortcut

If you see:
- near-real-time BigQuery dashboard, frequent updates, accuracy + performance
- avoid row-by-row UPDATEs
- stream deltas, compute current state in a view

Think: **stream changes to a movement table + balance view, reconcile nightly**

**Tiny mental image:** log every transaction live and add it to last night's balance, instead of rewriting the ledger each change.

**Final answer:** C. Use the BigQuery streaming to stream changes into a daily inventory movement table. Calculate balances in a view that joins it to the historical inventory balance table. Update the inventory balance table nightly.'''

E["test_4_q33"] = '''### Step 4: Choose the answer

- Moving staged data into the production table and clearing the staging table every few hours keeps a single master dataset without impacting ingestion or reporting.
- It satisfies the goal: one authoritative table, with periodic promotion that avoids contention.

### Exam shortcut

If you see:
- streaming into staging then promoting to production
- one master dataset, no ingestion/reporting impact
- periodic move-and-clear

Think: **promote staging → production and clear staging on an interval**

**Tiny mental image:** empty the inbox into the master file every few hours so neither pile grows messy.

**Final answer:** C. Move staged data to the production table and delete the staging table contents every three hours'''

E["test_4_q35"] = '''### Step 4: Choose the answer

- Nesting the author fields inside an author column (a nested/repeated record) denormalizes the data the BigQuery-recommended way, speeding author-related queries.
- It satisfies the goal: a single table with nested structures, avoiding costly joins.

### Exam shortcut

If you see:
- BigQuery schema best practice for related entities
- avoid joins, denormalize
- nested/repeated (STRUCT/ARRAY) fields

Think: **nest related fields (nested/repeated records)**

**Tiny mental image:** tuck the author's details inside each book's record instead of a separate table to join.

**Final answer:** C. Create a table that includes information about the books and authors, but nest the author fields inside the author column'''

E["test_4_q37"] = '''### Step 4: Choose the answer

- Recreating the table with a partitioning column (timestamp) and a clustering column (ID) lets BigQuery prune and skip data so the filtered query no longer full-scans.
- It satisfies the goal: minimize bytes scanned while keeping the same SQL.

### Exam shortcut

If you see:
- filtered BigQuery query still full-scans, reduce bytes
- filters on a time column + an ID column
- partition + cluster

Think: **partition (date/time) + cluster (ID)**

**Tiny mental image:** file by date and sort within each day by ID, so the query opens only the right drawers.

**Final answer:** C. Recreate the table with a partitioning column and clustering column'''

E["test_4_q50"] = '''### Step 4: Choose the answer

- Storing the full dataset in BigQuery enables warehouse-style analytics, while a compressed copy in Cloud Storage makes it available as files for other clouds' batch tools.
- It satisfies both: in-warehouse SQL analytics and portable file access across providers.

### Exam shortcut

If you see:
- warehouse SQL analytics AND files accessible to other clouds' tools
- one platform can't serve both as-is
- BigQuery + a Cloud Storage file copy

Think: **BigQuery (analytics) + compressed copy in Cloud Storage (files)**

**Tiny mental image:** keep the searchable warehouse and also box up a portable copy for other tools.

**Final answer:** C. Store the full dataset in BigQuery, and store a compressed copy of the data in a Cloud Storage bucket'''

E["test_5_q7"] = '''### Step 4: Choose the answer

- Splitting data into multiple tables (e.g., sharding) and using partitions reduces the rows BigQuery must scan; LIMIT does not reduce bytes scanned.
- It satisfies the question: physical data layout (tables/partitions) prunes data, unlike LIMIT.

### Exam shortcut

If you see:
- reduce rows/bytes BigQuery processes
- LIMIT does NOT cut bytes scanned
- partition/shard the data

Think: **partitions + table splitting (not LIMIT)**

**Tiny mental image:** opening fewer drawers (partitions) saves work; LIMIT just trims the answer after reading everything.

**Final answer:** A. Splitting tables into multiple tables; putting data in partitions'''

E["test_5_q8"] = '''### Step 4: Choose the answer

- The wildcard table reference must wrap the whole identifier in backticks with the * inside, which is the correctly-quoted form here.
- It satisfies the goal: valid wildcard-table syntax so the query matches the similarly-named tables.

### Exam shortcut

If you see:
- BigQuery wildcard table query failing on quoting
- backtick-quote the full identifier, * inside
- match many similarly-named tables

Think: **backtick-quoted identifier with the trailing \\***

**Tiny mental image:** wrap the whole table name in backticks and put the star inside the quotes.

**Final answer:** D. 'bigquery-public-data.noaa_gsod.gsod*`'''

append_entries(E)

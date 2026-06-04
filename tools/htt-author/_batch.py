from lib import append_entries

E = {}

E["test_5_q11"] = '''### Step 4: Choose the answer

- Streaming inventory changes into a daily movement table and computing balances in a view joined to the historical balances (refreshed nightly) keeps the dashboard near-real-time, accurate, and fast.
- It satisfies both: live accuracy via streamed deltas and high performance by avoiding constant row updates.

### Exam shortcut

If you see:
- near-real-time BigQuery dashboard, frequent updates, accuracy + performance
- avoid row-by-row UPDATEs
- stream deltas, compute current state in a view

Think: **stream changes to a movement table + balance view, reconcile nightly**

**Tiny mental image:** log every transaction live and add it to last night's balance, instead of rewriting the ledger.

**Final answer:** C. Use the BigQuery streaming the stream changes into a daily inventory movement table. Calculate balances in a view that joins it to the historical inventory balance table. Update the inventory balance table nightly.'''

E["test_5_q20"] = '''### Step 4: Choose the answer

- The BigQuery Web UI can load data containing nested and repeated fields; it can't upload SQL files, 20 MB files, or wildcard-match multiple files.
- It satisfies the question: nested/repeated loading is the supported Web UI operation.

### Exam shortcut

If you see:
- "what can the BigQuery Web UI do?"
- nested/repeated field loading supported
- size/wildcard/SQL-file uploads are not

Think: **load nested and repeated fields via the Web UI**

**Tiny mental image:** the console handles structured (nested) loads, not bulk wildcard or oversized uploads.

**Final answer:** B. Load data with nested and repeated fields.'''

E["test_5_q24"] = '''### Step 4: Choose the answer

- In legacy SQL, TABLE_DATE_RANGE selects across the daily app_events_YYYYMMDD tables for the past 30 days.
- It satisfies the goal: query a range of date-sharded tables in legacy SQL.

### Exam shortcut

If you see:
- query daily date-sharded tables (table_YYYYMMDD) over a range
- legacy SQL
- date-range wildcard function

Think: **TABLE_DATE_RANGE (legacy SQL)**

**Tiny mental image:** one function that fans out across all the daily tables in the window.

**Final answer:** A. Use the TABLE_DATE_RANGE function'''

E["test_5_q28"] = '''### Step 4: Choose the answer

- ROW_NUMBER partitioned by the unique ID (ordered by timestamp), keeping only row 1, deduplicates the possibly-duplicated streaming inserts at query time.
- It satisfies the goal: one row per unique ID despite at-least-once streaming duplicates.

### Exam shortcut

If you see:
- de-duplicate streamed rows with a unique ID + timestamp
- pick the latest/one record per ID at query time
- window function

Think: **ROW_NUMBER() OVER (PARTITION BY id ...) = 1**

**Tiny mental image:** number the copies of each ID and keep only number one.

**Final answer:** D. Use the ROW_NUMBER window function with PARTITION by unique ID along with WHERE row equals 1.'''

E["test_5_q30"] = '''### Step 4: Choose the answer

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

E["test_5_q46"] = '''### Step 4: Choose the answer

- There is no charge for a query that returns results from cache - that's the true statement about BigQuery caching.
- It satisfies the question: cached results are free (and cached by default, for ~24h, but not when a destination table is set).

### Exam shortcut

If you see:
- BigQuery caching facts
- cached results are free
- cached by default, ~24h, skipped with a destination table

Think: **no charge for cache-hit queries**

**Tiny mental image:** re-asking the same question returns the saved answer for free.

**Final answer:** D. There is no charge for a query that retrieves its results from cache.'''

E["test_6_q17"] = '''### Step 4: Choose the answer

- Recreating the table with a partitioning column (timestamp) and clustering column (ID) lets BigQuery prune so the filtered query no longer full-scans, with no SQL changes.
- It satisfies the goal: minimize bytes scanned while keeping the same queries.

### Exam shortcut

If you see:
- filtered BigQuery query still full-scans, reduce bytes
- filters on a time column + an ID column
- minimal SQL change

Think: **partition (date/time) + cluster (ID)**

**Tiny mental image:** file by date and sort within each day by ID, so the query opens only the right drawers.

**Final answer:** C. Recreate the table with a partitioning column and clustering column.'''

E["test_6_q21"] = '''### Step 4: Choose the answer

- The false statement is that you set a query language per dataset (default Standard SQL); the dialect is chosen per query, not per dataset.
- It satisfies the "not true" framing: there's no per-dataset language setting.

### Exam shortcut

If you see:
- "which Legacy vs Standard SQL statement is FALSE"
- dialect is set per query, not per dataset
- Standard SQL is preferred

Think: **no per-dataset language setting (chosen per query)**

**Tiny mental image:** you pick the language each time you ask, not once per cabinet.

**Final answer:** D. You need to set a query language for each dataset and the default is Standard SQL.'''

E["test_6_q25"] = '''### Step 4: Choose the answer

- Creating an authorized view per team in the same dataset, and granting each team data-viewer access to its view, exposes only the rows/tables that team should see.
- It satisfies the goal: per-team table/column visibility without granting access to the base tables.

### Exam shortcut

If you see:
- teams should see only certain tables/data in BigQuery
- expose filtered results, hide base tables
- per-group sharing

Think: **authorized views per team**

**Tiny mental image:** a tailored window for each team that shows only their slice, not the whole warehouse.

**Final answer:** C. Create authorized views for each team in the same dataset in which the data resides, and assign the users/groups data viewer access to the authorized views'''

E["test_6_q43"] = '''### Step 4: Choose the answer

- SELECT controls which columns are read, so choosing specific columns (not SELECT *) reduces the columns BigQuery processes.
- It satisfies the question: SELECT is the column-pruning lever (WHERE/LIMIT affect rows, not columns).

### Exam shortcut

If you see:
- reduce *columns* processed in BigQuery
- column pruning, not row filtering
- SELECT specific columns vs SELECT *

Think: **SELECT (only the needed columns)**

**Tiny mental image:** ask for two columns, not the whole row.

**Final answer:** C. SELECT'''

E["test_7_q11"] = '''### Step 4: Choose the answer

- Converting the date-sharded LOGS_yyyymmdd tables into a single date-partitioned table removes the 1,000-table wildcard limit while keeping date-range queries efficient.
- It satisfies the goal: long date-range queries succeed and run efficiently via partition pruning.

### Exam shortcut

If you see:
- wildcard queries over daily sharded tables hitting the 1,000-table limit
- consolidate many date-named tables
- migrate to partitioning

Think: **sharded tables → single date-partitioned table**

**Tiny mental image:** merge a thousand daily files into one cabinet with dated drawers.

**Final answer:** B. Convert the sharded tables into a single partitioned table'''

E["test_7_q16"] = '''### Step 4: Choose the answer

- Storing the CSV in Cloud Storage and linking it as permanent BigQuery external tables lets multiple engines query the same files cheaply, with aggregate queries served by BigQuery.
- It satisfies the goal: low-cost shared storage plus SQL query access over the external data.

### Exam shortcut

If you see:
- large CSV in Cloud Storage queried by multiple engines
- minimize cost, query aggregates with SQL
- external/permanent tables over the bucket

Think: **Cloud Storage + BigQuery permanent external tables**

**Tiny mental image:** keep the files in the shared warehouse and put a permanent SQL window over them.

**Final answer:** C. Use Cloud Storage for storage. Link as permanent tables in BigQuery for query.'''

E["test_7_q33"] = '''### Step 4: Choose the answer

- Normalizing the single patient table into separate patient and visits tables (plus supporting tables) eliminates the expensive self-joins that break at 100x scale.
- It satisfies the goal: a relational design that scales reporting without the self-join blow-up.

### Exam shortcut

If you see:
- a single table with self-joins failing as data grows
- reports too slow / out of resources
- relational redesign

Think: **normalize into separate related tables (remove self-joins)**

**Tiny mental image:** split the giant all-in-one ledger into patients and visits so the joins stay sane.

**Final answer:** C. Normalize the master patient-record table into the patient table and the visits table, and create other necessary tables to avoid self-join.'''

E["test_7_q40"] = '''### Step 4: Choose the answer

- Denormalized structures in BigQuery increase query speed (fewer joins) and make queries simpler to write.
- It satisfies the question: the benefits are speed and simplicity, not reduced storage.

### Exam shortcut

If you see:
- benefits of denormalization in BigQuery
- fewer joins → faster + simpler queries
- (storage may actually increase)

Think: **faster queries + simpler queries**

**Tiny mental image:** everything in one wide table means no hunting across joins - quicker and easier.

**Final answer:** B. Increases query speed, makes queries simpler'''

E["test_8_q31"] = '''### Step 4: Choose the answer

- You cannot turn a table into a partitioned table by ordering rows and changing its type; that's the unsupported method.
- It satisfies the "not supported" framing: loading per-partition, querying into a $YYYYMMDD destination, and streaming are valid; ORDER BY + type change is not.

### Exam shortcut

If you see:
- "which is NOT a way to populate a partitioned table"
- valid: load per partition, query into $YYYYMMDD, stream
- ORDER BY then "change type" is the impostor

Think: **can't sort rows and flip the table to "partitioned"**

**Tiny mental image:** sorting the pages doesn't magically turn the binder into a dated-tab binder.

**Final answer:** D. Use ORDER BY to put a table‘s rows into chronological order and then change the table‘s type to “Partitioned“.'''

E["test_8_q43"] = '''### Step 4: Choose the answer

- The two BigQuery denormalization methods are joining tables into one wide table and using nested/repeated fields.
- It satisfies the question: both consolidate related data to avoid query-time joins.

### Exam shortcut

If you see:
- ways to denormalize in BigQuery
- join into one table OR use nested/repeated (STRUCT/ARRAY)
- (partitioning is not denormalization)

Think: **join into one table + nested repeated fields**

**Tiny mental image:** flatten the joins into one wide table, or tuck the children inside each parent row.

**Final answer:** B. 1) Join tables into one table; 2) Use nested repeated fields'''

E["test_9_q16"] = '''### Step 4: Choose the answer

- Partitioning by transaction time serves the "past 30 days" filter, and clustering by state, city, then store ID matches the geographic drill-down for fast trend queries.
- It satisfies both access patterns: date pruning plus hierarchical geographic clustering.

### Exam shortcut

If you see:
- date-range filter + drill-down by a geographic hierarchy
- partition on time, cluster on the filter hierarchy
- order clustering columns coarse → fine (state → city → store)

Think: **partition by date, cluster state → city → store**

**Tiny mental image:** file by day, then sort within each day by state, then city, then store.

**Final answer:** C. Partition the table by transaction time and cluster it by state, city, and then store ID'''

E["test_12_q26"] = '''### Step 4: Choose the answer

- BigQuery external tables over Cloud Storage support Avro, ORC, Parquet, CSV, JSON, and Datastore/Firestore exports - but not Excel .xlsx.
- It satisfies the "not supported" framing: xlsx is the format BigQuery can't read as an external table.

### Exam shortcut

If you see:
- "which format is NOT supported for BigQuery external tables"
- supported: Avro, ORC, Parquet, CSV, JSON, Firestore/Datastore export
- Excel xlsx is the odd one out

Think: **Excel .xlsx is not supported**

**Tiny mental image:** the warehouse reads data formats, not spreadsheet workbooks.

**Final answer:** D. Excel xlsx format'''

E["test_13_q8"] = '''### Step 4: Choose the answer

- A materialized view precomputes the frequent query/aggregation, so repeated daily access is faster and simpler for other users, staying fresh automatically.
- It satisfies the goal: accelerated, simplified aggregations over the petabyte-scale table.

### Exam shortcut

If you see:
- same heavy query/aggregation run repeatedly, speed it up
- precompute results, auto-refresh
- simplify for other users

Think: **materialized view**

**Tiny mental image:** bake the common report once and keep it warm, instead of re-cooking each time.

**Final answer:** D. Create a materialized view based off of the query being run.'''

E["test_13_q12"] = '''### Step 4: Choose the answer

- Clustering the table by country and username co-locates rows for those filters, so the dashboard's country/username lookups scan far less data.
- It satisfies the goal: fast filtered access without a natural date partition column.

### Exam shortcut

If you see:
- dashboard filters on non-date fields (country, username)
- no good time/date partition key
- speed up filtered lookups

Think: **cluster by the filter columns (country, username)**

**Tiny mental image:** sort the giant table by country then username so each lookup jumps straight to its block.

**Final answer:** A. Cluster the table by country and username fields.'''

append_entries(E)

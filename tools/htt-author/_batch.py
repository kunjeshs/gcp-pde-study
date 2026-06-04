from lib import append_entries

E = {}

E["test_3_q19"] = '''### Step 4: Choose the answer

- A Cloud Composer DAG models the mix of sequential and concurrent Spark jobs as task dependencies and automates the scheduled run.
- It satisfies the goal: orchestrate complex inter-job ordering, not just submit jobs.

### Exam shortcut

If you see:
- jobs with mixed sequential + concurrent dependencies, scheduled
- automate a multi-job workflow
- orchestration across steps

Think: **Cloud Composer DAG**

**Tiny mental image:** a dependency graph the conductor follows, cueing some jobs in series and others in parallel.

**Final answer:** C. Create a Directed Acyclic Graph in Cloud Composer'''

E["test_4_q30"] = '''### Step 4: Choose the answer

- The bottleneck for a network transfer is the link itself, so upgrading the datacenter-to-GCP bandwidth is what actually speeds the daily uploads.
- It satisfies the goal: more throughput on the constrained path, not bigger CPU or disk on the server.

### Exam shortcut

If you see:
- transfers from on-prem to Cloud Storage too slow
- maximize transfer speed
- distractors about CPU/disk size

Think: **increase network bandwidth on the transfer link**

**Tiny mental image:** the truck isn't slow because of its engine - the road is too narrow; widen the road.

**Final answer:** C. Upgrade your datacenter‘s network bandwidth to GCP.'''

E["test_7_q47"] = '''### Step 4: Choose the answer

- The bottleneck is the datacenter-to-GCP link, so increasing that network bandwidth is what speeds up the daily transfers.
- It satisfies the goal: more throughput on the constrained path, not server CPU or disk.

### Exam shortcut

If you see:
- on-prem → Cloud Storage transfers too slow
- maximize transfer speed
- distractors about CPU/disk size

Think: **increase network bandwidth from the datacenter to GCP**

**Tiny mental image:** widen the road, don't upgrade the truck's stereo.

**Final answer:** C. Increase your network bandwidth from your datacenter to GCP.'''

E["test_13_q38"] = '''### Step 4: Choose the answer

- Cloud Build copies the DAG to the dev Composer bucket for testing, then on success copies it to the prod Composer bucket - DAGs deploy simply by landing in the bucket.
- It satisfies the CI/CD goal: tag-triggered, tested, environment-promoted deployment without containers.

### Exam shortcut

If you see:
- CI/CD for Cloud Composer DAGs, dev → prod promotion
- how DAGs deploy (copy to the Composer GCS bucket)
- triggered by a Git tag via Cloud Build

Think: **Cloud Build copies DAG to dev bucket, then prod bucket**

**Tiny mental image:** dropping the DAG file into Composer's folder is the deploy - test in the dev folder, then copy to prod.

**Final answer:** A. 1. Use Cloud Build to copy the code of the DAG to the Cloud Storage bucket of the development instance for DAG testing. 2. If the tests pass, use Cloud Build to copy the code to the bucket of the production instance.'''

E["test_14_q12"] = '''### Step 4: Choose the answer

- A Pub/Sub push subscription triggering a Cloud Function that calls the Python API is a serverless, secure queue that scales with trade volume and uses minimal idle resources.
- It satisfies the goal: event-driven trade processing with no always-on servers.

### Exam shortcut

If you see:
- secure queue triggering jobs via an API, efficient
- serverless, event-driven, high volume
- Pub/Sub + Cloud Function

Think: **Pub/Sub push → Cloud Function → API**

**Tiny mental image:** each trade rings a doorbell that wakes a function only when needed.

**Final answer:** A. Use a Pub/Sub push subscription to trigger a Cloud Function to pass the data to the Python API.'''

E["test_14_q15"] = '''### Step 4: Choose the answer

- Cloud Composer in a Shared VPC, with resources in the service project, is the Google-managed Airflow option that fits the Shared VPC model.
- It satisfies both: managed open-source orchestration and correct Shared VPC placement.

### Exam shortcut

If you see:
- managed open-source (Airflow) workflow scheduling
- Shared VPC networking
- where do Composer resources live?

Think: **Cloud Composer in Shared VPC, resources in the service project**

**Tiny mental image:** the tenant runs its scheduler while borrowing the landlord's network.

**Final answer:** D. Use Cloud Composer in a Shared VPC configuration. Place the Cloud Composer resources in the service project.'''

E["test_16_q32"] = '''### Step 4: Choose the answer

- Cloud Composer (managed Airflow) orchestrates the interdependent steps in order, mixing shell, Hadoop, and BigQuery tasks with built-in retries.
- It satisfies the goal: dependency-aware, long-running workflow orchestration with retry on failure.

### Exam shortcut

If you see:
- multi-step workflow with dependencies/ordering
- mixed task types (shell, Hadoop, BigQuery), retries
- orchestrate, not just schedule

Think: **Cloud Composer (Airflow DAG)**

**Tiny mental image:** a conductor cueing each section in order and signaling a retry when one stumbles.

**Final answer:** D. Cloud Composer'''

E["test_11_q23"] = '''### Step 4: Choose the answer

- Cloud Spanner gives horizontally scalable, strongly-consistent transactions at 10 TB, and secondary indexes optimize the range queries on non-key columns.
- It satisfies both: scale-out relational transactions plus index support for the query patterns.

### Exam shortcut

If you see:
- relational + horizontally scalable transactions at large scale
- range/secondary-column query patterns
- global consistency

Think: **Cloud Spanner + secondary indexes**

**Tiny mental image:** a relational database that grows sideways across machines, with extra indexes for fast range lookups.

**Final answer:** A. Use Cloud Spanner for storage and add secondary indexes to support query patterns'''

E["test_1_q9"] = '''### Step 4: Choose the answer

- gcloud datastore export to the bucket with --async issues the backup and returns immediately while it runs in the background.
- It satisfies the goal: a non-blocking managed export of Firestore/Datastore to Cloud Storage.

### Exam shortcut

If you see:
- back up Firestore/Datastore to a Cloud Storage bucket
- command returns immediately / runs in background
- gcloud (not gsutil), export, --async

Think: **gcloud datastore export gs://... --async**

**Tiny mental image:** fire off the backup and walk away - the --async flag means you don't wait.

**Final answer:** B. gcloud datastore export gs://game-ds-backup --async'''

E["test_12_q15"] = '''### Step 4: Choose the answer

- Bigtable delivers high-volume, low-latency writes at scale and exposes the HBase API, making it the managed successor to the company's HBase usage.
- It satisfies both: massive write throughput for drone telemetry and a familiar HBase-compatible interface.

### Exam shortcut

If you see:
- high-volume, low-latency writes (IoT/time-series)
- migrating from Hadoop HBase to managed
- scale to huge data

Think: **Cloud Bigtable**

**Tiny mental image:** a high-speed ledger built for nonstop sensor writes, speaking the HBase dialect.

**Final answer:** D. Bigtable'''

E["test_11_q53"] = '''### Step 4: Choose the answer

- Cloud Firestore is the managed, document-oriented database that maps naturally from MongoDB's document model.
- It satisfies the goal: a managed NoSQL document store for the migrated application.

### Exam shortcut

If you see:
- migrate MongoDB (or a document database) to managed GCP
- flexible document/JSON model
- not wide-column or relational

Think: **Cloud Firestore**

**Tiny mental image:** swap one document drawer for a managed one with the same flexible folders.

**Final answer:** D. Cloud Firestore'''

E["test_11_q9"] = '''### Step 4: Choose the answer

- In the Firestore data model, an entity (document) is analogous to a row in a relational table.
- It satisfies the question: entity ≈ row, kind ≈ table, property ≈ column.

### Exam shortcut

If you see:
- map Firestore/Datastore concepts to relational ones
- "what is like a row?"
- entity vs kind vs property

Think: **entity = row** (kind = table)

**Tiny mental image:** each entity is one record card; the kind is the whole filing drawer.

**Final answer:** B. Entity'''

E["test_11_q55"] = '''### Step 4: Choose the answer

- Hot-spotting on one node means the row key groups time-adjacent writes together, sending them to a single node instead of spreading them.
- It satisfies the diagnosis: sequential/time-based keys concentrate load; a better-distributed key fixes it.

### Exam shortcut

If you see:
- Bigtable writes hitting one node, uneven distribution
- time-series / sequential row keys
- hot-spotting

Think: **row key concentrates time-adjacent writes (bad key design)**

**Tiny mental image:** everyone arriving at once lines up at one register because the tickets are numbered in order.

**Final answer:** B. Using a row key that causes data that arrives close in time to be written to a single node, rather than evenly distributed.'''

E["test_10_q48"] = '''### Step 4: Choose the answer

- A document model stores each possession as a flexible document, absorbing frequent schema changes without costly normalized-schema migrations.
- It satisfies the goal: schema flexibility for evolving game features and possession types.

### Exam shortcut

If you see:
- frequent schema changes painful in a normalized relational model
- flexible/evolving entity attributes
- semi-structured records

Think: **document data model**

**Tiny mental image:** loose folders you can add fields to anytime, instead of rigid pre-cut table columns.

**Final answer:** A. Document model'''

E["test_11_q32"] = '''### Step 4: Choose the answer

- Cloud Storage is the right home for large FASTQ files; Dataflow reads them from the bucket and writes results to BigQuery.
- It satisfies the goal: cheap, scalable object storage for big files that the pipeline then processes.

### Exam shortcut

If you see:
- store large raw files (genomic/FASTQ, media, blobs)
- processed later by Dataflow/Dataproc
- object, not table, storage

Think: **Cloud Storage (files) → Dataflow → BigQuery (results)**

**Tiny mental image:** keep the bulky raw reels in the warehouse; the mill turns them into shelved results.

**Final answer:** A. Cloud Storage'''

E["test_11_q57"] = '''### Step 4: Choose the answer

- Interleaving the order-items table within the orders table co-locates the parent and child rows, making the one-to-many join fast in Spanner.
- It satisfies the goal: physical data locality that speeds parent-child joins, the Spanner-native fix.

### Exam shortcut

If you see:
- slow parent-child (one-to-many) joins in Cloud Spanner
- co-locate related rows for performance
- table interleaving

Think: **interleaved tables (parent-child locality)**

**Tiny mental image:** file each order's line items right behind the order, so the join doesn't hunt across the database.

**Final answer:** A. Use interleaved tables'''

E["test_12_q14"] = '''### Step 4: Choose the answer

- The UUID prefix still hot-spots because the chosen UUID variant produces sequentially ordered strings, so keys remain monotonic.
- It satisfies the diagnosis: a sequential UUID defeats the purpose; a truly random prefix spreads writes.

### Exam shortcut

If you see:
- Bigtable still hot-spotting despite a UUID prefix
- key ordering matters
- sequential vs random UUID

Think: **the UUID type is sequentially ordered (not random)**

**Tiny mental image:** your "random" tickets are actually numbered in order, so everyone still queues at one window.

**Final answer:** B. You have chosen a type of UUID that has sequentially ordered strings.'''

E["test_2_q13"] = '''### Step 4: Choose the answer

- Adding a second cluster to the Bigtable instance and using two app profiles isolates the heavy write traffic from the analytic batch jobs.
- It satisfies the goal: workload isolation so batch reads don't degrade write performance.

### Exam shortcut

If you see:
- Bigtable serving + batch/analytics contending
- isolate workloads for performance
- app profiles / multi-cluster routing

Think: **second Bigtable cluster + separate app profiles**

**Tiny mental image:** give the busy cashiers and the stocktaking crew their own copies of the store so they don't collide.

**Final answer:** A. Isolate the write and batch workloads by adding a second cluster to the Bigtable instance and create two app profiles, one for write traffic and one for batch jobs.'''

E["test_2_q19"] = '''### Step 4: Choose the answer

- Cloud Bigtable provides low-latency writes and scales to petabytes for high-volume telemetry, the priority being scalability with willingness to change the app.
- It satisfies the goal: massive, low-latency write throughput beyond what Cloud SQL/PostgreSQL can sustain.

### Exam shortcut

If you see:
- ingestion outgrowing a relational DB, need PB scale + low-latency writes
- scalability is the top priority, app changes acceptable
- high-volume time-series/telemetry

Think: **Cloud Bigtable**

**Tiny mental image:** swap the single ledger book for a warehouse of ledgers that scales to petabytes.

**Final answer:** C. Cloud Bigtable'''

E["test_2_q25"] = '''### Step 4: Choose the answer

- Performance suffers because 200 column families exceeds Bigtable's recommended limit of ~100 column families.
- It satisfies the diagnosis: too many column families degrades performance; the schema should consolidate them.

### Exam shortcut

If you see:
- Bigtable underperforming with many column families
- recall the ~100 column-family guideline
- schema-design limit

Think: **too many column families (>100 recommended max)**

**Tiny mental image:** the filing cabinet has hundreds of dividers when it's built for about a hundred - it jams.

**Final answer:** B. 200 column families exceeds the recommended 100 column family limit'''

append_entries(E)

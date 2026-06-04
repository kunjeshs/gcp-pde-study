from lib import append_entries

E = {}

E["test_7_q30"] = '''### Step 4: Choose the answer

- Pub/Sub decouples producer from consumer, and a Dataflow pipeline writing Avro to Cloud Storage (cheap, indefinite raw) and to BigQuery (near-real-time SQL over years) meets every requirement.
- It satisfies all: decoupled ingest, durable cheap archive, and SQL-queryable multi-year history.

### Exam shortcut

If you see:
- decouple producer/consumer + cheap indefinite raw storage + near-real-time SQL + multi-year history
- one pipeline covering archive and analytics
- streaming JSON at scale

Think: **Pub/Sub → Dataflow → Cloud Storage (raw) + BigQuery (SQL)**

**Tiny mental image:** one intake that files originals in cheap deep storage and shelves a live searchable copy.

**Final answer:** D. Create an application that publishes events to Cloud Pub/Sub, and create a Cloud Dataflow pipeline that transforms the JSON event payloads to Avro, writing the data to Cloud Storage and BigQuery.'''

E["test_7_q31"] = '''### Step 4: Choose the answer

- BigQuery charges for storage, queries, and streaming inserts; batch loading and exporting data are free.
- It satisfies the question: those three are the billable operations.

### Exam shortcut

If you see:
- "what does BigQuery charge for?"
- storage + queries + streaming inserts billable
- loading/exporting are free

Think: **storage, queries, streaming inserts**

**Tiny mental image:** you pay rent (storage), per search (queries), and for the express live drop (streaming) - bulk delivery is free.

**Final answer:** A. Storage, queries, and streaming inserts'''

E["test_7_q43"] = '''### Step 4: Choose the answer

- A session window with a 60-minute gap groups each user's activity and fires once they've been inactive for an hour, exactly the abandonment trigger.
- It satisfies the rule: the window closes after the inactivity gap, letting you check basket value and transaction status.

### Exam shortcut

If you see:
- act after a period of *user inactivity* / "no interaction for N minutes"
- per-user activity bursts separated by gaps
- abandonment / idle-timeout logic

Think: **session window (gap duration)**

**Tiny mental image:** the meter starts when the customer goes quiet and dings after an hour of silence.

**Final answer:** C. Use a session window with a gap time duration of 60 minutes.'''

E["test_7_q48"] = '''### Step 4: Choose the answer

- Rewriting the MapReduce job in Apache Spark uses in-memory processing to run far faster on the same cluster, improving responsiveness without added cost.
- It satisfies the constraint: more speed from a better engine, not more (costlier) hardware.

### Exam shortcut

If you see:
- batch MapReduce jobs falling behind, no budget increase
- speed up processing on existing resources
- engine choice, not cluster size

Think: **rewrite MapReduce → Spark (in-memory)**

**Tiny mental image:** swap the old steam engine for an electric motor on the same chassis - faster, no bigger fuel bill.

**Final answer:** B. Rewrite the job in Apache Spark.'''

E["test_7_q50"] = '''### Step 4: Choose the answer

- Cloud Composer (managed Airflow) orchestrates the interdependent steps in order, mixing shell, Hadoop, and BigQuery tasks with built-in retries.
- It satisfies the goal: dependency-aware, long-running, scheduled workflow orchestration with retry on failure.

### Exam shortcut

If you see:
- scheduled multi-step workflow with dependencies/ordering
- mixed task types (shell, Hadoop, BigQuery), retries
- orchestrate, not just schedule

Think: **Cloud Composer (Airflow DAG)**

**Tiny mental image:** a conductor cueing each section in order and signaling a retry when one stumbles.

**Final answer:** D. Cloud Composer'''

E["test_8_q11"] = '''### Step 4: Choose the answer

- Pub/Sub ingests the 10,000-device stream, Dataflow processes it in real time, and BigQuery stores it for analysis - a fully managed real-time stack.
- It satisfies the goal: scalable real-time process, store, and analyze for very large IoT datasets.

### Exam shortcut

If you see:
- large fleet of IoT devices, real-time process + store + analyze
- managed, scalable streaming
- land in a SQL warehouse

Think: **Pub/Sub → Dataflow → BigQuery**

**Tiny mental image:** a global intake belt feeding a live mill that stocks a searchable warehouse.

**Final answer:** B. Send the data to Google Cloud Pub/Sub, stream Cloud Pub/Sub to Google Cloud Dataflow, and store the data in Google BigQuery.'''

E["test_8_q13"] = '''### Step 4: Choose the answer

- Coalescing the small 200-400 MB parquet files to at least 1 GB reduces task/shuffle overhead and restores throughput cost-effectively on the preemptible cluster.
- It satisfies the goal: fewer, larger splits cut scheduling and I/O overhead without new hardware spend.

### Exam shortcut

If you see:
- Spark slow with many small input files
- shuffle-heavy, cost-sensitive, Dataproc + preemptibles
- file-size tuning

Think: **increase input file size (≈1 GB+)**

**Tiny mental image:** ship a few full pallets instead of thousands of tiny packages.

**Final answer:** A. Increase the size of your parquet files to ensure them to be 1 GB minimum.'''

E["test_8_q24"] = '''### Step 4: Choose the answer

- Batching the work into ten-second increments groups the high-rate calls to the GUID service, smoothing load and relieving backpressure.
- It satisfies the goal: fewer, bundled external calls under tens-of-thousands-per-second throughput.

### Exam shortcut

If you see:
- high-throughput pipeline calling an external service
- "reduce backpressure" / overwhelmed downstream
- micro-batching as the lever

Think: **batch into short time increments**

**Tiny mental image:** send one bus every ten seconds instead of a taxi per passenger.

**Final answer:** B. Batch the job into ten-second increments.'''

E["test_8_q30"] = '''### Step 4: Choose the answer

- Calling the Video Intelligence API for labels and storing results in Cloud Bigtable gives the fast, low-latency filtering needed across several TB.
- It satisfies both: ready-made video labeling plus a high-throughput store for quick preference filtering at scale.

### Exam shortcut

If you see:
- generate video/image labels without training a model
- very fast filtering/lookups over TBs
- recommendation/preference matching

Think: **Video Intelligence API (labels) + Bigtable (fast filtering)**

**Tiny mental image:** an off-the-shelf tagger feeding a lightning-fast lookup table.

**Final answer:** C. Build an application that calls the Cloud Video Intelligence API to generate labels. Store data in Cloud Bigtable, and filter the predicted labels to match the user‘s viewing history to generate preferences.'''

E["test_8_q33"] = '''### Step 4: Choose the answer

- Updating the pipeline with the drain flag finishes in-flight data before the incompatible new version takes over, so nothing is lost.
- It satisfies the goal: a clean handoff for an incompatible change without dropping buffered data.

### Exam shortcut

If you see:
- update a streaming Dataflow pipeline, change is incompatible
- no data loss
- drain to flush in-flight work

Think: **drain the pipeline on update**

**Tiny mental image:** empty the pipe of water before swapping in the new section.

**Final answer:** A. Update the current pipeline and use the drain flag.'''

E["test_8_q35"] = '''### Step 4: Choose the answer

- gsutil rsync runs outbound from the on-prem servers to Cloud Storage, so no external IP reaches into the data center, and it syncs daily deltas.
- It satisfies both: secure outbound-only transfer plus ongoing incremental sync after the initial upload.

### Exam shortcut

If you see:
- no inbound access to on-prem (no external IPs reaching in)
- initial upload + recurring daily deltas
- simple secure sync

Think: **gsutil rsync (outbound from on-prem)**

**Tiny mental image:** the building mails out its updates; nobody outside gets a key to come in.

**Final answer:** A. Execute gsutil rsync from the on-premises servers.'''

E["test_8_q37"] = '''### Step 4: Choose the answer

- A healthy pipeline drains the source and fills the sink; alert on an *increase* in undelivered Pub/Sub messages (backlog building) and a *decrease* in the destination's used_bytes growth (output stalling).
- It satisfies the goal: both signals flag the pipeline no longer processing data.

### Exam shortcut

If you see:
- monitor a Dataflow streaming pipeline is "still processing"
- watch source backlog and sink growth
- which direction signals trouble?

Think: **alert on rising source backlog + falling sink write rate**

**Tiny mental image:** worry when the inbox piles up *and* the outbox stops filling.

**Final answer:** B. An alert based on an increase of subscription/num_undelivered_messages for the source and a rate of change decrease of instance/storage/ used_bytes for the destination'''

E["test_8_q38"] = '''### Step 4: Choose the answer

- The Cloud Dataflow connector for Bigtable is what lets a Dataflow pipeline read from and write to Cloud Bigtable.
- It satisfies the question: that connector bridges Bigtable into Beam/Dataflow.

### Exam shortcut

If you see:
- use Bigtable inside a Dataflow pipeline
- the integration component name
- read/write Bigtable from Beam

Think: **Cloud Dataflow connector for Bigtable**

**Tiny mental image:** the adapter cable that plugs Bigtable into the Dataflow machine.

**Final answer:** A. Cloud Dataflow connector'''

E["test_8_q40"] = '''### Step 4: Choose the answer

- Partitioning the tables by a DATE/TIMESTAMP column lets date-filtered queries prune to the relevant partitions instead of scanning everything.
- It satisfies the goal: far less data scanned (lower cost) while keeping full SQL access.

### Exam shortcut

If you see:
- date-filtered BigQuery queries scanning the whole table
- rising bytes-scanned cost
- keep SQL, cut scan volume

Think: **partition by DATE/TIMESTAMP**

**Tiny mental image:** file records by month so you open only the months you asked for.

**Final answer:** A. Re-create the tables using DDL. Partition the tables by a column containing a TIMESTAMP or DATE Type.'''

E["test_9_q47"] = '''### Step 4: Choose the answer

- Dataprep (by Trifacta) lets non-developer analysts build and maintain visual transformation recipes that run on a schedule, adapting as the schema changes.
- It satisfies all three needs: scheduled execution, analyst-friendly editing, and a graphical design tool.

### Exam shortcut

If you see:
- scheduled CSV transformations with evolving schema
- non-developers modify them, graphical tool
- no-code data prep

Think: **Cloud Dataprep (Trifacta) recipes, scheduled**

**Tiny mental image:** a visual recipe the analysts tweak each month, run automatically on a timer.

**Final answer:** D. Use Dataprep by Trifacta to build and maintain the transformation recipes, and execute them on a scheduled basis'''

E["test_10_q26"] = '''### Step 4: Choose the answer

- A custom Apache Beam connector in a Dataflow pipeline reads the proprietary format and streams it into BigQuery as Avro, efficiently and with minimal resources.
- It satisfies both: handle the non-standard format and stream it compactly (Avro) into BigQuery.

### Exam shortcut

If you see:
- ingest a proprietary/unsupported format, stream into BigQuery
- minimal resource consumption
- custom parsing needed

Think: **custom Beam connector + Dataflow streaming (Avro into BigQuery)**

**Tiny mental image:** build a custom adapter so the odd-shaped feed plugs straight into the warehouse line.

**Final answer:** D. Use a custom connector with Apache Beam to write a Dataflow pipeline that streams the data into BigQuery in Avro format.'''

E["test_10_q27"] = '''### Step 4: Choose the answer

- Copying the ORC files onto the Dataproc cluster and mounting the Hive tables (or using the master-node→HDFS path) gets Hive running with local data for performance.
- It satisfies the goal: data replicated to the cluster so Hive reads from fast local storage.

### Exam shortcut

If you see:
- start Hive on Dataproc with ORC data in Cloud Storage
- replicate to local HDFS for performance
- two valid setup paths

Think: **stage files onto the cluster/HDFS (or use the Cloud Storage connector)**

**Tiny mental image:** bring the parts into the workshop so the machine runs at full speed.

**Final answer:** C. Transfer all ORC files from the Cloud Storage bucket to any node of the Dataproc cluster using the gsutil utility, and mount the Hive tables locally.'''

E["test_10_q57"] = '''### Step 4: Choose the answer

- Using Cloud Storage for persistent storage (and keeping preemptible VMs to a sensible fraction of workers) follows Google's Dataproc best practices.
- It satisfies the goal: durable data decoupled from ephemeral compute, with cost savings that don't jeopardize job completion.

### Exam shortcut

If you see:
- Dataproc best practices for a busy Spark cluster
- decouple storage from compute
- moderate preemptible usage

Think: **Cloud Storage for persistence (+ limited preemptible workers)**

**Tiny mental image:** keep the goods in the permanent warehouse and staff with mostly steady workers plus a few temps.

**Final answer:** A. Use Cloud Storage for persistent storage'''

E["test_11_q7"] = '''### Step 4: Choose the answer

- Cloud Bigtable stores 50 TB of frequently-updated, constantly-streaming financial time-series with low latency and exposes the HBase API for the migrated Hadoop jobs.
- It satisfies all: massive scale, high-throughput updates/streaming, and Hadoop compatibility.

### Exam shortcut

If you see:
- large, frequently-updated time-series with constant streaming
- low-latency writes/reads at TB scale
- migrate Hadoop/HBase jobs

Think: **Cloud Bigtable**

**Tiny mental image:** a high-speed ticker-tape ledger built for nonstop updates at huge scale.

**Final answer:** A. Cloud Bigtable'''

E["test_11_q10"] = '''### Step 4: Choose the answer

- Cloud Dataprep lets a newcomer visually run data quality checks and exploratory transformations on Cloud Storage data with no coding.
- It satisfies the goal: interactive profiling and cleansing for someone just learning the platform.

### Exam shortcut

If you see:
- data quality checks + exploratory analysis, beginner-friendly
- visual, no-code profiling of files
- data in Cloud Storage

Think: **Cloud Dataprep**

**Tiny mental image:** a point-and-click data inspector that needs no programming to explore the files.

**Final answer:** C. Cloud Dataprep'''

append_entries(E)

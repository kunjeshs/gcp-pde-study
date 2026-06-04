from lib import append_entries

E = {}

E["test_15_q20"] = '''### Step 4: Choose the answer

- Raising maxNumWorkers speeds the Dataflow writes, and adding Bigtable nodes lets the cluster serve more concurrent dashboard users.
- It satisfies both pressures: faster ingestion and higher read concurrency by scaling each tier.

### Exam shortcut

If you see:
- Dataflow → Bigtable writes too slow + many concurrent readers
- scale the writer and the store together
- two scaling actions

Think: **increase Dataflow maxNumWorkers + add Bigtable nodes**

**Tiny mental image:** hire more loaders at the dock and open more checkout lanes at the store.

**Final answer:** B. Increase the maximum number of Dataflow workers by setting maxNumWorkers in PipelineOptions'''

E["test_15_q39"] = '''### Step 4: Choose the answer

- Lifting the Spark/Hive/HDFS workloads to Dataproc with Cloud Storage (modernize later) meets the two-month deadline while capturing storage-decoupling savings.
- It satisfies both: fast migration on schedule plus immediate cost benefit from Cloud Storage over HDFS.

### Exam shortcut

If you see:
- hard migration deadline, maximize cost savings
- existing Hadoop/Spark/Hive
- lift-and-shift now, modernize later

Think: **Dataproc + Cloud Storage, modernize later**

**Tiny mental image:** move into the new building first and remodel after you've met the deadline.

**Final answer:** B. Migrate the workloads to Dataproc plus Cloud Storage; modernize later.'''

E["test_15_q42"] = '''### Step 4: Choose the answer

- Taking a Pub/Sub snapshot before deploying lets you Seek back and re-deliver messages if the new subscriber wrongly acknowledges and loses them.
- It satisfies the goal: a recovery point to replay from, guarding against ack bugs in the new code.

### Exam shortcut

If you see:
- protect against message loss from bad acks after a deploy
- need to replay/redeliver messages
- snapshot + Seek

Think: **Pub/Sub snapshot before deploy, Seek to replay on error**

**Tiny mental image:** save a checkpoint before the risky update so you can reload if it corrupts progress.

**Final answer:** B. Create a Pub/Sub snapshot before deploying new subscriber code. Use a Seek operation to re-deliver messages that became available after the snapshot was created.'''

E["test_15_q44"] = '''### Step 4: Choose the answer

- A sliding window of 30 seconds with a 5-second period, emitting on AfterWatermark, computes the trailing-30s average refreshed every 5 seconds.
- It satisfies the spec exactly: window size = data range (30s), period = update cadence (5s).

### Exam shortcut

If you see:
- moving average over the last N seconds, updated every M seconds
- map "size = N, period = M" to a sliding window
- emit on watermark

Think: **sliding window (duration = data span, period = refresh interval)**

**Tiny mental image:** a 30-second magnifier sliding forward 5 seconds at a time.

**Final answer:** D. Use a sliding window with a duration of 30 seconds and a period of 5 seconds. Emit results by setting the following trigger: AfterWatermark.pastEndOfWindow ()'''

E["test_15_q45"] = '''### Step 4: Choose the answer

- A streaming Dataflow job reading continuously from Pub/Sub with tumbling (fixed hourly) windows scales to high volume and produces the hourly aggregates.
- It satisfies both: elastic streaming ingestion and clean, non-overlapping hourly rollups.

### Exam shortcut

If you see:
- continuously load Pub/Sub events into BigQuery at scale
- aggregate over fixed, non-overlapping hourly buckets
- streaming, not batch polling

Think: **streaming Dataflow + tumbling (fixed) hourly windows**

**Tiny mental image:** an hourglass that empties and resets each hour, tallying that hour's grains.

**Final answer:** D. Create a streaming Dataflow job that reads continually from the Pub/Sub topic and performs the necessary aggregations using tumbling windows.'''

E["test_15_q48"] = '''### Step 4: Choose the answer

- Exporting pipeline metrics/logs to Cloud Monitoring and configuring an Alerting policy gives managed, cross-project health checks and failure notifications.
- It satisfies the goal: native monitoring and alerting across BigQuery, Dataflow, and Dataproc without custom apps.

### Exam shortcut

If you see:
- monitor pipelines across multiple projects, get failure alerts
- prefer managed/platform features
- health checks + notifications

Think: **Cloud Monitoring + Alerting policy**

**Tiny mental image:** one dashboard with built-in alarms watching all the projects, no custom watcher app.

**Final answer:** A. Export the information to Cloud Monitoring, and set up an Alerting policy'''

E["test_15_q49"] = '''### Step 4: Choose the answer

- Ingesting the Cloud Storage data into BigQuery and rewriting the PySpark logic as BigQuery SQL gives a serverless, SQL-native pipeline that runs far faster than the 12-hour job.
- It satisfies all: serverless, SQL syntax, and dramatically reduced run time.

### Exam shortcut

If you see:
- slow Spark/PySpark batch on structured data
- want serverless + SQL to speed development and runtime
- data already in Cloud Storage

Think: **load into BigQuery and transform with BigQuery SQL**

**Tiny mental image:** retire the hand-cranked mill and let the warehouse's SQL engine do the milling.

**Final answer:** C. Ingest your data into BigQuery from Cloud Storage, convert your PySpark commands into BigQuery SQL queries to transform the data, and then write the transformations to a new table.'''

E["test_15_q50"] = '''### Step 4: Choose the answer

- Replacing the SideInput join with CoGroupByKey performs the join as a scalable shuffle, removing the SideInput bottleneck and speeding the job.
- It satisfies the goal: a more efficient join pattern for large datasets than broadcasting a side input.

### Exam shortcut

If you see:
- Dataflow join via SideInput is slow / large side data
- need a scalable join
- CoGroupByKey vs SideInput

Think: **use CoGroupByKey instead of a large SideInput**

**Tiny mental image:** sort both decks and merge them, instead of handing every worker a full copy of one.

**Final answer:** D. Use CoGroupByKey instead of the SideInput.'''

E["test_15_q54"] = '''### Step 4: Choose the answer

- gsutil handles the one-off migration of the few large 90 GB files, while Pub/Sub plus Dataflow streams real-time updates from the transactional systems.
- It satisfies both halves: simple bulk move now, plus a managed streaming pipeline for continuous updates.

### Exam shortcut

If you see:
- bulk migrate a handful of very large files + ongoing real-time updates
- streaming ingestion/transformation
- Pub/Sub feeding the warehouse

Think: **gsutil (migration) + Pub/Sub → Dataflow (real-time)**

**Tiny mental image:** truck over the big crates once, then run a live conveyor for the daily flow.

**Final answer:** C. gsutil for the migration; Pub/Sub and Dataflow for the real-time updates'''

E["test_16_q25"] = '''### Step 4: Choose the answer

- A changed windowing/triggering strategy is incompatible with an in-place --update, so Drain the running pipeline (finishing in-flight data) and start a new job.
- It satisfies "no data loss": Drain flushes outstanding data before the incompatible pipeline is replaced.

### Exam shortcut

If you see:
- update a streaming pipeline whose windowing/triggering changed
- incompatible change (can't hot-update in place)
- no data loss

Think: **Drain the old job, deploy a new one** (vs --update for compatible changes)

**Tiny mental image:** when the new machine takes different-shaped parts, empty the old line fully before swapping.

**Final answer:** D. Stop the Cloud Dataflow pipeline with the Drain option. Create a new Cloud Dataflow job with the updated code'''

E["test_16_q30"] = '''### Step 4: Choose the answer

- Dataprep (by Trifacta) lets non-developer analysts build and maintain visual transformation recipes that run on a schedule, adapting as the schema changes.
- It satisfies all three needs: scheduled execution, analyst-friendly editing, and a graphical design tool.

### Exam shortcut

If you see:
- scheduled CSV transformations with evolving schema
- non-developers modify them, graphical tool
- no-code data prep

Think: **Cloud Dataprep (Trifacta) recipes, scheduled**

**Tiny mental image:** a visual recipe the analysts tweak each month, run automatically on a timer.

**Final answer:** A. Use Dataprep by Trifacta to build and maintain the transformation recipes, and execute them on a scheduled basis'''

E["test_16_q31"] = '''### Step 4: Choose the answer

- Copying the ORC files to the master node and using the Hadoop utility to load them into HDFS (or using the Cloud Storage connector for external tables) gets Hive running on Dataproc.
- It satisfies the goal: data replicated to local HDFS for performance, with Hive tables mounted from HDFS.

### Exam shortcut

If you see:
- start Hive on Dataproc with ORC data in Cloud Storage
- replicate to local HDFS for performance
- two valid setup paths

Think: **stage to master node → hadoop fs into HDFS (or use the Cloud Storage connector)**

**Tiny mental image:** bring the parts into the workshop's own bench so the machine runs at full speed.

**Final answer:** C. Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster. Then run the Hadoop utility to copy them do HDFS. Mount the Hive tables from HDFS.'''

E["test_16_q34"] = '''### Step 4: Choose the answer

- Putting the disk-I/O-heavy job's intermediate data on native HDFS (persistent disk) avoids round-tripping transient data through the Cloud Storage connector.
- It satisfies the fix: keep durable input/output in Cloud Storage but local-disk the I/O-intensive intermediates.

### Exam shortcut

If you see:
- disk-I/O-bound Dataproc job using the Cloud Storage connector
- intermediate/shuffle data is the bottleneck
- speed up without re-architecting

Think: **intermediate data on HDFS (persistent disk), not Cloud Storage**

**Tiny mental image:** do the scratch work on the local desk, not by mailing every draft to the warehouse.

**Final answer:** B. Allocate sufficient persistent disk space to the Hadoop cluster, and store the intermediate data of that particular Hadoop job on native HDFS'''

E["test_16_q37"] = '''### Step 4: Choose the answer

- A Dataflow job with KafkaIO and a sliding 1-hour window advancing every 5 minutes computes the moving average and alerts when it drops below 4000/sec.
- It satisfies the goal: a continuously updated trailing-hour average a fixed window can't provide.

### Exam shortcut

If you see:
- alert on a moving/rolling average over a trailing hour
- frequently re-evaluated
- stream from Kafka into Dataflow

Think: **sliding window (size 1h, hop 5m)**

**Tiny mental image:** a gliding spotlight on the last hour, re-checked every five minutes.

**Final answer:** A. Consume the stream of data in Dataflow using Kafka IO. Set a sliding time window of 1 hour every 5 minutes. Compute the average when the window closes, and send an alert if the average is less than 4000 messages.'''

E["test_16_q39"] = '''### Step 4: Choose the answer

- Apache Kafka provides per-key ordering, offset seeking, and publish/subscribe across many topics - the distinctive offset/replay capability here.
- It satisfies all the requirements, including seeking to a specific offset that Pub/Sub-style services don't expose directly.

### Exam shortcut

If you see:
- per-key ordering + seek to a specific offset
- pub/sub over many topics, centralized ingestion
- consumer-controlled replay by offset

Think: **Apache Kafka**

**Tiny mental image:** a tape deck you can rewind to an exact counter mark on hundreds of channels.

**Final answer:** A. Apache Kafka'''

E["test_16_q40"] = '''### Step 4: Choose the answer

- A Dataproc cluster with standard persistent disks, 50% preemptible workers, and data in Cloud Storage (gs:// not hdfs://) is the cost-effective, fault-tolerant managed Hadoop migration.
- It satisfies both: preemptibles plus standard disks cut cost, and Cloud Storage decouples durable data from ephemeral compute.

### Exam shortcut

If you see:
- migrate Hadoop to managed, cost-effective + fault-tolerant
- preemptible workers, standard (not SSD) disks
- data in Cloud Storage, swap hdfs:// → gs://

Think: **Dataproc + preemptibles + standard PD + Cloud Storage**

**Tiny mental image:** rent cheap temp workers and keep the goods in a permanent warehouse.

**Final answer:** A. Deploy a Dataproc cluster. Use a standard persistent disk and 50% preemptible workers. Store data in Cloud Storage, and change references in scripts from hdfs:// to gs://'''

E["test_16_q48"] = '''### Step 4: Choose the answer

- Cloud Pub/Sub guarantees at-least-once delivery, so consumers must handle possible duplicates.
- It satisfies the question: the default semantic is at-least-once (not at-most-once or best-effort).

### Exam shortcut

If you see:
- "what delivery guarantee does Pub/Sub provide?"
- duplicates possible, must be idempotent
- at-least-once by default

Think: **at-least-once delivery**

**Tiny mental image:** the courier guarantees it arrives - occasionally twice - so you handle the duplicate.

**Final answer:** B. Deliver at least once'''

E["test_2_q12"] = '''### Step 4: Choose the answer

- Airflow DAGs written in Python and run on Cloud Composer give a managed service for jobs with complex dependencies.
- It satisfies the goal: dependency-aware orchestration, managed, with DAGs authored in Python (Airflow's language).

### Exam shortcut

If you see:
- jobs with complex interdependencies, managed service
- workflow orchestration
- Airflow DAGs (authored in Python)

Think: **Cloud Composer (Airflow DAGs in Python)**

**Tiny mental image:** a managed conductor running a Python-scored dependency graph.

**Final answer:** A. Write Airflow directed acyclic graphs in Python and execute them with Cloud Composer.'''

E["test_3_q6"] = '''### Step 4: Choose the answer

- Cloud Composer in a Shared VPC, with its resources placed in the service project, is the Google-managed Airflow option that fits the Shared VPC networking model.
- It satisfies both: managed open-source orchestration and correct Shared VPC placement (service project consuming the host network).

### Exam shortcut

If you see:
- managed open-source (Airflow) workflow scheduling
- Shared VPC networking considerations
- where do Composer resources live?

Think: **Cloud Composer in Shared VPC, resources in the service project**

**Tiny mental image:** the tenant (service project) runs its scheduler while borrowing the landlord's (host) network.

**Final answer:** D. Use Cloud Composer in a Shared VPC configuration and place the Cloud Composer resources in the service project'''

E["test_3_q10"] = '''### Step 4: Choose the answer

- A Pub/Sub push subscription triggering a Cloud Function that calls the Python API is a serverless, secure queue that scales with trade volume and uses minimal idle resources.
- It satisfies the goal: event-driven processing with no always-on servers to manage.

### Exam shortcut

If you see:
- secure queue triggering code via an API, minimize resource usage
- serverless, event-driven, high volume
- Pub/Sub + Cloud Function

Think: **Pub/Sub push → Cloud Function → API**

**Tiny mental image:** each trade rings a doorbell that wakes a function only when needed, then it sleeps.

**Final answer:** A. Implement a Pub/Sub push subscription to trigger a Cloud Function that passes data to the Python API'''

append_entries(E)

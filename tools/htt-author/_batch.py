from lib import append_entries

E = {}

E["test_2_q35"] = '''### Step 4: Choose the answer

- Publishing sensor data to a Pub/Sub topic buffers bursts so the ingestion app can read at its own pace, eliminating the loss a REST endpoint suffers.
- It satisfies the goal: a scalable, durable intake that absorbs spikes instead of dropping data.

### Exam shortcut

If you see:
- an endpoint can't keep up with bursty ingest, data is lost
- need a buffer/shock absorber between producer and consumer
- high-rate streaming intake

Think: **Pub/Sub topic as the ingestion buffer**

**Tiny mental image:** a reservoir that catches the flood so the treatment plant sips steadily downstream.

**Final answer:** A. Write data to a Cloud Pub/Sub topic instead of a REST API endpoint and have the ingestion application read from the topic.'''

E["test_2_q45"] = '''### Step 4: Choose the answer

- The number of master nodes (single vs high-availability) is fixed at cluster creation and cannot be changed afterward.
- It satisfies the question: to get multiple masters you must create a new HA cluster, not modify the existing one.

### Exam shortcut

If you see:
- change Dataproc master-node count on a running cluster
- single vs HA mode after creation
- "can this be modified later?"

Think: **master count is set at creation - it can't be changed**

**Tiny mental image:** the building's number of control towers is poured into the foundation - you can't add one later.

**Final answer:** D. The number of master nodes cannot be changed once a cluster is created.'''

E["test_2_q46"] = '''### Step 4: Choose the answer

- A Pub/Sub message is retained until every subscription has at least one subscriber acknowledge it; an un-acked subscription keeps it (and backlog) alive.
- It satisfies the diagnosis: accumulation means some subscription isn't acknowledging, since deletion requires an ack per subscription.

### Exam shortcut

If you see:
- Pub/Sub messages/backlog piling up
- "when is a message deleted?"
- ack semantics per subscription

Think: **deleted once acknowledged on each subscription** (not per topic/bucket)

**Tiny mental image:** the parcel stays in the locker until every recipient's mailbox signs for its own copy.

**Final answer:** D. Once at least one subscriber for each subscription has acknowledged the message it will be deleted from storage.'''

E["test_2_q47"] = '''### Step 4: Choose the answer

- Pub/Sub replaces Kafka for ingestion and Dataflow replaces Flink for stream processing - the managed equivalents.
- It satisfies the migration: a serverless ingest-plus-processing stack with no clusters to run.

### Exam shortcut

If you see:
- migrate Kafka + Flink (or Spark Streaming) to managed GCP
- ingest stream + process stream
- serverless equivalents

Think: **Pub/Sub (ingest) + Dataflow (process)**

**Tiny mental image:** swap the self-run conveyor and mill for the managed pair that runs itself.

**Final answer:** A. Cloud Pub/Sub'''

E["test_3_q3"] = '''### Step 4: Choose the answer

- Apache Kafka provides per-key ordering, offset seeking, and publish/subscribe across hundreds of topics - the distinctive offset/replay capability here.
- It satisfies all the requirements, including the ability to seek to a specific offset that Pub/Sub-style services don't expose directly.

### Exam shortcut

If you see:
- per-key ordering + seek to a specific offset
- pub/sub over many topics, centralized ingestion
- consumer-controlled replay by offset

Think: **Apache Kafka**

**Tiny mental image:** a tape deck you can rewind to an exact counter mark on hundreds of channels.

**Final answer:** A. Apache Kafka'''

E["test_3_q18"] = '''### Step 4: Choose the answer

- A Dataproc cluster with standard persistent disks, 50% preemptible workers, and data in Cloud Storage (gs:// instead of hdfs://) is the most cost-effective, fault-tolerant managed Hadoop migration.
- It satisfies both: preemptibles plus standard disks cut cost, while Cloud Storage decouples durable data from ephemeral compute.

### Exam shortcut

If you see:
- migrate Hadoop to managed, cost-effective + fault-tolerant
- preemptible workers, standard (not SSD) disks
- data in Cloud Storage, swap hdfs:// → gs://

Think: **Dataproc + preemptibles + standard PD + Cloud Storage**

**Tiny mental image:** rent cheap temp workers and keep the goods in a permanent warehouse, not on their backs.

**Final answer:** A. Deploy a Dataproc cluster. Use a standard persistent disk and 50% preemptible workers. Store data in Cloud Storage, and change references in scripts from hdfs:// to gs://'''

E["test_3_q22"] = '''### Step 4: Choose the answer

- Updating with the --update option and reusing the existing job name performs an in-place update that drains in-flight data, so nothing is lost.
- It satisfies the goal: a seamless version swap that preserves state, unlike cancel (drops data) or a brand-new job name.

### Exam shortcut

If you see:
- deploy a new version of a running Dataflow pipeline
- no data loss, preserve in-flight state
- --update semantics

Think: **--update with the same job name (in-place update)**

**Tiny mental image:** swap the engine while the train keeps rolling, not derail it and start a new one.

**Final answer:** A. Update the pipeline using the --update option and set the --jobName to the existing job name.'''

E["test_3_q27"] = '''### Step 4: Choose the answer

- Routing vendor data through Pub/Sub and a Dataflow job that sanitizes invalid values before streaming into BigQuery keeps the ML training/serving data clean.
- It satisfies both: scalable near-real-time ingestion plus validation/cleansing of dirty vendor input.

### Exam shortcut

If you see:
- near-real-time ingest from multiple sources with invalid values
- must clean/validate before it lands in BigQuery
- feed BigQuery ML / a serving endpoint

Think: **Pub/Sub → Dataflow (sanitize) → BigQuery**

**Tiny mental image:** run the incoming produce through a wash-and-sort line before it hits the shelves.

**Final answer:** D. Send vendor data to a Pub/Sub topic and use Dataflow to process and sanitize the data before streaming it to BigQuery.'''

E["test_3_q29"] = '''### Step 4: Choose the answer

- Replacing the SideInput join with CoGroupByKey performs the join as a scalable shuffle, removing the SideInput bottleneck and speeding the pipeline.
- It satisfies the goal: a more efficient join pattern for large datasets than broadcasting a side input.

### Exam shortcut

If you see:
- Dataflow join via SideInput is slow / large side data
- need a scalable join
- CoGroupByKey vs SideInput

Think: **use CoGroupByKey instead of a large SideInput**

**Tiny mental image:** sort both decks of cards and merge them, instead of handing every worker a full copy of one deck.

**Final answer:** D. Replace the SideInput with CoGroupByKey to improve performance.'''

E["test_3_q30"] = '''### Step 4: Choose the answer

- Ingesting the Cloud Storage data into BigQuery and rewriting the PySpark logic as BigQuery SQL gives a serverless, SQL-native pipeline that runs far faster.
- It satisfies all: serverless, SQL syntax, and dramatically reduced run time versus the 12-hour PySpark job.

### Exam shortcut

If you see:
- slow Spark/PySpark batch on structured data
- want serverless + SQL to speed development and runtime
- data already in Cloud Storage

Think: **load into BigQuery and transform with BigQuery SQL**

**Tiny mental image:** retire the hand-cranked mill and let the warehouse's built-in SQL engine do the milling.

**Final answer:** C. Ingest your data into BigQuery from Cloud Storage, convert your PySpark commands into BigQuery SQL queries to transform the data, and then write the transformations to a new table'''

E["test_3_q31"] = '''### Step 4: Choose the answer

- A Dataflow job using KafkaIO with a sliding 1-hour window advancing every 5 minutes computes the moving average and alerts when it drops below 4000/sec.
- It satisfies the goal: a continuously updated trailing-hour average, which a fixed window can't provide.

### Exam shortcut

If you see:
- alert on a *moving/rolling* average over a trailing period
- frequently re-evaluated (every few minutes)
- stream from Kafka into Dataflow

Think: **sliding window (size = period, hop = update interval)**

**Tiny mental image:** a gliding spotlight on the last hour that re-checks the brightness every five minutes.

**Final answer:** A. Consume the stream of data in Dataflow using Kafka IO, set a sliding time window of 1 hour every 5 minutes, compute the average when the window closes, and send an alert if the average is less than 4000 messages per second'''

E["test_3_q34"] = '''### Step 4: Choose the answer

- Moving the intermediate/shuffle data onto native HDFS (persistent disk) avoids the latency of round-tripping temp data through the Cloud Storage connector.
- It satisfies the fix: keep durable input/output in Cloud Storage but put transient I/O-heavy intermediates on local HDFS.

### Exam shortcut

If you see:
- disk-I/O-bound Dataproc job using the Cloud Storage connector
- intermediate/shuffle data thrashing
- speed up without re-architecting

Think: **store intermediate data on HDFS (persistent disk), not Cloud Storage**

**Tiny mental image:** do the scratch work on the local desk, not by mailing every draft to the warehouse.

**Final answer:** B. Allocate enough persistent disk space to the Hadoop cluster and store the intermediate data of the slow Hadoop job on native Hadoop Distributed File System (HDFS)'''

E["test_3_q36"] = '''### Step 4: Choose the answer

- Cloud Composer (managed Airflow) orchestrates the interdependent steps in order, mixing shell, Hadoop, and BigQuery tasks with built-in retries.
- It satisfies the goal: dependency-aware, long-running workflow orchestration with configurable retry on failure.

### Exam shortcut

If you see:
- multi-step workflow with dependencies/ordering
- mixed task types (shell, Hadoop, BigQuery), retries on failure
- orchestrate, not just schedule

Think: **Cloud Composer (Airflow DAG)**

**Tiny mental image:** a conductor cueing each section in order and signaling a retry when one stumbles.

**Final answer:** D. Use Cloud Composer to orchestrate and manage the execution of the batch jobs'''

E["test_3_q37"] = '''### Step 4: Choose the answer

- Copying the ORC files to the master node and using the Hadoop utility to load them into HDFS (or using the Cloud Storage connector for external tables) gets Hive running on Dataproc.
- It satisfies the goal: data replicated to local HDFS for performance, with Hive tables mounted from HDFS.

### Exam shortcut

If you see:
- start Hive on Dataproc with ORC data in Cloud Storage
- replicate to local HDFS for performance
- two valid setup paths

Think: **stage to master node → hadoop fs into HDFS (or use the Cloud Storage connector)**

**Tiny mental image:** bring the parts into the workshop's own bench so the machine runs at full speed.

**Final answer:** C. Transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster using the gsutil utility, run the Hadoop utility to copy them to HDFS, and mount the Hive tables from HDFS.'''

E["test_3_q41"] = '''### Step 4: Choose the answer

- Raising maxNumWorkers speeds the Dataflow writes, and adding Bigtable nodes lets the cluster serve more concurrent dashboard users.
- It satisfies both pressures: faster ingestion and higher read concurrency by scaling each tier.

### Exam shortcut

If you see:
- Dataflow → Bigtable writes too slow + many concurrent readers
- scale the writer and the store together
- two scaling actions

Think: **increase Dataflow maxNumWorkers + add Bigtable nodes**

**Tiny mental image:** hire more loaders at the dock and open more checkout lanes at the store.

**Final answer:** B. Increase the maximum number of workers by setting maxNumWorkers in PipelineOptions'''

E["test_3_q44"] = '''### Step 4: Choose the answer

- Raising the maximum worker count (and/or using a larger worker instance type) adds the CPU headroom the maxed-out n1-standard-1 workers lack.
- It satisfies the goal: more parallelism/compute to clear the peak-period backlog.

### Exam shortcut

If you see:
- Dataflow workers pinned at max CPU during peaks
- need more throughput
- scale out (more workers) or up (bigger workers)

Think: **increase max workers (and/or larger worker machine type)**

**Tiny mental image:** add more lanes - or wider trucks - when the highway jams at rush hour.

**Final answer:** A. Increase the maximum number of workers in your pipeline'''

E["test_3_q46"] = '''### Step 4: Choose the answer

- A streaming Dataflow job reading continuously from Pub/Sub with tumbling (fixed hourly) windows scales to large volumes and produces the hourly aggregates.
- It satisfies both: elastic streaming ingestion and clean, non-overlapping hourly rollups.

### Exam shortcut

If you see:
- continuously load Pub/Sub events into BigQuery at scale
- aggregate over fixed, non-overlapping hourly buckets
- streaming, not batch polling

Think: **streaming Dataflow + tumbling (fixed) hourly windows**

**Tiny mental image:** an hourglass that empties and resets each hour, tallying that hour's grains.

**Final answer:** D. Use a streaming Dataflow job that reads continuously from the Pub/Sub topic and performs the necessary aggregations using tumbling windows.'''

E["test_3_q47"] = '''### Step 4: Choose the answer

- A sliding window of 30 seconds with a 5-second period, emitting on AfterWatermark, computes the trailing-30s average refreshed every 5 seconds.
- It satisfies the spec exactly: window size = data range (30s), period = update cadence (5s).

### Exam shortcut

If you see:
- moving average over the last N seconds, updated every M seconds
- map "size = N, period = M" to a sliding window
- emit on watermark

Think: **sliding window (duration = data span, period = refresh interval)**

**Tiny mental image:** a 30-second magnifying glass that slides forward 5 seconds at a time.

**Final answer:** D. Use a sliding window with a duration of 30 seconds and a period of 5 seconds and emit results using a trigger of AfterWatermark.pastEndOfWindow().'''

E["test_3_q48"] = '''### Step 4: Choose the answer

- Pub/Sub decouples producer from consumer, and a Dataflow pipeline writing Avro to Cloud Storage (cheap, indefinite raw storage) and to BigQuery (near-real-time SQL over 2+ years) meets every requirement.
- It satisfies all: decoupled ingest, durable cheap raw archive, and SQL-queryable warehouse for history.

### Exam shortcut

If you see:
- decouple producer/consumer + cheap indefinite raw storage + near-real-time SQL + multi-year history
- one pipeline covering archive and analytics
- streaming JSON at scale

Think: **Pub/Sub → Dataflow → Cloud Storage (raw) + BigQuery (SQL)**

**Tiny mental image:** one intake that both files the originals in cheap deep storage and shelves a live, searchable copy.

**Final answer:** D. Create an application that publishes events to Cloud Pub/Sub, and set up a Cloud Dataflow pipeline that transforms the JSON event payloads to Avro, writing the data to Cloud Storage and BigQuery'''

E["test_3_q50"] = '''### Step 4: Choose the answer

- Taking a Pub/Sub snapshot before deploying lets you Seek back and re-deliver messages if the new subscriber wrongly acknowledges and loses them.
- It satisfies the goal: a recovery point to replay from, guarding against ack bugs in the new code.

### Exam shortcut

If you see:
- protect against message loss from bad acks after a deploy
- need to replay/redeliver messages
- Pub/Sub snapshot + Seek

Think: **Pub/Sub snapshot before deploy, Seek to replay on error**

**Tiny mental image:** save a checkpoint before the risky update so you can reload if it corrupts your progress.

**Final answer:** B. Create a Pub/Sub snapshot before deploying new subscriber code, and use a Seek operation to re-deliver messages that became available after the snapshot was created if errors occur'''

append_entries(E)

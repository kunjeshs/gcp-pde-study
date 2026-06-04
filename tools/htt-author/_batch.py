from lib import append_entries

E = {}

E["test_5_q12"] = '''### Step 4: Choose the answer

- Having the sensor devices publish straight to Cloud Pub/Sub replaces the unreliable leased lines with a global, durable, managed ingestion service.
- It satisfies the goal: reliable event delivery, cost-effectively, with no self-run buffering.

### Exam shortcut

If you see:
- unreliable links between collection and processing, lost events
- want reliable global delivery, cost-effective
- avoid self-managed Kafka or pricey Interconnect

Think: **publish directly to Cloud Pub/Sub**

**Tiny mental image:** use the global postal system instead of a flaky private courier line.

**Final answer:** B. Have the data acquisition devices publish data to Cloud Pub/Sub.'''

E["test_5_q16"] = '''### Step 4: Choose the answer

- Using .fromQuery to read only the specific fields needed prunes columns at the source, cutting the data BigQueryIO pulls into the pipeline.
- It satisfies the goal: read less data for faster, cheaper pipeline input than scanning the whole table.

### Exam shortcut

If you see:
- speed up a BigQueryIO read in Dataflow
- only some columns/fields are needed
- avoid reading the whole table

Think: **BigQueryIO .fromQuery (select just the needed fields)**

**Tiny mental image:** ask for just the two columns you need, not a photocopy of the whole ledger.

**Final answer:** B. Use .fromQuery operation to read specific fields from the table.'''

E["test_5_q17"] = '''### Step 4: Choose the answer

- Pub/Sub ingests the real-time parcel events, Dataflow processes them, and Cloud Storage durably stores the data - a scalable managed real-time stack.
- It satisfies Flowlogistic's need: parcel-level real-time tracking with durable, queryable storage (not ephemeral Local SSD or a single SQL box).

### Exam shortcut

If you see:
- real-time event ingest + processing + durable storage
- scalable managed components
- reject Local SSD / single Cloud SQL for durable scale

Think: **Pub/Sub + Dataflow + Cloud Storage**

**Tiny mental image:** a global intake belt, a processing mill, and a permanent warehouse working together.

**Final answer:** A. Cloud Pub/Sub, Cloud Dataflow, and Cloud Storage'''

E["test_5_q27"] = '''### Step 4: Choose the answer

- Triggers decide when a window's accumulated results are emitted, based on watermark, processing time, or data-driven conditions.
- It satisfies the question: triggers control output timing of window contents.

### Exam shortcut

If you see:
- "when is a window's result emitted?"
- early/late firings, watermark/processing-time conditions
- Beam concept for output timing

Think: **Triggers**

**Tiny mental image:** the kitchen bell that decides exactly when the dish leaves the pass.

**Final answer:** D. Triggers'''

E["test_5_q32"] = '''### Step 4: Choose the answer

- The false statement is that pipelines can share data between instances; a Dataflow pipeline is a self-contained job, not a shared-data channel.
- It satisfies the "not true" framing: pipelines are operations forming a directed graph for one job, but they don't share data across instances.

### Exam shortcut

If you see:
- "which is NOT true about Dataflow pipelines"
- a claim about cross-instance data sharing
- pipeline = a DAG of operations for one job

Think: **pipelines don't share data between instances - that's the false one**

**Tiny mental image:** spot the line that says two separate machines secretly pass notes - they don't.

**Final answer:** D. Pipelines can share data between instances'''

E["test_5_q33"] = '''### Step 4: Choose the answer

- Dataproc runs Hadoop-ecosystem job types including Hive, Pig, and Spark; YARN is the resource manager, not a submittable job type.
- It satisfies the question: Hive/Pig/Spark are the supported jobs.

### Exam shortcut

If you see:
- "which job types does Dataproc support?"
- Hive, Pig, Spark, (Hadoop/MapReduce, PySpark, SparkSQL)
- YARN is the scheduler, not a job

Think: **Hive / Pig / Spark** (YARN ≠ a job type)

**Tiny mental image:** Hive, Pig, and Spark are the performers; YARN is the stage manager.

**Final answer:** A. Hive'''

E["test_5_q36"] = '''### Step 4: Choose the answer

- Drain stops a streaming pipeline gracefully, finishing in-flight data and writing it to output before shutting down.
- It satisfies the goal: no in-flight data is dropped, unlike Cancel which stops immediately.

### Exam shortcut

If you see:
- stop a streaming Dataflow job without losing in-flight data
- finish processing what's already in the pipeline
- Drain vs Cancel

Think: **Drain (graceful) vs Cancel (immediate)**

**Tiny mental image:** let the water already in the pipe flow out before closing the valve.

**Final answer:** B. Drain'''

E["test_5_q37"] = '''### Step 4: Choose the answer

- A Cloud Dataflow streaming pipeline inserts the per-minute sensor readings into BigQuery within seconds and scales as volume grows.
- It satisfies both: sub-minute availability for real-time aggregation and elastic scaling beyond periodic batch loads.

### Exam shortcut

If you see:
- many sensors, data available within ~1 minute
- real-time aggregation, expecting growth
- continuous insert into BigQuery

Think: **streaming Dataflow → BigQuery**

**Tiny mental image:** a live conveyor feeding the warehouse, not hourly truck drops.

**Final answer:** B. Use a Cloud Dataflow pipeline to stream data into the BigQuery table.'''

E["test_5_q38"] = '''### Step 4: Choose the answer

- Preemptible VMs slash the cost of the periodic 30-minute Dataproc batch job, which can tolerate occasional worker preemption.
- It satisfies the goal: major cost savings on a short, fault-tolerant, scheduled workload.

### Exam shortcut

If you see:
- cost-optimize a short/scheduled Dataproc batch job
- workload tolerates interruptions
- weekly/periodic, fault-tolerant

Think: **preemptible (spot) workers**

**Tiny mental image:** hire cheap temp workers for the short weekly shift; if a few leave early, the job still finishes.

**Final answer:** B. Use pre-emptible virtual machines (VMs) for the cluster'''

E["test_5_q44"] = '''### Step 4: Choose the answer

- Streaming buffer data isn't immediately consistent, so estimating the availability latency and waiting roughly twice as long before aggregating avoids missing in-flight rows.
- It satisfies the goal: reports include recently-streamed data without re-architecting ingestion.

### Exam shortcut

If you see:
- aggregations right after BigQuery streaming inserts miss recent rows
- streaming buffer / eventual availability
- adjust timing, not the ingestion method

Think: **wait out the streaming-availability latency before querying**

**Tiny mental image:** let the ink dry before you photocopy the page, or you'll miss the last lines.

**Final answer:** D. Estimate the average latency for data availability after streaming inserts, and always run queries after waiting twice as long.'''

E["test_5_q45"] = '''### Step 4: Choose the answer

- Duplicate deliveries to a push endpoint mean it isn't acknowledging messages within the ack deadline, so Pub/Sub redelivers them.
- It satisfies the diagnosis: missed/slow acks trigger Pub/Sub's at-least-once redelivery.

### Exam shortcut

If you see:
- Pub/Sub push endpoint flooded with duplicates
- consumer slow/failing to ack in time
- at-least-once redelivery behavior

Think: **endpoint not acking within the acknowledgement deadline**

**Tiny mental image:** the courier keeps re-dropping the parcel because no one signs for it in time.

**Final answer:** D. Your custom endpoint is not acknowledging messages within the acknowledgement deadline.'''

E["test_6_q2"] = '''### Step 4: Choose the answer

- Mirroring the on-prem Kafka topics to a Kafka cluster on GCE (no Connect plugins), then reading with Dataproc/Dataflow to GCS, replicates the logs as required.
- It satisfies the constraint: native Kafka mirroring avoids deploying Kafka Connect plugins.

### Exam shortcut

If you see:
- replicate on-prem Kafka to GCP via mirroring
- no Kafka Connect plugins
- land in Cloud Storage / BigQuery

Think: **mirror topics to a GCE Kafka cluster, then Dataflow/Dataproc → GCS**

**Tiny mental image:** echo the broadcast to a sister station, then record it there.

**Final answer:** A. Deploy a Kafka cluster on GCE VM Instances. Configure your on-prem cluster to mirror your topics to the cluster running in GCE. Use a Dataproc cluster or Dataflow job to read from Kafka and write to GCS.'''

E["test_6_q3"] = '''### Step 4: Choose the answer

- Watermarks plus event-time timestamps let Dataflow reason about when data is complete and still admit late or out-of-order records correctly.
- It satisfies the goal: handle lagged/disordered data within predictable windows.

### Exam shortcut

If you see:
- late or out-of-order data in Dataflow
- predictable windowed processing
- correctness despite lag

Think: **watermarks + event-time timestamps (and allowed lateness)**

**Tiny mental image:** a "we think all today's mail has arrived" marker that still accepts a few stragglers.

**Final answer:** C. Use watermarks and timestamps to capture the lagged data.'''

E["test_6_q4"] = '''### Step 4: Choose the answer

- A Dataproc cluster with standard persistent disks, 50% preemptible workers, and data in Cloud Storage (gs:// not hdfs://) is the cost-effective, fault-tolerant managed Hadoop migration.
- It satisfies both: preemptibles plus standard disks cut cost, and Cloud Storage decouples durable data from ephemeral compute.

### Exam shortcut

If you see:
- migrate Hadoop to managed, cost-effective + fault-tolerant
- preemptible workers, standard (not SSD) disks
- data in Cloud Storage, swap hdfs:// → gs://

Think: **Dataproc + preemptibles + standard PD + Cloud Storage**

**Tiny mental image:** rent cheap temp workers and keep the goods in a permanent warehouse.

**Final answer:** A. Deploy a Cloud Dataproc cluster. Use a standard persistent disk and 50% preemptible workers. Store data in Cloud Storage, and change references in scripts from hdfs:// to gs://'''

E["test_6_q5"] = '''### Step 4: Choose the answer

- Cloud Dataprep lets non-developer analysts build and maintain visual transformation recipes that run on a schedule, adapting as the schema changes.
- It satisfies all three needs: scheduled execution, analyst-friendly editing, and a graphical design tool.

### Exam shortcut

If you see:
- scheduled CSV transformations with evolving schema
- non-developers must modify them, graphical tool
- no-code data prep

Think: **Cloud Dataprep recipes (scheduled)**

**Tiny mental image:** a visual recipe card the analysts can tweak each month, run automatically on a timer.

**Final answer:** A. Use Cloud Dataprep to build and maintain the transformation recipes, and execute them on a scheduled basis'''

E["test_6_q7"] = '''### Step 4: Choose the answer

- A different windowing/triggering algorithm is incompatible with an in-place --update, so Drain the running pipeline (finishing in-flight data) and start a new job with the new code.
- It satisfies "no data loss": Drain flushes outstanding data before the incompatible pipeline is replaced.

### Exam shortcut

If you see:
- update a streaming pipeline whose windowing/triggering changed
- incompatible change (can't hot-update in place)
- no data loss

Think: **Drain the old job, deploy a new one** (vs --update for compatible changes)

**Tiny mental image:** when the new machine takes different-shaped parts, empty the old line fully before swapping it.

**Final answer:** D. Stop the Cloud Dataflow pipeline with the Drain option. Create a new Cloud Dataflow job with the updated code'''

E["test_6_q8"] = '''### Step 4: Choose the answer

- A dedicated calibration MapReduce job with all other jobs chained after it guarantees calibration always runs first, systematically.
- It satisfies the fix: a reproducible pipeline step rather than per-user or after-the-fact correction.

### Exam shortcut

If you see:
- a required preprocessing step keeps getting skipped
- make it systematic/repeatable in the pipeline
- ordering/dependency between jobs

Think: **dedicated upstream job, chain everything after it**

**Tiny mental image:** put the safety checklist as step zero so nothing moves until it's done.

**Final answer:** B. Introduce a new MapReduce job to apply sensor calibration to raw data, and ensure all other MapReduce jobs are chained after this.'''

E["test_6_q9"] = '''### Step 4: Choose the answer

- A try/catch in the DoFn routing bad rows via a side output into a dead-letter PCollection (stored to Pub/Sub) makes the pipeline resilient and lets you reprocess all failures.
- It satisfies both: the job no longer crashes on bad input, and every failed record is captured for replay.

### Exam shortcut

If you see:
- Dataflow failing on bad input, need reliability + reprocessing
- capture errors without dropping the pipeline
- dead-letter pattern

Think: **try/catch in DoFn + side output (dead-letter) to Pub/Sub**

**Tiny mental image:** set bad parts aside on a "rework" tray instead of letting one jam the line.

**Final answer:** D. Add a try catch block to your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to PubSub later.'''

E["test_6_q14"] = '''### Step 4: Choose the answer

- A ParDo that inspects each element and drops the corrupt ones cleanly filters out the 2% bad data inline.
- It satisfies the goal: per-element validation/filtering, the natural Beam transform for discarding records.

### Exam shortcut

If you see:
- filter/drop bad records in a Dataflow stream
- per-element validation
- discard, not split or join

Think: **ParDo (filter out corrupt elements)**

**Tiny mental image:** an inspector on the belt who tosses defective items into the bin.

**Final answer:** B. Add a ParDo transform in Cloud Dataflow to discard corrupt elements.'''

E["test_6_q18"] = '''### Step 4: Choose the answer

- Managed export of Datastore to a Nearline/Coldline Cloud Storage bucket creates archivable, point-in-time snapshots cheaply (and streaming exports to partitioned BigQuery is the other valid path).
- It satisfies the goal: periodic snapshots for recovery/cloning, retained long-term at low cost.

### Exam shortcut

If you see:
- periodic snapshots of Datastore for PITR/cloning
- archive long-term, cost-effective
- managed export

Think: **Datastore managed export → Cloud Storage Nearline/Coldline**

**Tiny mental image:** take a dated photo of the database and file it in cheap deep storage.

**Final answer:** A. Use managed export, and store the data in a Cloud Storage bucket using Nearline or Coldline class.'''

append_entries(E)

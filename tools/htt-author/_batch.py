from lib import append_entries

E = {}

E["test_14_q19"] = '''### Step 4: Choose the answer

- Transfer Service for on-premises data uses local agents that move the daily JSON files into Cloud Storage without public-internet access, then BigQuery queries them.
- It satisfies both: recurring transfer from a network-isolated source plus exploration in BigQuery.

### Exam shortcut

If you see:
- recurring on-prem transfer, source not on public internet
- agent-based, scheduled, into Cloud Storage
- then explore in BigQuery

Think: **Storage Transfer Service for on-premises data (agents)**

**Tiny mental image:** station your own couriers inside the locked building to ship mail out on schedule.

**Final answer:** C. Use Transfer Service for on-premises data to copy data from your on-premises environment to Cloud Storage. Use the BigQuery Data Transfer Service to import data into BigQuery.'''

E["test_16_q43"] = '''### Step 4: Choose the answer

- At 20 Mb/sec, 2 PB can't move online in six months, so Transfer Appliance ships the data physically within the window.
- It satisfies the constraint: offline bulk transfer when bandwidth, not the deadline alone, is the bottleneck.

### Exam shortcut

If you see:
- petabytes with low bandwidth, fixed deadline
- online transfer would take far too long
- one-time bulk migration

Think: **Transfer Appliance** (offline shipping)

**Tiny mental image:** when it won't fit through the straw, ship the whole tank.

**Final answer:** A. Use Transfer Appliance to copy the data to Cloud Storage'''

E["test_1_q48"] = '''### Step 4: Choose the answer

- Running a data quality assessment on the extracted source data - value ranges, distributions, invalid/missing counts - reveals the scope of the problem before any ETL is written.
- It satisfies the goal: understand the data's actual condition first, rather than trusting source owners or polluting the warehouse.

### Exam shortcut

If you see:
- gauge data quality "before writing ETL"
- profile ranges, distributions, null/invalid counts
- understand scope of bad data first

Think: **data quality assessment / profiling of the source**

**Tiny mental image:** inspect and measure the lumber before you start building, not after the house leans.

**Final answer:** C. Perform a data quality assessment on the source data after it is extracted from the source system. These should include checks for ranges of values in each attribute, distribution of values in each attribute, counts of the number of invalid and missing values, and other checks on source data.'''

E["test_5_q39"] = '''### Step 4: Choose the answer

- Keeping the frequently-updated prices in a Cloud Storage bucket and querying them as a BigQuery external (federated) source means the latest file is read on demand with no reload cost.
- It satisfies the goal: always-current data combined in BigQuery as cheaply as possible.

### Exam shortcut

If you see:
- small, frequently-updated reference data to join in BigQuery
- avoid repeated load jobs / minimize cost
- keep it always current

Think: **BigQuery external (federated) table over Cloud Storage**

**Tiny mental image:** read the live price sheet pinned to the wall instead of reprinting the whole catalog every half hour.

**Final answer:** B. Store and update the data in a regional Google Cloud Storage bucket and create a federated data source in BigQuery'''

E["test_7_q45"] = '''### Step 4: Choose the answer

- ParDo applies a per-element transform that extracts the customer name from each record and emits it to the output PCollection.
- It satisfies the requirement: element-wise processing/extraction, the core Beam transform for this.

### Exam shortcut

If you see:
- per-element transform/extraction in Dataflow/Beam
- map/filter each record to an output PCollection
- custom processing logic

Think: **ParDo (with a DoFn)**

**Tiny mental image:** a worker on the line who picks one field off each passing item.

**Final answer:** A. ParDo'''

E["test_8_q36"] = '''### Step 4: Choose the answer

- Permission-denied errors running a BigQuery-source pipeline locally mean your gcloud credentials lack access to the BigQuery resources.
- It satisfies the diagnosis: pipelines run fine locally, but the local identity must be authorized for BigQuery.

### Exam shortcut

If you see:
- "permission denied" running a pipeline locally against BigQuery
- it's an auth/credentials issue, not a capability limit
- local execution is allowed

Think: **local gcloud identity lacks BigQuery access**

**Tiny mental image:** you're at the right door, but your badge isn't on the access list.

**Final answer:** A. Your gcloud does not have access to the BigQuery resources'''

E["test_15_q53"] = '''### Step 4: Choose the answer

- Batching the work into ten-second increments groups the high-rate HTTP calls, smoothing load and relieving backpressure on the GUID service.
- It satisfies the goal: fewer, bundled external calls under tens-of-thousands-per-second throughput.

### Exam shortcut

If you see:
- high-throughput pipeline making external HTTP calls
- "reduce backpressure" / overwhelmed downstream service
- micro-batching as a lever

Think: **batch into short time increments to throttle external calls**

**Tiny mental image:** send one bus every ten seconds instead of flagging a taxi for each passenger.

**Final answer:** D. Batch the job into ten-second increments.'''

E["test_16_q51"] = '''### Step 4: Choose the answer

- An extracted data source caches a static snapshot, so charts and tables refresh far faster than querying a live source each time.
- It satisfies the goal: improved interactive performance by reading from the in-memory extract.

### Exam shortcut

If you see:
- slow chart/table refresh in Looker Studio (Data Studio)
- improve dashboard performance
- live vs extracted source

Think: **extracted (cached) data source**

**Tiny mental image:** work from a printed snapshot on your desk instead of phoning the warehouse for every number.

**Final answer:** C. Use an extracted data source'''

E["test_11_q51"] = '''### Step 4: Choose the answer

- A service account scoped to exactly read the batch files and write to BigQuery runs the automated job securely without over-granting.
- It satisfies "most secure": least-privilege automation, not a human account or an Owner-level role.

### Exam shortcut

If you see:
- automate an unattended pipeline securely
- read from Cloud Storage, write to BigQuery
- avoid Owner role / human accounts

Think: **least-privilege service account scoped to the job's reads and writes**

**Tiny mental image:** give the night robot a keycard for just its two doors, not the master key.

**Final answer:** B. Use a service account that has permission to read the batch files and write to BigQuery.'''

E["test_10_q17"] = '''### Step 4: Choose the answer

- Each server publishes bid events to Pub/Sub, and a Dataflow pull subscription processes them in real time, awarding the bid to the first event processed.
- It satisfies the goal: globally scalable, ordered real-time collation across many servers.

### Exam shortcut

If you see:
- collate real-time events from many distributed producers
- globally scalable ingest + stream processing
- determine first/earliest

Think: **Pub/Sub ingest + Dataflow streaming**

**Tiny mental image:** every branch drops tickets in one central chute, and a sorter declares whoever's slip lands first.

**Final answer:** A. Have each application server write the bid events to Google Cloud Pub/Sub, and use a pull subscription with Google Cloud Dataflow to pull and process the events, giving the bid to the first user processed'''

E["test_1_q10"] = '''### Step 4: Choose the answer

- A sliding (hopping) window continuously re-evaluates the trailing hour as it advances, which is exactly what a rolling mean/standard-deviation alert needs.
- It satisfies the goal: overlapping windows that always reflect "the last hour" for anomaly detection.

### Exam shortcut

If you see:
- a rolling/continuous "last N minutes" computation
- overlapping windows, frequent re-evaluation
- moving average / trailing statistics

Think: **sliding (hopping) windows**

**Tiny mental image:** a moving spotlight that always lights the most recent hour as it glides forward.

**Final answer:** D. sliding window (also called hopping windows)'''

E["test_10_q44"] = '''### Step 4: Choose the answer

- gcloud functions deploy (with a Pub/Sub trigger) is the command that deploys the function to run on messages to the topic.
- It satisfies the task: deploying the Cloud Function, not publishing or pulling messages.

### Exam shortcut

If you see:
- deploy a Cloud Function triggered by Pub/Sub
- distinguish deploy vs publish/pull
- gcloud command choice

Think: **gcloud functions deploy (--trigger-topic)**

**Tiny mental image:** "deploy" installs the machine; "publish/pull" just move the parcels.

**Final answer:** D. gcloud functions deploy'''

E["test_12_q7"] = '''### Step 4: Choose the answer

- Streaming (unbounded) data requires a non-global windowing function; without one, the Dataflow job fails at pipeline construction for all streaming inserts.
- It satisfies the diagnosis: unbounded sources can't use the default global window without windowing/triggers.

### Exam shortcut

If you see:
- streaming Dataflow job fails for all inserts at creation
- unbounded source with no window applied
- windowing/transformation in play

Think: **unbounded streams need a non-global window**

**Tiny mental image:** you can't tally an endless parade without dividing it into segments first.

**Final answer:** C. The job fails because a non-global windowing function has not been applied, causing the job to fail during pipeline creation.'''

E["test_10_q23"] = '''### Step 4: Choose the answer

- Pig (PigLatin) expresses ETL data flows with native support for checkpointing and splitting pipelines on Hadoop.
- It satisfies the requirement: a dataflow-oriented language built for multi-stage, splittable ETL.

### Exam shortcut

If you see:
- Hadoop ETL needing checkpointing and pipeline splits
- dataflow scripting over raw MapReduce
- declarative transformation chains

Think: **Pig / PigLatin**

**Tiny mental image:** a pipeline language with built-in valves and save-points, not hand-wired MapReduce plumbing.

**Final answer:** B. PigLatin using Pig'''

E["test_10_q14"] = '''### Step 4: Choose the answer

- A side input supplies the extra data to a DoFn each time it processes a PCollection element, exactly the construct needed here.
- It satisfies the goal: additional read-only input available alongside the main element stream.

### Exam shortcut

If you see:
- a DoFn needs extra/reference data per element
- enrich or look up against a second dataset
- Apache Beam construct

Think: **side input**

**Tiny mental image:** the worker keeps a reference sheet beside the conveyor to consult on each item.

**Final answer:** B. Side input'''

E["test_11_q30"] = '''### Step 4: Choose the answer

- Bigtable exposes the HBase API, so the team migrates off on-prem Hadoop/HBase to a managed service with minimal program changes.
- It satisfies both: a fully managed wide-column store and HBase-API compatibility for existing code.

### Exam shortcut

If you see:
- migrate Hadoop/HBase to managed GCP
- keep using the HBase API with minimal changes
- large-scale NoSQL wide-column

Think: **Cloud Bigtable (HBase-compatible API)**

**Tiny mental image:** swap the engine but keep the same dashboard and controls the drivers already know.

**Final answer:** B. Bigtable'''

E["test_1_q46"] = '''### Step 4: Choose the answer

- Creating a Pub/Sub schema and assigning it to the topic at creation enforces a standard message structure on everything published.
- It satisfies the goal: validation at publish time on the topic, the producer-facing boundary.

### Exam shortcut

If you see:
- enforce a standard message structure in Pub/Sub
- validate at publish, on the topic (not subscription)
- schema enforcement

Think: **Pub/Sub schema assigned to the topic at creation**

**Tiny mental image:** the post office rejects any letter that doesn't fit the approved envelope template at the counter.

**Final answer:** B. Create a schema and assign it to a topic during topic creation.'''

E["test_2_q5"] = '''### Step 4: Choose the answer

- PCollections are the core Beam data abstraction that carries the (key, value) elements through the Dataflow workflow.
- It satisfies the question: the construct representing the distributed dataset being processed.

### Exam shortcut

If you see:
- the core dataset abstraction in Beam/Dataflow
- holds the elements flowing through transforms
- key-value or any record stream

Think: **PCollection**

**Tiny mental image:** the conveyor belt itself, carrying every item between machines.

**Final answer:** B. PCollections'''

E["test_2_q8"] = '''### Step 4: Choose the answer

- Cloud Dataflow is the managed service for streaming sensor data with windowed, stateful analysis like rolling mean/standard-deviation alerts.
- It satisfies the goal: serverless stream processing with native windowing for the anomaly logic.

### Exam shortcut

If you see:
- streaming sensor/IoT analytics, managed service
- windowed/stateful real-time computation
- anomaly detection on a moving window

Think: **Cloud Dataflow (Apache Beam streaming)**

**Tiny mental image:** a self-managing stream mill that watches the sensor flow and rings the bell on outliers.

**Final answer:** A. Cloud Dataflow'''

E["test_2_q33"] = '''### Step 4: Choose the answer

- Dataflow FlexRS lowers batch cost by scheduling jobs flexibly on preemptible resources, ideal when completion time can slip.
- It satisfies the goal: meaningful savings on non-urgent batch jobs with no pipeline rewrite.

### Exam shortcut

If you see:
- cut Dataflow *batch* cost, timing is flexible
- willing to wait longer for cheaper runs
- minimal changes to the pipeline

Think: **Dataflow FlexRS (Flexible Resource Scheduling)**

**Tiny mental image:** book the off-peak, standby fare because you don't care exactly when you land.

**Final answer:** C. Use Dataflow FlexRS'''

append_entries(E)

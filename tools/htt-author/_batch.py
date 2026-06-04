from lib import append_entries

E = {}

E["test_11_q24"] = '''### Step 4: Choose the answer

- gcloud dataflow sql query runs a SQL statement as a Dataflow job and writes the results to a BigQuery table.
- It satisfies the goal: SQL on Dataflow with a BigQuery sink, via the correct gcloud group/verb.

### Exam shortcut

If you see:
- run a SQL query *as a Dataflow job*, output to BigQuery
- gcloud command structure
- Dataflow SQL

Think: **gcloud dataflow sql query**

**Tiny mental image:** the right tool is "dataflow sql," not the bq or bigquery groups.

**Final answer:** C. gcloud dataflow sql query'''

E["test_11_q47"] = '''### Step 4: Choose the answer

- --maxNumWorkers caps how many workers the Dataflow job can scale to, limiting resource use while testing.
- It satisfies the goal: bound the autoscaler so a test run can't consume large resources.

### Exam shortcut

If you see:
- limit/cap Dataflow processing resources
- restrict autoscaling during testing
- worker-count parameter

Think: **--maxNumWorkers**

**Tiny mental image:** set a hiring ceiling so the test crew stays small.

**Final answer:** D. --maxNumWorkers'''

E["test_12_q13"] = '''### Step 4: Choose the answer

- gcloud dataproc clusters update with --num-secondary-workers adds preemptible (secondary) workers to the running cluster.
- It satisfies the goal: scale out with preemptibles, which are the "secondary" worker type.

### Exam shortcut

If you see:
- add preemptible VMs to a running Dataproc cluster
- preemptibles = secondary workers
- update an existing cluster

Think: **gcloud dataproc clusters update --num-secondary-workers**

**Tiny mental image:** dial up the count of temp ("secondary") workers on the live cluster.

**Final answer:** C. gcloud dataproc clusters update with the --num-secondary-workers parameter'''

E["test_13_q2"] = '''### Step 4: Choose the answer

- Dataform gives developers an intuitive environment to build, manage, version, and schedule SQL-as-code ELT pipelines in BigQuery.
- It satisfies the goal: an ELT-native, SQL-first development workflow for BigQuery.

### Exam shortcut

If you see:
- ELT with "SQL as code," version-controlled, scheduled
- developer-friendly SQL pipeline authoring in BigQuery
- transformations live in the warehouse

Think: **Dataform**

**Tiny mental image:** a Git-style IDE where your transformations are just managed SQL files.

**Final answer:** A. Use Dataform to build, manage, and schedule SQL pipelines.'''

E["test_13_q9"] = '''### Step 4: Choose the answer

- Enabling Pub/Sub exactly-once delivery on the pull subscription prevents two agents from receiving the same order, with no extra components.
- It satisfies both: no duplicate processing and no added workflow complexity.

### Exam shortcut

If you see:
- prevent duplicate processing of Pub/Sub messages
- avoid adding components/complexity
- pull subscription

Think: **Pub/Sub exactly-once delivery**

**Tiny mental image:** a ticket system that hands each order to exactly one clerk, never two.

**Final answer:** C. Use Pub/Sub exactly-once delivery in your pull subscription.'''

E["test_13_q13"] = '''### Step 4: Choose the answer

- Data freshness of 40 seconds with only 5 seconds of system lag means each message is processed quickly, but the job can't drain the Pub/Sub backlog - add workers/optimize.
- It satisfies the diagnosis: the bottleneck is throughput against a growing subscription backlog, not per-message processing time.

### Exam shortcut

If you see:
- data freshness much larger than system lag
- messages process fast but backlog grows
- Dataflow falling behind the subscription

Think: **scale up workers to clear the backlog (throughput, not per-message latency)**

**Tiny mental image:** each customer is served quickly, but the line keeps growing - open more registers.

**Final answer:** C. Messages in your Dataflow job are processed in less than 30 seconds, but your job cannot keep up with the backlog in the Pub/Sub subscription. Optimize your job or increase the number of workers to fix this.'''

E["test_13_q14"] = '''### Step 4: Choose the answer

- Dataform assertions express uniqueness and null-value checks declaratively in the pipeline code, failing the run if the data violates them.
- It satisfies the goal: data-quality tests integrated directly into the Dataform ELT workflow.

### Exam shortcut

If you see:
- data-quality checks (uniqueness, non-null) inside a Dataform/ELT pipeline
- declarative tests on final tables
- fail the pipeline on bad data

Think: **Dataform assertions**

**Tiny mental image:** built-in unit tests for your tables that block the build when they fail.

**Final answer:** C. Build Dataform assertions into your code.'''

E["test_13_q15"] = '''### Step 4: Choose the answer

- Dataprep gives the data science team a low-code way to explore, cleanse, and validate the files directly in Cloud Storage.
- It satisfies the goal: interactive, no-code data preparation on the raw Cloud Storage data.

### Exam shortcut

If you see:
- explore/clean/validate Cloud Storage data, low-code
- non-engineers preparing data
- visual profiling and cleansing

Think: **Cloud Dataprep**

**Tiny mental image:** a click-driven workbench that lets the team tidy the raw files without code.

**Final answer:** D. Provide the data science team access to Dataprep to prepare, validate, and explore the data within Cloud Storage.'''

E["test_13_q22"] = '''### Step 4: Choose the answer

- A BigQuery scheduled query runs the every-two-hours transformation, and routing run notifications to Pub/Sub with a Cloud Function emails after three consecutive failures.
- It satisfies all: scheduled SQL with retry plus a custom failure-count alert the scheduled query alone can't express.

### Exam shortcut

If you see:
- periodic BigQuery SQL transform with retry
- email only after N consecutive failures
- custom alerting logic on top of scheduling

Think: **scheduled query → Pub/Sub notification → Cloud Function (count failures, email)**

**Tiny mental image:** a timer runs the job; a small watcher counts strikes and rings the alarm on the third.

**Final answer:** D. Create a BigQuery scheduled query to run the SQL transformation with schedule options that repeats every two hours, and enable notification to Pub/Sub topic. Use Pub/Sub and Cloud Functions to send an email after three failed executions.'''

E["test_13_q27"] = '''### Step 4: Choose the answer

- Migrating the Parquet data into BigQuery and refactoring the Spark jobs to read/write BigQuery on Dataproc Serverless gives managed services with the data already in BigQuery.
- It satisfies the goal: data lands in BigQuery for future pipelines, serverless Spark, and minimal ETL/overhead changes.

### Exam shortcut

If you see:
- migrate Spark + Parquet, want data *in BigQuery* for future use
- managed/serverless, minimal code and overhead
- BigQuery-centric target

Think: **data → BigQuery, Spark on Dataproc Serverless reading/writing BigQuery**

**Tiny mental image:** move the goods straight into the warehouse and let the serverless crew work them in place.

**Final answer:** C. Migrate your data to BigQuery. Refactor Spark pipelines to write and read data on BigQuery, and run them on Dataproc Serverless.'''

E["test_13_q33"] = '''### Step 4: Choose the answer

- A session window with a 15-minute gap keeps aggregating a sensor's readings until 15 minutes of silence, then closes - matching the "close after 15 min of no data" rule.
- It satisfies the goal: activity-bounded windows that span however long data keeps arriving.

### Exam shortcut

If you see:
- window should close after N minutes of *no data*
- per-sensor activity bursts of variable length
- gap-based closing

Think: **session window (gap = inactivity timeout)**

**Tiny mental image:** keep recording while the sensor chatters; stop once it's quiet for 15 minutes.

**Final answer:** A. Use session windows with a 15-minute gap duration.'''

E["test_13_q35"] = '''### Step 4: Choose the answer

- Draining the old pipeline finishes in-flight windows before the new version starts, avoiding data loss and keeping latency within bounds.
- It satisfies the goal: a clean handoff with no dropped data and no large processing gap.

### Exam shortcut

If you see:
- deploy a new streaming pipeline version, no data loss
- bounded latency increase
- graceful cutover

Think: **Drain old, then start new**

**Tiny mental image:** let the current batch finish flowing out before switching to the new line.

**Final answer:** C. Drain the old pipeline, then start the new pipeline.'''

E["test_13_q40"] = '''### Step 4: Choose the answer

- Copying the ORC files to Cloud Storage and exposing them as external BigQuery tables lets the team run SQL on the Hive-partitioned data cheaply, with no cluster to keep running.
- It satisfies the goal: familiar SQL exploration of the existing ORC data at minimal storage/compute cost.

### Exam shortcut

If you see:
- query existing ORC/Hive data with SQL, cost-effective
- no persistent cluster, no data reload into native tables
- explore in place

Think: **ORC in Cloud Storage + BigQuery external tables**

**Tiny mental image:** put a SQL window over the existing files instead of rebuilding a warehouse or running a cluster all day.

**Final answer:** D. Copy the ORC files on Cloud Storage, then create external BigQuery tables for the data scientist team.'''

E["test_13_q41"] = '''### Step 4: Choose the answer

- Specifying a worker region with --region lets Dataflow place workers across zones in that region, surviving individual zonal failures at submission.
- It satisfies the goal: regional resilience instead of pinning the job to one zone.

### Exam shortcut

If you see:
- protect a Dataflow job from zonal failure
- regional vs single-zone placement
- --region vs --zone

Think: **--region (regional worker placement)**

**Tiny mental image:** let the crew set up anywhere in the region, not in one building that might go dark.

**Final answer:** C. Specify a worker region by using the --region flag.'''

E["test_13_q43"] = '''### Step 4: Choose the answer

- Wrapping the DoFn logic in exception handling and routing failed records through a side output to a new Pub/Sub topic captures business-logic failures for alerting.
- It satisfies the goal: custom-logic failures (not delivery failures) are redirected and monitorable on the alert topic.

### Exam shortcut

If you see:
- route messages that fail *custom business logic* in a DoFn
- send them to an alert/Pub/Sub topic
- distinguish from Pub/Sub dead-lettering (delivery failures)

Think: **DoFn try/catch → side output → new Pub/Sub topic**

**Tiny mental image:** the inspector sets aside parts that fail the custom test onto a separate alert chute.

**Final answer:** B. Use an exception handling block in your Dataflows DoFn code to push the messages that failed to be transformed through a side output and to a new Pub/Sub topic. Use Cloud Monitoring to monitor the topic/num_unacked_messages_by_region metric on this new topic.'''

E["test_13_q45"] = '''### Step 4: Choose the answer

- Defining watermarks to model expected arrival time, and allowing late data, lets the pipeline assign stragglers to their correct hopping windows.
- It satisfies the goal: late records are recognized as late and folded into the right window's aggregation.

### Exam shortcut

If you see:
- late data not recognized, wrong aggregations
- hopping/sliding windows
- need correct handling of stragglers

Think: **watermarks + allowed lateness**

**Tiny mental image:** a "most mail is in" marker that still accepts and correctly files late letters.

**Final answer:** A. Use watermarks to define the expected data arrival window. Allow late data as it arrives.'''

E["test_13_q47"] = '''### Step 4: Choose the answer

- The BigQuery Storage Write API provides exactly-once streaming semantics at high throughput, and a regional target table keeps the high-rate writes consistent.
- It satisfies both: exactly-once delivery and ~1.5 GB/s ingestion that the older streaming API can't match.

### Exam shortcut

If you see:
- exactly-once streaming into BigQuery at high throughput
- source lacks exactly-once
- modern write path

Think: **BigQuery Storage Write API (regional table)**

**Tiny mental image:** the new high-speed loading dock that guarantees each crate is logged exactly once.

**Final answer:** A. Use the BigQuery Storage Write API and ensure that your target BigQuery table is regional.'''

E["test_13_q51"] = '''### Step 4: Choose the answer

- Moving the data to Cloud Storage and running the existing Spark jobs on Dataproc is a managed lift-and-shift with minimal code changes on a tight timeline.
- It satisfies the goal: managed execution, no persistent cluster to own, and the Spark code largely unchanged.

### Exam shortcut

If you see:
- migrate Spark jobs fast, minimal code changes
- managed service, no long-lived Hadoop cluster
- lift-and-shift

Think: **data → Cloud Storage, run on Dataproc**

**Tiny mental image:** move into the managed workshop and run the same machines you already know.

**Final answer:** D. Move your data to Cloud Storage. Run your jobs on Dataproc.'''

E["test_13_q54"] = '''### Step 4: Choose the answer

- Cloud Data Fusion with the Wrangler tool normalizes the inconsistent fields visually and runs as a recurring job, with no coding.
- It satisfies the goal: a quick, no-code, scheduled data-normalization pipeline.

### Exam shortcut

If you see:
- normalize/standardize messy fields, no coding, recurring
- visual data wrangling
- quick scheduled cleanup

Think: **Cloud Data Fusion + Wrangler (scheduled)**

**Tiny mental image:** a point-and-click cleanup wizard that reruns itself each week.

**Final answer:** A. Use Cloud Data Fusion and Wrangler to normalize the data, and set up a recurring job.'''

E["test_13_q55"] = '''### Step 4: Choose the answer

- Exponential backoff as the retry policy spaces out retries during consumer downtime, and dead-lettering to a different topic after 10 attempts stores the unprocessed messages.
- It satisfies all: reliability during outages, gradual retries, and capture of poison messages after the retry limit.

### Exam shortcut

If you see:
- retry failed Pub/Sub messages gradually
- store undeliverable messages after N attempts
- dead-letter to a separate topic

Think: **exponential backoff + dead-letter topic (max delivery attempts)**

**Tiny mental image:** retry with longer pauses each time, then drop the stubborn parcel into the separate "undeliverable" bin.

**Final answer:** D. Use exponential backoff as the subscription retry policy, and configure dead lettering to a different topic with maximum delivery attempts set to 10.'''

append_entries(E)

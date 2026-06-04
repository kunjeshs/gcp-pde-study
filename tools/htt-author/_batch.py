from lib import append_entries

E = {}

E["test_3_q11"] = '''### Step 4: Choose the answer

- Dialogflow implements the text-and-voice chatbot with low/no code by defining intents from the most common queries.
- It satisfies the goal: keyword/intent-driven responses without building a custom NLP app.

### Exam shortcut

If you see:
- chatbot for text + voice, low/no-code
- train on keywords/intents
- Dialogflow

Think: **Dialogflow (define intents)**

**Tiny mental image:** map common questions to intents and let Dialogflow run the conversation.

**Final answer:** D. Use Dialogflow to implement the chatbot and define the intents based on the most common queries.'''

E["test_4_q43"] = '''### Step 4: Choose the answer

- Switching to flat-rate (capacity) pricing with a hierarchical priority/reservation model gives business units guaranteed slot allocations, fixing the contention without new projects.
- It satisfies both: predictable slot capacity and priority-based sharing across units.

### Exam shortcut

If you see:
- users starved of on-demand slots, avoid adding projects
- guarantee/allocate capacity across teams
- flat-rate / reservations + priorities

Think: **flat-rate pricing + reservation hierarchy/priorities**

**Tiny mental image:** buy a fixed pool of slots and divvy guaranteed shares to each business unit.

**Final answer:** C. Switch to flat-rate pricing and set up a hierarchical priority system for your projects'''

E["test_14_q16"] = '''### Step 4: Choose the answer

- Running the non-time-sensitive SQL pipelines as batch queries (which queue instead of failing) and ad-hoc queries as interactive jobs resolves the concurrency quota errors.
- It satisfies the goal: batch jobs wait for slots rather than erroring, leaving interactive capacity for analysts.

### Exam shortcut

If you see:
- BigQuery concurrency/quota errors, some jobs not time-sensitive
- batch queries queue (no concurrency error); interactive run immediately
- separate batch vs interactive

Think: **pipelines → batch queries, ad-hoc → interactive**

**Tiny mental image:** put the patient jobs in the queue lane and keep the express lane for live queries.

**Final answer:** B. Update SQL pipelines to run as a batch query, and run ad-hoc queries as interactive query jobs.'''

E["test_1_q40"] = '''### Step 4: Choose the answer

- Exporting Cloud Audit Logs to Cloud Storage with a locked retention policy (and a lifecycle rule to delete at 3 years) keeps the IAM-change logs immutable for the required period.
- It satisfies the mandate: tamper-proof 3-year retention of IAM change logs, then automatic cleanup.

### Exam shortcut

If you see:
- retain audit/IAM-change logs immutably for N years
- export Cloud Audit Logs to Cloud Storage
- locked retention policy + lifecycle delete

Think: **Audit Logs → Cloud Storage + locked retention + lifecycle**

**Tiny mental image:** funnel the change logs into a time-locked vault that auto-empties after 3 years.

**Final answer:** A. Use Cloud Audit Logs and export them to Cloud Storage. Create a retention policy and retention policy lock to prevent the logs from being deleted prior to them reaching 3 years of age. Define a lifecycle policy to delete the logs after three years.'''

E["test_2_q3"] = '''### Step 4: Choose the answer

- Key Visualizer is the Bigtable tool that visualizes access patterns and hot row-key ranges to diagnose row-key design problems.
- It satisfies the goal: review access patterns across row keys to find the imbalance.

### Exam shortcut

If you see:
- diagnose Bigtable performance / row-key hot-spotting
- visualize access patterns across key ranges
- Key Visualizer

Think: **Bigtable Key Visualizer**

**Tiny mental image:** a heatmap of your row keys showing where the traffic piles up.

**Final answer:** C. Key Visualizer'''

E["test_2_q4"] = '''### Step 4: Choose the answer

- job/system_lag reports the maximum time an item has been waiting to be processed in the Dataflow pipeline.
- It satisfies the goal: track the longest current processing delay.

### Exam shortcut

If you see:
- max time an element has waited in a Dataflow pipeline
- processing latency / backlog age
- system_lag

Think: **job/system_lag**

**Tiny mental image:** the longest any item has sat in the queue waiting its turn.

**Final answer:** B. job/system_lag'''

E["test_4_q12"] = '''### Step 4: Choose the answer

- Loading the new records into a table and applying a single MERGE (writing to a new table) avoids the per-row UPDATE DML limit that triggers quotaExceeded.
- It satisfies the goal: bulk-apply a million updates in one set-based operation instead of many UPDATEs.

### Exam shortcut

If you see:
- quotaExceeded on many BigQuery UPDATEs
- bulk-apply updates via load + MERGE
- set-based, not row-by-row

Think: **load to a table + single MERGE**

**Tiny mental image:** reconcile all the changes in one sweep, not a million separate edits.

**Final answer:** D. Import the new records from the CSV file into a new BigQuery table. Merge the new records with the existing records using a BigQuery job and write the results to a new BigQuery table.'''

E["test_4_q19"] = '''### Step 4: Choose the answer

- The redelivery (high message rate, no errors) means the subscriber can't keep up with volume and/or isn't acknowledging messages, so Pub/Sub re-delivers them.
- It satisfies the diagnosis: unacked/too-slow processing causes at-least-once redelivery, inflating the rate.

### Exam shortcut

If you see:
- Pub/Sub processing rate higher than expected, no errors
- duplicates from redelivery
- subscriber too slow or not acking

Think: **subscriber can't keep up / doesn't ack → redelivery**

**Tiny mental image:** the courier keeps re-dropping parcels no one signs for fast enough.

**Final answer:** D. The subscriber code is unable to keep up with the message volume.'''

E["test_4_q32"] = '''### Step 4: Choose the answer

- A batch job that processes some elements and then fails with DoFn-specific errors points to runtime exceptions in the worker code (the DoFn logic).
- It satisfies the diagnosis: validation/graph-construction errors fail before processing; this failed mid-run, so it's worker code.

### Exam shortcut

If you see:
- Dataflow processes a few elements then fails, DoFn errors
- runtime (not construction/validation) failure
- worker code exception

Think: **errors in the worker (DoFn) code**

**Tiny mental image:** the line ran a bit, then a faulty step (DoFn) threw and stopped it.

**Final answer:** B. Errors in the worker code'''

E["test_5_q40"] = '''### Step 4: Choose the answer

- Loading the new records into a table and applying a single MERGE (writing to a new table) avoids the per-statement UPDATE DML limit that causes quotaExceeded.
- It satisfies the goal: bulk-apply a million updates in one set-based operation.

### Exam shortcut

If you see:
- quotaExceeded on many BigQuery UPDATEs
- bulk-apply via load + MERGE
- set-based, not row-by-row

Think: **load to a table + single MERGE**

**Tiny mental image:** reconcile all changes in one sweep, not a million separate edits.

**Final answer:** D. Import the new records from the CSV file into a new BigQuery table. Create a BigQuery job that merges the new records with the existing records and writes the results to a new BigQuery table.'''

E["test_10_q33"] = '''### Step 4: Choose the answer

- A Cloud Monitoring dashboard on the BigQuery slots/allocated_for_project metric lets each team watch its own project's slot usage directly.
- It satisfies the goal: per-project slot visibility from a built-in metric, no custom log pipeline.

### Exam shortcut

If you see:
- monitor BigQuery slot usage per project/team
- built-in metric slots/allocated_for_project
- Cloud Monitoring dashboard

Think: **Cloud Monitoring + slots/allocated_for_project**

**Tiny mental image:** a ready-made gauge of each project's slot consumption.

**Final answer:** B. Develop a Cloud Monitoring dashboard utilizing the BigQuery metric slots/allocated_for_project.'''

E["test_13_q18"] = '''### Step 4: Choose the answer

- Assigning notification logic to the operator's on_failure_callback fires when the at-risk task fails, alerting you.
- It satisfies the goal: a callback that runs specifically on task failure (not retry or SLA miss).

### Exam shortcut

If you see:
- notify when an Airflow task fails
- operator callback parameter
- on_failure_callback (vs on_retry/sla_miss)

Think: **on_failure_callback**

**Tiny mental image:** wire the alarm to the "task failed" hook on that operator.

**Final answer:** C. Assign a function with notification logic to the on_failure_callback parameter tor the operator responsible for the task at risk.'''

E["test_13_q36"] = '''### Step 4: Choose the answer

- Checking for duplicate rows, using Audit logs to find the job IDs, and Cloud Monitoring to identify the Dataflow jobs/versions reveals that more than one pipeline is writing to the table - stop all but the latest.
- It satisfies the goal: root-cause the doubled partition size (duplicate writes from overlapping pipeline versions) and fix it.

### Exam shortcut

If you see:
- BigQuery partition size doubled, source volume unchanged
- suspect duplicate writes from multiple pipeline versions
- trace via Audit logs + Monitoring, stop extra writers

Think: **find duplicate writers (Audit logs + Monitoring), keep only the latest pipeline**

**Tiny mental image:** two pipelines were quietly pouring the same data in - shut the old one off.

**Final answer:** C. 1. Check for duplicate rows in the BigQuery tables that have the daily partition data size doubled. 2. Check the BigQuery Audit logs to find job IDs. 3. Use Cloud Monitoring to determine when the identified Dataflow jobs started and the pipeline code version. 4. When more than one pipeline ingests data into a table, stop all versions except the latest one.'''

E["test_14_q25"] = '''### Step 4: Choose the answer

- Worker pod evictions from memory pressure are resolved by increasing the Composer environment size and giving the Airflow workers more memory.
- It satisfies the goal: more memory headroom so tasks stop being OOM-evicted.

### Exam shortcut

If you see:
- Cloud Composer worker pod evictions, high worker memory
- tasks failing from memory pressure
- bigger environment / more worker memory

Think: **increase environment size + worker memory**

**Tiny mental image:** the workers are running out of RAM - give them a bigger room.

**Final answer:** B. Increase the Cloud Composer 2 environment size from medium to large.'''

E["test_14_q55"] = '''### Step 4: Choose the answer

- The administrative resource charts plus querying INFORMATION_SCHEMA reveal slot utilization and per-job performance over time, pinpointing queuing/contention.
- It satisfies the goal: investigate job-level performance to find where the slowdowns occur.

### Exam shortcut

If you see:
- investigate BigQuery slowness, slot contention/queuing
- per-job performance over time
- admin resource charts + INFORMATION_SCHEMA

Think: **admin resource charts + INFORMATION_SCHEMA queries**

**Tiny mental image:** read the slot-usage charts and query the job history to see what's stuck.

**Final answer:** C. Use available administrative resource charts to determine how slots are being used and how jobs are performing over time. Run a query on the INFORMATION_SCHEMA to review query performance.'''

E["test_15_q15"] = '''### Step 4: Choose the answer

- Loading the new records into a table and applying a single MERGE (writing to a new table) avoids the per-statement UPDATE DML limit that causes quotaExceeded.
- It satisfies the goal: bulk-apply a million updates in one set-based operation.

### Exam shortcut

If you see:
- quotaExceeded on many BigQuery UPDATEs
- bulk-apply via load + MERGE
- set-based, not row-by-row

Think: **load to a table + single MERGE**

**Tiny mental image:** reconcile all changes in one sweep, not a million separate edits.

**Final answer:** D. Import the new records from the CSV file into a new BigQuery table. Create a BigQuery job that merges the new records with the existing records and writes the results to a new BigQuery table.'''

E["test_15_q30"] = '''### Step 4: Choose the answer

- A Cloud Monitoring dashboard on the BigQuery slots/allocated_for_project metric lets each team watch its own project's slot usage directly.
- It satisfies the goal: per-project slot visibility from a built-in metric, no custom log pipeline.

### Exam shortcut

If you see:
- monitor BigQuery slot usage per project/team
- built-in metric slots/allocated_for_project
- Cloud Monitoring dashboard

Think: **Cloud Monitoring + slots/allocated_for_project**

**Tiny mental image:** a ready-made gauge of each project's slot consumption.

**Final answer:** B. Create a Cloud Monitoring dashboard based on the BigQuery metric slots/allocated_for_project'''

E["test_15_q57"] = '''### Step 4: Choose the answer

- A batch job that processes a few elements then fails with DoFn-specific errors points to runtime exceptions in the worker code.
- It satisfies the diagnosis: validation/graph-construction errors fail before processing; this failed mid-run, so it's worker code.

### Exam shortcut

If you see:
- Dataflow processes a few elements then fails, DoFn errors
- runtime (not construction/validation) failure
- worker code exception

Think: **exceptions in the worker (DoFn) code**

**Tiny mental image:** the line ran a bit, then a faulty step threw and stopped it.

**Final answer:** B. Exceptions in worker code'''

E["test_16_q4"] = '''### Step 4: Choose the answer

- subscription/num_undelivered_messages shows the backlog on a pull subscription, signaling when subscribers aren't keeping up with ingestion.
- It satisfies the goal: monitor consumer lag at the subscription level.

### Exam shortcut

If you see:
- subscribers not keeping up with Pub/Sub ingestion
- backlog on a pull subscription
- num_undelivered_messages (subscription)

Think: **subscription/num_undelivered_messages**

**Tiny mental image:** the pile of unread messages growing on the subscription tells you it's falling behind.

**Final answer:** D. subscription/num_undelivered_messages'''

E["test_14_q3"] = '''### Step 4: Choose the answer

- A dual-region Cloud Storage bucket with turbo replication minimizes RPO during a regional failure while keeping a single, transparent bucket for the applications.
- It satisfies the goal: low-RPO resilience with no application changes (one bucket, replicated across regions).

### Exam shortcut

If you see:
- survive a regional failure, minimize RPO, no app disruption
- single transparent bucket, fast cross-region replication
- dual-region + turbo replication

Think: **dual-region bucket + turbo replication**

**Tiny mental image:** one bucket backed by a synced twin region, replicated fast, invisible to the apps.

**Final answer:** C. Adopt a dual-region Cloud Storage bucket, and enable turbo replication in your architecture.'''

E["test_15_q11"] = '''### Step 4: Choose the answer

- A multi-regional Cloud Storage bucket maximizes availability and is directly accessible by Dataproc, BigQuery, and Compute Engine for any file format.
- It satisfies the goal: a single highly-available store for CSV/Avro/PDF that all tools read, with performance not a concern.

### Exam shortcut

If you see:
- one store shared by Dataproc + BigQuery + Compute Engine
- mixed formats (CSV/Avro/PDF), maximize availability
- performance not the priority

Think: **multi-regional Cloud Storage bucket**

**Tiny mental image:** one highly-available warehouse every department can enter, holding boxes of any shape.

**Final answer:** D. Store the data in a multi-regional Cloud Storage bucket. Access the data directly using Dataproc, BigQuery, and Compute Engine.'''

E["test_15_q34"] = '''### Step 4: Choose the answer

- Scheduling a daily export of the table to a dual/multi-region Cloud Storage bucket gives an RPO under 24 hours at minimal cost.
- It satisfies the goal: cheap, region-resilient backup meeting the sub-24h recovery point.

### Exam shortcut

If you see:
- protect a BigQuery table from regional failure, RPO < 24h, minimize cost
- daily export to a multi/dual-region bucket
- cheaper than snapshots/dual-write

Think: **daily export to a dual/multi-region Cloud Storage bucket**

**Tiny mental image:** dump a daily copy into a cross-region bucket - cheap insurance within a day's RPO.

**Final answer:** A. Schedule a daily export of the table to a Cloud Storage dual or multi-region bucket.'''

append_entries(E)

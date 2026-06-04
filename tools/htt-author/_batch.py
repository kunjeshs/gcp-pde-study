from lib import append_entries

E = {}

E["test_6_q28"] = '''### Step 4: Choose the answer

- Using device_id as the row key (with date and data_point as column data) keeps each device's time-series together and spreads writes across devices, avoiding the hot-spotting a date-led key causes.
- It satisfies the goal: balanced writes and efficient per-device reads in Bigtable.

### Exam shortcut

If you see:
- Bigtable row-key design for per-device time-series
- avoid leading the key with a timestamp/date (hot-spotting)
- lead with the entity (device_id)

Think: **row key = device_id (not date-led)**

**Tiny mental image:** file by device first so all devices' writes spread out instead of stacking on today's date.

**Final answer:** C. Rowkey: device_id Column data: date, data_point'''

E["test_7_q44"] = '''### Step 4: Choose the answer

- Monthly tables exported compressed to Cloud Storage give recoverable, low-cost backups so you can restore the affected month after a late-detected ETL error.
- It satisfies both: granular per-month recovery and minimized backup storage cost.

### Exam shortcut

If you see:
- errors undetected for weeks, need granular recovery + cheap backups
- monthly tables + compressed export to Cloud Storage
- restore an affected period

Think: **monthly tables + compressed export to Cloud Storage**

**Tiny mental image:** keep each month's data in its own zipped box so you can restore just the bad month.

**Final answer:** B. Organize your data in separate tables for each month, and export, compress, and store the data in Cloud Storage.'''

E["test_13_q3"] = '''### Step 4: Choose the answer

- A materialized view aggregating the base table with a filter on the last year's partitions always reflects the latest data, while cutting compute cost and maintenance versus a scheduled rebuild.
- It satisfies all: auto-fresh results, lower cost/duration, and no manual refresh job.

### Exam shortcut

If you see:
- repeated aggregations (AVG/MAX/SUM) over recent partitions, always current
- reduce cost/maintenance, no manual refresh
- materialized view with a partition filter

Think: **materialized view (filtered to recent partitions)**

**Tiny mental image:** an auto-updating precomputed summary scoped to the last year.

**Final answer:** A. Create a materialized view to aggregate the base table data. Include a filter clause to specify the last one year of partitions.'''

E["test_13_q10"] = '''### Step 4: Choose the answer

- Distributing worker nodes across multiple availability zones mitigates zone failures, giving the Dataproc cluster higher availability and fault tolerance.
- It satisfies the goal: resilience against a single zone outage.

### Exam shortcut

If you see:
- Dataproc high availability / fault tolerance
- survive a zone failure
- spread workers across zones

Think: **distribute workers across multiple zones**

**Tiny mental image:** don't put the whole crew in one building that might go dark.

**Final answer:** D. Distribute worker nodes across multiple availability zones to mitigate the risk of zone failures.'''

E["test_13_q31"] = '''### Step 4: Choose the answer

- Bigtable garbage collection is not immediate, so applying a timestamp range filter in the query excludes data older than 30 days with minimal cost and overhead.
- It satisfies the goal: hide stale rows at query time rather than running deletes or changing GC.

### Exam shortcut

If you see:
- Bigtable shows data past the GC window (GC isn't instant)
- exclude old data cheaply, no extra jobs
- timestamp range filter at query time

Think: **timestamp range filter in the query**

**Tiny mental image:** GC hasn't swept yet, so just ask only for the last 30 days.

**Final answer:** B. Use a timestamp range filter in the query to fetch the customer‘s data for a specific range.'''

E["test_13_q46"] = '''### Step 4: Choose the answer

- A BigQuery reservation at the project level applies dedicated slot capacity to the scan-intensive CDC process, giving predictable cost.
- It satisfies the goal: assign reserved slots to the project running the CDC, moving off variable on-demand pricing.

### Exam shortcut

If you see:
- predictable BigQuery cost for a heavy/scan-intensive workload
- reservations are assigned at project (or folder/org) level
- move off on-demand

Think: **BigQuery reservation assigned to the project**

**Tiny mental image:** buy a fixed slot allotment and pin it to the project doing the heavy scanning.

**Final answer:** D. Create a BigQuery reservation for the project.'''

E["test_13_q52"] = '''### Step 4: Choose the answer

- A reservation with a fixed 500-slot baseline and no autoscaling gives the marketing team steady, predictable monthly spend.
- It satisfies the goal: flat capacity-based cost with no variable autoscaling surprises.

### Exam shortcut

If you see:
- make BigQuery spend predictable/steady each month
- fixed baseline slots, autoscaling off
- capacity reservation, bill back

Think: **fixed-baseline reservation, no autoscaling**

**Tiny mental image:** rent a fixed block of slots so the bill is the same every month.

**Final answer:** C. Create a BigQuery reservation with a baseline of 500 slots with no autoscaling for the marketing team, and bill them back accordingly.'''

E["test_14_q24"] = '''### Step 4: Choose the answer

- Partitioning by create_date serves the recent-data filter, and clustering by location_id and device_version speeds the specific filtered queries.
- It satisfies both: date pruning plus clustering on the exact filter columns for cost and performance.

### Exam shortcut

If you see:
- recent-data (date) filter + filters on a few specific columns
- partition by date, cluster by the filter columns
- IoT/time-series in BigQuery

Think: **partition by date, cluster by the filter columns**

**Tiny mental image:** file by day, then sort within each day by location and device version.

**Final answer:** B. Partition table data by create_date, cluster table data by location_id, and device_version.'''

E["test_15_q14"] = '''### Step 4: Choose the answer

- Monthly tables exported compressed to Cloud Storage give recoverable, low-cost backups so you can restore the affected month after a late-detected ETL error.
- It satisfies both: granular per-month recovery and minimized backup storage cost.

### Exam shortcut

If you see:
- errors undetected for weeks, need granular recovery + cheap backups
- monthly tables + compressed export to Cloud Storage
- restore an affected period

Think: **monthly tables + compressed export to Cloud Storage**

**Tiny mental image:** keep each month's data in its own zipped box so you can restore just the bad month.

**Final answer:** B. Organize your data in separate tables for each month, and export, compress, and store the data in Cloud Storage.'''

E["test_15_q29"] = '''### Step 4: Choose the answer

- Raising the maximum worker count (and/or using a larger worker instance type) adds the compute the maxed-out n1-standard-1 workers lack.
- It satisfies the goal: more parallelism/compute to increase pipeline throughput.

### Exam shortcut

If you see:
- Dataflow pipeline underperforming, small/few workers
- scale out (more workers) or up (bigger workers)
- increase throughput

Think: **increase max workers (and/or larger worker type)**

**Tiny mental image:** add more lanes - or wider trucks - to clear the traffic.

**Final answer:** A. Increase the number of max workers'''

E["test_15_q32"] = '''### Step 4: Choose the answer

- Copying the data to a new table clustered on the package-tracking ID co-locates each package's records, speeding the geospatial lifecycle queries.
- It satisfies the goal: better performance via clustering on the queried entity.

### Exam shortcut

If you see:
- partitioned table slowing over time, queries by a high-cardinality ID
- improve performance with clustering
- cluster on the queried entity

Think: **cluster on the package-tracking ID**

**Tiny mental image:** group each package's events so its lifecycle query reads one tight block.

**Final answer:** B. Implement clustering in BigQuery on the package-tracking ID column.'''

E["test_2_q31"] = '''### Step 4: Choose the answer

- Setting the dataproc:dataproc.scheduler.max-concurrent-jobs cluster property at cluster creation caps the number of concurrent jobs.
- It satisfies the goal: bound concurrency via the correct cluster property at creation time.

### Exam shortcut

If you see:
- limit concurrent jobs on a Dataproc cluster
- cluster property dataproc:dataproc.scheduler.max-concurrent-jobs
- set at cluster creation

Think: **dataproc:dataproc.scheduler.max-concurrent-jobs at create**

**Tiny mental image:** set the "max jobs at once" dial when you build the cluster.

**Final answer:** B. Set dataproc:dataproc.scheduler.max-concurrent-jobs property when creating a cluster.'''

E["test_3_q40"] = '''### Step 4: Choose the answer

- Cloud Build with Terraform provisions the specialized GKE infrastructure (GPUs, local SSDs, 8 Gbps) and launches containers with the latest registry configs in a managed, repeatable way.
- It satisfies both: declarative infrastructure provisioning and CI/CD container deployment.

### Exam shortcut

If you see:
- provision specialized GKE infra + deploy latest container configs
- managed, repeatable deployment process
- Cloud Build + Terraform (IaC)

Think: **Cloud Build + Terraform (IaC + CI/CD)**

**Tiny mental image:** code-defined infrastructure plus an automated build that ships the newest images.

**Final answer:** B. Use Cloud Build with Terraform build to provision the infrastructure and launch containers with the latest available configurations from the container registry'''

E["test_3_q45"] = '''### Step 4: Choose the answer

- Automating the 10 intents that cover 70% of requests frees live agents to handle the complex 30%, maximizing impact quickly.
- It satisfies the goal: automate the high-volume, simple intents first for the biggest deflection.

### Exam shortcut

If you see:
- which chatbot intents to automate first
- a small set of intents covers most volume
- automate the high-frequency simple ones first

Think: **automate the few intents covering most requests first**

**Tiny mental image:** knock out the common questions so humans focus on the hard ones.

**Final answer:** A. Automate the 10 intents that cover 70% of the requests so that live agents can handle more complicated requests'''

E["test_4_q6"] = '''### Step 4: Choose the answer

- Cloud Composer (managed Airflow) orchestrates the interdependent Dataproc and Dataflow jobs as a daily DAG.
- It satisfies the goal: managed, dependency-aware scheduling of a complex multi-job pipeline.

### Exam shortcut

If you see:
- automate a multi-job pipeline with interdependencies, daily
- managed orchestration (Dataproc + Dataflow steps)
- DAG, not just a scheduler

Think: **Cloud Composer (Airflow DAG)**

**Tiny mental image:** a conductor running the daily score of dependent jobs in order.

**Final answer:** B. Cloud Composer'''

E["test_4_q14"] = '''### Step 4: Choose the answer

- Exporting the Dataprep job as a Dataflow template and running it from a Cloud Composer DAG lets you reuse the recipe daily after the variable-time load completes.
- It satisfies both: reusable templated execution and dependency on the upstream load finishing.

### Exam shortcut

If you see:
- reuse a Dataprep recipe daily, after a variable-time upstream job
- need dependency-aware orchestration (not a fixed cron)
- Dataprep → Dataflow template → Composer

Think: **Dataprep → Dataflow template, run via Cloud Composer**

**Tiny mental image:** turn the recipe into a reusable template and let the orchestrator run it once the load finishes.

**Final answer:** D. Export the Dataprep job as a Dataflow template, and incorporate it into a Cloud Composer job.'''

E["test_4_q31"] = '''### Step 4: Choose the answer

- Exporting Cloud Logging data daily to BigQuery and building views filtered by project, log type, resource, and user produces the daily consumption-and-user reports efficiently.
- It satisfies the goal: SQL-queryable, filterable daily reports from the usage logs.

### Exam shortcut

If you see:
- daily reports on resource consumption + who used them
- source is Cloud Logging / audit logs
- export to BigQuery and build views

Think: **Cloud Logging → BigQuery export + filtered views**

**Tiny mental image:** pour the logs into the warehouse each day and slice them with saved views.

**Final answer:** A. Export Cloud Logging data to BigQuery daily and create views that filter by project, log type, resource, and user'''

E["test_6_q49"] = '''### Step 4: Choose the answer

- Exporting the Dataprep job as a Dataflow template and running it from a Cloud Composer DAG reuses the recipe daily after the variable-time load completes.
- It satisfies both: reusable templated execution and dependency on the upstream load finishing.

### Exam shortcut

If you see:
- reuse a Dataprep recipe daily, after a variable-time upstream job
- dependency-aware orchestration (not a fixed cron)
- Dataprep → Dataflow template → Composer

Think: **Dataprep → Dataflow template, run via Cloud Composer**

**Tiny mental image:** turn the recipe into a reusable template and let the orchestrator run it once the load finishes.

**Final answer:** D. Export the Cloud Dataprep job as a Cloud Dataflow template, and incorporate it into a Cloud Composer job.'''

E["test_6_q51"] = '''### Step 4: Choose the answer

- Cloud Composer (managed Airflow) orchestrates the interdependent Dataproc and Dataflow jobs as a daily DAG.
- It satisfies the goal: managed, dependency-aware scheduling of a multi-step pipeline.

### Exam shortcut

If you see:
- automate a multi-job pipeline with interdependencies, daily
- managed orchestration (Dataproc + Dataflow)
- DAG, not just a scheduler

Think: **Cloud Composer (Airflow DAG)**

**Tiny mental image:** a conductor running the daily score of dependent jobs in order.

**Final answer:** B. Cloud Composer'''

E["test_14_q44"] = '''### Step 4: Choose the answer

- Enabling the Airflow REST API, having Cloud Storage notifications trigger a Cloud Function that calls the DAG via the Airflow REST API and web server URL (over VPC Serverless Access), triggers the DAG reactively without internet.
- It satisfies the goal: event-driven DAG runs on file arrival within a no-internet Composer 2 subnetwork.

### Exam shortcut

If you see:
- trigger a Composer DAG on new GCS file (event-driven, not scheduled)
- no internet access on the subnetwork
- GCS notification → Cloud Function → Airflow REST API

Think: **GCS notification → Cloud Function → Airflow REST API (via private access)**

**Tiny mental image:** each new file pings a function that quietly tells Airflow to run the DAG.

**Final answer:** D. 1. Enable the Airflow REST API, and set up Cloud Storage notifications to trigger a Cloud Function instance. 2. Write a Cloud Function instance to call the DAG by using the Airflow REST API and the web server URL. 3. Use VPC Serverless Access to reach the web server URL.'''

E["test_15_q21"] = '''### Step 4: Choose the answer

- A Cloud Composer DAG models the mix of sequential and concurrent Spark jobs as task dependencies and automates the scheduled run.
- It satisfies the goal: orchestrate complex inter-job ordering, not just submit jobs.

### Exam shortcut

If you see:
- jobs with mixed sequential + concurrent dependencies, scheduled
- automate a multi-job workflow
- orchestration across steps

Think: **Cloud Composer DAG**

**Tiny mental image:** a dependency graph the conductor follows, some jobs in series, others in parallel.

**Final answer:** C. Create a Directed Acyclic Graph in Cloud Composer'''

E["test_15_q31"] = '''### Step 4: Choose the answer

- Automating the 10 intents that cover 70% of requests frees live agents for the complex 30%, delivering the most value fastest.
- It satisfies the goal: automate the high-volume, simple intents first.

### Exam shortcut

If you see:
- which chatbot intents to automate first
- a small set of intents covers most volume
- automate the high-frequency simple ones first

Think: **automate the few intents covering most requests first**

**Tiny mental image:** knock out the common questions so humans focus on the hard ones.

**Final answer:** A. Automate the 10 intents that cover 70% of the requests so that live agents can handle more complicated requests.'''

append_entries(E)

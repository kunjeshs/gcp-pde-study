from lib import append_entries

E = {}

E["test_13_q57"] = '''### Step 4: Choose the answer

- Datastream replicates the needed Cloud SQL tables into BigQuery, so the 100-300 daily campaign queries run entirely in BigQuery and barely touch the source databases.
- It satisfies both: high query concurrency in BigQuery and minimal load on the Cloud SQL instances.

### Exam shortcut

If you see:
- join operational DB data with warehouse data, many heavy queries
- minimize load on the source OLTP databases
- avoid hammering Cloud SQL with federated queries

Think: **Datastream CDC replication into BigQuery**

**Tiny mental image:** copy the live ledgers into the analytics room so analysts never crowd the busy front desk.

**Final answer:** C. Create streams in Datastream to replicate the required tables from both Cloud SQL databases to BigQuery for these queries.'''

E["test_13_q59"] = '''### Step 4: Choose the answer

- With the Interconnect already in place, a Dataflow pipeline can read directly from the on-prem Kafka and write to BigQuery with minimal latency.
- It satisfies the goal: high-throughput streaming straight from Kafka, no Pub/Sub bridge adding hops.

### Exam shortcut

If you see:
- on-prem Kafka reachable via Interconnect, stream to BigQuery
- minimal latency, high throughput
- avoid extra bridging components

Think: **Dataflow reads Kafka directly → BigQuery**

**Tiny mental image:** the private highway is already built - drive straight through instead of transferring at a depot.

**Final answer:** C. Use Dataflow, write a pipeline that reads the data from Kafka, and writes the data to BigQuery.'''

E["test_14_q4"] = '''### Step 4: Choose the answer

- A dual-region bucket with turbo replication guarantees RPO=15 minutes, and seeking the subscription back plus restarting Dataflow in the secondary region recovers from the outage.
- It satisfies the target: 15-minute RPO via turbo replication and a clean cross-region failover.

### Exam shortcut

If you see:
- survive a regional outage with RPO ~15 minutes
- Cloud Storage durability + Pub/Sub replay
- turbo replication is the 15-min lever

Think: **dual-region bucket + turbo replication, seek + restart in secondary region**

**Tiny mental image:** a synced twin warehouse with express replication, and a replay button to recover the last few minutes.

**Final answer:** D. 1. Use a dual-region Cloud Storage bucket with turbo replication enabled. 2. Monitor Dataflow metrics with Cloud Monitoring to determine when an outage occurs. 3. Seek the subscription back in time by 60 minutes to recover the acknowledged messages. 4. Start the Dataflow job in a secondary region.'''

E["test_14_q8"] = '''### Step 4: Choose the answer

- Cloud Data Fusion provides a managed, visual ETL flow to cleanse and transform the messy CSVs before they land in BigQuery.
- It satisfies the goal: enforce data quality with built-in transformations rather than loading dirty data first.

### Exam shortcut

If you see:
- cleanse/transform messy files before BigQuery
- managed, visual data integration with quality steps
- type/format fixes pre-load

Think: **Cloud Data Fusion (transform before load)**

**Tiny mental image:** run the ingredients through a wash-and-prep station before the kitchen.

**Final answer:** A. Use Data Fusion to transform the data before loading it into BigQuery.'''

E["test_14_q11"] = '''### Step 4: Choose the answer

- A custom Apache Beam connector in a Dataflow pipeline reads the proprietary flight format and streams it into BigQuery as Avro, efficiently.
- It satisfies both: handle the non-standard format and stream it compactly into BigQuery with minimal resources.

### Exam shortcut

If you see:
- ingest a proprietary/unsupported format, stream into BigQuery
- minimal resource consumption
- custom parsing needed

Think: **custom Beam connector + Dataflow streaming (Avro into BigQuery)**

**Tiny mental image:** build a custom adapter so the odd-shaped feed plugs straight into the warehouse line.

**Final answer:** D. Use an Apache Beam custom connector to write a Dataflow pipeline that streams the data into BigQuery in Avro format.'''

E["test_14_q21"] = '''### Step 4: Choose the answer

- Routing vendor data through Pub/Sub and a Dataflow job that sanitizes invalid values before streaming into BigQuery keeps the ML data clean.
- It satisfies both: scalable near-real-time ingestion plus validation of dirty multi-vendor input.

### Exam shortcut

If you see:
- near-real-time ingest from multiple sources with invalid values
- must clean/validate before BigQuery
- feed BigQuery ML / a serving endpoint

Think: **Pub/Sub → Dataflow (sanitize) → BigQuery**

**Tiny mental image:** run the incoming produce through a wash-and-sort line before the shelves.

**Final answer:** D. Create a Pub/Sub topic and send all vendor data to it. Use Dataflow to process and sanitize the Pub/Sub data and stream it to BigQuery.'''

E["test_14_q29"] = '''### Step 4: Choose the answer

- A per-table Composer DAG (Dataproc + BigQuery operators) launched by a Cloud Storage object trigger via a Cloud Function reacts to unpredictable uploads and scales to hundreds of tables.
- It satisfies the goal: event-driven freshness, per-table isolation, and reliable sequential orchestration.

### Exam shortcut

If you see:
- files arrive unpredictably, then sequential Dataproc → BigQuery steps
- hundreds of tables, freshest data, reliable
- event-triggered orchestration

Think: **Composer DAG per table, triggered by a GCS object event (Cloud Function)**

**Tiny mental image:** each shipment trips its own assembly line the moment it lands on the dock.

**Final answer:** D. 1. Create an Apache Airflow directed acyclic graph (DAG) in Cloud Composer with sequential tasks by using the Dataproc and BigQuery operators. 2. Create a separate DAG for each table that needs to go through the pipeline. 3. Use a Cloud Storage object trigger to launch a Cloud Function that triggers the DAG.'''

E["test_14_q30"] = '''### Step 4: Choose the answer

- Taking a Pub/Sub snapshot two days before deployment (and seeking to a timestamp) lets the updated pipeline replay the last two days of messages.
- It satisfies the goal: a recovery point that re-delivers historical messages to the new pipeline.

### Exam shortcut

If you see:
- reprocess Pub/Sub messages from the last N days after an update
- need a replay point / time-based rewind
- snapshot + Seek

Think: **Pub/Sub snapshot (before) + Seek to timestamp**

**Tiny mental image:** bookmark the stream two days back so you can rewind and replay from there.

**Final answer:** B. Use Pub/Sub Snapshot capture two days before the deployment.'''

E["test_14_q31"] = '''### Step 4: Choose the answer

- Cloud Data Fusion offers a GUI-based pipeline to land Parquet/CSV files into Cloud Storage as the object sink while using your own encryption keys.
- It satisfies the goal: a visual, no-code integration tool writing to a Cloud Storage sink with CMEK.

### Exam shortcut

If you see:
- move mixed-format files into a Cloud Storage sink
- GUI/visual, no-code
- use your own (CMEK) encryption keys

Think: **Cloud Data Fusion (visual pipeline)**

**Tiny mental image:** drag-and-drop the files into the encrypted bucket via a visual designer.

**Final answer:** B. Use Cloud Data Fusion to move files into Cloud Storage.'''

E["test_14_q36"] = '''### Step 4: Choose the answer

- A view with a filter dropping rows under 8 vCPU (using UNNEST for the nested fields) excludes them at query time with no extra storage cost.
- It satisfies the goal: cost-effective, repeatable reporting via a logical view rather than a materialized copy.

### Exam shortcut

If you see:
- exclude/filter rows for recurring reports, cost-effective
- no extra storage, logic applied at query time
- nested/repeated fields need flattening

Think: **a filtered view (UNNEST the nested fields)**

**Tiny mental image:** a saved filtered lens over the table - it stores nothing, just shows the rows you want.

**Final answer:** A. Create a view with a filter to drop rows with fewer than 8 vCPU, and use the UNNEST operator.'''

E["test_14_q41"] = '''### Step 4: Choose the answer

- Enabling Private Google Access on the subnet lets internal-IP-only Dataflow workers reach Cloud Storage and BigQuery, satisfying the no-external-IP policy.
- It satisfies both: compliance with internal-only IPs and continued access to Google APIs.

### Exam shortcut

If you see:
- workers/VMs must use internal IPs only (no external)
- still need to reach Google APIs (GCS, BigQuery)
- org policy bans external IPs

Think: **Private Google Access on the subnet**

**Tiny mental image:** a private side door to Google's services so the no-public-address rule still holds.

**Final answer:** D. Ensure that Private Google Access is enabled in the subnetwork. Use Dataflow with only internal IP addresses.'''

E["test_14_q42"] = '''### Step 4: Choose the answer

- The CSV-read transform is fused with the read, capping parallelism; inserting a Reshuffle breaks the fusion so the autoscaler can distribute work across more workers.
- It satisfies the fix: prevent fusion so the per-line output parallelizes and scaling kicks in.

### Exam shortcut

If you see:
- Dataflow autoscaler stuck at low worker count despite low performance
- one transform fanning out many elements (e.g., per CSV line)
- fusion limiting parallelism

Think: **add a Reshuffle to break fusion**

**Tiny mental image:** the work is glued into one lump - shuffle it into pieces so many workers can grab parts.

**Final answer:** B. Change the pipeline code, and introduce a Reshuffle step to prevent fusion.'''

E["test_14_q43"] = '''### Step 4: Choose the answer

- Datastream from Oracle to BigQuery with private connectivity to the VPC continuously replicates the 50 tables with no infrastructure to manage.
- It satisfies the goal: serverless CDC replication straight into BigQuery over private networking.

### Exam shortcut

If you see:
- continuously replicate an OLTP database (Oracle/MySQL/Postgres) to BigQuery
- minimize/avoid managing infrastructure
- private connectivity to a VPC

Think: **Datastream (serverless CDC) → BigQuery**

**Tiny mental image:** a managed pipe that keeps the warehouse mirror in sync with the live database automatically.

**Final answer:** D. Create a Datastream service from Oracle to BigQuery, use a private connectivity configuration to the same VPC network, and a connection profile to BigQuery.'''

E["test_14_q53"] = '''### Step 4: Choose the answer

- Migrating Hadoop to Dataproc with Cloud Storage for HDFS use cases, and orchestrating with Cloud Composer (managed Airflow), reuses existing pipelines with minimal change.
- It satisfies the goal: a near lift-and-shift that keeps the Airflow orchestration the team already runs.

### Exam shortcut

If you see:
- migrate Hadoop + existing Airflow orchestration, minimal change
- Cloud Storage for HDFS use cases
- keep the orchestration tool

Think: **Dataproc + Cloud Storage + Cloud Composer (managed Airflow)**

**Tiny mental image:** move the same machines and the same conductor into the new managed building.

**Final answer:** B. Use Dataproc to migrate Hadoop clusters to Google Cloud, and Cloud Storage to handle any HDFS use cases. Orchestrate your pipelines with Cloud Composer.'''

E["test_14_q59"] = '''### Step 4: Choose the answer

- A Dataflow pipeline written with the Beam Python SDK can branch into streaming or batch and call Cloud DLP to de-identify before writing to the BigQuery sink, all programmatically and cost-effectively.
- It satisfies all: code-driven flexibility for stream/batch, in-pipeline DLP obfuscation, and a single BigQuery destination.

### Exam shortcut

If you see:
- programmatic pipeline, choose streaming OR batch
- de-identify sensitive data in-flight, minimize cost
- land in BigQuery

Think: **Dataflow (Beam SDK) + Cloud DLP → BigQuery**

**Tiny mental image:** one coded pipeline that can run fast or in bulk, scrubbing secrets on the way into the warehouse.

**Final answer:** C. Create your pipeline with Dataflow through the Apache Beam SDK for Python, customizing separate options within your code for streaming, batch processing, and Cloud DLP. Select BigQuery as your data sink.'''

E["test_15_q2"] = '''### Step 4: Choose the answer

- Cloud Composer (managed Airflow) orchestrates a complex pipeline that spans services across cloud providers.
- It satisfies the goal: a workflow orchestrator for hybrid/multi-cloud steps, not a single-engine processor.

### Exam shortcut

If you see:
- orchestrate a complex pipeline across clouds/providers
- coordinate many heterogeneous steps
- orchestration, not data processing

Think: **Cloud Composer (Airflow)**

**Tiny mental image:** a conductor cueing players from several different orchestras to play in sync.

**Final answer:** B. Cloud Composer'''

E["test_15_q5"] = '''### Step 4: Choose the answer

- Cloud Pub/Sub ingest plus Cloud Dataflow streaming autoscales, guarantees at-least-once delivery, and supports ordered 1-hour windowed processing.
- It satisfies every requirement with fully managed, serverless components.

### Exam shortcut

If you see:
- autoscaling pipeline, at-least-once, windowed/ordered processing
- managed streaming ingest + analysis
- no clusters to run

Think: **Pub/Sub + Dataflow**

**Tiny mental image:** a self-sizing intake plus a self-sizing mill that never drops a package.

**Final answer:** D. Use Cloud Pub/Sub for message ingestion and Cloud Dataflow for streaming analysis.'''

E["test_15_q8"] = '''### Step 4: Choose the answer

- A healthy pipeline drains the source and fills the sink; alert on an increase in undelivered Pub/Sub messages and a decrease in the destination's used_bytes growth.
- It satisfies the goal: both signals flag that the pipeline has stopped processing.

### Exam shortcut

If you see:
- confirm a Dataflow streaming pipeline is "still processing"
- watch source backlog and sink growth
- which direction signals trouble

Think: **alert on rising source backlog + falling sink write rate**

**Tiny mental image:** worry when the inbox piles up *and* the outbox stops filling.

**Final answer:** B. An alert based on an increase of subscription/num_undelivered_messages for the source and a rate of change decrease of instance/storage/ used_bytes for the destination'''

E["test_15_q18"] = '''### Step 4: Choose the answer

- Pub/Sub delivers the real-time stream, Cloud Storage holds batch historical exports, and BigQuery serves ANSI SQL over real-time and historical data.
- It satisfies all three consumer access patterns with one managed stack.

### Exam shortcut

If you see:
- real-time stream + ANSI SQL (live + historical) + batch exports
- one platform covering all three
- market/event data feeds

Think: **Pub/Sub + Cloud Storage + BigQuery**

**Tiny mental image:** a live ticker, an archive room, and a SQL search desk from one feed.

**Final answer:** B. Cloud Pub/Sub, Cloud Storage, BigQuery'''

E["test_15_q19"] = '''### Step 4: Choose the answer

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

append_entries(E)

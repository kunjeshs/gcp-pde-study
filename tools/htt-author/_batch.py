from lib import append_entries

E = {}

E["test_4_q2"] = '''### Step 4: Choose the answer

- Having the devices publish directly to Cloud Pub/Sub replaces the unreliable leased lines with a global, durable, managed ingestion service.
- It satisfies the goal: reliable event delivery and predictable behavior, cost-effectively, with no self-run buffers.

### Exam shortcut

If you see:
- unreliable links between collection and processing, lost events
- want reliable global event delivery, cost-effective
- replace self-managed buffering (Kafka) or expensive Interconnect

Think: **publish directly to Cloud Pub/Sub**

**Tiny mental image:** drop letters in the global postal system instead of trusting a flaky private courier line.

**Final answer:** B. Configure the data acquisition devices to publish data to Cloud Pub/Sub.'''

E["test_4_q3"] = '''### Step 4: Choose the answer

- Partitioning the table by a DATE/TIMESTAMP column lets date-filtered queries prune to only the relevant partitions instead of scanning everything.
- It satisfies the goal: far less data scanned (lower cost) while keeping full SQL access.

### Exam shortcut

If you see:
- date-filtered BigQuery queries scanning the whole table
- rising bytes-scanned cost
- keep SQL, cut scan volume

Think: **partition the table by DATE/TIMESTAMP**

**Tiny mental image:** file records by month so you only open the months you asked for, not the whole cabinet.

**Final answer:** A. Use DDL to recreate the tables and partition them by a column containing a TIMESTAMP or DATE type'''

E["test_4_q4"] = '''### Step 4: Choose the answer

- A ParDo that inspects each element and drops the corrupt ones cleanly filters out the 2% bad data inline.
- It satisfies the goal: per-element validation/filtering, the natural Beam transform for discarding records.

### Exam shortcut

If you see:
- filter/drop bad records in a Dataflow stream
- per-element validation
- discard, not split or join

Think: **ParDo (filter out corrupt elements)**

**Tiny mental image:** an inspector on the belt who tosses the defective items into the bin.

**Final answer:** B. Add a ParDo transform within the Cloud Dataflow to discard corrupt elements.'''

E["test_4_q8"] = '''### Step 4: Choose the answer

- Coalescing the small 200-400 MB parquet files to at least 1 GB reduces task/shuffle overhead and improves the Spark job's throughput cost-effectively.
- It satisfies the goal: fewer, larger splits cut scheduling and I/O overhead without new hardware spend.

### Exam shortcut

If you see:
- Spark job slow with many small input files
- shuffle-heavy, cost-sensitive, on Dataproc + Cloud Storage
- file-size tuning

Think: **increase input file size (≈1 GB+) to reduce overhead**

**Tiny mental image:** ship a few full pallets instead of thousands of tiny packages.

**Final answer:** A. Ensure that the parquet files are at least 1 GB in size.'''

E["test_4_q15"] = '''### Step 4: Choose the answer

- Cloud Data Fusion provides a managed, visual ETL flow to cleanse and transform the messy CSVs before they land in BigQuery.
- It satisfies the goal: enforce data quality with built-in transformations rather than loading dirty data first.

### Exam shortcut

If you see:
- cleanse/transform messy files before BigQuery
- managed, visual data integration with quality steps
- type/format fixes pre-load

Think: **Cloud Data Fusion (transform before load)**

**Tiny mental image:** run the ingredients through a wash-and-prep station before they hit the kitchen.

**Final answer:** A. Use Data Fusion to transform the data before loading it into BigQuery'''

E["test_4_q23"] = '''### Step 4: Choose the answer

- Hashing each table's non-timestamp columns after sorting (via Dataproc and the BigQuery connector) lets you compare outputs deterministically without a join key.
- It satisfies the goal: a key-free, order-independent equality check between the original and migrated results.

### Exam shortcut

If you see:
- compare two tables that have no primary/join key
- verify migrated output equals original
- order-independent, exclude volatile (timestamp) columns

Think: **sort + hash the rows and compare hashes**

**Tiny mental image:** take a fingerprint of each deck after sorting - identical fingerprints mean identical decks.

**Final answer:** C. Use a Dataproc cluster and the BigQuery Hadoop connector to read the data from each table and calculate a hash from non-timestamp columns of the table after sorting. Compare the hashes of each table.'''

E["test_4_q24"] = '''### Step 4: Choose the answer

- gsutil rsync runs outbound from the on-prem servers to Cloud Storage, so no external IP needs to reach into the data center, and it syncs daily deltas.
- It satisfies both: secure (outbound-only) transfer and ongoing incremental sync after the initial upload.

### Exam shortcut

If you see:
- no inbound access to on-prem (no external IPs reaching in)
- initial upload + recurring daily deltas to Cloud Storage
- simple, secure sync

Think: **gsutil rsync (outbound from on-prem)**

**Tiny mental image:** the building mails out its updates; nobody from outside gets a key to come in.

**Final answer:** A. Use “gsutil rsync“ command to sync the on-premises servers with Cloud Storage'''

E["test_4_q25"] = '''### Step 4: Choose the answer

- A try/catch in the DoFn routing bad rows via a side output into a dead-letter PCollection (stored to Pub/Sub) makes the pipeline resilient and lets you reprocess all failures.
- It satisfies both: the job no longer crashes on bad input, and every failed record is captured for replay.

### Exam shortcut

If you see:
- Dataflow failing on bad input, need reliability + reprocessing
- capture errors without dropping the pipeline
- dead-letter pattern

Think: **try/catch in DoFn + side output (dead-letter) to Pub/Sub**

**Tiny mental image:** set bad parts aside on a "rework" tray instead of letting one jam the whole line.

**Final answer:** D. Include a try...catch block in your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to Pub/Sub later'''

E["test_4_q27"] = '''### Step 4: Choose the answer

- Managed export of Datastore to a Nearline/Coldline Cloud Storage bucket creates archivable, point-in-time snapshots cheaply (and streaming exports to partitioned BigQuery is the other valid path).
- It satisfies the goal: periodic snapshots for recovery/cloning, retained long-term at low cost.

### Exam shortcut

If you see:
- periodic snapshots of Datastore for PITR/cloning
- archive long-term, cost-effective
- managed export

Think: **Datastore managed export → Cloud Storage Nearline/Coldline**

**Tiny mental image:** take a dated photo of the database and file it in cheap deep storage.

**Final answer:** A. Use managed export to export the data from Cloud Datastore and store it in a Cloud Storage bucket with Nearline or Coldline storage class'''

E["test_4_q28"] = '''### Step 4: Choose the answer

- Mirroring the on-prem Kafka topics to a Kafka cluster on GCE (no Kafka Connect plugins), then reading with Dataproc/Dataflow to write to GCS/BigQuery, replicates the log data.
- It satisfies the constraint: native Kafka mirroring avoids the prohibited Connect plugins.

### Exam shortcut

If you see:
- replicate on-prem Kafka to GCP, no Kafka Connect plugins allowed
- land in Cloud Storage / BigQuery
- mirror topics natively

Think: **mirror Kafka topics to a GCE Kafka cluster, then Dataflow/Dataproc → GCS**

**Tiny mental image:** echo the broadcast to a sister station, then record it there for the archive.

**Final answer:** A. Set up a Kafka cluster on GCE VM instances and configure the on-prem cluster to mirror the topics to the GCE cluster. Then use either a Dataproc cluster or Dataflow job to read from Kafka and write to GCS.'''

E["test_4_q36"] = '''### Step 4: Choose the answer

- A Cloud Dataflow streaming pipeline inserts the per-minute readings into BigQuery within seconds and scales as the sensor fleet grows.
- It satisfies both: sub-minute availability for real-time aggregation and elastic scaling beyond batch loads.

### Exam shortcut

If you see:
- high-cardinality sensor data, available within ~1 minute
- real-time aggregation, expecting big growth
- continuous insert into BigQuery

Think: **streaming Dataflow → BigQuery (not periodic bq load/INSERT)**

**Tiny mental image:** a live conveyor feeding the warehouse continuously, not hourly truck drops.

**Final answer:** B. Stream sensor data into the BigQuery table using a Cloud Dataflow pipeline'''

E["test_4_q38"] = '''### Step 4: Choose the answer

- Cloud Dataprep lets you build visual recipes to detect invalid entries and transform the Cloud Storage data with no code or SQL.
- It satisfies the constraint: interactive, no-programming data cleaning and transformation.

### Exam shortcut

If you see:
- clean/transform data with no programming or SQL
- visual recipes, interactive profiling
- analysts/non-engineers doing the prep

Think: **Cloud Dataprep**

**Tiny mental image:** a spreadsheet-style wizard that fixes the data by clicking, not coding.

**Final answer:** B. Utilize Cloud Dataprep with recipes for error detection and data transformations'''

E["test_4_q41"] = '''### Step 4: Choose the answer

- A streaming job using PubSubIO and BigQueryIO, with the small reference data held in memory as a side input, enriches each event and writes results to BigQuery.
- It satisfies the design: in-memory reference join via side input on an unbounded stream.

### Exam shortcut

If you see:
- enrich a Pub/Sub stream with small static reference data
- reference fits in memory on a worker
- write enriched results to BigQuery

Think: **streaming job: PubSubIO + BigQueryIO, reference as a side input**

**Tiny mental image:** the line worker keeps a small lookup card in hand to stamp each passing item.

**Final answer:** C. A streaming job that utilizes PubSubIO to stream data from Cloud Pub/Sub, and BigQueryIO to enrich the data with the reference data from BigQuery. Side-inputs are used to store the reference data in memory on a single worker, and the enriched data is written to BigQuery for analysis'''

E["test_4_q45"] = '''### Step 4: Choose the answer

- Pub/Sub delivers the real-time event streams, Cloud Storage holds batch historical exports, and BigQuery serves ANSI SQL over real-time and historical data.
- It satisfies all three consumer needs with one cohesive, managed stack.

### Exam shortcut

If you see:
- real-time streams + ANSI SQL (live + historical) + batch exports
- one platform covering all three
- market/event data

Think: **Pub/Sub + Cloud Storage + BigQuery**

**Tiny mental image:** a live ticker, an archive room, and a SQL search desk all fed from the same feed.

**Final answer:** B. Cloud Pub/Sub, Cloud Storage, BigQuery'''

E["test_4_q51"] = '''### Step 4: Choose the answer

- A multi-regional Cloud Storage bucket maximizes availability and is directly accessible by Dataproc, BigQuery, and Compute Engine for any file format.
- It satisfies the goal: a single highly-available store for CSV/Avro/PDF that all tools can read, with performance not a concern.

### Exam shortcut

If you see:
- one store shared by Dataproc + BigQuery + Compute Engine
- mixed formats (CSV/Avro/PDF), maximize availability
- performance not the priority

Think: **multi-regional Cloud Storage bucket**

**Tiny mental image:** one highly-available warehouse every department can walk into, holding boxes of any shape.

**Final answer:** D. Store the data in a multi-regional Cloud Storage bucket and directly access it using Dataproc, BigQuery, and Compute Engine'''

E["test_4_q52"] = '''### Step 4: Choose the answer

- An IoT gateway feeding Cloud Pub/Sub, processed by Cloud Dataflow, absorbs global spikes elastically and replaces the costly single on-prem Kafka cluster.
- It satisfies the goal: managed, globally scalable ingest and processing that handles bursty batched traffic.

### Exam shortcut

If you see:
- global IoT ingest, spiky/batched volume, self-managed Kafka too costly
- need elastic managed ingest + processing
- replace single-region cluster

Think: **IoT gateway → Pub/Sub → Dataflow**

**Tiny mental image:** swap the one overworked depot for a global mail network that scales with the surge.

**Final answer:** C. Connect an IoT gateway to Cloud Pub/Sub and use Cloud Dataflow to process the messages.'''

E["test_4_q54"] = '''### Step 4: Choose the answer

- Cloud Pub/Sub ingest plus Cloud Dataflow streaming processing autoscales, guarantees at-least-once delivery, and supports ordered 1-hour windowed processing.
- It satisfies every requirement with fully managed, serverless components.

### Exam shortcut

If you see:
- autoscaling pipeline, at-least-once, windowed/ordered processing
- managed streaming ingest + analysis
- no clusters to run

Think: **Pub/Sub + Dataflow**

**Tiny mental image:** a self-sizing intake plus a self-sizing mill that never drops a package.

**Final answer:** D. Use Cloud Pub/Sub for message ingestion and Cloud Dataflow for streaming analysis'''

E["test_4_q57"] = '''### Step 4: Choose the answer

- Cloud Composer (managed Airflow) orchestrates complex, cross-cloud pipelines, coordinating tasks across providers and services.
- It satisfies the goal: a workflow orchestrator that spans hybrid/multi-cloud steps, not a single-engine processor.

### Exam shortcut

If you see:
- orchestrate a complex pipeline across clouds/providers
- coordinate many heterogeneous steps
- orchestration, not data processing

Think: **Cloud Composer (Airflow)**

**Tiny mental image:** a conductor cueing musicians from several different orchestras to play in sync.

**Final answer:** B. Cloud Composer'''

E["test_5_q2"] = '''### Step 4: Choose the answer

- A streaming job with PubSubIO and BigQueryIO, holding the small reference data in memory as a side input, enriches each event and writes to BigQuery.
- It satisfies the design: in-memory reference join via side input on an unbounded stream.

### Exam shortcut

If you see:
- enrich a Pub/Sub stream with small static BigQuery reference
- reference fits in memory
- write enriched results to BigQuery

Think: **streaming: PubSubIO + BigQueryIO, reference as side input**

**Tiny mental image:** the worker keeps a small lookup card in hand to stamp each item.

**Final answer:** C. Streaming job, PubSubIO, BigQueryIO, side-inputs'''

E["test_5_q4"] = '''### Step 4: Choose the answer

- By default, Dataflow places unbounded data into a single global window until you apply your own windowing.
- It satisfies the question: the default behavior is one global window, not time- or size-based windows.

### Exam shortcut

If you see:
- "default windowing for unbounded data in Dataflow"
- what happens before you set a window
- global vs time/size windows

Think: **single global window (default)**

**Tiny mental image:** until you draw the dividing lines, everything lands in one big bucket.

**Final answer:** B. Single, Global Window'''

append_entries(E)

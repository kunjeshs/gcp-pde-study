from lib import append_entries

E = {}

E["test_6_q19"] = '''### Step 4: Choose the answer

- Cloud Dataprep lets you build visual recipes to detect invalid entries and transform the Cloud Storage data with no code or SQL.
- It satisfies the constraint: interactive, no-programming data cleaning and transformation.

### Exam shortcut

If you see:
- clean/transform data with no programming or SQL
- visual recipes, interactive profiling
- analysts doing the prep

Think: **Cloud Dataprep**

**Tiny mental image:** a click-driven wizard that fixes the data without writing code.

**Final answer:** B. Use Cloud Dataprep with recipes to detect errors and perform transformations.'''

E["test_6_q24"] = '''### Step 4: Choose the answer

- Mounting the nightly mysqldump backups into Cloud SQL and processing with Dataproc runs analytics off the backups, not the live cluster.
- It satisfies the goal: analytics with minimal impact on the production databases.

### Exam shortcut

If you see:
- analytics must not load the production OLTP database
- nightly backups/dumps already exist
- process a copy, not the source

Think: **load the backups elsewhere and analyze the copy**

**Tiny mental image:** study last night's photocopy so you never disturb the busy original ledger.

**Final answer:** D. Mount the backups to Google Cloud SQL, and then process the data using Google Cloud Dataproc.'''

E["test_6_q29"] = '''### Step 4: Choose the answer

- A Dataflow job with KafkaIO and a sliding 1-hour window advancing every 5 minutes computes the moving average and alerts when it drops below 4000/sec.
- It satisfies the goal: a continuously updated trailing-hour average that a fixed window can't provide.

### Exam shortcut

If you see:
- alert on a moving/rolling average over a trailing hour
- frequently re-evaluated
- stream from Kafka into Dataflow

Think: **sliding window (size 1h, hop 5m)**

**Tiny mental image:** a gliding spotlight on the last hour, re-checked every five minutes.

**Final answer:** A. Consume the stream of data in Cloud Dataflow using Kafka IO. Set a sliding time window of 1 hour every 5 minutes. Compute the average when the window closes, and send an alert if the average is less than 4000 messages.'''

E["test_6_q32"] = '''### Step 4: Choose the answer

- A Transform is the Beam component that performs a data processing operation, and you express conditional/looping/branching logic to build the pipeline graph.
- It satisfies the question: Transforms are the processing steps (PCollection is data, Pipeline is the container).

### Exam shortcut

If you see:
- the Beam component that *processes* data
- build branching logic via code
- distinguish from PCollection (data) / Pipeline (container)

Think: **Transform**

**Tiny mental image:** the machine that acts on the items, not the belt (PCollection) or the factory (Pipeline).

**Final answer:** B. Transform'''

E["test_6_q33"] = '''### Step 4: Choose the answer

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

E["test_6_q34"] = '''### Step 4: Choose the answer

- An IoT gateway feeding Cloud Pub/Sub, processed by Cloud Dataflow, absorbs global spikes elastically and replaces the costly single us-east Kafka cluster.
- It satisfies the goal: managed, globally scalable ingest and processing for bursty batched traffic.

### Exam shortcut

If you see:
- global IoT ingest, spiky/batched volume, single Kafka too costly
- need elastic managed ingest + processing
- "Google-recommended cloud-native"

Think: **IoT gateway → Pub/Sub → Dataflow**

**Tiny mental image:** swap the one overworked depot for a global mail network that scales with surges.

**Final answer:** C. An IoT gateway connected to Cloud Pub/Sub, with Cloud Dataflow to read and process the messages from Cloud Pub/Sub.'''

E["test_6_q36"] = '''### Step 4: Choose the answer

- Scheduling the Dataflow job via App Engine Cron Service runs the batch job once daily after the 2 AM log is ready, with no idle resources.
- It satisfies "inexpensively": a triggered batch run, not an always-on streaming job or manual start.

### Exam shortcut

If you see:
- run a batch Dataflow job once per day, cheaply
- triggered on a schedule, not streaming
- no manual intervention

Think: **scheduled trigger (App Engine Cron / Cloud Scheduler) → batch Dataflow**

**Tiny mental image:** an alarm clock that starts the machine each morning, then shuts it off.

**Final answer:** C. Create a cron job with Google App Engine Cron Service to run the Cloud Dataflow job.'''

E["test_6_q38"] = '''### Step 4: Choose the answer

- BigQuery can serve as a Dataflow sink in both batch and streaming write modes.
- It satisfies the question: there's no single-mode restriction - either works.

### Exam shortcut

If you see:
- "in which mode can BigQuery be a sink?"
- batch loads vs streaming inserts
- Dataflow → BigQuery

Think: **both batch and streaming**

**Tiny mental image:** the warehouse accepts both nightly truckloads and the live conveyor.

**Final answer:** A. Both batch and streaming'''

E["test_6_q44"] = '''### Step 4: Choose the answer

- Dataflow (Apache Beam) runs both batch and streaming pipelines under one unified model.
- It satisfies the question: it is not limited to one mode.

### Exam shortcut

If you see:
- "does Dataflow do batch or streaming?"
- unified batch + streaming model
- Beam's core value proposition

Think: **both batch and streaming**

**Tiny mental image:** one engine that runs whether the data arrives in crates or on a live belt.

**Final answer:** B. Both Batch and Streaming Data Pipelines'''

E["test_6_q45"] = '''### Step 4: Choose the answer

- A Dataproc cluster using the Cloud Storage connector reuses existing Hadoop jobs, minimizes cluster management, and persists data beyond the cluster's life.
- It satisfies all three: job reuse, managed service, and durable data decoupled from compute.

### Exam shortcut

If you see:
- reuse existing Hadoop jobs, minimal cluster management
- data must outlive the cluster
- managed Hadoop on GCP

Think: **Dataproc + Cloud Storage connector**

**Tiny mental image:** rent a managed workshop but keep your materials in a permanent warehouse next door.

**Final answer:** D. Create a Cloud Dataproc cluster that uses the Google Cloud Storage connector.'''

E["test_6_q47"] = '''### Step 4: Choose the answer

- Pub/Sub delivers the real-time event stream, Cloud Storage holds batch historical exports, and BigQuery serves ANSI SQL over real-time and historical data.
- It satisfies all three consumer access patterns with one managed stack.

### Exam shortcut

If you see:
- real-time stream + ANSI SQL (live + historical) + batch exports
- one platform covering all three
- market/event data feeds

Think: **Pub/Sub + Cloud Storage + BigQuery**

**Tiny mental image:** a live ticker, an archive room, and a SQL search desk fed from the same feed.

**Final answer:** B. Cloud Pub/Sub, Cloud Storage, BigQuery'''

E["test_6_q48"] = '''### Step 4: Choose the answer

- The Dataflow SDKs became the Apache Beam project, the unified batch/streaming programming model.
- It satisfies the question: Dataflow's SDK lineage is Apache Beam.

### Exam shortcut

If you see:
- "Dataflow SDK became which Apache project?"
- unified batch + streaming model
- portable pipeline SDK

Think: **Apache Beam**

**Tiny mental image:** the open-sourced blueprint Dataflow now builds from is named Beam.

**Final answer:** D. Apache Beam'''

E["test_7_q5"] = '''### Step 4: Choose the answer

- Keeping the raw posts in Cloud Storage (cheap archive/reprocessing) and writing the API-extracted topics/sentiment into BigQuery (for dashboards) is the lowest-cost split.
- It satisfies all: durable raw archive, SQL-queryable analytics, and shareable dashboards.

### Exam shortcut

If you see:
- archive raw data cheaply + analyze structured results
- dashboards/SQL on the extracted data
- lowest cost, fewest steps

Think: **raw → Cloud Storage, analytics → BigQuery**

**Tiny mental image:** keep the original letters in cheap storage and file the summarized notes in the searchable index.

**Final answer:** C. Store the raw social media posts in Cloud Storage, and write the data extracted from the API into BigQuery.'''

E["test_7_q7"] = '''### Step 4: Choose the answer

- A byte-mismatch after a successful CSV load usually means the source wasn't in BigQuery's default UTF-8 encoding, so characters were reinterpreted.
- It satisfies the diagnosis: the data loaded, but an encoding mismatch altered the bytes.

### Exam shortcut

If you see:
- CSV loads fine but bytes don't match the source
- character/encoding discrepancies
- BigQuery default is UTF-8

Think: **source encoding ≠ BigQuery default (UTF-8)**

**Tiny mental image:** the text arrived intact but was read in the wrong alphabet, garbling some letters.

**Final answer:** C. The CSV data loaded in BigQuery is not using BigQuery‘s default encoding.'''

E["test_7_q10"] = '''### Step 4: Choose the answer

- Streaming (unbounded) data requires a non-global windowing function; without one, the Dataflow job fails at pipeline construction for all streaming inserts.
- It satisfies the diagnosis: unbounded sources can't use the default global window without windowing.

### Exam shortcut

If you see:
- streaming Dataflow job fails for all inserts at creation
- unbounded source, no window applied
- windowing/transformation in play

Think: **unbounded streams need a non-global window**

**Tiny mental image:** you can't tally an endless parade without dividing it into segments first.

**Final answer:** D. They have not applied a non-global windowing function, which causes the job to fail when the pipeline is created'''

E["test_7_q14"] = '''### Step 4: Choose the answer

- Dataflow's three main trigger types are time-based, data-driven (element count), and composite; a trigger based on element size in bytes is not one of them.
- It satisfies the "NOT one of" framing: byte-size triggering isn't a supported category.

### Exam shortcut

If you see:
- "which is NOT a Dataflow trigger type"
- time, data-driven (count), composite are the three
- byte-size is the impostor

Think: **no "element size in bytes" trigger**

**Tiny mental image:** spot the odd one out: the bell rings on time or count, never on weight.

**Final answer:** A. Trigger based on element size in bytes'''

E["test_7_q22"] = '''### Step 4: Choose the answer

- Using Dataflow to find nulls and a custom script to convert them to 0 keeps the feature real-valued (not removed) for the logistic regression model.
- It satisfies the constraint: nulls are imputed to a numeric value rather than dropped or set to a non-numeric token.

### Exam shortcut

If you see:
- impute nulls for an ML model, must stay real-valued
- cannot remove the rows/feature
- numeric default (0), not 'none'

Think: **detect nulls and impute to a numeric value (0)**

**Tiny mental image:** fill the blank cells with a real number so the math model still adds up.

**Final answer:** D. Use Cloud Dataflow to find null values in sample source data. Convert all nulls to 0 using a custom script.'''

E["test_7_q24"] = '''### Step 4: Choose the answer

- Each server publishes bid events to Pub/Sub, and a Dataflow pull subscription processes them in real time, awarding the item to the first event processed.
- It satisfies the goal: globally scalable, real-time collation that resolves near-simultaneous bids.

### Exam shortcut

If you see:
- collate real-time events from many distributed servers
- determine first/earliest
- globally scalable ingest + stream processing

Think: **Pub/Sub ingest + Dataflow streaming**

**Tiny mental image:** every branch drops tickets in one central chute, and a sorter declares whoever's lands first.

**Final answer:** D. Have each application server write the bid events to Google Cloud Pub/Sub as they occur. Use a pull subscription to pull the bid events using Google Cloud Dataflow. Give the bid for each item to the user in the bid event that is processed first.'''

E["test_7_q25"] = '''### Step 4: Choose the answer

- Hashing each table's non-timestamp columns after sorting (via Dataproc and the BigQuery connector) compares outputs deterministically without a join key.
- It satisfies the goal: a key-free, order-independent equality check between original and migrated results.

### Exam shortcut

If you see:
- compare two tables with no primary/join key
- verify migrated output equals original
- order-independent, exclude timestamp columns

Think: **sort + hash the rows, compare hashes**

**Tiny mental image:** fingerprint each sorted deck - identical prints mean identical decks.

**Final answer:** C. Use a Dataproc cluster and the BigQuery Hadoop connector to read the data from each table and calculate a hash from non-timestamp columns of the table after sorting. Compare the hashes of each table.'''

E["test_7_q27"] = '''### Step 4: Choose the answer

- A multi-regional Cloud Storage bucket maximizes availability and is directly accessible by Dataproc, BigQuery, and Compute Engine for any file format.
- It satisfies the goal: a single highly-available store for CSV/Avro/PDF that all tools read, with performance not a concern.

### Exam shortcut

If you see:
- one store shared by Dataproc + BigQuery + Compute Engine
- mixed formats (CSV/Avro/PDF), maximize availability
- performance not the priority

Think: **multi-regional Cloud Storage bucket**

**Tiny mental image:** one highly-available warehouse every department can enter, holding boxes of any shape.

**Final answer:** D. Store the data in a multi-regional Cloud Storage bucket. Access the data directly using Cloud Dataproc, BigQuery, and Compute Engine.'''

append_entries(E)

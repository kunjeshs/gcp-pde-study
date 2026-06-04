from lib import append_entries

E = {}

E["test_2_q55"] = '''### Step 4: Choose the answer

- Nearline is the lowest-cost Cloud Storage class for data accessed roughly once a month, matching the ~30-day access pattern.
- It satisfies the goal: minimal storage cost for monthly-access archival data, without Coldline/Archive retrieval penalties.

### Exam shortcut

If you see:
- accessed about once a month (~30 days)
- minimize storage cost
- map access frequency to a storage class

Think: **Nearline** (monthly), vs Coldline (quarterly), Archive (yearly)

**Tiny mental image:** the shelf you reach for once a month - not the daily counter, not the deep-freeze.

**Final answer:** A. Nearline Storage'''

E["test_3_q4"] = '''### Step 4: Choose the answer

- Transfer Service for on-premises data uses local agents that work without public-internet inbound access, landing daily files in Cloud Storage for BigQuery.
- It satisfies both: recurring large transfers from a network-isolated source, then query via BigQuery.

### Exam shortcut

If you see:
- recurring on-prem transfer, source not reachable from public internet
- agent-based, scheduled, into Cloud Storage
- then load to BigQuery

Think: **Storage Transfer Service for on-premises data (agents)**

**Tiny mental image:** station your own couriers inside the locked building to ship the mail out on schedule.

**Final answer:** C. Use Transfer Service for on-premises data to transfer the data to Cloud Storage, then import the data into BigQuery using the BigQuery Data Transfer Service.'''

E["test_3_q5"] = '''### Step 4: Choose the answer

- An RDB backup copied to Cloud Storage with gsutil and imported into Memorystore is the simplest, lowest-cost, Google-recommended Redis migration.
- It satisfies minimal cost/time/effort: a native snapshot-and-import flow with no extra infrastructure.

### Exam shortcut

If you see:
- migrate Redis to Memorystore, minimal cost/time/effort
- "Google-recommended" Redis migration
- snapshot/backup based

Think: **RDB backup → Cloud Storage → import to Memorystore**

**Tiny mental image:** save the game, copy the save file over, and load it on the new console.

**Final answer:** A. Backup the Redis database as an RDB file, copy the file to a Cloud Storage bucket using the gsutil utility, and import the file into the Memorystore for Redis instance'''

E["test_3_q8"] = '''### Step 4: Choose the answer

- Storage Transfer Service agents installed on-premises run a reliable, scheduled weekly job from the POSIX source over the available bandwidth.
- It satisfies the goal: managed, repeatable, resumable weekly transfers - far more reliable than scripted gsutil.

### Exam shortcut

If you see:
- recurring/weekly on-prem transfer over the network
- POSIX source, moderate bandwidth
- "reliable" / Google-recommended

Think: **Storage Transfer Service for on-premises data (agents), scheduled**

**Tiny mental image:** a managed delivery service with tracking and retries, not you driving the boxes each week.

**Final answer:** C. Install Storage Transfer Service agents on-premises in your data center and configure a weekly transfer job.'''

E["test_3_q16"] = '''### Step 4: Choose the answer

- Lifting the Spark/Hive/HDFS workloads to Dataproc with Cloud Storage (modernize later) hits the tight two-month deadline while already capturing storage-decoupling savings.
- It satisfies both constraints: fast migration on schedule plus immediate cost benefit from Cloud Storage over HDFS.

### Exam shortcut

If you see:
- hard migration deadline, maximize cost savings
- existing Hadoop/Spark/Hive
- lift-and-shift now, modernize later

Think: **Dataproc + Cloud Storage, modernize later**

**Tiny mental image:** move into the new building first and remodel the rooms after you've met the deadline.

**Final answer:** B. Migrate the workloads to Dataproc plus Cloud Storage; modernize later: This option suggests moving the workloads to Dataproc plus Cloud Storage without modernizing and doing so at a later time'''

E["test_3_q24"] = '''### Step 4: Choose the answer

- At 20 Mb/sec, 2 PB cannot move online in six months, so Transfer Appliance ships the data physically within the window.
- It satisfies the constraint: offline bulk transfer when bandwidth, not time alone, is the bottleneck.

### Exam shortcut

If you see:
- petabytes with low bandwidth / "would take too long online"
- a hard deadline the network can't meet
- one-time bulk migration

Think: **Transfer Appliance** (offline shipping)

**Tiny mental image:** when the data won't fit through the straw, FedEx the whole tank instead.

**Final answer:** A. Use Transfer Appliance to copy the data to Cloud Storage'''

E["test_4_q21"] = '''### Step 4: Choose the answer

- Exporting to Avro and shipping it on a Transfer Appliance moves 10 TB of sensitive records securely and quickly, then loads cleanly into BigQuery.
- It satisfies both: encrypted physical transfer (no public URLs) and a time-efficient bulk path.

### Exam shortcut

If you see:
- large, sensitive bulk load into BigQuery
- secure (reject public-URL options)
- time-efficient at multi-TB scale

Think: **Avro export + Transfer Appliance → BigQuery**

**Tiny mental image:** ship the patient files in a sealed armored case, not posted on an open web link.

**Final answer:** B. Export the records from the database as an Avro file, copy the file onto a Transfer Appliance, send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.'''

E["test_4_q34"] = '''### Step 4: Choose the answer

- gsutil handles the one-off migration of the few large 90 GB files, while Pub/Sub plus Dataflow streams real-time updates from the transactional systems.
- It satisfies both halves: simple bulk move now, plus a managed streaming pipeline for continuous updates.

### Exam shortcut

If you see:
- bulk migrate a handful of very large files + ongoing real-time updates
- streaming ingestion/transformation
- Pub/Sub feeding the warehouse

Think: **gsutil (migration) + Pub/Sub → Dataflow (real-time)**

**Tiny mental image:** truck over the big crates once, then run a live conveyor belt for the daily flow.

**Final answer:** C. Use gsutil for the migration; Pub/Sub and Dataflow for real-time updates'''

E["test_4_q44"] = '''### Step 4: Choose the answer

- Establishing Cloud Interconnect and then using Storage Transfer Service gives a fast, secure, high-bandwidth path to move 1 PB.
- It satisfies the goal: minimized transfer time over a private, dedicated connection following best practice.

### Exam shortcut

If you see:
- petabyte online transfer, minimize time, secure connection
- dedicated/private high bandwidth needed
- "Google-recommended secure connection"

Think: **Cloud Interconnect + Storage Transfer Service**

**Tiny mental image:** lay a private high-speed pipeline instead of trickling it through the public garden hose.

**Final answer:** A. Use the Storage Transfer Service after establishing a Cloud Interconnect connection between the on-premises data center and Google Cloud'''

E["test_5_q22"] = '''### Step 4: Choose the answer

- Exporting to Avro and shipping it on a Transfer Appliance moves the 10 TB of sensitive records securely and efficiently, then loads into BigQuery.
- It satisfies both: encrypted physical transfer (no public URLs) and a time-efficient bulk path.

### Exam shortcut

If you see:
- large, sensitive bulk load into BigQuery
- secure (reject public-URL options)
- time-efficient at multi-TB scale

Think: **Avro export + Transfer Appliance → BigQuery**

**Tiny mental image:** ship the patient files in a sealed armored case, not on an open web link.

**Final answer:** B. Export the records from the database as an Avro file. Copy the file onto a Transfer Appliance and send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.'''

E["test_6_q30"] = '''### Step 4: Choose the answer

- Copying the ORC files to the master node and using the Hadoop utility to put them into HDFS (or using the Cloud Storage connector for external tables) gets Hive running on Dataproc.
- It satisfies the goal: data replicated to local HDFS for performance, with Hive tables mounted from HDFS.

### Exam shortcut

If you see:
- start Hive on Dataproc with data already in Cloud Storage
- replicate to local HDFS for performance
- ORC files staged in a bucket

Think: **stage to master node → hadoop fs into HDFS (or use the Cloud Storage connector)**

**Tiny mental image:** bring the parts into the workshop's own bench so the machine runs at full speed.

**Final answer:** C. Run the gsutil utility to transfer all ORC files from the Cloud Storage bucket to the master node of the Dataproc cluster. Then run the Hadoop utility to copy them do HDFS. Mount the Hive tables from HDFS.'''

E["test_7_q46"] = '''### Step 4: Choose the answer

- At 20 Mb/sec, 2 PB can't move online within six months, so Transfer Appliance ships the data physically in time.
- It satisfies the constraint: offline bulk transfer when bandwidth, not the deadline alone, is the bottleneck.

### Exam shortcut

If you see:
- petabytes with low bandwidth, fixed deadline
- online transfer would take far too long
- one-time bulk migration

Think: **Transfer Appliance** (offline shipping)

**Tiny mental image:** when it won't fit through the straw, ship the whole tank.

**Final answer:** A. Use Transfer Appliance to copy the data to Cloud Storage'''

E["test_11_q17"] = '''### Step 4: Choose the answer

- Dataflow's prebuilt Cloud Storage Avro to Bigtable template gives a reliable, monitorable, managed copy job with no custom code.
- It satisfies the goal: a supported, observable pipeline for loading Avro into Bigtable.

### Exam shortcut

If you see:
- load files from Cloud Storage into Bigtable
- want reliable, monitored, no custom code
- a Google-provided template exists

Think: **Dataflow GCS-Avro-to-Bigtable template**

**Tiny mental image:** use the labeled, off-the-shelf conveyor instead of hand-building one in Python.

**Final answer:** C. Cloud Dataflow, starting with a Cloud Storage Avro to Bigtable template.'''

E["test_11_q29"] = '''### Step 4: Choose the answer

- Storage Transfer Service moving the log files into a Multi-Regional bucket gives globally distributed teams low-latency access for ANSI SQL analysis.
- It satisfies the goal: managed transfer plus a multi-region landing zone for global analytics.

### Exam shortcut

If you see:
- bring backup/log files into Cloud Storage
- globally distributed teams analyzing the data
- managed/online transfer

Think: **Storage Transfer Service → Multi-Regional bucket**

**Tiny mental image:** stock a warehouse with depots on every continent so each team is nearby.

**Final answer:** B. Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination'''

E["test_13_q7"] = '''### Step 4: Choose the answer

- The 403s mean the signed URLs expired mid-run; regenerating them with a longer validity and splitting into parallel jobs lets the remaining files finish.
- It satisfies the fix: fresh, longer-lived credentials plus parallelism to complete before they lapse again.

### Exam shortcut

If you see:
- Storage Transfer Service failing partway with HTTP 403
- source unchanged, signed URLs involved
- long-running job that started fine

Think: **signed URLs expired - regenerate with longer validity (and parallelize)**

**Tiny mental image:** the gate passes timed out halfway through - reissue longer-dated passes and send several crews at once.

**Final answer:** C. Create a new TSV file for the remaining files by generating signed URLs with a longer validity period. Split the TSV file into multiple smaller files and submit them as separate Storage Transfer Service jobs in parallel.'''

E["test_13_q16"] = '''### Step 4: Choose the answer

- A dual-region bucket with turbo replication gives RPO=15 minutes, and reading from the in-region copy keeps latency minimal; on failure, redeploy Dataproc and read the same bucket.
- It satisfies both targets: tight RPO via turbo replication and low read latency by staying same-region.

### Exam shortcut

If you see:
- survive a single-region failure with small RPO (~15 min)
- minimal read latency for the compute
- Cloud Storage + Dataproc

Think: **dual-region bucket + turbo replication, read in-region**

**Tiny mental image:** keep a synced twin warehouse next door, but always shop from the one closest to the kitchen.

**Final answer:** D. 1. Create a dual-region Cloud Storage bucket in the us-central1 and us-south1 regions. 2. Enable turbo replication. 3. Run the Dataproc cluster in a zone in the us-central1 region, reading from the bucket in the same region. 4. In case of a regional failure, redeploy the Dataproc clusters to the us-south1 region and read from the same bucket.'''

E["test_13_q32"] = '''### Step 4: Choose the answer

- BigQuery time travel recovers table data from any point in the last seven days as a built-in managed feature, with the lowest RPO and no extra cost.
- It satisfies the goal: instant point-in-time recovery from corruption without snapshots or exports to maintain.

### Exam shortcut

If you see:
- recover BigQuery data from corruption within the last 7 days
- lowest RPO, cost-effective, managed
- no extra copies to maintain

Think: **BigQuery time travel**

**Tiny mental image:** a built-in rewind button that jumps the table back to before the spill.

**Final answer:** A. Access historical data by using time travel in BigQuery.'''

E["test_14_q6"] = '''### Step 4: Choose the answer

- An RDB backup copied to Cloud Storage with gsutil and imported into Memorystore is the simplest, lowest-cost, Google-recommended Redis migration.
- It satisfies minimal cost/time/effort: a native snapshot-and-import flow with no extra infrastructure.

### Exam shortcut

If you see:
- migrate Redis to Memorystore, minimal cost/time/effort
- "Google-recommended" Redis migration
- snapshot/backup based

Think: **RDB backup → Cloud Storage → import to Memorystore**

**Tiny mental image:** save the game, copy the save file, load it on the new console.

**Final answer:** A. Make an RDB backup of the Redis database, use the gsutil utility to copy the RDB file into a Cloud Storage bucket, and then import the RDB file into the Memorystore for Redis instance.'''

E["test_14_q7"] = '''### Step 4: Choose the answer

- Moving 1 PB within hours rules out shipping an appliance; Cloud Interconnect plus Storage Transfer Service provides the high-bandwidth, secure online path.
- It satisfies both: extreme volume in a tight time window over a private, dedicated connection.

### Exam shortcut

If you see:
- petabyte transfer in *hours* (not weeks)
- secure, high-bandwidth, online
- appliance shipping is too slow for the deadline

Think: **Cloud Interconnect + Storage Transfer Service**

**Tiny mental image:** open a dedicated firehose pipeline; there's no time to mail a truck.

**Final answer:** A. Establish a Cloud Interconnect connection between the on-premises data center and Google Cloud, and then use the Storage Transfer Service.'''

E["test_14_q13"] = '''### Step 4: Choose the answer

- Storage Transfer Service for on-premises data, installed in the data center, runs a reliable scheduled weekly job from the POSIX source.
- It satisfies the goal: managed, resumable, repeatable weekly transfers rather than fragile scripted gsutil.

### Exam shortcut

If you see:
- recurring/weekly on-prem transfer over the network
- POSIX source, moderate bandwidth
- "reliable" / Google-recommended

Think: **Storage Transfer Service for on-premises data (agents), scheduled**

**Tiny mental image:** a managed courier with tracking and retries, not you driving the boxes weekly.

**Final answer:** C. Install Storage Transfer Service for on-premises data in your data center, and then configure a weekly transfer job.'''

append_entries(E)

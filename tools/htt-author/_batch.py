from lib import append_entries

E = {}

E["test_11_q11"] = '''### Step 4: Choose the answer

- Adding a read replica offloads read traffic from the primary with essentially no application changes, the first thing to try for read-SLA misses.
- It satisfies the goal: more read capacity, minimal disruption, native Cloud SQL feature.

### Exam shortcut

If you see:
- read SLAs not met, "minimal changes to applications"
- scale out reads, not writes
- managed relational database

Think: **Cloud SQL read replica**

**Tiny mental image:** open a second checkout lane so the reading queue clears faster.

**Final answer:** D. Create a read replica.'''

E["test_11_q28"] = '''### Step 4: Choose the answer

- Adding a dedicated calibration MapReduce job and chaining all other jobs after it guarantees calibration always runs first, systematically.
- It satisfies the fix: a reproducible pipeline step, not manual or user-applied corrections.

### Exam shortcut

If you see:
- a required preprocessing step keeps getting skipped
- make it systematic/repeatable in the pipeline
- ordering/dependency between jobs

Think: **dedicated upstream job, chain everything after it**

**Tiny mental image:** put the safety checklist as step zero on the assembly line so nothing moves until it's done.

**Final answer:** D. Add a new MapReduce job to apply sensor calibration to the raw data, and ensure that all other MapReduce jobs are chained after this step.'''

E["test_13_q11"] = '''### Step 4: Choose the answer

- Spinning up a Standard Tier Redis instance in the development environment and forcing a failover (force-data-loss) tests DR accurately without touching production.
- It satisfies both: a realistic failover drill and zero risk to production data.

### Exam shortcut

If you see:
- simulate/test a failover without harming production
- Memorystore Redis Standard Tier
- DR drill in a safe environment

Think: **replicate the instance in dev, force a manual failover there**

**Tiny mental image:** run the fire drill in the practice building, not the live office.

**Final answer:** B. Create a Standard Tier Memorystore for Redis instance in a development environment. Initiate a manual failover by using the force-data-loss data protection mode.'''

E["test_13_q19"] = '''### Step 4: Choose the answer

- After promoting the Region2 replica to primary, creating two new read replicas (Region3 and a new region) restores the original read capacity before cutover.
- It satisfies the goal: the application regains the same number of replicas it had pre-disaster.

### Exam shortcut

If you see:
- promote a read replica during DR
- must restore the *same* read capacity
- replicas were lost when the old primary failed

Think: **rebuild read replicas off the new primary to match prior capacity**

**Tiny mental image:** after the captain steps up, you re-staff the crew positions that moved up with him.

**Final answer:** C. Create two new read replicas from the new primary instance, one in Region3 and one in a new region.'''

E["test_13_q24"] = '''### Step 4: Choose the answer

- Cloud Load Balancing distributing traffic across multiple Compute Engine instances removes the single point of failure for the web tier.
- It satisfies high availability and fault tolerance by spreading requests across redundant backends.

### Exam shortcut

If you see:
- highly available / fault-tolerant web tier
- remove single points of failure
- many instances behind one entry point

Think: **Cloud Load Balancing across multiple instances (ideally multi-zone)**

**Tiny mental image:** several open tellers with a host directing customers, so one closing doesn't stop service.

**Final answer:** B. Use Cloud Load Balancing to distribute incoming traffic across multiple Compute Engine instances in the same zone.'''

E["test_13_q58"] = '''### Step 4: Choose the answer

- Setting the topic's message retention policy to 30 days lets any new subscription replay the last 30 days of data.
- It satisfies the goal: late-joining subscribers can read historical messages without re-publishing.

### Exam shortcut

If you see:
- new Pub/Sub subscribers must access older/historical messages
- retain N days of data on the topic
- replay before a known event

Think: **Pub/Sub topic message retention policy**

**Tiny mental image:** a DVR that keeps the last 30 days, so anyone tuning in late can still rewind.

**Final answer:** B. Set the topic retention policy to 30 days.'''

E["test_14_q14"] = '''### Step 4: Choose the answer

- Cloud SQL for PostgreSQL with high availability is ACID-compliant and fails over automatically, minimizing human intervention.
- It satisfies both: full relational ACID guarantees plus a managed automatic-failover standby.

### Exam shortcut

If you see:
- ACID/relational database required
- automatic recovery, minimal human intervention
- managed OLTP

Think: **Cloud SQL (PostgreSQL/MySQL) with HA / automatic failover**

**Tiny mental image:** a backup generator that flips on by itself the instant the power cuts.

**Final answer:** B. Configure a Cloud SQL for PostgreSQL instance with high availability enabled.'''

E["test_14_q39"] = '''### Step 4: Choose the answer

- Setting a retention policy and then locking it makes the legal-hold documents immutable - they cannot be deleted or overwritten until the retention period passes.
- It satisfies the goal: a tamper-proof guarantee, since a locked retention policy itself cannot be removed or shortened.

### Exam shortcut

If you see:
- prevent deletion/modification of compliance/legal documents
- immutability / WORM guarantee
- Cloud Storage objects

Think: **bucket retention policy + lock it**

**Tiny mental image:** seal the records in a time-locked safe whose timer can't be wound back.

**Final answer:** A. Set a retention policy. Lock the retention policy.'''

E["test_14_q58"] = '''### Step 4: Choose the answer

- An HA primary in region A, an HA read replica in region B, plus cascading read replicas, with promotion of region B on outage, gives low RTO/RPO and minimal reader interruption.
- It satisfies all: cross-region reads, high availability, and a fast regional failover target.

### Exam shortcut

If you see:
- Cloud SQL with cross-region readers, low RTO/RPO
- survive a regional outage with quick failover
- many geographically spread readers

Think: **HA primary + HA cross-region replica (+ cascading replicas), promote on outage**

**Tiny mental image:** a fully-staffed branch in another city ready to take over the instant headquarters goes dark.

**Final answer:** C. Create a highly available Cloud SQL instance in region A. Create a highly available read replica in region B. Scale up read workloads by creating cascading read replicas in multiple regions. Promote the read replica in region B when region A is down.'''

E["test_15_q36"] = '''### Step 4: Choose the answer

- A Dataflow job that reads the source, defaults the out-of-range values, and writes to a new Cloud Storage dataset is rerunnable and preserves the originals.
- It satisfies all: repeatable correction, errors fixed, and raw data retained untouched for compliance.

### Exam shortcut

If you see:
- correct data, keep the original for compliance
- must be able to rerun the process
- never overwrite the source dataset

Think: **Dataflow transform → write to a NEW dataset**

**Tiny mental image:** edit a photocopy and file it next to the sealed original, never marking the original.

**Final answer:** C. Create a Dataflow workflow that reads the data from Cloud Storage, checks for values outside the expected range, sets the value to an appropriate default, and writes the updated records to a new dataset in Cloud Storage.'''

E["test_16_q38"] = '''### Step 4: Choose the answer

- A failover replica in another zone of the same region gives Cloud SQL automatic high availability if the primary zone fails.
- It satisfies the requirement: zone-failure resilience with automatic failover, not read scaling or cross-region DR.

### Exam shortcut

If you see:
- Cloud SQL high availability against a zone failure
- automatic failover within a region
- failover replica vs read replica

Think: **Cloud SQL HA = failover replica in another zone, same region**

**Tiny mental image:** a standby twin in the next room that takes over instantly if the first trips.

**Final answer:** A. Create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region.'''

E["test_1_q47"] = '''### Step 4: Choose the answer

- Cloud DLP discovers the PII and Data Catalog stores the resulting metadata tags on the objects - two managed services working together.
- It satisfies the task: automated sensitive-data detection plus durable, searchable metadata tagging.

### Exam shortcut

If you see:
- detect PII AND tag/catalog it with metadata
- two managed services together
- migration into Cloud Storage

Think: **Cloud DLP (detect) + Data Catalog (tag/catalog)**

**Tiny mental image:** a scanner that spots the sensitive pages and a catalog that files an index card for each.

**Final answer:** D. Data Loss Prevention and Data Catalog'''

E["test_2_q43"] = '''### Step 4: Choose the answer

- Pub/Sub schema support covers Protocol Buffer and Avro, enforcing a standard message format between decoupled services.
- It satisfies the design goal: schema-validated messages in one of the two supported definition formats.

### Exam shortcut

If you see:
- enforce a message schema in Pub/Sub
- "which schema types are supported?"
- decoupling services with a standard format

Think: **Pub/Sub schemas = Protocol Buffer + Avro**

**Tiny mental image:** the post office accepts letters only in two approved envelope templates.

**Final answer:** B. Protocol Buffer'''

E["test_6_q22"] = '''### Step 4: Choose the answer

- The false statement is that BigQuery can export only JSON or Avro - it also supports CSV (and Parquet), so that claim is incorrect.
- It satisfies the "which is false" framing: the format limitation stated is simply not true.

### Exam shortcut

If you see:
- "which statement is FALSE" about BigQuery export
- a claim that limits export formats too narrowly
- recall CSV/JSON/Avro/Parquet are supported

Think: **export formats include CSV too - so "only JSON or Avro" is false**

**Tiny mental image:** spot the menu item that's mislabeled "out of stock" when it's actually available.

**Final answer:** C. Data can only be exported in JSON or Avro format.'''

E["test_13_q21"] = '''### Step 4: Choose the answer

- Data Catalog auto-catalogs BigQuery datasets and Pub/Sub topics, and its APIs let you catalog the PostgreSQL tables, all with minimal effort.
- It satisfies discoverability: one searchable catalog spanning the native services automatically and the external source via API.

### Exam shortcut

If you see:
- find/discover data assets across many platforms
- minimal development/configuration
- BigQuery + Pub/Sub auto, plus an external source

Think: **Data Catalog (auto for native services, API for external)**

**Tiny mental image:** one library index that auto-lists the in-house shelves and lets you hand-enter the outside collection.

**Final answer:** B. Use Data Catalog to automatically catalog BigQuery datasets and Pub/Sub topics. Use Data Catalog APIs to manually catalog PostgreSQL tables.'''

E["test_13_q29"] = '''### Step 4: Choose the answer

- Dataplex auto-discovery of raw files belongs in the raw zone; moving the JSON/CSV files there lets Dataplex discover them automatically.
- It satisfies the fix: the curated zone expects structured/curated data, so raw file dumps go in the raw zone.

### Exam shortcut

If you see:
- Dataplex not discovering raw files (JSON/CSV)
- files placed in the curated zone
- raw vs curated zone semantics

Think: **raw file dumps belong in the raw zone for auto-discovery**

**Tiny mental image:** you put the unsorted mail in the "sorted" bin - move it to the intake tray so the sorter finds it.

**Final answer:** A. Move the JSON and CSV files to the raw zone.'''

E["test_1_q26"] = '''### Step 4: Choose the answer

- Storage Transfer Service moving the backup files into a Multi-Regional Cloud Storage bucket gives global marketing teams low-latency, durable access to the latest logs for analysis.
- It satisfies the goal: managed transfer plus a multi-region landing zone suited to globally distributed analytics.

### Exam shortcut

If you see:
- bring backup/log files into Cloud Storage
- globally distributed teams analyzing the data
- managed/online transfer

Think: **Storage Transfer Service → Multi-Regional bucket**

**Tiny mental image:** drop the files in a warehouse with depots on every continent so each team's nearby.

**Final answer:** A. Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination'''

E["test_2_q7"] = '''### Step 4: Choose the answer

- A managed instance group autoscales VMs up and down based on CPU load, matching the researchers' existing VM-based cluster.
- It satisfies the goal: automatic, policy-driven scaling without re-platforming away from virtual machines.

### Exam shortcut

If you see:
- autoscale a fleet of VMs by CPU/metric
- keep a VM-based architecture
- self-healing/managed scaling

Think: **Managed instance group (autoscaling)**

**Tiny mental image:** a thermostat that adds or removes workers automatically as the heat (load) rises and falls.

**Final answer:** B. Managed instance groups'''

E["test_2_q26"] = '''### Step 4: Choose the answer

- Storage Transfer Service performs a reliable, managed, online one-time copy of 100 TB from S3 into Cloud Storage with retries and validation.
- It satisfies the priority: complete, verified transfer over the network from another cloud, no appliance needed.

### Exam shortcut

If you see:
- bulk transfer from AWS S3 (or another cloud) into Cloud Storage
- online/networked, reliable, complete
- one-time or scheduled

Think: **Cloud Storage Transfer Service** (Transfer Appliance only when bandwidth is the blocker)

**Tiny mental image:** a managed moving company that checks every box arrived, instead of you carrying them by hand.

**Final answer:** C. Cloud Storage Transfer Service'''

E["test_2_q34"] = '''### Step 4: Choose the answer

- Google's recommended Hadoop-migration pattern is ephemeral clusters with data in Cloud Storage instead of HDFS on local disks.
- It satisfies best practice: decouple storage from compute so clusters can spin up/down on demand and storage scales independently.

### Exam shortcut

If you see:
- migrating Hadoop/Spark to GCP "best practice"
- separate storage from compute
- ephemeral vs always-on clusters

Think: **ephemeral Dataproc clusters + Cloud Storage (not HDFS)**

**Tiny mental image:** rent the workshop only when you're building, and keep your materials in a permanent warehouse.

**Final answer:** A. Use ephemeral clusters and Cloud Storage instead of HDFS on local storage.'''

append_entries(E)

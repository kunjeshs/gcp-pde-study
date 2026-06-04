from lib import append_entries

E = {}

E["test_14_q33"] = '''### Step 4: Choose the answer

- A Cloud DLP deep inspection job on each table, using a template with the STREET_ADDRESS infoType, finds every street-address instance reliably.
- It satisfies the goal: purpose-built detection of a specific sensitive type, not brittle keyword matching.

### Exam shortcut

If you see:
- find all instances of a specific sensitive type (addresses, SSNs)
- need accurate detection across tables
- infoType-based inspection

Think: **Cloud DLP deep inspection job + the matching infoType**

**Tiny mental image:** a trained sniffer dog for "street address," not someone grepping for the word "street."

**Final answer:** B. Create a deep inspection job on each table in your dataset with Cloud Data Loss Prevention and create an inspection template that includes the STREET_ADDRESS infoType.'''

E["test_14_q38"] = '''### Step 4: Choose the answer

- DLP format-preserving encryption (FFX) tokenizes the email consistently in both datasets, so the analysts can still join on it without seeing the real value.
- It satisfies both: PII is de-identified before BigQuery, yet the email remains a usable join key.

### Exam shortcut

If you see:
- de-identify a field that is also a join key
- must keep matching/referential integrity across datasets
- DLP before loading to BigQuery

Think: **DLP format-preserving encryption (FFX) tokenization**

**Tiny mental image:** replace every email with the same codename everywhere, so the two lists still line up.

**Final answer:** B. 1. Create a pipeline to de-identify the email field by using recordTransformations in Cloud DLP with format-preserving encryption with FFX as the de-identification transformation type. 2. Load the booking and user profile data into a BigQuery table.'''

E["test_14_q46"] = '''### Step 4: Choose the answer

- VPC Network Peering plus a no-external-IP proxy VM in Project B on the peered subnet lets Dataflow reach the private Cloud SQL instance entirely over internal networking.
- It satisfies the constraint: the connection works and the traffic never touches the public internet.

### Exam shortcut

If you see:
- Dataflow in one project must reach a private Cloud SQL in another
- no public IP, no Shared VPC / VPC-SC
- traffic must stay off the public internet

Think: **VPC Peering + private proxy VM to Cloud SQL**

**Tiny mental image:** build a private hallway between the two buildings and post a doorman who relays messages.

**Final answer:** D. Set up VPC Network Peering between Project A and Project B. Create a Compute Engine instance without external IP address in Project B on the peered subnet to serve as a proxy server to the Cloud SQL database.'''

E["test_14_q50"] = '''### Step 4: Choose the answer

- A VPC Service Controls perimeter around project A blocks data exfiltration of the Pub/Sub topic to project B and any future project outside the perimeter.
- It satisfies the goal: a service-level boundary that confines access to resources inside project A.

### Exam shortcut

If you see:
- confine a managed-API resource (Pub/Sub, BigQuery, GCS) to one project
- prevent access from other/future projects
- stop data exfiltration

Think: **VPC Service Controls perimeter around the project**

**Tiny mental image:** draw a fence around the building so only those inside can reach the safe.

**Final answer:** B. Configure VPC Service Controls in the organization with a perimeter around project A.'''

E["test_14_q54"] = '''### Step 4: Choose the answer

- The gcp.resourceLocations org policy set to in:europe-west3-locations restricts resource creation to exactly that region preventively.
- It satisfies the goal using Google's recommended, declarative control rather than custom scripts or after-the-fact cleanup.

### Exam shortcut

If you see:
- restrict resources to a specific region/location
- "Google-recommended" / preventive control
- data residency / location compliance

Think: **org policy: constraints/gcp.resourceLocations (precise location value)**

**Tiny mental image:** a geofence that simply refuses to create anything outside the chosen city.

**Final answer:** A. Set the constraints/gcp.resourceLocations organization policy constraint to in:europe-west3-locations.'''

E["test_14_q60"] = '''### Step 4: Choose the answer

- BigQuery AEAD functions let you encrypt with per-user keys, so deleting one user's key crypto-shreds just that user's data.
- It satisfies per-user crypto-deletion natively, which table-level CMEK (one key for the whole table) cannot do.

### Exam shortcut

If you see:
- per-row / per-user "crypto-deletion" or "crypto-shredding"
- encrypt within BigQuery with granular keys
- delete a key to render one subject's data unreadable

Think: **BigQuery AEAD encryption functions**

**Tiny mental image:** each customer's data is in its own tiny lockbox - shred that one key and only their box is gone.

**Final answer:** A. Implement Authenticated Encryption with Associated Data (AEAD) BigQuery functions while storing your data in BigQuery.'''

E["test_15_q24"] = '''### Step 4: Choose the answer

- An aggregated export sink captures Data Access logs from all projects into a Cloud Storage bucket in a new, locked-down audit project, away from the analyst-Owners.
- It satisfies both: centralized 6-month retention and access limited to audit personnel only.

### Exam shortcut

If you see:
- collect audit/data-access logs across ALL projects
- keep them from project Owners/admins
- central retention for N months

Think: **aggregated log export sink to an isolated audit project**

**Tiny mental image:** funnel every branch's ledgers into one sealed vault that only the auditors can open.

**Final answer:** D. Export the data access logs via an aggregated export sink to a Cloud Storage bucket in a newly created project for audit logs. Restrict access to the project that contains the exported logs.'''

E["test_15_q26"] = '''### Step 4: Choose the answer

- Precomputing predictions in Dataflow and serving them from Bigtable delivers single-user-ID lookups well under 100 ms.
- It satisfies the latency SLA a live BigQuery query cannot guarantee for point lookups.

### Exam shortcut

If you see:
- serve BigQuery ML predictions via REST under ~100 ms
- single-key (user ID) lookups
- need an online serving store

Think: **precompute in Dataflow, serve from Bigtable**

**Tiny mental image:** bake all the answers ahead of time and file them, so each request is just opening a drawer.

**Final answer:** D. Create a Dataflow pipeline using BigQueryIO to read predictions for all users from the query. Write the results to Bigtable using BigtableIO. Grant the Bigtable Reader role to the application service account so that the application can read predictions for individual users from Bigtable.'''

E["test_15_q35"] = '''### Step 4: Choose the answer

- Since the network team defines firewall rules by network tag, check for a rule allowing TCP 12345-12346 on the Dataflow network tag - the ports workers use to talk to each other.
- It satisfies the diagnosis: matches the tag-based firewall convention and the exact inter-worker port range.

### Exam shortcut

If you see:
- Dataflow workers can't communicate with each other
- firewall rules defined by network tags
- TCP ports 12345/12346

Think: **firewall rule allowing 12345-12346 on the Dataflow network tag**

**Tiny mental image:** the team can't talk because the intercom ports are firewalled - open them for that crew's badge.

**Final answer:** B. Determine whether there is a firewall rule set to allow traffic on TCP ports 12345 and 12346 for the Dataflow network tag.'''

E["test_15_q40"] = '''### Step 4: Choose the answer

- DLP format-preserving encryption tokenizes the ID reversibly, so reps with the key can recover the original when required.
- It satisfies both: the value is redacted for everyone, yet authorized staff can de-tokenize on demand.

### Exam shortcut

If you see:
- redact a sensitive ID but allow authorized re-identification later
- need reversibility (not a one-way hash)
- preserve original format

Think: **DLP format-preserving encryption (FPE) token**

**Tiny mental image:** a coat-check tag - hand over the coat, the matching ticket gets it back.

**Final answer:** D. Before loading the data into BigQuery, use Cloud Data Loss Prevention (DLP) to replace input values with a cryptographic format-preserving encryption token.'''

E["test_15_q51"] = '''### Step 4: Choose the answer

- A DLP format-preserving token replaces names and emails consistently, so they stay masked yet remain valid join keys.
- It satisfies both priorities: PII is protected and referential integrity across records is maintained.

### Exam shortcut

If you see:
- mask PII but it is also a common join key
- "maintain referential integrity"
- streaming de-identification

Think: **DLP format-preserving / deterministic tokenization**

**Tiny mental image:** swap each name for the same codename everywhere, so the records still connect.

**Final answer:** D. Create a pseudonym by replacing PII data with a cryptographic format-preserving token.'''

E["test_15_q59"] = '''### Step 4: Choose the answer

- A VPC Service Controls perimeter with Cloud Storage restricted, granting only the Development Team an access level, lets Dev read GCS while External keeps only BigQuery access.
- It satisfies both: External is fenced out of Cloud Storage, while both teams retain BigQuery via their viewer role.

### Exam shortcut

If you see:
- two groups, one allowed an extra service the other isn't
- both already have broad viewer access
- restrict a specific API (Cloud Storage) to some users

Think: **VPC Service Controls perimeter restricting the API, access level for the allowed group**

**Tiny mental image:** everyone can enter the library, but only staff badges open the archive room.

**Final answer:** D. Create a VPC Service Controls perimeter containing both projects and Cloud Storage as a restricted API. Add the Development Team users to the perimeter‘s Access Level.'''

E["test_16_q26"] = '''### Step 4: Choose the answer

- Encrypting each file client-side with a key plus unique AAD, and keeping the AAD entirely outside Google Cloud, means provider staff can never decrypt the objects.
- It satisfies "Trust No One": even with infrastructure access, Google lacks the AAD needed to recover the plaintext.

### Exam shortcut

If you see:
- "Trust No One" / provider must be unable to decrypt
- client-side encryption with a secret kept off-platform
- additional authenticated data (AAD)

Think: **client-side encryption, keep the AAD/secret outside Google Cloud**

**Tiny mental image:** lock the box and keep the second combination dial at home, so the warehouse can never open it.

**Final answer:** A. Use gcloud kms keys create to create a symmetric key. Then use gcloud kms encrypt to encrypt each archival file with the key and unique additional authenticated data (AAD). Use gsutil cp to upload each encrypted file to the Cloud Storage bucket, and keep the AAD outside of Google Cloud.'''

E["test_16_q41"] = '''### Step 4: Choose the answer

- Copying the dependencies to a Cloud Storage bucket inside the VPC perimeter lets the init action fetch them with no internet access.
- It satisfies both constraints: startup dependency install while the no-internet policy holds.

### Exam shortcut

If you see:
- Dataproc init action needs packages but no internet allowed
- private/VPC-only nodes
- existing initialization action

Think: **stage dependencies in Cloud Storage within the VPC perimeter**

**Tiny mental image:** stock the pantry inside the locked compound so the cook never leaves to shop.

**Final answer:** C. Copy all dependencies to a Cloud Storage bucket within your VPC security perimeter'''

E["test_1_q11"] = '''### Step 4: Choose the answer

- HBase, Cassandra, and MongoDB are the three that scale to 100 TB/yr of wide, field-queryable telemetry with high availability and low latency, without needing ACID.
- It satisfies the profile: distributed NoSQL stores built for massive write volume and per-field reads.

### Exam shortcut

If you see:
- huge-volume IoT/telemetry, no ACID needed
- high availability + low latency, query individual fields
- pick the scalable NoSQL stores

Think: **HBase / Cassandra / MongoDB** (skip Redis, MySQL, HDFS+Hive)

**Tiny mental image:** choose the fleet of delivery vans built to scale, not the single armored truck or the warehouse forklift.

**Final answer:** B. HBase'''

E["test_3_q7"] = '''### Step 4: Choose the answer

- Cloud SQL for PostgreSQL with high availability gives an ACID-compliant database that automatically fails over with minimal human intervention.
- It satisfies both: full relational ACID guarantees plus a managed automatic-failover standby.

### Exam shortcut

If you see:
- ACID/relational database required
- automatic recovery, minimal human intervention on failure
- managed OLTP

Think: **Cloud SQL (PostgreSQL/MySQL) with HA / automatic failover**

**Tiny mental image:** a backup generator that flips on by itself the instant the power cuts.

**Final answer:** B. Configure a Cloud SQL for PostgreSQL instance with high availability enabled.'''

E["test_5_q18"] = '''### Step 4: Choose the answer

- A multi-regional BigQuery dataset gives built-in high availability, and point-in-time recovery (time travel) restores data without paying to maintain extra copies.
- It satisfies all three: high availability, recoverable backups, and minimized cost (no duplicate backup tables).

### Exam shortcut

If you see:
- BigQuery must be highly available, recoverable, low cost
- backup/recovery without extra storage spend
- multi-region vs scheduled copies

Think: **multi-region dataset + point-in-time (time-travel) recovery**

**Tiny mental image:** an "undo" button that's already included, instead of paying to photocopy everything nightly.

**Final answer:** C. Set the BigQuery dataset to be multi-regional. In the event of an emergency, use a point-in-time snapshot to recover the data.'''

E["test_7_q34"] = '''### Step 4: Choose the answer

- HBase, Cassandra, and MongoDB scale to 100 TB/yr of wide, field-queryable telemetry with high availability and low latency, and don't need ACID.
- It satisfies the profile: distributed NoSQL stores built for massive write volume and per-field reads.

### Exam shortcut

If you see:
- huge-volume IoT/telemetry, ACID not required
- high availability + low latency, query individual fields
- pick the scalable NoSQL stores

Think: **HBase / Cassandra / MongoDB** (skip Redis, MySQL, HDFS+Hive)

**Tiny mental image:** the fleet of vans built to scale, not the single armored truck or the warehouse forklift.

**Final answer:** B. HBase'''

E["test_8_q10"] = '''### Step 4: Choose the answer

- A failover replica in another zone of the same region gives Cloud SQL automatic high availability if the primary zone fails.
- It satisfies the requirement: zone-failure resilience with automatic failover, not just read scaling or cross-region DR.

### Exam shortcut

If you see:
- Cloud SQL high availability against a zone failure
- automatic failover within a region
- distinguish failover replica vs read replica

Think: **Cloud SQL HA = failover replica in another zone, same region**

**Tiny mental image:** a standby twin in the next room that takes over instantly if the first one trips.

**Final answer:** B. Create a Cloud SQL instance in one zone, and create a failover replica in another zone within the same region.'''

E["test_10_q19"] = '''### Step 4: Choose the answer

- A Dataflow job that reads the data, corrects the out-of-range values, and writes to a new Cloud Storage dataset fixes the errors while preserving the originals.
- It satisfies both: corrected data is produced and the raw data is retained untouched for compliance.

### Exam shortcut

If you see:
- correct/clean data but keep the original for compliance
- never overwrite the source
- batch transform in Cloud Storage

Think: **Dataflow transform → write to a NEW dataset (preserve source)**

**Tiny mental image:** edit a photocopy and file it alongside the sealed original, never marking the original.

**Final answer:** A. Use a Dataflow workflow to read the data from Cloud Storage, identify and correct values outside the expected range, and write the updated data to a new dataset in Cloud Storage'''

append_entries(E)

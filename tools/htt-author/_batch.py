from lib import append_entries

E = {}

E["test_2_q29"] = '''### Step 4: Choose the answer

- A project per initiative grouped in a folder, with policies on the folder, isolates resources while enforcing the shared constraints in one place.
- It satisfies both needs: per-initiative separation of VMs/buckets/functions and uniform, inherited compliance policy.

### Exam shortcut

If you see:
- several initiatives sharing one set of constraints
- want isolation plus inherited policy
- "where do I attach the org policy?"

Think: **project per workload, grouped in a folder, policy on the folder**

**Tiny mental image:** separate offices on the same floor, with the building's rules posted at the floor's entrance.

**Final answer:** A. Use a project for each initiative and place those projects in a folder. Attach policies to the folder to enforce constraints.'''

E["test_2_q38"] = '''### Step 4: Choose the answer

- AES-256 is the symmetric cipher Google uses for data-at-rest encryption at the infrastructure level.
- It satisfies the question precisely: a strong, standard bulk-encryption algorithm, not a key-exchange or legacy one.

### Exam shortcut

If you see:
- "encryption at rest" algorithm on Google Cloud
- bulk symmetric encryption of stored data
- distractors mixing in asymmetric/legacy ciphers

Think: **AES-256**

**Tiny mental image:** a heavy-duty 256-bit vault door that every block of stored data sits behind by default.

**Final answer:** B. AES256'''

E["test_2_q41"] = '''### Step 4: Choose the answer

- Archive class is the lowest-cost Cloud Storage tier, built for data accessed less than once a year but retained for years.
- It satisfies the goal: cheap long-term retention of audit records that are unlikely to ever be read.

### Exam shortcut

If you see:
- retain for years, accessed rarely / "almost never"
- lowest storage cost is the priority
- compliance archive

Think: **Cloud Storage Archive class**

**Tiny mental image:** deep cold storage in the back of the warehouse - cheapest shelf, slowest to reach.

**Final answer:** A. Cloud Storage Archive class storage'''

E["test_2_q49"] = '''### Step 4: Choose the answer

- Cloud EKM lets BigQuery use encryption keys held in an external key manager outside the public cloud, with minimal operational overhead.
- It satisfies both constraints: keys stay off the cloud provider, yet integrate natively with BigQuery encryption.

### Exam shortcut

If you see:
- keys must live outside Google Cloud / external key manager
- still want native BigQuery (or GCP) encryption integration
- minimize key-management overhead

Think: **Cloud External Key Manager (Cloud EKM)**

**Tiny mental image:** the bank stores your valuables, but the only key hangs in your own house across the street.

**Final answer:** D. Use Cloud EKM for external key management'''

E["test_3_q12"] = '''### Step 4: Choose the answer

- DLP format-preserving encryption tokenizes the GIIN reversibly, so reps with the key can recover the original when needed.
- It satisfies both halves: the column is redacted for everyone, yet authorized staff can de-tokenize on demand.

### Exam shortcut

If you see:
- redact/mask sensitive values but allow authorized re-identification later
- need reversibility (not a one-way hash)
- keep the original format/structure

Think: **Cloud DLP format-preserving encryption (FPE) tokens**

**Tiny mental image:** a coat-check tag - you hand over the coat, but the matching ticket gets it back.

**Final answer:** D. Before loading the data into BigQuery, use Cloud Data Loss Prevention (DLP) to replace the input values with a format-preserving encryption token'''

E["test_3_q13"] = '''### Step 4: Choose the answer

- Multiple service accounts attached to IAM groups grant each group exactly the access it needs, the recommended least-privilege pattern.
- It satisfies the mandate: scalable, auditable, group-based control over PII access rather than per-user or shared identities.

### Exam shortcut

If you see:
- control access for many users/teams to sensitive data
- "Google-recommended" service-account practice
- avoid shared or per-individual identities

Think: **IAM groups with appropriately-scoped service accounts**

**Tiny mental image:** department badges open only their own doors, instead of one master key copied for everyone.

**Final answer:** D. Use Cloud Storage to comply with major data protection standards. Use multiple service accounts attached to IAM groups to grant the appropriate access to each group'''

E["test_3_q14"] = '''### Step 4: Choose the answer

- Hosting the dependencies in a Cloud Storage bucket inside the VPC perimeter lets the init action fetch them without any internet access.
- It satisfies both constraints: dependencies install at startup while the no-internet security policy stays intact.

### Exam shortcut

If you see:
- nodes must install packages but cannot reach the internet
- an existing Dataproc initialization action
- private/VPC-only connectivity

Think: **stage dependencies in Cloud Storage within the VPC perimeter**

**Tiny mental image:** stock the pantry inside the locked compound so the cook never has to leave to shop.

**Final answer:** C. Store all dependencies in a Cloud Storage bucket located within your VPC security perimeter'''

E["test_3_q17"] = '''### Step 4: Choose the answer

- CSEK keeps the key entirely under your control, and storing it in a separate project only the security team can reach upholds "Trust No One."
- It satisfies TNO: Google never persists the key, and access is locked to a tightly-scoped custodian project.

### Exam shortcut

If you see:
- "Trust No One" / provider staff must not be able to decrypt
- you supply and custody the key yourself
- archival upload to Cloud Storage

Think: **customer-supplied encryption keys (CSEK), key held off-platform / in an isolated custody location**

**Tiny mental image:** you mail a locked box to the warehouse but keep the only key in a vault they can't enter.

**Final answer:** D. Specify customer-supplied encryption key (CSEK) in the .boto configuration file. Use gsutil cp to upload each archival file to the Cloud Storage bucket. Save the CSEK in a different project that only the security team can access.'''

E["test_3_q28"] = '''### Step 4: Choose the answer

- A DLP format-preserving cryptographic token produces a consistent pseudonym, so the same input always maps to the same token and joins still work.
- It satisfies both requirements: PII is masked in the real-time stream while referential integrity is preserved.

### Exam shortcut

If you see:
- mask/de-identify PII but still need to join or correlate records
- "maintain referential integrity"
- streaming/real-time de-identification

Think: **DLP format-preserving / deterministic tokenization (pseudonymization)**

**Tiny mental image:** swap every name for the same codename everywhere, so the story still connects.

**Final answer:** D. Create a pseudonym by replacing the PII data with a cryptographic format-preserving token to maintain referential integrity'''

E["test_4_q5"] = '''### Step 4: Choose the answer

- A Cloud Function reading the Pub/Sub topics and calling the DLP API inspects each message inline and quarantines anything with PII.
- It satisfies the goal: a scalable, cloud-native managed pipeline that stops PII before it reaches analytics.

### Exam shortcut

If you see:
- inspect/stop PII in transit through a pipeline
- "cloud-native managed services", no VMs to run
- event-driven on Pub/Sub

Think: **Cloud Function + Cloud DLP inspection, quarantine on match**

**Tiny mental image:** a mail scanner that pulls suspicious envelopes off the belt before they reach the office.

**Final answer:** D. Build a Cloud Function that reads the topics and makes a call to the Cloud Data Loss Prevention (Cloud DLP) API. Use the tagging and confidence levels to either pass or quarantine the data in a bucket for review.'''

E["test_4_q7"] = '''### Step 4: Choose the answer

- Precomputing predictions in Dataflow and serving them from Bigtable gives single-key lookups well under 100 ms.
- It satisfies the latency SLA for per-user-ID reads that a live BigQuery query cannot reliably meet.

### Exam shortcut

If you see:
- serve precomputed results by key with very low latency (<100 ms)
- single-row lookups for a REST API
- BigQuery ML predictions feeding online serving

Think: **batch-score in Dataflow, serve from Bigtable**

**Tiny mental image:** bake all the answers ahead of time and file them so each lookup is just opening the right drawer.

**Final answer:** D. Create a Dataflow pipeline using BigQueryIO to read predictions for all users from the query. Write the results to Bigtable using BigtableIO. Grant the Bigtable Reader role to the application service account so that the application can read predictions for individual users from Bigtable'''

E["test_4_q47"] = '''### Step 4: Choose the answer

- A resource hierarchy lets policies set high up (org/folder) inherit down to projects, drastically cutting the number of policies to manage.
- It satisfies the goal: central IT inherits access everywhere and per-project control stays simple.

### Exam shortcut

If you see:
- many projects, "minimize the number of policies"
- central team needs access to everything
- simplify access-control management

Think: **resource hierarchy + IAM policy inheritance**

**Tiny mental image:** set house rules once at the front gate and every room inherits them automatically.

**Final answer:** B. Implement a resource hierarchy to leverage access control policy inheritance.'''

E["test_4_q53"] = '''### Step 4: Choose the answer

- A dataset per department with leads as WRITER (create/update tables) and analysts as READER (query only) maps roles exactly to duties.
- It satisfies all three rules: per-department isolation, leads who can modify, analysts who can only read.

### Exam shortcut

If you see:
- per-team data isolation in BigQuery
- some users edit tables, others only query
- map roles to dataset, not project

Think: **dataset per team; WRITER for editors, READER for query-only**

**Tiny mental image:** each department's filing cabinet - leads have the edit key, analysts have a read-only window.

**Final answer:** B. Create a dataset for each department. Assign the department leads the WRITER role, and assign the data analysts the READER role on their dataset.'''

E["test_4_q56"] = '''### Step 4: Choose the answer

- Analytics Hub shares a live, governed view of the original dataset, so consumers always see current data with no copies to maintain.
- It satisfies both goals: cost-effective (no duplicated storage or ETL) and always up-to-date, with auditing built in.

### Exam shortcut

If you see:
- share BigQuery data with external/third parties
- must stay always up-to-date, cost-effective
- avoid exporting/copying data

Think: **Analytics Hub (in-place data sharing)**

**Tiny mental image:** publishing a live web page everyone reads, instead of mailing out copies that go stale.

**Final answer:** A. Control data access with Analytics Hub and grant third-party companies access to the original dataset while monitoring and auditing data access.'''

E["test_5_q3"] = '''### Step 4: Choose the answer

- Creating keys in Cloud KMS and using them to encrypt the Compute Engine data gives you full create/rotate/destroy control (CMEK).
- It satisfies the requirement: customer-managed key lifecycle over data at rest on the VMs.

### Exam shortcut

If you see:
- encrypt at rest with keys you create, rotate, and destroy
- data on Compute Engine / self-managed services
- customer control over key lifecycle

Think: **CMEK with Cloud KMS-generated keys**

**Tiny mental image:** you cut the locks yourself and can re-key or shred them whenever you like.

**Final answer:** B. Create encryption keys in Cloud Key Management Service. Use those keys to encrypt your data in all of the Compute Engine cluster instances.'''

E["test_5_q5"] = '''### Step 4: Choose the answer

- Batch-scoring all users in Dataflow and serving from Bigtable delivers per-user-ID lookups under 100 ms, which a live BigQuery query cannot guarantee.
- It satisfies the SLA: low-latency online serving backed by a precomputed key-value store.

### Exam shortcut

If you see:
- serve BigQuery ML predictions to a REST API
- single user-ID lookups under ~100 ms
- need an online serving layer, not ad hoc queries

Think: **precompute in Dataflow, serve from Bigtable**

**Tiny mental image:** prep every order in advance and shelve it, so checkout is just grabbing the labeled bag.

**Final answer:** D. Create a Cloud Dataflow pipeline using BigQueryIO to read predictions for all users from the query. Write the results to Cloud Bigtable using BigtableIO. Grant the Bigtable Reader role to the application service account so that the application can read predictions for individual users from Cloud Bigtable.'''

E["test_5_q19"] = '''### Step 4: Choose the answer

- Primitive (basic) roles bundle viewing and querying together, so "view datasets but not run queries" is the one scenario they cannot express.
- It satisfies the question's "not possible" framing: that separation needs predefined roles or an authorized view, not primitive roles.

### Exam shortcut

If you see:
- "which is NOT possible with primitive/basic roles"
- a request to split *view* from *query* (or similar fine-grained split)
- coarse owner/editor/viewer only

Think: **primitive roles are coarse - they can't separate view from query**

**Tiny mental image:** a light switch with only on/off can't give you a dimmer setting.

**Final answer:** C. Give a user access to view all datasets in a project, but not run queries on them.'''

E["test_5_q21"] = '''### Step 4: Choose the answer

- Introducing a resource hierarchy lets IAM policies inherit downward, so central IT gets blanket access and the total policy count drops sharply.
- It satisfies the goal: simpler access management across many projects via inheritance rather than per-resource rules.

### Exam shortcut

If you see:
- sprawling projects, "minimize number of policies"
- central IT needs access to all projects
- ad hoc cross-project sharing

Think: **resource hierarchy + policy inheritance (plus groups)**

**Tiny mental image:** post one rulebook at the org's front door and every folder and project reads from it.

**Final answer:** B. Introduce resource hierarchy to leverage access control policy inheritance.'''

E["test_5_q43"] = '''### Step 4: Choose the answer

- An authorized view selecting only the first three columns exposes exactly those columns while hiding the underlying table.
- It satisfies the goal: column-scoped read access that primitive or predefined roles alone cannot provide.

### Exam shortcut

If you see:
- grant access to only certain columns/rows of a table
- hide the base table, expose a filtered projection
- column- or row-level sharing in BigQuery

Think: **authorized view (column/row scoping)**

**Tiny mental image:** a window cut to show only three shelves of the cabinet, the rest stays behind the wall.

**Final answer:** C. Authorized view'''

E["test_6_q15"] = '''### Step 4: Choose the answer

- Running the automated job as a least-privilege service account that can read the batch files and write to BigQuery secures the workload without over-granting.
- It satisfies the goal: unattended automation with only the permissions the job actually needs.

### Exam shortcut

If you see:
- automate a job currently run manually as Owner
- non-public data, scheduled/unattended execution
- "securely run" / least privilege

Think: **dedicated service account scoped to exactly the job's reads and writes**

**Tiny mental image:** give the night-shift robot a keycard for just the two doors it uses, not the master key.

**Final answer:** C. Use a service account with the ability to read the batch files and to write to BigQuery'''

append_entries(E)

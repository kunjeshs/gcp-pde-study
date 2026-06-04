from lib import append_entries

E = {}

E["test_6_q20"] = '''### Step 4: Choose the answer

- A BigQuery dataset restricted to authorized personnel, paired with Data Access audit logs, records every read in a tamper-proof trail.
- It satisfies the mandate: native, immutable logging of who accessed the regulated data, no custom plumbing.

### Exam shortcut

If you see:
- "auditable record of access" to regulated data
- need to log *who read* the data
- analytical data

Think: **BigQuery + Data Access audit logs**

**Tiny mental image:** a turnstile that stamps everyone who even glances at the restricted file.

**Final answer:** B. In a BigQuery dataset that is viewable only by authorized personnel, with the Data Access log used to provide the auditability.'''

E["test_6_q50"] = '''### Step 4: Choose the answer

- Giving the consultant an anonymized sample in a separate project lets them build the transformation without ever touching real user PII.
- It satisfies privacy: the external party works on realistic-but-fake data, isolated from production.

### Exam shortcut

If you see:
- external/untrusted party needs to develop against your data
- private user data / PII must stay protected
- they only need representative data, not real records

Think: **anonymized/sample dataset in an isolated project**

**Tiny mental image:** hand the contractor a crash-test dummy, not a real patient.

**Final answer:** D. Create an anonymized sample of the data for the consultant to work with in a different project.'''

E["test_7_q8"] = '''### Step 4: Choose the answer

- A service account granted dataset access lets the application query BigQuery on users' behalf, without users authenticating or getting dataset access.
- It satisfies all constraints: secure programmatic access, no per-user auth, no direct dataset grants to people.

### Exam shortcut

If you see:
- an app queries data on behalf of users
- users must NOT authenticate directly or get dataset access
- secure service-to-service access

Think: **service account with dataset access (app uses the SA)**

**Tiny mental image:** the app is a licensed broker - customers ask it, it holds the only account at the exchange.

**Final answer:** C. Create a service account and grant dataset access to that account. Use the service account‘s private key to access the dataset'''

E["test_7_q13"] = '''### Step 4: Choose the answer

- Loading each client into its own dataset, restricting that dataset to approved users, and applying the right IAM roles isolates clients from one another.
- It satisfies the goal: per-client data boundaries with appropriate, auditable access for each client's users.

### Exam shortcut

If you see:
- multiple tenants/clients must not see each other's data
- BigQuery with direct query access per client
- "appropriate access" / least privilege per tenant

Think: **dataset per client + restrict to approved users + IAM roles**

**Tiny mental image:** give each client their own locked room rather than a shared table with name cards.

**Final answer:** B. Load data into a different dataset for each client.'''

E["test_7_q29"] = '''### Step 4: Choose the answer

- Recreating the events view over events_partitioned in standard SQL makes it consumable by the ODBC driver (with a service account for auth).
- It satisfies the connection need: ODBC works against standard-SQL objects, and the partition-pruning cost savings are preserved.

### Exam shortcut

If you see:
- ODBC/JDBC connecting to BigQuery
- an existing legacy-SQL view in the way
- need driver compatibility plus authentication

Think: **standard-SQL view (+ service account for the driver)**

**Tiny mental image:** translate the old document into the language the new reader actually understands.

**Final answer:** C. Create a new view over events_partitioned using standard SQL'''

E["test_7_q42"] = '''### Step 4: Choose the answer

- An authorized view exposes the aggregates while shielding the user-level tables, with no extra stored copy, and each project pays for its own queries.
- It satisfies every constraint: controlled access, minimal storage, and consumer-borne analysis cost.

### Exam shortcut

If you see:
- share aggregates while protecting underlying user-level data
- minimize storage (no copies)
- consuming projects pay for their own queries

Think: **BigQuery authorized view**

**Tiny mental image:** a service window that hands out the summary plate without letting anyone into the kitchen.

**Final answer:** A. Create and share an authorized view that provides the aggregate results.'''

E["test_7_q51"] = '''### Step 4: Choose the answer

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

E["test_8_q21"] = '''### Step 4: Choose the answer

- A view presenting just the needed columns/rows to the visualization tool simplifies what the sales team queries without duplicating storage.
- It satisfies "most cost-effective": no extra stored table, smaller scans, and a cleaner interface for users.

### Exam shortcut

If you see:
- users overwhelmed by too many columns / costly broad queries
- want a simpler, cheaper interface for a BI tool
- avoid copying data

Think: **a BigQuery view (curated projection)**

**Tiny mental image:** a tidy menu of the dishes people actually order, instead of the whole pantry inventory.

**Final answer:** C. Create a view on the table to present to the virtualization tool.'''

E["test_10_q20"] = '''### Step 4: Choose the answer

- Data Catalog is the managed metadata service for recording and later retrieving information about the PII analysis (tags, classifications, locations).
- It satisfies the goal: easy discovery and retrieval of metadata describing the analysis, separate from the data itself.

### Exam shortcut

If you see:
- store/retrieve *metadata* about data or analysis results
- tag, classify, or discover sensitive-data findings
- a managed catalog, not a data store

Think: **Data Catalog**

**Tiny mental image:** the library's card catalog - it tells you about the books without being the books.

**Final answer:** A. Data Catalog'''

E["test_13_q5"] = '''### Step 4: Choose the answer

- Dataflow calling Cloud DLP to mask sensitive fields, then writing to BigQuery, keeps the data useful for analysis while meeting privacy rules.
- It satisfies both: masked (not deleted) data preserves analytical value, and DLP enforces the privacy requirement.

### Exam shortcut

If you see:
- preprocess restricted data for analytics while staying compliant
- mask/de-identify but keep the data usable
- pipeline from Cloud Storage to BigQuery

Think: **Dataflow + Cloud DLP masking, land in BigQuery**

**Tiny mental image:** redact the secret names with a marker but leave the rest of the report readable.

**Final answer:** A. Use Dataflow and the Cloud Data Loss Prevention API to mask sensitive data. Write the processed data in BigQuery.'''

E["test_13_q6"] = '''### Step 4: Choose the answer

- Leaving the Authorized Networks list empty and running the Cloud SQL Auth proxy on every app gives secure connections despite changing public IPs.
- It satisfies the goal: no fragile IP allowlists to maintain, just IAM-authorized, encrypted proxy connections.

### Exam shortcut

If you see:
- clients with dynamic/changing public IPs connecting to Cloud SQL
- avoid maintaining Authorized Networks
- secure, encrypted connection

Think: **Cloud SQL Auth proxy, empty Authorized Networks**

**Tiny mental image:** an escort that verifies each guest by ID, so you never have to keep a list of their home addresses.

**Final answer:** C. Leave the Authorized Network empty. Use Cloud SQL Auth proxy on all applications.'''

E["test_13_q20"] = '''### Step 4: Choose the answer

- Granting compute.networkUser to the service account that runs the Dataflow pipeline lets its workers attach to the Shared VPC subnetwork.
- It satisfies deployment: the executing identity can use the shared network the network team provided.

### Exam shortcut

If you see:
- run Dataflow (or workers) on a Shared VPC subnet
- "which identity needs compute.networkUser?"
- host-project network shared to a service project

Think: **compute.networkUser on the pipeline's worker service account**

**Tiny mental image:** the work crew needs a gate pass to the shared yard, not just the foreman.

**Final answer:** B. Assign the compute.networkUser role to the service account that executes the Dataflow pipeline.'''

E["test_13_q26"] = '''### Step 4: Choose the answer

- A new key, a new bucket with that key as the default CMEK, and copying objects without specifying a key re-encrypts everything and forces future CMEK protection.
- It satisfies all three: retires the compromised key, re-encrypts data, and prevents any non-CMEK writes going forward.

### Exam shortcut

If you see:
- compromised KMS key, must re-encrypt and retire it
- guarantee future objects are CMEK-protected
- Cloud Storage default encryption key

Think: **new key + new bucket with default CMEK, copy without specifying a key**

**Tiny mental image:** move everything into a new vault whose lock is automatic, then throw away the old compromised key.

**Final answer:** D. Create a new Cloud KMS key. Create a new Cloud Storage bucket configured to use the new key as the default CMEK key. Copy all objects from the old bucket to the new bucket without specifying a key.'''

E["test_13_q37"] = '''### Step 4: Choose the answer

- A public-visibility tag template lets all employees search by has_sensitive_data, while bigquery.dataViewer for HR on the sensitive tables restricts who sees the rows.
- It satisfies both with minimal overhead: searchable tags for everyone, data access only for HR, no extra tag-viewer grants.

### Exam shortcut

If you see:
- everyone can search/discover by a tag, but only some can read the data
- "minimize configuration overhead"
- Data Catalog tag template + BigQuery access

Think: **public tag template + dataViewer to the privileged group on sensitive tables**

**Tiny mental image:** the catalog card is on the open shelf for all to find; only HR has the key to that specific drawer.

**Final answer:** C. Create the gdpr tag template with public visibility. Assign the bigquery.dataViewer role to the HR group on the tables that contain sensitive data.'''

E["test_13_q44"] = '''### Step 4: Choose the answer

- Data Viewer on the shared dataset (read-only) plus a per-analyst dataset with Data Editor scoped to that dataset gives shared visibility and private workspaces.
- It satisfies both goals: nobody edits the shared data, and each analyst has an isolated space others can't see.

### Exam shortcut

If you see:
- one shared read-only dataset plus private per-user workspaces
- scope roles at the *dataset* level, not the project
- view-but-not-edit shared, edit-own-private

Think: **dataViewer on shared dataset + dataEditor on each analyst's own dataset**

**Tiny mental image:** a shared reference library (look, don't write) plus a personal locked desk for each person.

**Final answer:** C. Give analysts the BigQuery Data Viewer role on the shared dataset. Create a dataset for each analyst, and give each analyst the BigQuery Data Editor role at the dataset level for their assigned dataset.'''

E["test_13_q56"] = '''### Step 4: Choose the answer

- An Analytics Hub private exchange publishing the sales dataset gives business units self-service, live access with no copies to maintain.
- It satisfies all three: self-serving subscriptions, low maintenance, and cost-effective in-place sharing.

### Exam shortcut

If you see:
- share a BigQuery dataset org-wide, self-service
- low-maintenance, cost-effective, always current
- no per-consumer copies

Think: **Analytics Hub private exchange**

**Tiny mental image:** publish one live listing everyone can subscribe to, instead of mailing copies to each team.

**Final answer:** A. Create an Analytics Hub private exchange, and publish the sales dataset.'''

E["test_13_q60"] = '''### Step 4: Choose the answer

- A BigLake table over the Cloud Storage data, with Data Catalog policy tags for column security, supports Spark and SQL in place and scales into a data mesh.
- It satisfies all of it: no costly reload, fine-grained column security, and open processing via the Spark-BigQuery connector.

### Exam shortcut

If you see:
- query Cloud Storage data with Spark AND SQL in place
- column-level security, cost-effective, data-mesh-ready
- avoid loading/duplicating into native tables

Think: **BigLake table + Data Catalog policy tags**

**Tiny mental image:** put a smart, governed window over the existing warehouse instead of rebuilding the warehouse.

**Final answer:** B. 1. Define a BigLake table. 2. Create a taxonomy of policy tags in Data Catalog. 3. Add policy tags to columns. 4. Process with the Spark-BigQuery connector or BigQuery SQL.'''

E["test_14_q5"] = '''### Step 4: Choose the answer

- Having each team publish to Analytics Hub and subscribe to others lets teams keep full ownership while exchanging data with no copies or pipelines.
- It satisfies the goal: decentralized control plus low-ops, low-cost in-place data exchange.

### Exam shortcut

If you see:
- many teams own their data but must share/exchange it
- minimize operational tasks and cost
- query within each team's own project

Think: **Analytics Hub publish/subscribe (data mesh)**

**Tiny mental image:** a shared marketplace where each stall owns its goods and others subscribe to the live feed.

**Final answer:** C. Ask each team to publish their data in Analytics Hub. Direct the other teams to subscribe to them.'''

E["test_14_q17"] = '''### Step 4: Choose the answer

- Cloud Storage plus multiple service accounts attached to IAM groups grants each group exactly its PII access, the recommended least-privilege pattern.
- It satisfies the mandate: access-controlled, auditable, group-scoped handling of regulated PII.

### Exam shortcut

If you see:
- control access to PII for many users/teams
- "Google-recommended" service accounts
- avoid shared or per-individual identities

Think: **IAM groups with appropriately-scoped service accounts**

**Tiny mental image:** department badges open only their own doors, not one master key copied for all.

**Final answer:** D. Use Cloud Storage to comply with major data protection standards. Use multiple service accounts attached to IAM groups to grant the appropriate access to each group.'''

E["test_14_q27"] = '''### Step 4: Choose the answer

- The analytics team still sees sensitive columns because they hold the Fine-Grained Reader role on the policy tags; removing it (and enforcing access control in the taxonomy) closes the gap.
- It satisfies the fix: policy-tag enforcement only restricts users who lack the Fine-Grained Reader role.

### Exam shortcut

If you see:
- policy tags set but a group can still read protected columns
- column-level security via Data Catalog taxonomy
- "why isn't the restriction taking effect?"

Think: **remove Fine-Grained Reader on the tags + enforce access control in the taxonomy**

**Tiny mental image:** the lock is installed, but they still hold a copy of the key - take the key back.

**Final answer:** B. Ensure that the data analytics team members do not have the Data Catalog Fine-Grained Reader role for the policy tags.'''

append_entries(E)

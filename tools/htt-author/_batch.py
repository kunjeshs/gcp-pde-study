from lib import append_entries

E = {}

E["test_12_q5"] = '''### Step 4: Choose the answer

- A BigQuery dataset restricted to authorized personnel plus Data Access logs gives both access control and a regulator-grade audit trail.
- It satisfies the mandate directly: native, immutable logs of every read, with no custom plumbing to maintain.

### Exam shortcut

If you see:
- "auditable record of access" / regulatory access trail
- need to know *who read* the data, not just who changed config
- analytical data already in scope

Think: **BigQuery + Data Access audit logs**

**Tiny mental image:** a library where the turnstile automatically stamps every visitor who even *looks* at a restricted book.

**Final answer:** A. Should the data be stored in a BigQuery dataset that is viewable only by authorized personnel, with the Data Access log used to provide auditability.'''

E["test_10_q5"] = '''### Step 4: Choose the answer

- A service account with Google-managed keys lets the VM authenticate automatically with no exportable secret to protect.
- It meets every requirement: no personal credentials, least-privilege roles on the account, and zero key-file exposure.

### Exam shortcut

If you see:
- workload on Compute Engine needs to call Google APIs
- "don't use my credentials" / "recommended practice"
- avoid storing/handling key files

Think: **attached service account + Google-managed keys**

**Tiny mental image:** giving the robot its own staff badge that the building reissues automatically, instead of photocopying yours.

**Final answer:** B. Create a service account and assign roles to the service account that are needed to execute the data transformation programs. Use Google managed keys to store both public and private portion of the service account keys.'''

E["test_11_q18"] = '''### Step 4: Choose the answer

- The Cloud SQL Auth proxy is purpose-built for secure production connections, handling encryption and IAM authorization transparently.
- It satisfies the requirement: no manual certs, no IP allowlists, just an authenticated, encrypted channel.

### Exam shortcut

If you see:
- connect securely to Cloud SQL from an app/VM
- avoid managing SSL certs or authorized networks
- "recommended best practice" for Cloud SQL auth

Think: **Cloud SQL Auth proxy**

**Tiny mental image:** a security escort that checks your badge and walks you through an already-locked corridor, so you never touch the keys.

**Final answer:** D. Cloud SQL Auth proxy'''

E["test_1_q28"] = '''### Step 4: Choose the answer

- A custom role with only the needed permissions grants precisely what maintainers require and excludes the rest.
- It satisfies the requirement and embodies least privilege, the practice the question is testing.

### Exam shortcut

If you see:
- predefined roles grant *more* than the task needs
- "least privilege" / "only the permissions needed"
- a specific, stable set of duties

Think: **custom IAM role**

**Tiny mental image:** tailoring a suit to fit instead of draping someone in three oversized coats.

**Final answer:** C. Create a custom role with only the permissions needed. This follows the principal of least privilege.'''

E["test_11_q37"] = '''### Step 4: Choose the answer

- `gcloud dataproc clusters create` is the only command with the correct group ordering and a real verb that accepts `--gce-pd-kms-key`.
- It satisfies the goal: provision a CMEK-encrypted Dataproc cluster from the command line.

### Exam shortcut

If you see:
- a gcloud command to stand up a Dataproc cluster
- a CMEK / `--gce-pd-kms-key` flag at provisioning time
- choices that scramble the noun order

Think: **`gcloud dataproc clusters create`** (group = dataproc clusters, verb = create)

**Tiny mental image:** address an envelope city-then-street, not street-then-city - the order is the whole point.

**Final answer:** A. gcloud dataproc clusters create'''

E["test_1_q50"] = '''### Step 4: Choose the answer

- DLP's re-identification risk analysis directly outputs quantified risk metrics over the quasi-identifiers.
- It satisfies the goal: a measurable, methodologically sound risk score with no custom modeling.

### Exam shortcut

If you see:
- quasi-identifiers (age, ZIP, gender) and re-identification worry
- need a *number*/score for the risk
- k-anonymity, l-diversity, k-map terminology

Think: **Cloud DLP re-identification risk analysis**

**Tiny mental image:** an actuary calculating the odds an "anonymous" survey could still point back to one person.

**Final answer:** D. Run a re-identification risk analysis using the Data Loss Prevention service.'''

E["test_2_q6"] = '''### Step 4: Choose the answer

- Granting Service Account User to Data Fusion gives it permission to act as the service account that runs Dataproc.
- It satisfies the fix: the impersonation the error names is now authorized.

### Exam shortcut

If you see:
- "not authorized to act as a service account"
- one service launching another (Data Fusion → Dataproc, Composer → workers)
- impersonation during provisioning

Think: **grant Service Account User (actAs) to the calling service**

**Tiny mental image:** a manager needs written permission to sign on behalf of a colleague before HR will process it.

**Final answer:** B. Grant the Service Account User role to Cloud Data Fusion.'''

E["test_2_q10"] = '''### Step 4: Choose the answer

- GDPR is the regulation triggered by collecting and profiling personal data of EU residents.
- It satisfies the scenario directly: EU individuals, detailed personal profiles, and automated recommendations all fall under GDPR.

### Exam shortcut

If you see:
- personal data of EU/EEA residents
- profiling, consent, "right to be forgotten"
- a company expanding into Europe

Think: **GDPR**

**Tiny mental image:** crossing into the EU, your data-handling passport gets stamped "GDPR applies here."

**Final answer:** C. GDPR'''

E["test_2_q11"] = '''### Step 4: Choose the answer

- Two function-based groups, each granted exactly its required roles, scale cleanly and keep least privilege intact.
- It satisfies both needs: analysts get read/write GCS plus BigQuery query, engineers additionally get bucket/lifecycle management.

### Exam shortcut

If you see:
- multiple teams with different permission needs
- "recommended practice" for managing access at scale
- onboarding/offboarding churn

Think: **IAM groups by job function, roles granted to groups**

**Tiny mental image:** hand out department keycards, not a custom-cut key for each new hire.

**Final answer:** B. Create a group for data analysts and a group for data engineers. Add the identities of data analysts to the data analyst group. Add the identities of the data engineers to the data engineer group. Grant roles to the data analyst group to allow access needed by data analysts. Grant roles to the data engineer group needed by the data engineers.'''

E["test_2_q15"] = '''### Step 4: Choose the answer

- A Resource Location Restriction org policy on topics forces all message storage into approved EU regions.
- It satisfies the GDPR concern centrally and preventively, not per-resource and after the fact.

### Exam shortcut

If you see:
- data must stay in specific regions (EU/data residency)
- an org-wide, preventive guarantee
- "Resource Location Restriction"

Think: **org policy: Resource Location Restriction (on the right resource)**

**Tiny mental image:** a geofence around the EU that simply refuses to let the data cross the border.

**Final answer:** A. Set a Resource Location Restriction organization policy to ensure all topics are stored only in acceptable regions.'''

E["test_2_q22"] = '''### Step 4: Choose the answer

- roles/dataproc.editor grants exactly stop/manage clusters and run workflow templates without IAM-admin power.
- It satisfies the task and stays close to least privilege using a maintained predefined role.

### Exam shortcut

If you see:
- need to modify/operate resources but not manage IAM
- "least privilege" with predefined roles available
- viewer too weak, admin too strong

Think: **the predefined editor role for that service**

**Tiny mental image:** a shift operator who can run and stop the machines but can't rewrite who's allowed in the building.

**Final answer:** A. roles/dataproc.editor'''

E["test_2_q23"] = '''### Step 4: Choose the answer

- An org policy constraint enforced in the resource hierarchy is the mechanism that can silently block service-account creation.
- It satisfies the symptom: the action fails for everyone in scope, independent of individual permissions.

### Exam shortcut

If you see:
- an action blocked despite seemingly correct IAM
- "constraints/..." org policy names
- restrictions set at org/folder/project level

Think: **organization policy constraint on the resource hierarchy**

**Tiny mental image:** a building-wide rule that overrides your personal keycard - the door just won't open for anyone.

**Final answer:** A. A policy has been applied to the resource hierarchy that enforces the constraints/iam.disableServiceAccountKeyCreation constraint.'''

append_entries(E)

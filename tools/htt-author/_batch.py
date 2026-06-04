from lib import append_entries

E = {}

E["test_13_q4"] = '''### Step 4: Choose the answer

- BigQuery Omni connects to the S3 data, and BigLake tables over both Cloud Storage and S3 let users query through BigQuery without any direct bucket access.
- It satisfies both: cross-cloud querying and fine-grained access control that hides the underlying storage.

### Exam shortcut

If you see:
- query data across clouds (GCS + S3) via BigQuery
- users must NOT get direct bucket access
- BigQuery Omni + BigLake (governed access)

Think: **BigQuery Omni + BigLake tables**

**Tiny mental image:** a governed SQL window over both clouds' buckets - no one reaches the files directly.

**Final answer:** A. Setup a BigQuery Omni connection to the AWS S3 bucket data. Create BigLake tables over the Cloud Storage and S3 data and query the data using BigQuery directly.'''

E["test_13_q30"] = '''### Step 4: Choose the answer

- Per-department projects with Dataplex mapping each department to a data lake (Cloud Storage buckets) and zones (BigQuery datasets), each department owning and sharing its data, implements a true data mesh.
- It satisfies the goal: decentralized, domain-owned data with unified governance and sharing.

### Exam shortcut

If you see:
- data mesh across departments/domains, structure GCS + BigQuery
- decentralized ownership with central governance
- map lakes/zones to data

Think: **Dataplex data mesh (lakes + zones, domain-owned)**

**Tiny mental image:** each department owns its own lake, all governed through one Dataplex map.

**Final answer:** D. 1. Create multiple projects for storage of the data for each of your departments applications. 2. Enable each department to create Cloud Storage buckets and BigQuery datasets. 3. In Dataplex, map each department to a data lake and the Cloud Storage buckets, and map the BigQuery datasets to zones. 4. Enable each department to own and share the data of their data lakes.'''

E["test_13_q48"] = '''### Step 4: Choose the answer

- Upgrading the Hive external table to a BigLake table and enabling metadata caching speeds queries over the many partitioned Cloud Storage files.
- It satisfies the goal: faster queries via cached metadata and BigLake's optimized access, no data movement.

### Exam shortcut

If you see:
- slow queries over many partitioned files in Cloud Storage / external Hive table
- speed up without migrating the data
- BigLake + metadata caching

Think: **BigLake table + metadata caching**

**Tiny mental image:** cache the file index so the query stops re-listing thousands of files each time.

**Final answer:** C. Upgrade the external table to a BigLake table. Enable metadata caching for the table.'''

E["test_13_q50"] = '''### Step 4: Choose the answer

- Exporting to a Cloud Storage Archive-class bucket with a locked retention policy stores the backup cheaply and immutably for 3 years, with an external table for occasional SQL access.
- It satisfies all: lowest-cost cold storage, immutable/locked retention, and infrequent SQL querying.

### Exam shortcut

If you see:
- cheap, immutable backup for N years, infrequent SQL access
- Archive storage class + locked retention policy
- external table for occasional queries

Think: **export to Archive bucket + locked retention + external table**

**Tiny mental image:** seal the old data in a cheap time-locked vault, with a SQL window for the rare peek.

**Final answer:** D. 1. Perform a BigQuery export to a Cloud Storage bucket with archive storage class. 2. Set a locked retention policy on the bucket. 3. Create a BigQuery external table on the exported files.'''

E["test_13_q53"] = '''### Step 4: Choose the answer

- Dataplex provides managed data management, discovery, lineage tracking, and quality validation across the scattered storage services, quickly and cost-effectively.
- It satisfies all four needs in one managed governance product, no custom build.

### Exam shortcut

If you see:
- data discovery + management + lineage + quality across many sources
- cost-optimized, quick to implement
- unified governance

Think: **Dataplex**

**Tiny mental image:** one governance fabric draped over all the scattered data, tracking and validating it.

**Final answer:** D. Use Dataplex to manage data, track data lineage, and perform data quality validation.'''

E["test_14_q2"] = '''### Step 4: Choose the answer

- Granting dataplex.dataOwner to engineers on the whole lake and dataplex.dataReader to analysts on the curated zone uses Dataplex's own roles to scope access correctly.
- It satisfies both: engineers get full lake access, analysts read only the curated zone.

### Exam shortcut

If you see:
- Dataplex data-mesh permissions, full vs curated access
- use dataplex.dataOwner / dataReader (not raw BigQuery/GCS roles)
- scope to lake vs zone

Think: **dataplex.dataOwner (lake) for engineers, dataplex.dataReader (curated zone) for analysts**

**Tiny mental image:** owners hold the whole lake; readers get a window into just the polished zone.

**Final answer:** A. 1. Grant the dataplex.dataOwner role to the data engineer group on the customer data lake. 2. Grant the dataplex.dataReader role to the analytic user group on the customer curated zone.'''

E["test_14_q37"] = '''### Step 4: Choose the answer

- Autoclass automatically moves objects between storage classes based on access, with no retrieval charges and instant availability, matching the unpredictable access and cost goals.
- It satisfies all: automatic cost optimization, no retrieval fees, instant access, and freedom to delete anytime.

### Exam shortcut

If you see:
- unknown/random access pattern, no retrieval charges, instant availability
- automatic, transparent storage-class optimization
- avoid manual lifecycle tuning

Think: **Cloud Storage Autoclass**

**Tiny mental image:** a self-tiering bucket that moves data to the cheapest class automatically, with no surprise retrieval bills.

**Final answer:** A. Create the bucket with the Autoclass storage class feature.'''

E["test_14_q45"] = '''### Step 4: Choose the answer

- Autoclass transparently tiers each object based on its actual access, minimizing cost for random, write-once access without any user-visible retrieval penalty.
- It satisfies the goal: automatic, invisible cost optimization for unpredictable access patterns.

### Exam shortcut

If you see:
- write-once objects, random/unknown access
- minimize cost transparently, no retrieval surprises
- automatic tiering

Think: **Cloud Storage Autoclass**

**Tiny mental image:** the bucket quietly shelves each object at the right cost tier based on how it's actually used.

**Final answer:** A. Create a Cloud Storage bucket with Autoclass enabled.'''

E["test_15_q27"] = '''### Step 4: Choose the answer

- Clustering the ingest-date-partitioned table on the package-tracking ID co-locates each package's records, speeding the geospatial lifecycle queries.
- It satisfies the goal: better performance via clustering on the queried entity, no re-partitioning.

### Exam shortcut

If you see:
- partitioned table slowing over time, queries by a high-cardinality ID
- improve performance with clustering
- cluster on the queried entity

Think: **cluster on the package-tracking ID**

**Tiny mental image:** group each package's events so its lifecycle query reads one tight block.

**Final answer:** B. Implement clustering in BigQuery on the package-tracking ID column.'''

E["test_14_q35"] = '''### Step 4: Choose the answer

- Creating one Dataplex lake per domain, a zone per team, and letting each domain manage its own lake decentralizes ownership and removes the central-team bottleneck.
- It satisfies the data-mesh goal: domain-owned data with federated governance, no central choke point.

### Exam shortcut

If you see:
- data mesh, central platform team is the bottleneck
- domains should own their data
- Dataplex lake-per-domain, zone-per-team, domain-managed

Think: **lake per domain, zone per team, domains self-manage**

**Tiny mental image:** give each business domain the keys to its own lake instead of routing everything through HQ.

**Final answer:** C. 1. Create one lake for each domain. Inside each lake, create one zone for each team. 2. Attach each of the BigQuery datasets created by the individual teams as assets to the respective zone. 3. Direct each domain to manage their own lakes data assets.'''

E["test_13_q42"] = '''### Step 4: Choose the answer

- A hopping (sliding) window in Dataflow continuously recomputes demand over a moving interval, and writing aggregates to Memorystore gives the real-time dashboard low-latency reads.
- It satisfies both: up-to-date rolling demand and fast serving for live driver redirection.

### Exam shortcut

If you see:
- real-time rolling/moving aggregation (demand, hotspots)
- low-latency serving for a live dashboard
- hopping/sliding window + Memorystore

Think: **Dataflow hopping window → Memorystore (real-time serving)**

**Tiny mental image:** a sliding view of recent demand pushed to a lightning-fast cache the dashboard reads.

**Final answer:** B. Group the data by using a hopping window in a Dataflow pipeline, and write the aggregated data to Memorystore.'''

E["test_1_q3"] = '''### Step 4: Choose the answer

- The Cloud Natural Language API's Entity Analysis extracts subjects/topics from blog posts as labels, with no ML expertise or training needed, shipping fast.
- It satisfies the constraints: a prebuilt API delivering topic labels quickly without building a model.

### Exam shortcut

If you see:
- generate topic/subject labels from text, no ML experience, fast
- prebuilt API, not a custom model
- entities = topics/labels

Think: **Cloud Natural Language API (Entity Analysis)**

**Tiny mental image:** call a ready-made text-understanding service and use the entities it returns as tags.

**Final answer:** A. Utilize the Cloud Natural Language API in the application and process the generated Entity Analysis as labels'''

E["test_1_q6"] = '''### Step 4: Choose the answer

- Overfitting is reduced by adding more training examples, using fewer features, and increasing regularization strength.
- It satisfies the question: these three all push the model toward generalization.

### Exam shortcut

If you see:
- "ways to reduce overfitting"
- more data, fewer features, stronger regularization
- (decreasing data or regularization makes it worse)

Think: **more training data + fewer features + more regularization**

**Tiny mental image:** more examples, a simpler model, and a firmer hand to stop memorizing noise.

**Final answer:** A. Increase the number of training examples'''

E["test_1_q32"] = '''### Step 4: Choose the answer

- A quarantine bucket whose upload event triggers a Cloud Function calling the DLP API detects PII immediately and moves flagged files to the Classified Data bucket.
- It satisfies the goal: event-driven, immediate PII detection using a managed service (no custom model).

### Exam shortcut

If you see:
- detect PII on upload and act immediately
- event-driven (Cloud Function on object create), not hourly batch
- use DLP infotypes, not a custom ML model

Think: **quarantine bucket → Cloud Function → DLP API → move on detection**

**Tiny mental image:** every new file trips a scanner that checks for PII the instant it lands.

**Final answer:** C. Create a quarantine bucket for uploading, once a file is uploaded trigger a Cloud Function to call the Data Loss Prevention API to apply infotypes to detect PII. If PII is detected, move file to the Classified Data bucket.'''

E["test_1_q36"] = '''### Step 4: Choose the answer

- L1 (Lasso) regularization drives the weights of the least important features toward zero, effectively performing feature selection.
- It satisfies the goal: zero out unimportant features, which L2 (Ridge) only shrinks, not zeroes.

### Exam shortcut

If you see:
- push least-important feature weights to exactly zero
- automatic feature selection / sparsity
- L1/Lasso vs L2/Ridge

Think: **L1 (Lasso) regularization**

**Tiny mental image:** L1 prunes useless features down to zero; L2 just trims them a bit.

**Final answer:** A. L1 or Lasso Regression'''

E["test_10_q52"] = '''### Step 4: Choose the answer

- Adding more training instances gives the model more signal to learn from, raising both precision and recall.
- It satisfies the goal: improve generalization and predictive quality with more data (regularization/dropout fight overfitting, not low scores from too little data).

### Exam shortcut

If you see:
- low precision AND recall (underperforming model)
- more data improves learning
- regularization/dropout address overfitting, not underfitting

Think: **use more training instances**

**Tiny mental image:** show the model more examples so it actually learns the pattern.

**Final answer:** C. Use more training instances'''

E["test_1_q45"] = '''### Step 4: Choose the answer

- Vertex AI custom training is the managed service that lets the team bring and tune their own models, including manual hyperparameter tuning.
- It satisfies both: managed infrastructure plus full control to customize and tune.

### Exam shortcut

If you see:
- managed ML but full model customization + manual hyperparameter tuning
- bring your own training code
- not AutoML (hands-off) / BigQuery ML (SQL only)

Think: **Vertex AI custom training**

**Tiny mental image:** Google runs the gym, but you write the workout and tune every dial.

**Final answer:** A. Vertex AI custom training'''

E["test_2_q2"] = '''### Step 4: Choose the answer

- L2 regularization penalizes large weights during training, reducing overfitting so the model generalizes better in production.
- It satisfies the goal: a training-time technique that curbs overfitting (gradient descent/backprop are just training mechanics).

### Exam shortcut

If you see:
- model overfits (great in validation, poor in production)
- training-time technique to reduce overfitting
- regularization

Think: **L2 regularization**

**Tiny mental image:** a penalty that discourages the model from over-trusting any single weight.

**Final answer:** A. L2 Regularization'''

E["test_2_q9"] = '''### Step 4: Choose the answer

- Kubeflow runs ML workflows natively on Kubernetes, letting the team reuse their existing Kubernetes expertise.
- It satisfies the goal: ML pipelines on Kubernetes, leveraging their container skills.

### Exam shortcut

If you see:
- ML pipelines/workflows on Kubernetes
- reuse existing Kubernetes/GKE expertise
- portable ML orchestration

Think: **Kubeflow**

**Tiny mental image:** ML pipelines that live right inside the Kubernetes the team already runs.

**Final answer:** C. Kubeflow'''

E["test_2_q14"] = '''### Step 4: Choose the answer

- BigQuery ML lets SQL-proficient analysts build and train models directly on the relational data using SQL, with no Python/Java needed.
- It satisfies both: ML on ~1 TB of relational data and an SQL-only workflow.

### Exam shortcut

If you see:
- analysts know SQL but not Python/Java
- build ML models on relational/warehouse data
- ML inside the database

Think: **BigQuery ML**

**Tiny mental image:** train models with the SQL the analysts already speak, right where the data lives.

**Final answer:** C. BigQuery ML'''

append_entries(E)

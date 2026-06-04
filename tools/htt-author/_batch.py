from lib import append_entries

E = {}

E["test_14_q9"] = '''### Step 4: Choose the answer

- To fight overfitting, increase the training dataset and decrease the number of input features, both improving generalization.
- It satisfies the goal: more examples plus a simpler feature set reduces overfitting.

### Exam shortcut

If you see:
- model overfitting, improve on new data
- more data + fewer features
- simplify and add examples

Think: **more training data + fewer features**

**Tiny mental image:** show more examples and trim noisy features so it stops memorizing.

**Final answer:** B. Increase the size of the training dataset, and decrease the number of input features.'''

E["test_14_q10"] = '''### Step 4: Choose the answer

- Dialogflow implements the text-and-voice chatbot with no/low code by defining intents from the most common queries.
- It satisfies the goal: keyword/intent-driven conversational responses without building a custom NLP app.

### Exam shortcut

If you see:
- chatbot for text + voice, low/no-code
- train on keywords/intents
- Dialogflow

Think: **Dialogflow (define intents)**

**Tiny mental image:** map common questions to intents and let Dialogflow handle the conversation.

**Final answer:** D. Use Dialogflow to implement the chatbot, defining the intents based on the most common queries collected.'''

E["test_14_q20"] = '''### Step 4: Choose the answer

- A GPU accelerator speeds the TensorFlow training cost-effectively and supports the custom ops that need a CPU, which TPUs don't accommodate.
- It satisfies both: faster training and compatibility with custom/partial-CPU operations.

### Exam shortcut

If you see:
- speed up TensorFlow training with custom ops (need CPU)
- TPU can't run arbitrary custom ops
- GPU vs TPU

Think: **GPU accelerator (custom ops → not TPU)**

**Tiny mental image:** a GPU turbo that still runs your hand-written operations; a TPU would choke.

**Final answer:** C. Train the model using a VM with a GPU hardware accelerator.'''

E["test_14_q57"] = '''### Step 4: Choose the answer

- With data processing finished, the next lifecycle step is to delineate which data goes to training versus testing.
- It satisfies the sequence: after prep comes the train/test split, before training and evaluation.

### Exam shortcut

If you see:
- ML lifecycle ordering, "what's next after data prep?"
- split into train/test before training
- then train → evaluate → deploy → monitor

Think: **define the train/test split (next step)**

**Tiny mental image:** before teaching the model, set aside the exam it won't see during study.

**Final answer:** C. Delineate what data will be used for testing and what will be used for training the model.'''

E["test_15_q10"] = '''### Step 4: Choose the answer

- Denormalizing the data and appending hourly status updates (instead of in-place UPDATEs) maximizes BigQuery performance and usability for the data science team.
- It satisfies both: fewer joins via denormalization and efficient append-only ingestion at PB scale.

### Exam shortcut

If you see:
- huge structured dataset into BigQuery for ML, maximize performance
- denormalize + append (no UPDATEs)
- avoid join-heavy normalized schema

Think: **denormalize + append-only status updates**

**Tiny mental image:** one wide table you keep adding rows to, not a web of tables you keep editing.

**Final answer:** A. Denormalize the data as must as possible.'''

E["test_15_q13"] = '''### Step 4: Choose the answer

- Cloud Vision AutoML trained on the existing labeled dataset produces a custom component classifier for the PoC within days.
- It satisfies both: custom recognition of 750 components and a fast, low-code build.

### Exam shortcut

If you see:
- custom image classification with a labeled dataset, fast PoC
- prebuilt Vision API can't recognize your specific items
- AutoML Vision on the existing data

Think: **Cloud Vision AutoML (existing dataset)**

**Tiny mental image:** feed your labeled photos into AutoML and get a custom recognizer in days.

**Final answer:** A. Use Cloud Vision AutoML with the existing dataset.'''

E["test_15_q16"] = '''### Step 4: Choose the answer

- Dialogflow Enterprise Edition interprets the customer voice commands and drives orders into the backend systems, integrating with assistants like Google Home.
- It satisfies the goal: a conversational agent that understands intent and connects to fulfillment.

### Exam shortcut

If you see:
- interpret voice commands / conversational ordering
- integrate with assistants, call backends
- intent + fulfillment

Think: **Dialogflow (Enterprise)**

**Tiny mental image:** a voice-order taker that understands the request and rings it up.

**Final answer:** C. Dialogflow Enterprise Edition'''

E["test_15_q25"] = '''### Step 4: Choose the answer

- Cloud GPUs accelerate training while supporting the custom C++ ops once you implement GPU kernel support, which TPUs can't easily run.
- It satisfies both: faster, lower-cost training and compatibility with custom operations.

### Exam shortcut

If you see:
- custom TensorFlow C++ ops, want acceleration, low cost
- TPUs can't run arbitrary custom ops
- GPU (with custom kernel support)

Think: **Cloud GPUs (after GPU kernel support)**

**Tiny mental image:** a GPU you can teach your custom operations to run on; a TPU won't take them.

**Final answer:** C. Use Cloud GPUs after implementing GPU kernel support for your customs ops.'''

E["test_15_q28"] = '''### Step 4: Choose the answer

- Higher error on the train set than the test set signals underfitting, so increasing model complexity (an extra layer, larger vocabularies/n-grams) improves performance.
- It satisfies the diagnosis: the model is too simple to fit the training data, so add capacity.

### Exam shortcut

If you see:
- train error higher than test error (underfitting)
- model too simple for the data
- add capacity/complexity

Think: **increase model complexity (underfitting fix)**

**Tiny mental image:** the model can't even ace the practice set - give it more capacity to learn.

**Final answer:** D. Increase the complexity of your model by, e.g., introducing an additional layer or increase sizing the size of vocabularies or n-grams used.'''

E["test_15_q37"] = '''### Step 4: Choose the answer

- One-hot encoding the city values into binary columns with SQL prepares the categorical predictor in the column form BigQuery ML needs, with minimal coding.
- It satisfies the goal: efficient, in-warehouse encoding of city names for training and serving.

### Exam shortcut

If you see:
- categorical string feature (city) for BigQuery ML
- represent as columns for training/serving, minimal code
- one-hot encoding

Think: **one-hot encode the categorical column in SQL**

**Tiny mental image:** turn each city into its own yes/no column the model can read.

**Final answer:** B. Use SQL in BigQuery to transform the state column using a one-hot encoding method, and make each city a column with binary values.'''

E["test_15_q43"] = '''### Step 4: Choose the answer

- Defining preprocessing in BigQuery ML's TRANSFORM clause makes the model auto-apply the same steps at prediction, so you can feed raw data without re-transforming - eliminating training/serving skew.
- It satisfies the goal: identical preprocessing at train and predict time, baked into the model.

### Exam shortcut

If you see:
- avoid training/serving skew in BigQuery ML
- predict on raw, untransformed data
- TRANSFORM clause auto-applies preprocessing

Think: **BigQuery ML TRANSFORM clause (auto-applied at prediction)**

**Tiny mental image:** bake the prep recipe into the model so it preps every input the same way automatically.

**Final answer:** A. When creating your model, use BigQuery‘s TRANSFORM clause to define preprocessing steps. At prediction time, use BigQuery‘s ML.EVALUATE clause without specifying any transformations on the raw input data.'''

E["test_16_q24"] = '''### Step 4: Choose the answer

- Hyperparameter tuning on the SVM is the principled way to raise AUC beyond the default-parameter baseline.
- It satisfies the goal: improve the existing model by optimizing its parameters.

### Exam shortcut

If you see:
- model trained with default parameters, improve a metric (AUC)
- tune before switching algorithms
- hyperparameter tuning

Think: **hyperparameter tuning**

**Tiny mental image:** dial in the model's settings before throwing it out for a different one.

**Final answer:** A. Perform hyperparameter tuning'''

E["test_16_q35"] = '''### Step 4: Choose the answer

- Running the existing Spark ML models on Dataproc, reading directly from BigQuery, migrates the retraining pipelines quickly with minimal change.
- It satisfies the goal: reuse Spark code on managed Dataproc against the BigQuery data.

### Exam shortcut

If you see:
- migrate existing Spark ML training, data in BigQuery
- reuse Spark code (don't rewrite in TensorFlow)
- Dataproc + BigQuery connector

Think: **Dataproc Spark ML reading from BigQuery**

**Tiny mental image:** run the same Spark models on managed Dataproc, pulling straight from the warehouse.

**Final answer:** C. Use Dataproc for training existing Spark ML models, but start reading data directly from BigQuery'''

E["test_16_q36"] = '''### Step 4: Choose the answer

- BigQuery natively supports geospatial (GIS) functions and ML predictions over the 40 TB dataset, and feeds a dashboard of at-risk ships by region.
- It satisfies all: storage at scale, native prediction (BigQuery ML), geospatial processing (GeoJSON/GIS), and BI.

### Exam shortcut

If you see:
- large analytics dataset needing native prediction (ML) + geospatial (GIS)
- dashboard/reporting on top
- SQL at TB+ scale

Think: **BigQuery (BigQuery ML + GIS)**

**Tiny mental image:** one warehouse that maps the ships, predicts delays, and feeds the dashboard.

**Final answer:** A. BigQuery'''

E["test_15_q3"] = '''### Step 4: Choose the answer

- Analytics Hub shares a live, governed view of the dataset with third parties, keeping data current with no copies and low cost.
- It satisfies both goals: minimal data-sharing cost (no duplication) and always-current data.

### Exam shortcut

If you see:
- share BigQuery data with external/third parties
- low cost, always current
- avoid exporting/copying

Think: **Analytics Hub (in-place sharing)**

**Tiny mental image:** publish one live listing they subscribe to, instead of mailing copies that go stale.

**Final answer:** A. Use Analytics Hub to control data access, and provide third party companies with access to the dataset.'''

E["test_4_q13"] = '''### Step 4: Choose the answer

- Creating monthly tables and exporting them compressed to Cloud Storage gives recoverable, low-cost backups that let you restore the affected month after a late-detected error.
- It satisfies both: granular recovery (per month) and minimized backup storage cost via compression in Cloud Storage.

### Exam shortcut

If you see:
- errors undetected for weeks, need granular recovery + cheap backups
- partition/shard by month, export compressed to Cloud Storage
- restore an affected period

Think: **monthly tables + compressed export to Cloud Storage**

**Tiny mental image:** keep each month's data in its own zipped box so you can restore just the bad month.

**Final answer:** B. Create separate tables for each month, then export, compress, and store the data in Cloud Storage'''

E["test_5_q13"] = '''### Step 4: Choose the answer

- Switching to flat-rate (capacity) pricing with reservations and a hierarchical priority model gives business units guaranteed slot allocations, fixing the contention without new projects.
- It satisfies both: predictable slot capacity and priority-based sharing across units.

### Exam shortcut

If you see:
- users starved of on-demand slots, avoid adding projects
- guarantee/allocate capacity across teams
- flat-rate / reservations + priorities

Think: **flat-rate pricing + reservation hierarchy/priorities**

**Tiny mental image:** buy a fixed pool of slots and divvy guaranteed shares to each business unit.

**Final answer:** C. Switch to flat-rate pricing and establish a hierarchical priority model for your projects.'''

E["test_5_q14"] = '''### Step 4: Choose the answer

- For autoscaling Dataflow, the maximum number of workers is the parameter that bounds how far the job can scale (and thus cost/throughput).
- It satisfies the goal: control the upper limit of the autoscaled worker pool.

### Exam shortcut

If you see:
- limit/control Dataflow autoscaling cost or throughput
- cap the worker pool
- maxNumWorkers

Think: **maximum number of workers**

**Tiny mental image:** set the hiring ceiling for the autoscaling crew.

**Final answer:** D. The maximum number of workers'''

E["test_6_q6"] = '''### Step 4: Choose the answer

- A BigQuery view that concatenates FirstName and LastName exposes FullName with no extra storage and no data rewrite, minimizing cost.
- It satisfies the goal: a derived FullName field computed at query time, cheaply.

### Exam shortcut

If you see:
- expose a derived/computed column, minimize cost
- no data duplication or UPDATE
- view computes it on the fly

Think: **a BigQuery view (computed column)**

**Tiny mental image:** a virtual column that stitches first + last names on demand, storing nothing extra.

**Final answer:** A. Create a view in BigQuery that concatenates the FirstName and LastName field values to produce the FullName.'''

E["test_6_q26"] = '''### Step 4: Choose the answer

- A small set of generalized charts and tables bound to criteria filters lets users select values dynamically, instead of pre-building one chart per combination.
- It satisfies the goal: flexible, filter-driven visualization that scales to many criteria combinations.

### Exam shortcut

If you see:
- many possible criteria combinations to visualize
- avoid one chart per combination
- generalized charts with interactive filters

Think: **generalized charts + criteria filters (parameterized)**

**Tiny mental image:** one flexible dashboard with dropdown filters, not a thousand static charts.

**Final answer:** B. Look through the current data and compose a small set of generalized charts and tables bound to criteria filters that allow value selection.'''

append_entries(E)

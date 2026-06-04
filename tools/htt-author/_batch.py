from lib import append_entries

E = {}

E["test_2_q16"] = '''### Step 4: Choose the answer

- Predicting a numeric quantity (how many products will sell) is a regression problem.
- It satisfies the question: continuous numeric output = regression, not classification.

### Exam shortcut

If you see:
- predict a number/quantity/amount
- continuous output
- regression vs classification

Think: **Regression (numeric prediction)**

**Tiny mental image:** forecasting a count on a dial, not sorting into yes/no buckets.

**Final answer:** A. Regression'''

E["test_2_q36"] = '''### Step 4: Choose the answer

- kubectl scale deployment with --replicas 4 sets the deployment to the desired four replicas.
- It satisfies the goal: declare the target replica count, not the delta.

### Exam shortcut

If you see:
- scale a Kubernetes deployment to N replicas
- --replicas sets the desired total
- kubectl scale

Think: **kubectl scale deployment --replicas 4**

**Tiny mental image:** tell Kubernetes "I want four," and it makes it so.

**Final answer:** A. kubectl scale deployment command with the --replicas 4 parameter.'''

E["test_2_q44"] = '''### Step 4: Choose the answer

- The F-score (F1) combines precision and recall into a single metric, ideal for ranking the fraud-classification models.
- It satisfies the goal: one number balancing precision and recall (RMSE/MSE are regression metrics).

### Exam shortcut

If you see:
- balance precision and recall in one metric
- classification, imbalanced (fraud)
- F-score / F1

Think: **F-score (harmonic mean of precision and recall)**

**Tiny mental image:** one dial that blends precision and recall into a single score.

**Final answer:** A. F-score'''

E["test_2_q52"] = '''### Step 4: Choose the answer

- Dialogflow builds the conversational chatbot that understands customer questions and routes them to the right support team.
- It satisfies the goal: a managed natural-language conversational agent.

### Exam shortcut

If you see:
- build a chatbot / conversational agent / intent routing
- understand and respond to user questions
- Dialogflow

Think: **Dialogflow**

**Tiny mental image:** a smart virtual receptionist that understands the question and directs the caller.

**Final answer:** D. Dialogflow'''

E["test_2_q53"] = '''### Step 4: Choose the answer

- Feature crosses add representational capacity, helping an underfitting model with few features learn more complex patterns.
- It satisfies the goal: increase model expressiveness to fix underfitting (more features/interactions).

### Exam shortcut

If you see:
- model underfitting, too few features
- need more representational power
- feature crosses / add features

Think: **feature crosses (add capacity)**

**Tiny mental image:** combine features into new ones so the model has richer signal to learn from.

**Final answer:** B. Use feature crosses'''

E["test_2_q54"] = '''### Step 4: Choose the answer

- Nearline is the low-cost Cloud Storage class for files accessed about once a month, with reliable, highly available storage.
- It satisfies the goal: minimal cost for monthly-access training data while staying durable and available.

### Exam shortcut

If you see:
- large dataset accessed ~monthly, minimize cost
- still reliable/highly available
- map access frequency to class

Think: **Nearline** (monthly access)

**Tiny mental image:** the shelf you reach for once a month - cheaper than the daily counter.

**Final answer:** B. Cloud Storage Nearline storage'''

E["test_3_q20"] = '''### Step 4: Choose the answer

- Training an AutoML Vision model on labeled package images and wrapping it in an API detects damage and flags items for human review in real time.
- It satisfies the goal: a custom image classifier (the generic Vision API can't recognize "damaged") served via API.

### Exam shortcut

If you see:
- custom image recognition (damage/defects) the prebuilt API can't do
- real-time flagging, integrate via API
- AutoML Vision on your labeled images

Think: **AutoML Vision model + API**

**Tiny mental image:** train a custom "is this package damaged?" eye and expose it as a service.

**Final answer:** B. Train an AutoML model on a corpus of images and build an API around it to integrate with package tracking applications'''

E["test_3_q33"] = '''### Step 4: Choose the answer

- Running the existing Spark ML models on Dataproc, reading directly from BigQuery via the connector, migrates the retraining pipelines with minimal change.
- It satisfies the goal: reuse Spark ML code on managed Dataproc against the BigQuery data.

### Exam shortcut

If you see:
- migrate existing Spark ML training to GCP, data in BigQuery
- reuse Spark code (don't rewrite in TensorFlow)
- Dataproc + BigQuery connector

Think: **Dataproc Spark ML reading from BigQuery**

**Tiny mental image:** run the same Spark models on managed Dataproc, pulling straight from the warehouse.

**Final answer:** C. Use Dataproc for training existing Spark ML models but read data directly from BigQuery'''

E["test_3_q42"] = '''### Step 4: Choose the answer

- A GPU accelerator speeds the TensorFlow training cost-effectively and supports the custom ops that must run partially on CPU, which TPUs don't accommodate.
- It satisfies both: faster training and compatibility with custom/partial-CPU TensorFlow operations.

### Exam shortcut

If you see:
- speed up TensorFlow training, custom ops (partial CPU)
- TPU can't run arbitrary custom ops
- GPU vs TPU choice

Think: **GPU accelerator (custom ops → not TPU)**

**Tiny mental image:** a GPU turbo that still runs your hand-written operations; a TPU would choke on them.

**Final answer:** C. Use a VM with a GPU hardware accelerator to train the model.'''

E["test_3_q52"] = '''### Step 4: Choose the answer

- One-hot encoding the city values into binary columns with SQL prepares the categorical predictor in the column form BigQuery ML needs.
- It satisfies the goal: efficient, in-warehouse encoding of city names for training and serving.

### Exam shortcut

If you see:
- categorical string feature (city) for BigQuery ML
- represent as columns for training/serving
- one-hot encoding

Think: **one-hot encode the categorical column in SQL**

**Tiny mental image:** turn each city into its own yes/no column the model can read.

**Final answer:** B. Use SQL in BigQuery to apply one-hot encoding to the state column and convert each city to a binary value column'''

E["test_4_q11"] = '''### Step 4: Choose the answer

- Denormalizing the data and appending hourly status updates (instead of in-place UPDATEs) maximizes BigQuery query performance and usability for the data science team.
- It satisfies both: fewer joins via denormalization and efficient append-only ingestion at PB scale.

### Exam shortcut

If you see:
- huge structured dataset into BigQuery for ML, maximize performance
- denormalize + append (no UPDATEs)
- avoid join-heavy normalized schema

Think: **denormalize + append-only status updates**

**Tiny mental image:** one wide table you keep adding rows to, not a web of tables you keep editing.

**Final answer:** A. Denormalize the data as much as possible.'''

E["test_4_q16"] = '''### Step 4: Choose the answer

- Dialogflow Enterprise Edition interprets the voice commands from in-home assistants and drives the order into the backend systems.
- It satisfies the goal: a conversational agent that understands intent and integrates with fulfillment.

### Exam shortcut

If you see:
- interpret voice commands / conversational ordering
- integrate with assistants (Google Home), call backends
- intent + fulfillment

Think: **Dialogflow (Enterprise)**

**Tiny mental image:** a voice-order taker that understands the request and rings it up in the backend.

**Final answer:** C. Implement Dialogflow Enterprise Edition'''

E["test_4_q17"] = '''### Step 4: Choose the answer

- Applying regularization techniques like dropout or batch normalization improves generalization and addresses the train/test error gap.
- It satisfies the goal: reduce overfitting so the model performs consistently.

### Exam shortcut

If you see:
- large train/test error discrepancy
- improve generalization
- dropout / batch normalization / regularization

Think: **regularization (dropout, batch norm)**

**Tiny mental image:** add discipline during training so the model generalizes instead of memorizing.

**Final answer:** C. Use regularization techniques like dropout or batch normalization to prevent overfitting'''

E["test_4_q48"] = '''### Step 4: Choose the answer

- Cloud GPUs accelerate training while supporting the model once you implement GPU kernel support for the custom C++ ops, which TPUs can't easily run.
- It satisfies both: faster, lower-cost training and compatibility with custom operations.

### Exam shortcut

If you see:
- custom TensorFlow C++ ops, want acceleration
- TPUs can't run arbitrary custom ops
- GPU (with custom kernel support)

Think: **Cloud GPUs (after GPU kernel support for custom ops)**

**Tiny mental image:** a GPU you can teach your custom operations to run on; a TPU won't take them.

**Final answer:** C. Use Cloud GPUs after implementing GPU kernel support for your custom ops.'''

E["test_4_q49"] = '''### Step 4: Choose the answer

- Cloud Vision AutoML trained on the existing labeled dataset (≈1000 images per component) produces a custom image classifier for the PoC within days.
- It satisfies both: custom recognition of 750 components and a fast, low-code build.

### Exam shortcut

If you see:
- custom image classification with a labeled dataset, fast PoC
- prebuilt Vision API can't recognize your specific items
- AutoML Vision on the existing data

Think: **Cloud Vision AutoML (existing dataset)**

**Tiny mental image:** feed your labeled component photos into AutoML and get a custom recognizer in days.

**Final answer:** A. Use Cloud Vision AutoML with the existing dataset.'''

E["test_5_q9"] = '''### Step 4: Choose the answer

- Overfitting is reduced by getting more training examples, using a smaller feature set, and increasing the regularization parameters.
- It satisfies the question: all three push the model toward generalization.

### Exam shortcut

If you see:
- "ways to reduce overfitting"
- more data, fewer features, stronger regularization
- (less data or weaker regularization makes it worse)

Think: **more data + fewer features + more regularization**

**Tiny mental image:** more examples, a simpler model, and a firmer hand to stop memorizing noise.

**Final answer:** A. Get more training examples'''

E["test_5_q15"] = '''### Step 4: Choose the answer

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

E["test_5_q26"] = '''### Step 4: Choose the answer

- The Cloud Natural Language API's Entity Analysis extracts topics from blog posts as labels with no ML expertise or training, shipping fast.
- It satisfies the constraints: a prebuilt API delivering topic labels quickly without building a model.

### Exam shortcut

If you see:
- generate topic/subject labels from text, no ML experience, fast
- prebuilt API, not a custom model
- entities = topics/labels

Think: **Cloud Natural Language API (Entity Analysis)**

**Tiny mental image:** call a ready-made text service and use the entities it returns as tags.

**Final answer:** A. Call the Cloud Natural Language API from your application. Process the generated Entity Analysis as labels.'''

E["test_5_q29"] = '''### Step 4: Choose the answer

- In Wide & Deep, the wide (linear) part handles memorization and the deep (neural) part handles generalization, making it a strong fit for recommender systems.
- It satisfies the question: wide = memorize, deep = generalize, great for recommendations.

### Exam shortcut

If you see:
- Wide & Deep model facts
- wide = memorization, deep = generalization
- good for recommender systems

Think: **wide memorizes, deep generalizes (recommenders)**

**Tiny mental image:** the wide side remembers specific combos; the deep side spots new patterns.

**Final answer:** A. The wide model is used for memorization, while the deep model is used for generalization.'''

E["test_5_q34"] = '''### Step 4: Choose the answer

- Dialogflow Enterprise Edition interprets the customer voice commands and drives orders into the backend systems.
- It satisfies the goal: a conversational agent that understands intent and integrates with fulfillment.

### Exam shortcut

If you see:
- interpret voice commands / conversational ordering
- integrate with assistants, call backends
- intent + fulfillment

Think: **Dialogflow (Enterprise)**

**Tiny mental image:** a voice-order taker that understands the request and rings it up.

**Final answer:** C. Dialogflow Enterprise Edition'''

append_entries(E)

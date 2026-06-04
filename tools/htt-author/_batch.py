from lib import append_entries

E = {}

E["test_5_q35"] = '''### Step 4: Choose the answer

- A neural network learns by adjusting its weights and biases during training; features and input values are given, not learned.
- It satisfies the question: weights and biases are the trainable parameters.

### Exam shortcut

If you see:
- "what does a neural network adjust as it learns?"
- weights + biases are trainable
- features/inputs are fixed data

Think: **weights and biases**

**Tiny mental image:** training tunes the dials (weights/biases), not the data you feed in.

**Final answer:** A. Weights'''

E["test_5_q41"] = '''### Step 4: Choose the answer

- A deep neural network with multiple hidden layers automatically learns face features from the labeled images, far better than manual feature engineering or clustering.
- It satisfies the goal: let deep learning discover the hierarchical visual features itself.

### Exam shortcut

If you see:
- image recognition from labeled images
- let the model learn features automatically
- deep learning, multiple hidden layers

Think: **deep neural network (auto feature learning)**

**Tiny mental image:** stack enough layers and the network learns "eyes, noses, faces" on its own.

**Final answer:** C. Use deep learning by creating a neural network with multiple hidden layers to automatically detect features of faces.'''

E["test_5_q42"] = '''### Step 4: Choose the answer

- Training an AutoML Vision model on labeled package images and wrapping it in an API detects damage and flags items for human review in real time.
- It satisfies the goal: a custom image classifier (the generic Vision API can't recognize "damaged") served via API.

### Exam shortcut

If you see:
- custom image recognition (damage/defects) the prebuilt API can't do
- real-time flagging, integrate via API
- AutoML Vision on your labeled images

Think: **AutoML Vision model + API**

**Tiny mental image:** train a custom "is this damaged?" eye and expose it as a service.

**Final answer:** B. Train an AutoML model on your corpus of images, and build an API around that model to integrate with the package tracking applications.'''

E["test_6_q10"] = '''### Step 4: Choose the answer

- Subsampling the training dataset reduces the data processed per epoch, speeding up training.
- It satisfies the goal: faster training (more layers/features would slow it down).

### Exam shortcut

If you see:
- neural network training too slow, speed it up
- reduce data processed (subsample training set)
- not the test set

Think: **subsample the training dataset**

**Tiny mental image:** train on a representative slice to iterate faster.

**Final answer:** B. Subsample your training dataset.'''

E["test_6_q12"] = '''### Step 4: Choose the answer

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

E["test_6_q13"] = '''### Step 4: Choose the answer

- With labeled outcomes you can use supervised learning for fraud and to predict location, and clustering to group transactions by similarity.
- It satisfies the question: supervised fraud detection, clustering into categories, and supervised location prediction.

### Exam shortcut

If you see:
- "which ML applications fit this data?"
- supervised = predict labeled outcomes (fraud, location)
- clustering = group by similarity

Think: **supervised (fraud/location) + clustering (group by similarity)**

**Tiny mental image:** label-driven predictions plus unsupervised grouping of similar transactions.

**Final answer:** A. Supervised learning to determine which transactions are most likely to be fraudulent.'''

E["test_6_q31"] = '''### Step 4: Choose the answer

- categorical_column_with_hash_bucket handles a categorical column when you don't know all possible values, hashing them into a fixed number of buckets.
- It satisfies the goal: encode an open-ended/unknown vocabulary without enumerating it.

### Exam shortcut

If you see:
- categorical feature with unknown/unbounded vocabulary
- don't know all possible values
- hash buckets vs vocabulary list

Think: **categorical_column_with_hash_bucket**

**Tiny mental image:** when you can't list every category, hash each into one of N bins.

**Final answer:** B. categorical_column_with_hash_bucket'''

E["test_6_q40"] = '''### Step 4: Choose the answer

- BigQuery natively supports geospatial (GIS) functions and ML predictions over the 40 TB dataset, and feeds a dashboard of at-risk ships by region.
- It satisfies all: storage at scale, native prediction (BigQuery ML), geospatial processing (GeoJSON/GIS), and BI dashboards.

### Exam shortcut

If you see:
- large analytics dataset needing native prediction (ML) + geospatial (GIS)
- dashboard/reporting on top
- SQL at TB+ scale

Think: **BigQuery (BigQuery ML + GIS)**

**Tiny mental image:** one warehouse that maps the ships, predicts delays, and feeds the dashboard.

**Final answer:** A. BigQuery'''

E["test_6_q41"] = '''### Step 4: Choose the answer

- You split into train and test so you can verify the model generalizes to unseen data, not just memorizes the training set.
- It satisfies the question: the test set measures generalization.

### Exam shortcut

If you see:
- "why split into train/test?"
- evaluate on unseen data
- generalization, not memorization

Think: **test set checks generalization to new data**

**Tiny mental image:** hold back an exam the model hasn't studied to see if it really learned.

**Final answer:** B. To make sure your model is generalized for more than just the training data'''

E["test_6_q42"] = '''### Step 4: Choose the answer

- Cloud Vision AutoML trained on the existing labeled dataset (≈1000 images per component) produces a custom classifier for the PoC within days.
- It satisfies both: custom recognition of 750 components and a fast, low-code build.

### Exam shortcut

If you see:
- custom image classification with a labeled dataset, fast PoC
- prebuilt Vision API can't recognize your specific items
- AutoML Vision on the existing data

Think: **Cloud Vision AutoML (existing dataset)**

**Tiny mental image:** feed your labeled component photos into AutoML and get a custom recognizer in days.

**Final answer:** A. Use Cloud Vision AutoML with the existing dataset.'''

E["test_7_q4"] = '''### Step 4: Choose the answer

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

E["test_7_q17"] = '''### Step 4: Choose the answer

- Feature-crossing latitude and longitude, bucketized at the minute level with L1 regularization, captures the location's nonlinear effect on price while keeping the sparse cross compact.
- It satisfies the goal: encode the physical location dependency effectively, with L1 pruning unhelpful buckets.

### Exam shortcut

If you see:
- location (lat/long) strongly affects the target, nonlinearly
- bucketize + feature cross lat/long
- L1 regularization to control the sparse cross

Think: **bucketized feature cross of lat × long + L1**

**Tiny mental image:** chop the map into a grid and cross the coordinates so each neighborhood gets its own signal.

**Final answer:** C. Create a feature cross of latitude and longitude, bucketize at the minute level and use L1 regularization during optimization.'''

E["test_7_q35"] = '''### Step 4: Choose the answer

- Combining highly co-dependent features into one representative feature reduces dimensionality and speeds training with minimal accuracy loss.
- It satisfies the goal: fewer features without discarding the signal they share.

### Exam shortcut

If you see:
- too many features, speed up training, keep accuracy
- merge correlated/co-dependent features
- dimensionality reduction

Think: **combine co-dependent features into one**

**Tiny mental image:** fold redundant columns that say the same thing into a single column.

**Final answer:** B. Combine highly co-dependent features into one representative feature.'''

E["test_7_q38"] = '''### Step 4: Choose the answer

- Linear regression predicts the continuous house price and runs cheaply on a single resource-constrained VM.
- It satisfies both: a numeric prediction and a lightweight algorithm (neural nets are heavier; logistic is for classification).

### Exam shortcut

If you see:
- predict a continuous value on limited compute
- lightweight, low-resource algorithm
- regression, not deep nets

Think: **linear regression**

**Tiny mental image:** a simple line-fit that runs on a shoestring machine.

**Final answer:** A. Linear regression'''

E["test_8_q14"] = '''### Step 4: Choose the answer

- Training a (linear) regression to output a continuous credit-default risk score fits the labeled default data and the prediction goal.
- It satisfies the goal: predict a default-risk score from the historical labeled applications.

### Exam shortcut

If you see:
- predict a default rate / risk score from labeled history
- continuous score output
- regression on labeled data

Think: **regression to a risk score**

**Tiny mental image:** fit the past defaults to produce a risk number for new applicants.

**Final answer:** B. Train a linear regression to predict a credit default risk score.'''

E["test_8_q29"] = '''### Step 4: Choose the answer

- To fight overfitting, increase the training dataset and remove some input features, both pushing the model toward generalization.
- It satisfies the goal: more data plus a simpler feature set reduces overfitting.

### Exam shortcut

If you see:
- model overfitting, improve with new data
- more data + fewer features
- simplify and add examples

Think: **more training data + fewer features**

**Tiny mental image:** show more examples and trim the noisy features so it stops memorizing.

**Final answer:** A. Increase the size of the training dataset and remove some input features'''

E["test_8_q34"] = '''### Step 4: Choose the answer

- Predicting a continuous stock price from history is a regression task, so you use a regressor.
- It satisfies the question: continuous numeric output = regressor (not classifier/clustering).

### Exam shortcut

If you see:
- predict a continuous value (price)
- numeric output
- regressor vs classifier

Think: **Regressor**

**Tiny mental image:** forecasting a price on a continuous dial, not a category.

**Final answer:** B. Regressor'''

E["test_10_q12"] = '''### Step 4: Choose the answer

- Subsampling the training dataset reduces the data processed per epoch, speeding up the slow neural-network training.
- It satisfies the goal: faster training (more layers/features would slow it down).

### Exam shortcut

If you see:
- neural network training too slow, speed it up
- reduce data processed (subsample training set)
- not the test set

Think: **subsample the training dataset**

**Tiny mental image:** train on a representative slice to iterate faster.

**Final answer:** D. Should you subsample your training dataset?'''

E["test_13_q28"] = '''### Step 4: Choose the answer

- Partitioning the table by the weather date and setting partition expiration to 30 days automatically drops old data, minimizing cost with no scheduled deletes.
- It satisfies the goal: keep only the last 30 days by the data's own date, managed automatically.

### Exam shortcut

If you see:
- retain only the last N days, minimize cost
- partition by the meaningful date + partition expiration
- automatic cleanup (not scheduled DELETE)

Think: **partition by the data date + partition expiration**

**Tiny mental image:** dated drawers that auto-empty after 30 days, no janitor needed.

**Final answer:** B. Create a BigQuery table partitioned by datetime value of the weather date. Set up partition expiration to 30 days.'''

E["test_13_q34"] = '''### Step 4: Choose the answer

- Storing header rows with their line items as nested and repeated fields co-locates the tightly-coupled data, so joins are eliminated and analytics queries run efficiently.
- It satisfies the goal: a single denormalized table reflecting the fixed header-to-lines relationship.

### Exam shortcut

If you see:
- closely related parent/child tables always joined (header/lines)
- BigQuery efficiency, avoid joins
- nested and repeated fields

Think: **nest the line items as repeated fields inside the header**

**Tiny mental image:** tuck each order's line items inside the order row so no join is needed.

**Final answer:** A. Create a sales_transaction table that holds the sales_transaction_header information as rows and the sales_transaction_line rows as nested and repeated fields.'''

append_entries(E)

<h1>🛡️ IBM Cloud-Based Network Intrusion Detection System (NIDS)</h1>

This project is a no-code machine learning solution built using IBM Cloud's Watsonx.ai AutoAI to detect malicious network traffic. The system distinguishes between normal traffic and intrusion types using a preprocessed dataset from Kaggle.

---

<h2>📌 Problem Statement</h2>

Design and deploy a Machine Learning-based Network Intrusion Detection System (NIDS) capable of identifying and classifying various network-based attacks — such as DoS, Probe, R2L, and U2R — using real network traffic data.

> Problem Statement No. 40 from SB4 Academia AI Challenge 2025

---

<h2>📦 Dataset</h2>

- ✅ Source: Kaggle Network Intrusion Dataset  
  https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection

- 🧪 Structure:
  - 41 features per connection (3 categorical, 38 numerical)
  - Class labels: Normal or Attack
  - Upgraded version includes multiclass labels: DoS, Probe, R2L, U2R

📁 Datasets Used:
> 🔗 Given Dataset:    
> [Train_data.csv](https://github.com/unitedrider007/IBM-edunet-project/blob/main/Train_data.csv)      
> [Test_data.csv](https://github.com/unitedrider007/IBM-edunet-project/blob/main/Test_data.csv)

> 🔗 Enhanced Dataset with labeled attack types:  
> [Train_data_with_attack_types_enhanced.csv](https://github.com/unitedrider007/IBM-edunet-project/blob/main/Train_data_with_attack_types_enhanced.csv)

---

<h2>🧠 Technology Stack</h2>

| Component        | Tool/Service                         |
|------------------|--------------------------------------|
| Platform         | IBM Cloud Lite                      |
| ML Engine        | Watsonx.ai AutoAI                   |
| Deployment       | Watsonx Runtime + Deployment Space  |
| Input Format     | CSV (No coding used)                |

---

<h2>🚀 IBM Cloud Workflow</h2>

1. Sign in to IBM Cloud and provision Watsonx.ai Studio.
2. Create a new project and associate IBM Object Storage.
3. Upload Train_data.csv to AutoAI and create a multiclass classification experiment.
4. Choose "class" as the prediction column.
5. Let AutoAI run experiments and choose the best pipeline (e.g., Pipeline 6).
6. Save the best model and promote it to a Deployment Space.
7. Create an online deployment and test using Test_data.csv.
8. Save predictions as Nids_test_result.json.

> 🔗 Detailed Deployment Guide: See [NIDS_project.pdf](https://github.com/unitedrider007/IBM-edunet-project/blob/main/NIDS_project.pdf)

---

<h2>🎯 Output Highlights</h2>

- Binary model: Detects anomalies vs normal
- Upgraded model: Classifies attack type (DoS, R2L, Probe, U2R -refer below)
- Prediction Accuracy: Near 100% (based on AutoAI output)
- Output: JSON file with predictions and probability confidence

<h2>🔧 For Version Update: Python Code for Multiclass Attack Type Labeling</h2>

This upgrade uses [Python Code](https://github.com/unitedrider007/IBM-edunet-project/blob/main/update_Train_data_to_include_attack_types.py) to convert a binary-labeled dataset (Normal vs Anomaly) into a multiclass-labeled dataset (Normal, DoS, Probe, R2L, U2R) using rule-based logic.


---

<h3>🧩 Approach</h3>

We defined signature profiles for each attack type using domain knowledge. Then, we wrote a function to score how well each row matches each profile.
The best-matching attack type is selected and added as a new column `attack_type`.
Each attack type is defined with its behavioral features:
The column `attack_type` is appended to the dataset, and a binary `class` column is also mapped:
- anomaly → DoS, Probe, R2L, U2R
- normal → Normal

---

<h3>📁 Output</h3>

A new dataset file:
- ✅ `Train_data_with_attack_types.csv`

This enriched dataset enables:
- Multiclass ML training in IBM Watsonx.ai AutoAI
- Better insight into types of threats
- Model explainability
---

<h2>🧪 Attack Signature Logic</h2>

IBM AutoAI learned attack patterns based on these feature indicators:

| Attack Type | Key Indicators |
|-------------|----------------|
| DoS         | High count, serror_rate, low diff_srv_rate |
| Probe       | High diff_srv_rate, high dst_host_diff_srv_rate |
| R2L         | num_failed_logins > 0, is_guest_login = 1 |
| U2R         | root_shell = 1, su_attempted = 1, num_file_creations > 0 |

---

---

<h2>🔗 Related Resources</h2>

- IBM Cloud: https://cloud.ibm.com  
- Watsonx.ai Studio Docs: https://www.ibm.com/docs/en/watsonx/  
- GitHub Enhanced Dataset: [Train_data_with_attack_types_enhanced.csv](https://github.com/unitedrider007/IBM-edunet-project/blob/main/Train_data_with_attack_types_enhanced.csv)
---

<h2>🙋‍♂️ Author</h2>

- 👨‍💻 Cybersecurity Learner   
- 🌐 GitHub: Anshuman

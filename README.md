<h1>🛡️ IBM Cloud-Based Network Intrusion Detection System (NIDS)</h1>

This project is a no-code machine learning solution built using IBM Cloud's Watsonx.ai AutoAI to detect malicious network traffic. The system distinguishes between normal traffic and intrusion types using a preprocessed dataset from Kaggle.

---

<h2>📌 Problem Statement</h2>

Design and deploy a Machine Learning-based Network Intrusion Detection System (NIDS) capable of identifying and classifying various network-based attacks — such as DoS, Probe, R2L, and U2R — using real network traffic data.

> 🔗 Problem Statement No. 40 from SB4 Academia AI Challenge 2025

---

<h2>📦 Dataset</h2>

- ✅ Source: Kaggle Network Intrusion Dataset  
  https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection

- 🧪 Structure:
  - 41 features per connection (3 categorical, 38 numerical)
  - Class labels: Normal or Attack
  - Upgraded version includes multiclass labels: DoS, Probe, R2L, U2R

📁 Datasets Used:
- Train_data.csv
- Test_data.csv
- Nids_test_result.json

> 🔗 Enhanced Dataset with labeled attack types:  
> https://github.com/unitedrider007/IBM-edunet-project/Train_data_with_attack_types_enhanced.csv

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

> 🔗 Detailed Deployment Guide: See NIDS_project.pdf

---

<h2>🎯 Output Highlights</h2>

- Binary model: Detects anomalies vs normal
- Upgraded model: Classifies attack type (DoS, R2L, Probe, U2R)
- Prediction Accuracy: Near 100% (based on AutoAI output)
- Output: JSON file with predictions and probability confidence


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
- GitHub Enhanced Dataset: https://github.com/unitedrider007/IBM-edunet-project/blob/3592cf13bb57d194e4f4cb340f5fe60642a3bb2e/Train_data_with_attack_types_enhanced.csv
---

<h2>🙋‍♂️ Author</h2>

- 👨‍💻 Cybersecurity Learner   
- 🌐 GitHub: Anshuman

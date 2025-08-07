import pandas as pd
import numpy as np
import random
from collections import defaultdict

# Define theoretical features for each attack type
attack_profiles = {
    "DoS": {
        "src_bytes": (0, 500),           # Low volume sent
        "dst_bytes": (1000, 10000),      # High volume received
        "count": (50, 100),              # High connection count
        "serror_rate": (0.8, 1.0),       # High error rate
        "same_srv_rate": (0.9, 1.0),
        "diff_srv_rate": (0.0, 0.2)
    },
    "Probe": {
        "src_bytes": (0, 200),
        "dst_bytes": (0, 500),
        "count": (20, 60),
        "serror_rate": (0.0, 0.2),
        "same_srv_rate": (0.2, 0.6),
        "diff_srv_rate": (0.4, 0.9)
    },
    "R2L": {
        "src_bytes": (0, 100),
        "dst_bytes": (0, 100),
        "count": (1, 5),
        "serror_rate": (0.0, 0.1),
        "num_failed_logins": (2, 5),
        "logged_in": (0, 0),
        "is_guest_login": (1, 1)
    },
    "U2R": {
        "src_bytes": (0, 50),
        "dst_bytes": (0, 50),
        "count": (1, 3),
        "serror_rate": (0.0, 0.1),
        "num_file_creations": (1, 5),
        "root_shell": (1, 1),
        "su_attempted": (1, 1)
    },
    "Normal": {
        "src_bytes": (100, 10000),
        "dst_bytes": (100, 10000),
        "count": (1, 10),
        "serror_rate": (0.0, 0.1),
        "same_srv_rate": (0.7, 1.0),
        "diff_srv_rate": (0.0, 0.3)
    }
}

# Common fields across all rows
common_fields = {
    "duration": (0, 60),
    "protocol_type": ["tcp", "udp", "icmp"],
    "service": ["http", "ftp", "smtp", "dns", "ssh"],
    "flag": ["SF", "REJ", "S0", "RSTR"],
}

# Map attack type to class (binary)
attack_class = {
    "DoS": "anomaly",
    "Probe": "anomaly",
    "R2L": "anomaly",
    "U2R": "anomaly",
    "Normal": "normal"
}

# Function to score how well a row matches a profile
def match_score(row, profile):
    score = 0
    for feature, (low, high) in profile.items():
        if feature in row:
            try:
                val = float(row[feature])
                if low <= val <= high:
                    score += 1
            except:
                continue
    return score

# Assign attack_type and class to each row
def assign_attack_type(row):
    best_attack = None
    best_score = -1
    for attack, profile in attack_profiles.items():
        score = match_score(row, profile)
        if score > best_score:
            best_score = score
            best_attack = attack
    return best_attack

# Generate a dataset 
def generate_theoretical_attack_dataset(num_samples=1000):
    data = []
    attack_types = list(attack_profiles.keys())
    samples_per_attack = num_samples // len(attack_types)

    for attack in attack_types:
        for _ in range(samples_per_attack):
            row = {}

            # Add common fields
            row["duration"] = random.randint(*common_fields["duration"])
            row["protocol_type"] = random.choice(common_fields["protocol_type"])
            row["service"] = random.choice(common_fields["service"])
            row["flag"] = random.choice(common_fields["flag"])

            # Add features for the current attack type
            for feature, (low, high) in attack_profiles[attack].items():
                row[feature] = round(random.uniform(low, high), 2)

            # Fill missing features with 0 if not defined for this attack type
            all_possible_features = set(f for d in attack_profiles.values() for f in d)
            for feature in all_possible_features:
                if feature not in row:
                    row[feature] = 0

            # Add labels
            row["attack_type"] = attack
            row["class"] = attack_class[attack]

            data.append(row)

    df = pd.DataFrame(data)
    return df

# Generate and show the synthetic dataset
synthetic_df = generate_theoretical_attack_dataset(1000)


# Load your uploaded dataset
input_path = "Train_data.csv"
df = pd.read_csv(input_path)

df['attack_type'] = df.apply(assign_attack_type, axis=1)
df['class'] = df['attack_type'].map(attack_class)

# Save the dataset for export if needed
output_path = "Train_data_with_attack_types_enhanced.csv"
df.to_csv(output_path, index=False)

print(f"Saved labeled dataset to {output_path}")


from pathlib import Path
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

from src.preprocessing.build_dataset import process_file

# ---- Load data ----

X1, y1 = process_file(
    Path("data/raw/chb01/chb01_01.edf"),
    is_seizure_file=False
)

X2, y2 = process_file(
    Path("data/raw/chb01/chb01_15.edf"),
    is_seizure_file=True,
    seizure_start=1732,
    preictal_duration=600
)

X = np.vstack((X1, X2))
y = np.hstack((y1, y2))

# ---- Train/Test Split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---- Scaling ----

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ---- Model ----

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# ---- Evaluation ----

y_prob = model.predict_proba(X_test)[:, 1]

threshold = 0.4  # try 0.3 first

y_pred = (y_prob >= threshold).astype(int)

print(classification_report(y_test, y_pred))
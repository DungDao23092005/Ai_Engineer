# ========================
# 1. Import thư viện
# ========================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# ========================
# 2. Đọc dữ liệu
# ========================
diabetes_df = pd.read_csv("diabetes.csv", header=1)
diabetes_df = diabetes_df.apply(pd.to_numeric, errors="coerce")
print(diabetes_df.shape)
print(diabetes_df.isnull().sum())  # kiểm tra NaN

# ========================
# 3. Tách features & target
# ========================
x = diabetes_df.drop("Outcome", axis=1)
y = diabetes_df["Outcome"]

# ========================
# 4. Train/Test split
# ========================
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# ========================
# 5. Impute NaN (fit trên train only)
# ========================
imputer = SimpleImputer(strategy="median")
x_train_imputed = imputer.fit_transform(x_train)
x_test_imputed  = imputer.transform(x_test)

# ========================
# 6. Scale (fit trên train only)
# ========================
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train_imputed)
x_test_scaled  = scaler.transform(x_test_imputed)

# ========================
# 7. Train model
# ========================
clf = SVC()
clf.fit(x_train_scaled, y_train)

# ========================
# 8. Evaluate
# ========================
y_pred = clf.predict(x_test_scaled)
print(classification_report(y_test, y_pred, zero_division=0))
# Task:
# Load the Breast Cancer dataset, create a DataFrame from it,
# split it into training and test sets,
# fit three models (LogisticRegression, DecisionTreeClassifier, KNeighborsClassifier),
# scale the data, evaluate their accuracy (accuracy_score, classification_report),
# and display the confusion matrix as a heatmap.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = datasets.load_breast_cancer(as_frame=True)
df = data.frame

X = df.drop(columns=["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

lr = LogisticRegression(max_iter=2000)
tree = DecisionTreeClassifier(random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)

models = {
    "LogisticRegression": lr,
    "DecisionTree": tree,
    "KNN": knn
}

def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()

print("Results without PCA:\n")
for name, model in models.items():
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    acc = accuracy_score(y_test, y_pred)
    print(f"{name} accuracy: {acc:.3f}")
    print(classification_report(y_test, y_pred, target_names=data.target_names))
    plot_confusion_matrix(y_test, y_pred, f"{name}")
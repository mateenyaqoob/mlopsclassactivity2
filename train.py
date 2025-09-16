import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import sys

def train(version, data_paths):
    dfs = [pd.read_csv(p) for p in data_paths]
    df = pd.concat(dfs, ignore_index=True)
    X, y = df.iloc[:, :-1], df['target']
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    model_filename = f"model_{version}.pkl"
    joblib.dump(model, model_filename)
    print(f"✅ Model version {version} trained and saved as {model_filename}")

if __name__ == "__main__":
    version = sys.argv[1]
    data_paths = sys.argv[2:]
    train(version, data_paths)

import pandas as pd

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.dropna()
    df.to_csv(output_path, index=False)
    print(f"✅ Data preprocessed and saved to {output_path}")

if __name__ == "__main__":
    preprocess("data/iris.csv", "data/cleaned_iris.csv")

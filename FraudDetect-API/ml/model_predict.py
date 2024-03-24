import os
from typing import List, Tuple
import joblib
from sklearn.pipeline import Pipeline

# Load the model
model_file = os.path.join(os.path.dirname(__file__), "fraud_model.joblib")

loaded_model: Tuple[Pipeline, List[str]] = joblib.load(model_file)
model, targets = loaded_model

# Run a prediction
p = model.predict([x_test.iloc[0]])

if p[0] == 1:
    print("Fraud")
else:
    print("Not Fraud")

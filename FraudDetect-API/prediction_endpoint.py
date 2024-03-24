import numpy as np
from pydantic import BaseModel
from typing import List, Optional, Tuple  # Added Tuple import for type hinting
from sklearn.pipeline import Pipeline
import os
import joblib


class PredictionInput(BaseModel):
    data: List[float]  # Define input data type


class PredictionOutput(BaseModel):
    category: int  # Define output category


class FraudDetector:
    model: Optional[Pipeline]
    targets: Optional[List[int]]

    def load_model(self):
        """Loads the model"""
        model_file = os.path.join(os.path.dirname(
            __file__), "ml/fraud_model.joblib")
        # Adjust the type hint to include Tuple
        loaded_model: Tuple[Pipeline, List[int]] = joblib.load(model_file)
        model, targets = loaded_model
        self.model = model
        self.targets = targets

    def predict(self, input_data: PredictionInput) -> PredictionOutput:
        """Runs a prediction"""
        # Reshape input data into 2D array
        input_data_np = np.array(input_data.data).reshape(1, -1)
        # Perform prediction
        prediction = self.model.predict(input_data_np)
        # Get category from targets based on prediction
        category = self.targets[prediction[0]]
        # Return prediction output
        return PredictionOutput(category=category)

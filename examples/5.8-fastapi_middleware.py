from fastapi import FastAPI, Request
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import pandas as pd

app = FastAPI()

# Define a simple machine learning model (linear regression for demonstration)
model = LinearRegression()

# Custom middleware for machine learning prediction
class MachineLearningMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, request: Request, *args, **kwargs):
        # Intercept incoming request
        if request.method == 'POST':
            # Assuming incoming data is in JSON format
            data = await request.json()
            features = pd.DataFrame([data])  # Convert JSON data to pandas DataFrame
            prediction = self.make_prediction(features)  # Make prediction using the model
            response = await self.app(request, *args, **kwargs)  # Pass control to the route handler
            response.json_body['prediction'] = prediction  # Include prediction in the response
            return response

        # If not a POST request, continue as usual
        return await self.app(request, *args, **kwargs)

    def make_prediction(self, features):
        # Dummy implementation for demonstration (replace with your model prediction logic)
        return model.predict(features)

# Include the middleware in the FastAPI app
app.add_middleware(MachineLearningMiddleware)

# Define a Pydantic model for the incoming data
class InputData(BaseModel):
    feature1: float
    feature2: float

# Route handler for prediction endpoint
@app.post("/predict/")
async def predict(data: InputData):
    return {"message": "Prediction made successfully"}

# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # Test the API with the following  data:
    # {
    #     "feature1": 10,
    #     "feature2": 20
    # }

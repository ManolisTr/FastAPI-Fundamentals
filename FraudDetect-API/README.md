# FraudDetect-API


## About Dataset
This dataset contains credit card transactions made by European cardholders in the year 2023. It comprises over 550,000 records, and the data has been anonymized to protect the cardholders' identities. The primary objective of this dataset is to facilitate the development of fraud detection algorithms and models to identify potentially fraudulent transactions.

[Credit Card Fraud Detection Dataset 2023]([URL](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023/code?datasetId=3752264&sortBy=voteCount))


## Key Features:

- id: Unique identifier for each transaction
- V1-V28: Anonymized features representing various transaction attributes (e.g., time, location, etc.)
- Amount: The transaction amount
- Class: Binary label indicating whether the transaction is fraudulent (1) or not (0)

# Fraud Detection API

This is a FastAPI-based API for fraud detection using a pre-trained machine learning model. It provides an endpoint for making predictions based on input data.

## Getting Started

To get started with this API, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone git@github.com:ManolisTr/FraudDetect-API.git
```

2. Install the required dependencies:
    
```bash
    pip install -r requirements.txt
```

3. Run the API server:

```bash
    uvicorn main:app --reload
```
4. Once the server is running, you can access the API documentation at http://localhost:8000/docs to test the endpoints using Swagger UI.


## Usage
### Making Predictions
To make predictions, send a POST request to the /prediction endpoint with input data in the request body. The input data should be a list of floats representing the features for prediction.

Example request:

```json

{
    "data": [0.4204676968993798, -0.07019389049348876, -0.5692655717641448, 0.19167256419205933, -0.00960663187396111, 0.42690292787138234, -0.35672761014973314, 0.09614260112475115, 0.07780566887853127, -0.6732832135986757, 0.5865055532599223, -0.7509423643768935, -1.0333555313016676, -0.8868947555187794, 0.5434225753594195, -1.075064762436905, -0.6651887984556643, -1.1490843582067032, -0.16878231339316183, 0.23511589500238225, 0.13496893644837274, 0.0704325754363474, 0.047770019508129695, -0.8516220843795598, 0.1028764294955881, -0.3754361962902003, 0.8208072193643625, 0.6659830110239932, -0.492623668290211]
}

```

Example response:

```json
{
    "category": 0
}
```

## Model Training
The model used for fraud detection is trained using logistic regression. You can find the training code in the train_model.py file. The trained model is saved as ml/fraud_model.joblib.


## Features

- **Initial Release (v1.0.0)**
  - Logistic Regression Model: The first release includes a logistic regression model for fraud detection.
  
- **Future Releases**
  - Support for Additional Models: Future releases will introduce support for additional machine learning models such as decision trees, random forests, etc.
  - Enhanced Feature Set: More features will be added to improve the accuracy and effectiveness of fraud detection.
  - API Enhancements: Additional functionality and improvements to the API will be implemented based on user feedback and requirements.

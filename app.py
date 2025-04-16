from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
from transformation import CreditDataTransformer

app = Flask(__name__)

# Load the model and transformer
model = joblib.load('credit_risk_model_xgb.pkl')
transformer = CreditDataTransformer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        input_data = request.form.to_dict()
        
        # Convert numerical fields from strings to numbers
        numerical_fields = [
            'duration', 'credit_amount', 'installment_rate', 
            'residence_since', 'age', 'existing_credits', 'dependents'
        ]
        
        for field in numerical_fields:
            if field in input_data:
                input_data[field] = float(input_data[field])
        
        # Transform the input data
        transformed_data = transformer.transform_input(input_data)
        
        # Make prediction
        prediction = model.predict(transformed_data)[0]
        probability = model.predict_proba(transformed_data)[0][1]
        
        # Prepare response
        result = {
            'prediction': 'Good Credit Risk' if prediction == 1 else 'Bad Credit Risk',
            'probability': float(probability),
            'confidence': 'High' if (probability > 0.7 or probability < 0.3) else 'Medium'
        }
        
        return render_template('result.html', result=result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
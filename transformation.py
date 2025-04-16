import joblib
import pandas as pd

class CreditDataTransformer:
    def __init__(self):
        # Load the category mappings
        self.mappings = joblib.load('category_mappings.pkl')
        self.column_order = [
            'checking_account', 'duration', 'credit_history', 'purpose', 'credit_amount',
            'savings_account', 'employment', 'installment_rate', 'personal_status_sex',
            'other_debtors', 'residence_since', 'property', 'age', 'other_installment_plans',
            'housing', 'existing_credits', 'job', 'dependents', 'telephone', 'foreign_worker'
        ]
    
    def transform_input(self, input_data):
        """
        Transform raw input data into the format expected by the model
        
        Args:
            input_data: Dictionary containing the input features
            
        Returns:
            pd.DataFrame: Transformed data ready for prediction
        """
        # Create a DataFrame with the input data
        df = pd.DataFrame([input_data])
        
        # Apply categorical mappings
        for col in self.mappings:
            if col in df.columns:
                df[col] = df[col].map(self.mappings[col])
        
        # Ensure all columns are present and in correct order
        for col in self.column_order:
            if col not in df.columns:
                df[col] = 0  # Add missing columns with default value
        
        # Reorder columns to match training data
        df = df[self.column_order]
        
        return df
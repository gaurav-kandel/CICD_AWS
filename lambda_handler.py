import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Function to train the model and save it as a pickle file
def train_model(X, y, model_filename='model.pkl'):

    # Create a linear regression model
    model = LinearRegression()

    # Train the model on the training data
    model.fit(X, y)

    # Save the trained model to a pickle file
    with open(model_filename, 'wb') as file:
        pickle.dump(model, file)

    print(f"Model trained and saved to {model_filename}")


# Function to load the model and make predictions
def predict(X_new, model_filename='model.pkl'):
    # Load the trained model from the pickle file
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)

    # Make predictions on new data
    predictions = model.predict(X_new)
    
    return predictions

# Example usage
if __name__ == "__main__":
    # Generate some example data
    # Independent variables (features)
    
    print("Starting Model...")
    X = np.random.rand(100, 1)  # 100 samples, 1 feature (random data)

    # Dependent variable (target)
    y = 3 * X.squeeze() + 2 + np.random.randn(100)  # y = 3X + 2 + noise

    # Train the model and save it
    train_model(X, y)

    # Predict on the test set
    predictions = predict([[0.01]])
    print(predictions)
    print("Done")
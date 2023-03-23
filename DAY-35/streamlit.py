import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=["class"])

# Create the Random Forest Classifier model
def train_model(n_estimators, max_depth, random_state):
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    model.fit(X_train, y_train)
    return model

# Create a Streamlit app
def app():
    st.set_page_config(page_title="Iris Dataset Classifier")
    st.title("Iris Dataset Classifier")
    
    # Display the dataset
    st.subheader("Iris Dataset")
    st.write(X)
    st.write(y)
    
    # Get input parameters from the sidebar
    n_estimators = st.sidebar.slider("Number of trees", 1, 1000, 100, 1)
    max_depth = st.sidebar.slider("Maximum depth", 1, 100, 10, 1)
    random_state = st.sidebar.slider("Random state", 0, 100, 42, 1)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model on the training data
    model = train_model(n_estimators, max_depth, random_state)
    
    # Make predictions on the test data
    y_pred = model.predict(X_test)
    
    # Evaluate the model's accuracy
    accuracy = model.score(X_test, y_test)
    
    # Display the accuracy of the model
    st.subheader("Model Accuracy")
    st.write(f"The accuracy of the model is {accuracy:.2f}.")
    
    # Get user input for new data
    sepal_length = st.slider("Sepal length", 0.0, 10.0, 5.0, 0.1)
    sepal_width = st.slider("Sepal width", 0.0, 10.0, 5.0, 0.1)
    petal_length = st.slider("Petal length", 0.0, 10.0, 5.0, 0.1)
    petal_width = st.slider("Petal width", 0.0, 10.0, 5.0, 0.1)
    
    # Create a new DataFrame for the user input
    new_data = pd.DataFrame({
        "sepal length (cm)": [sepal_length],
        "sepal width (cm)": [sepal_width],
        "petal length (cm)": [petal_length],
        "petal width (cm)": [petal_width]
    })
    
    # Use the model to make a prediction on the new data
    prediction = model.predict(new_data)
    
    # Display the prediction
    st.subheader("Prediction")
    st.write(f"The predicted class is {iris.target_names[prediction[0]]}.")

import pytest
# TODO: add necessary import
import numpy as np
from sklearn.pipeline import Pipeline

from ml.data import process_data, apply_label
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_apply_labels():
    """
    # Tests that apply labels function correctly classifies as '>50K' or '<=50K'
    """
    # Your code here
    # Test that sample >50K
    sample = [1, 0]
    assert apply_label(sample) == ">50K"

    # Test that sample <=50K
    sample = [0, 1]
    assert apply_label(sample) == "<=50K"

# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    # Tests that 'train_model' function works correctly and verifies capacity to make predictions
    """
    # Your code here
    # Sample data set for function
    X_train = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [5.0, 6.0], [6.0, 7.0]])
    y_train = np.array([0, 0, 0, 1, 1])

    model = train_model(X_train, y_train)

    # Tests that function returns a scikit-learn pipeline using logistic regression
    assert isinstance(model, Pipeline), "Does not return a scikit-learn Pipeline"
    assert hasattr(
        model.named_steps["logisticregression"], "classes_"
    ), "Model is not fitted"

    # Tests that predictions are correct
    predictions = model.predict(X_train)
    assert len(predictions) == len(y_train), "Model does not have one prediction per sample"


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # Tests that model is outputing correct precision, recall, and f1-score
    """
    # Your code here
    # Arrays used to test metrics
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 1, 0, 1])
    
    # Compute metrics of model
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    
    assert np.isclose(precision, 2/3)
    assert np.isclose(recall, 2/3)
    assert np.isclose(fbeta, 2/3)

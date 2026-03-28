from src.load_data import load_data
from src.preprocess import preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate
import joblib

data = load_data("data/cardio.csv")

X_train, X_test, y_train, y_test = preprocess_data(data)

model = train_model(X_train, y_train)

accuracy = evaluate(model, X_test, y_test)

print("Model Accuracy:", accuracy)

joblib.dump(model, "model/model.pkl")
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=40)


with open("artifacts/model.pkl", "rb") as f:
    model = pickle.load(f)


y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)


print(f"Accuracy on test set: {accuracy:.2f}")
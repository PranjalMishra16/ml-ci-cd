import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state = 40)


model = RandomForestClassifier(n_estimators=100, random_state = 40)
model.fit(x_train, y_train)


with open("artifacts/model.pkl", "wb") as f:
    pickle.dump(model,f)
print("Model saved to artifacts folder")
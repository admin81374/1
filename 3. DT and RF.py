from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

print("Decision Tree Prediction:")
print(dt_pred)
print("Test Score:", dt.score(X_test, y_test))
print("Confusion Matrix:")
print(confusion_matrix(y_test, dt_pred))


rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

print("\nRandom Forest Prediction:")
print(rf_pred)
print("Test Score:", rf.score(X_test, y_test))
print("Confusion Matrix:")
print(confusion_matrix(y_test, rf_pred))


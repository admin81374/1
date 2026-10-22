from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

iris = load_iris()
X = iris.data
y = iris.target

km = KMeans(n_clusters=3, random_state=42)
km.fit(X)
km_pred = km.predict(X)

print("K-Means Prediction:")
print(km_pred)
print("Test Score:", km.score(X))
print("Confusion Matrix:")
print(confusion_matrix(y, km_pred))

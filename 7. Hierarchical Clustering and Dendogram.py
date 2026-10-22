import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

iris = load_iris()
x = iris.data

z = linkage(x, method='ward')

plt.figure(figsize=(10, 6))
dendrogram(z, labels=iris.target, leaf_rotation=90)

plt.title("hierarchical clustering dendrogram")
plt.xlabel("data points")
plt.ylabel("distance")
plt.show()

clusters = fcluster(z, t=3, criterion='maxclust')

print("cluster labels:")
print(clusters)

#for provided dataset
data = pd.read_csv("data.csv") 
x = data.drop("Result", axis=1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

# Change column numbers if needed
X = pd.to_numeric(data.iloc[:-1, 1])
Y = pd.to_numeric(data.iloc[:-1, 2])

df = pd.DataFrame({"X": X, "Y": Y}).dropna()
X = df["X"]
Y = df["Y"]

m = sum((X-X.mean())*(Y-Y.mean())) / sum((X-X.mean())**2)
c = Y.mean() - m*X.mean()

print("Slope:", m)
print("Intercept:", c)

# Change column number if needed
x = data.iloc[-1, 1]
print("Prediction:", m*x+c)

plt.scatter(X, Y)
plt.plot(X, m*X+c)
plt.show()

#data.iloc[:-1, 1] → Last row ko chhodkar 2nd column se X.
#data.iloc[:-1, 2] → Last row ko chhodkar 3rd column se Y.
#data.iloc[-1, 1] → Last row ki Age.

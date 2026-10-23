import pandas as pd

data = pd.read_csv(r"\Example1.csv")

print("\nTable:")
print(data.to_string(index=False))

a = data.values.tolist()

print("\nTotal training instances:", len(a))

attribute = len(a[0]) - 1
hypothesis = ['0'] * attribute

print("\nInitial hypothesis:", hypothesis)

for i in range(len(a)):
    attributes = a[i][:-1]
    target = a[i][-1]

    if target == "Yes":
        for j in range(attribute):
            if hypothesis[j] == '0' or hypothesis[j] == attributes[j]:
                hypothesis[j] = attributes[j]
            else:
                hypothesis[j] = '?'

    print("\nHypothesis for training instance", i + 1, "is:")
    print(hypothesis)

print("\nFinal maximally specific hypothesis:")
print(hypothesis)

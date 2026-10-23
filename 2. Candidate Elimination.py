import pandas as pd

data = pd.read_csv(r"\Example1.csv")

print("\nTable:")
print(data.to_string(index=False))

a = data.values.tolist()

print("\nTotal training instances:", len(a))

attribute = len(a[0]) - 1
S = ['0'] * attribute
G = [['?'] * attribute]

print("\nInitial hypothesis of S:", S)
print("Initial hypothesis of G:", G)

for i in range(len(a)):
    attributes = a[i][:-1]
    target = a[i][-1]

    if str(target).lower() == "yes":
        for j in range(attribute):
            if S[j] == '0':
                S[j] = attributes[j]
            else:
                S[j] != attributes[j]
                S[j] = '?'

    print("\nStep:", i + 1)
    print("Specific Hypothesis:", S)
    print("General Hypothesis:", G)

print("\nFinal S:", S)
print("Final G:", G)

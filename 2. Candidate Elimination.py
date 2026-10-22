import pandas as pd

# With header: remove header=None
data = pd.read_csv(r"C:\Users\zoya1\OneDrive\Desktop\pract\Example1.csv", header=None)

print("Table:")
# With header: print(data.to_string(index=False))
print(data.to_string(index=False, header=False))

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

n = len(X[0])
S = ['0'] * n
G = [['?'] * n]

for i, x in enumerate(X):

    if str(Y[i]).lower() == 'yes':  # Example: '1', 'positive'
        for j in range(n):
            if S[j] == '0':
                S[j] = x[j]
            elif S[j] != x[j]:
                S[j] = '?'

    print("\nStep", i + 1)
    print("Specific_h:", S)
    print("General_h:", G)

print("\nFinal Specific Hypothesis:", S)
print("Final General Hypothesis:", G)


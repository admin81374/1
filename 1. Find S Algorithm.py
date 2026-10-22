import csv

a = []

with open(r"C:\Users\zoya1\OneDrive\Desktop\pract\Example1.csv", 'r') as f:
    a = list(csv.reader(f))

print("Table:")
for row in a:
    print(*row, sep="\t")

print("\nTotal training instances:", len(a))

n = len(a[0]) - 1
h = ['0'] * n

print("\nInitial hypothesis:", h)

#with header: for row in a[1:]:
for row in a:
    if row[n] == 'Yes':     # Example: '1', 'positive'
        for j in range(n):
            if h[j] == '0' or h[j] == row[j]:
                h[j] = row[j]
            else:
                h[j] = '?'

        print("Hypothesis:", h)

print("\nMaximally specific hypothesis:", h)


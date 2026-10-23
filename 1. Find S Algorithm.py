import csv

a = []

with open(r"Example1.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        a.append(row)

print("\nTable-")
for row in a:
    print(*row, sep="\t")

data = a #with header: data = a[1:]

print("\nTotal training instances:", len(data))

num_attribute = len(a[0]) - 1
hypothesis = ['0'] * num_attribute

print("\nInitial hypothesis:", hypothesis)

for i in range(len(data)):
    attributes = data[i][:-1]
    target = data[i][-1]

    if target == "Yes":      # Example: '1', 'positive'
        for j in range(num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == attributes[j]:
                hypothesis[j] = attributes[j]
            else:
                hypothesis[j] = '?'

    print("\nHypothesis for training instance", i + 1, "is:")
    print(hypothesis)

print("\nFinal maximally specific hypothesis:")
print(hypothesis)


   



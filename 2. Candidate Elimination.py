import csv
a = []
with open(r"Example1.csv","r",newline = "")as file:
    reader = csv.reader(file)
    for row in reader:
        a.append(row)

print("\nTable")
for row in a :
    print(*row,sep = "\t")

data = a[1:]
print("\nlenght - ",data)

attribute = len(a[0])-1
S = '0' * attribute
G = '0' * attribute
print("\nInital hypothesis of S- ", S)
print("\nInital hypothesis of G - ",G)

for i in range(len(data)):
    attributes = data[i][:-1]
    target = data[i][-1]

    if target == "yes":      # Example: '1', 'positive'
         for j in range(attribute):
             if S[j] == attributes[j]:
                 S[j] = attributes[j]
             elif S[j] != attributes[j]:
                 S[j] = '?'
    print("\nStep - ",i+1)
    print("Specific Hypothesis- ", S)
    print("General hypothesis- ",S)
print("FInal S - ", S)
print("final G - ",G)

 



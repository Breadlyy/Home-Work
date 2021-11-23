lst1 = [
  {'name': 'Josef Novák', 'age': 27},
  {'name': 'Jan Srp', 'age': 80}
]
# create a copy of lst1
lst2 = []
for v in lst1:
    lst2.append(v)
lst2.pop()
lst2[0]['age'] = 15
print(lst1)
print(lst2)
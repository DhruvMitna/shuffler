from random import choice

items = input("Enter the items (separated by a comma) which you want to randomly sort: ")
itemsList = items.split(",")
list2, outList = itemsList, []

print()

if len(itemsList) > 1:

 for _ in range(len(itemsList)):

  selected = choice(list2)

  outList.append(selected)
  list2.remove(selected)

else:

 print("You must enter at least 2 items.")

for selection in outList:

 print(selection)
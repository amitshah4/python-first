import traceback

#Worknig with 
# [] lists Unordered Mutable Hetrogenious
# {} dictionaries  Ordered Mutable Key-Value
# () tuples Unordered Immutable Hetrogenious

months = ['January','February','March']

months.append('April')
months.append('May')
months.append('May')
months.append('May')
months.append('May')
months.remove('February')
months.insert(1,'February')
months.pop(-2)
months.sort()
months.remove('May')

print("Starting the loop of list")
for index, month in enumerate(months):
    print(index,month)

print(months)
print(type(months))

print(set(months))
print(type(set(months)))

months =set(months) #set data type
months.add('June')
months.remove("May")
#NOTE elements in set can not be refereed by index 

print("Starting the loop of set")

for index, month in enumerate(months):
    print(index,month)

    
try: 
    print(months[6])
except Exception as e:
    #  print(ValueError)
    print("Something went wrong:",e)
    
"""

This is a block of comments instead of 
using multiple # satements 
Multilne comment

"""
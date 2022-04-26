# from typing import KeysView
# from unicodedata import name

# in the input function do we need the : especially when we write
from unicodedata import name


students=[{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
# print(students[0]["name"])
# for student in students:print("Hello ",student.get("name"),"you were born in 2002") 
print("Hello ",students[0]["name"],"you were born in 2001")
print("Hello ",students[1]["name"],"you were born in 2000")
print("Hello ",students[2]["name"],"you were born in 2002")
print("Hello ",students[3]["name"],"you were born in 2000")

# divisible_by_three=range(1,n)
# for x in divisible_by_three:
#     if x%3==0:
#         print(x)
divisible_by_three=int(input("Enter a number :"))
if (divisible_by_three%3==0):
  
          print("{} is divsible by 3:".format(divisible_by_three))
else:
    print("{} is not divisible by 3 :".format(divisible_by_three)) 
smallest=[3,6,8,2,4,1,5,7]
x=min(smallest)
print(x)
t=['a','b','a','e','d','b','c','e','f','g','h']
y=list(set(t))
divisible_by_seven=[]
for numb in range(100,201):
    if (numb %7==0):
        divisible_by_seven.append(numb)
print(divisible_by_seven)

 >>> country_codes["Burundi"]=257#one links the key to the dictionary and assign it with its value
>>> print(country_codes)
{'Kenya': 254, 'Uganda': 256, 'Rwanda': 250, 'Burundi': 257}
>>> country_codes["Egypt"]=420#one links the key to the dictionary and assign it with its value
>>> print(country_codes)
{'Kenya': 254, 'Uganda': 256, 'Rwanda': 250, 'Burundi': 257, 'Egypt': 420}
>>> country_codes.pop("Uganda")#is a method that removes an item in a dict by taking in the key of the specified item.
256
>>> print(country_codes)
{'Kenya': 254, 'Rwanda': 250, 'Burundi': 257, 'Egypt': 420}
>>> #
>>> #also pop returns the value of the key but not in the new dictionary.
>>> #backend Programming languages are:PYTHON \--/LVE Javascipt,Java,c# GO LANG ,Ruby
>>> #i have faith in you in lists that was awesome,dictionaries always.+fan assignment.
[1]+  Stopped                 python3
   
   

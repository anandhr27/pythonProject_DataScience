#-----------------------------------------------------------------------------------
print("="*70)
print("Question 1")
print("="*70)
#-----------------------------------------------------------------------------------
# Need to print the reverse order
aList = [100, 200, 300, 400, 500]

print("Reverse Order using slicing method is:", aList[::-1])
aList.reverse()
print("Reverse Order using in-build method is:", aList)

"""
Output:
Reverse Order using slicing method is: [500, 400, 300, 200, 100]
Reverse Order using in-build method is: [500, 400, 300, 200, 100]
"""

#-----------------------------------------------------------------------------------
print("="*70)
print("Question 2")
print("="*70)
#-----------------------------------------------------------------------------------

List1 = [10, 20, 30]
List2 = [100, 200, 300]

print("List1 \t List2")
for x, y in zip(List1, List2):
    print(x, "\t\t", y)

"""
The output should be:
List1 	 List2
10 		 100
20 		 200
30 		 300
"""
#-----------------------------------------------------------------------------------
print("="*70)
print("Question 3")
print("="*70)
#-----------------------------------------------------------------------------------
List1 = ["a", "b", ["c", "d", ["e","f"],"g","h"],"I","j"]
subList = [1,2,3]

# for item, x in enumerate(List1):
#     print(item, x)

# Output:
# 0 a
# 1 b
# 2 ['c', 'd', ['e', 'f'], 'g', 'h']
# 3 I
# 4 j

"""
# Program for Output:1 
#get the 2nd elements in List1
"""
element_2 = List1[2]

print("2nd element of List1 =: ", element_2)

element_2[2].extend(subList)
print("2nd element after extend subList: ",element_2)

List1[2] = element_2

print("Output of List1 after extend: ", List1)

"""
# Program for Output:2 
#get the 2nd elements in List1
"""
List1 = ["a", "b", ["c", "d", ["e","f"],"g","h"],"I","j"]
subList = [1,2,3]
element_2 = List1[2]

print("2nd element of List1 =: ", element_2)

element_2[2].append(subList)
print("2nd element after append subList: ",element_2)

List1[2] = element_2

print("Output of List1 after append: ", List1)

"""
# Another Method:
List1 = ["a", "b", ["c", "d", ["e","f"],"g","h"],"I","j"]
subList = [1,2,3]

List1[2][2].extend(subList)
print(List1)

List1 = ["a", "b", ["c", "d", ["e","f"],"g","h"],"I","j"]
List1[2][2].append(subList)
print(List1)
"""


"""
the output should be:
1) List1 = [“a”, “b”, [“c”, ”d”, [“e”,”f”,1,2,3],”g”,”h”],”I”,”j”]
2) List1 = [“a”, “b”, [“c”, ”d”, [“e”,”f”,[1,2,3]],”g”,”h”],”I”,”j”]

"""
#-----------------------------------------------------------------------------------
print("="*70)
print("Question 4")
print("="*70)
#-----------------------------------------------------------------------------------
print("Using For Loop")
for item in range(1, 6):
    print(item, end=" ")

print("\n")

print("Using While Loop")
number = 1
while number <=5:
    print(number, end =" ")
    number += 1

print("\n")

#-----------------------------------------------------------------------------------
print("="*70)
print("Question 5")
print("="*70)
#-----------------------------------------------------------------------------------
def myFun(name, age):
    print(name, age)

myFun("Python", 25)


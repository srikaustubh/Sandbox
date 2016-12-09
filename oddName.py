__author__ = 'jc449799'
"""
"""

valid = False
while not valid:
    name = input("Enter your name: ")
    if name != "" and not name.isspace():
        valid = True
print(valid)
print(name)
print("*******************")
for i in range(0,len(name),2):
    print(name[i])

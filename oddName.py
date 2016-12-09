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
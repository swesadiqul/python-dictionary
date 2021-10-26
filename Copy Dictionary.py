#Programmer Sadiq
#By@Sadiqul Islam
#Python - Copy Dictionaries


#Copy a Dictionary
'''
-You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
-There are ways to make a copy, one way is to use the built-in Dictionary method copy().
-Example: Make a copy of a dictionary with the copy() method. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
    }

mydict = student.copy()
print(mydict)

'''Another way to make a copy is to use the built-in function dict().'''
student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
    }
mydict = dict(student)
print(mydict)

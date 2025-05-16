student={
    "name" : "Rishabh Sharma",
    "subjects" :{
        "physics":97,
        "chems" : 98,
        "maths" : 95
    }
}
print (student["subjects"]["chems"])
'''student.keys() : used for printing the keys of the dictionary'''
print (student.keys())
'''in This by using list we have type casted the information of dictionary in the list'''
print (list(student.keys()))
'''by using len funtion we have clculated the lenght of the dictionary keys'''
print (len(list(student.keys())))
'''by using len function we can directly calculate the length of the dictionary'''
print (len(student))
'''student.values(): by using this we can easiely print the values present in the dictionary'''
print (student.values())
'''same we can typecast values in any form'''
print(list(student.values()))
''' student.items: it will return the pairs form the dictionary in the form of tuples'''
print(student.items())
'''can be typecasted'''
print(list(student.items()))
'''we can axisis the pairs individually by this methode'''
pairs=list(student.items())
print(pairs[0])
'''student.update() : using this we add new dictionary or additional keys and values'''
student.update({"city":"delhi"})
print(student)

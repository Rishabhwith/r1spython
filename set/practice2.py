''' figure out a way to store 9 & 9.0 as seperate values in the set (you can take help of buit in data types)'''

'''values= {9,"9.0"}#1st way
print(values)'''

values={
    ("float",9.0),
    ("int",9)
}
print(values)


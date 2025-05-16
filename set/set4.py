'''Q1> how to add the elements to a set'''
'''Ans. By using set.add(element) we can add new elements to the set'''
'''Q2> how to remove the element form the set'''
'''ans. by using the set.remove(ele) we can remove the element'''
'''Q3> how can we clear a set'''
'''ans. by using set.clear() we can clear the set'''
'''Q4> how can we remove a random value'''
'''ans. by using the set.pop() we can remove any random value from the set''' 
collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnaghar")
collection.add((1,2,3,4))
collection.remove(1)#use to remove the element from a set
#collection.clear()# use to clear the set
#print(len(collection))#use to find the length of set
collection.pop()
print(collection)
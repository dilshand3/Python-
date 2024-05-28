list1 = [1,2,3,4,5]
list2 = ["dilshan","sefali","nikhil","jahid-khan"]
list3 = list((2,3,1,3,4))

list1.extend(list2)#this is method is used for connecting multiple list in single list
print(list1)

list2.append("nandini")#it will append the value at end of list
print(list2)

print(list2.__len__())#it will show the length of list we can also write like this print(len(list2))

list2.insert(1,"virat kohli")#this insert item in middle of two list item like 1 is the index where will virat kohli name will set
print(list2)

list1.remove(2)#it will delete the item from list and 2 there is item not any index
print(list1)

print(list1.index(4))#this is will show the index of value 

list3.sort()#this is for the sorting the list 
print(list3)


list4 = list2.copy()#this is will copy the item of list2 into list4
print(list4)
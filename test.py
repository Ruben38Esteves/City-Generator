list1 = [1,2,3,4,5,6,7]
list2 = [3,5,7,8]

#list3 = [x for x in list1 if x in list2]
list3 = list1 + list2
list4 = list1 + [x for x in list2 if x not in list1]

print(list4)
# Ex.1 ================================
list_1 = list(range(1, 101))
list_2 = []
for i in list_1:
    if i % 7 == 0:
        list_2.append(i)
list_3 = list_2[:5]
assert len(list_3) == 5
b= list_3[0]
assert b == 7
print("Answer Ex.1:", (list_3))



#Ex.2 =====================================
numbers_list1=[1,1,1,2,2,2,3,3,4,4,4,4,5,5,5]
numbers_list_exclusive1=dict.fromkeys(numbers_list1)
print("Answer Ex.2",(numbers_list_exclusive1))




#Ex.3 ==================================
numbers_list2=[1,1,1,2,2,2,3,3,4,4,4,4,5,5,5]
numbers_list_exclusive2=set(numbers_list2)
print("Answer Ex.3",(numbers_list_exclusive2))


#Ex.4====================================
cities = ('Minsk', 'Gomel', 'Mogivel', 'Orsha', 'Vitebsk', 'Grodno')
cities_new=list(cities)
assert cities_new!=tuple
cities_new.append("Brest")
print("Answer Ex.3",(cities_new))
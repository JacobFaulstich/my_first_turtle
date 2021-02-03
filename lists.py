'''new_list = ["dog", "cat", "mouse", "bird", "monkey"]
print(new_list)'''

class_list = ["Selena", "Skyler", "Brooke", "Andrew", "Bowen", "Alex", "Landons", "Chloe", "Jacob", "Other TA", "Joshua"]
print(class_list)
class_list.append("Edna")
class_list.append("Ed")
print(class_list)
popped_person = class_list.pop(8)
print(popped_person, "was removed from the class. ")
print("The new class list is,", class_list)
index_number = class_list.index("Brooke")
print(index_number)
pop_brooke = class_list.pop(2)
print(pop_brooke)

'''
mascot_list = ["Eagles", "Warriors", "Panthers", "Tigers", "Woodmen", "Patriots", "Cougars", "Wildcats", "Knights", "Trojans"]


switch = input("What mascot is in the wrong place? ")
switch_index = mascot_list.index(switch)
mascot_list.pop(switch_index)
replace_index = input("Where is it supposed to be? ")
replace_index = int(replace_index)
mascot_list.insert(replace_index, switch)


switch2 = input("What mascot is in the wrong place? ")
switch2_index = mascot_list.index(switch2)
mascot_list.pop(switch2_index)
replace2_index = input("Where is it supposed to be? ")
replace2_index = int(replace2_index)
mascot_list.insert(replace2_index, switch2)

incorrect = input("Which mascot isn't supposed to be in the list? ")
wrong_num = mascot_list.index(incorrect)
mascot_list.pop(wrong_num)

correct = input("Which mascot should be on the list? ")
correct_index = input("where should it be? ")
correct_index = int(correct_index)
mascot_list.insert(correct_index, correct)

print(mascot_list)'''

mascot_list = ["Eagles", "Warriors", "Panthers", "Tigers", "Woodmen", "Patriots", "Cougars", "Wildcats", "Knights", "Trojans"]

print("The current list is", mascot_list)
 
remove = input("Which mascot is incorrect? ")
remove_index = mascot_list.index(remove)
mascot_list.pop(remove_index)
print("The new list is....", mascot_list)

add = input("which mascot is missing? ")
add_index = int(input("Where should the missing mascot go? "))
mascot_list.insert(add_index, add)
print("The new list is....", mascot_list)
 
swap1 = input("What is the first mascot that is out of order? ")
swap2 = input("What is the second mascot that is out of order? ")
swap1_index = mascot_list.index(swap1)
swap2_index = mascot_list.index(swap2)

mascot_list.pop(swap2_index)
mascot_list.pop(swap1_index)

mascot_list.insert(swap1_index, swap2)
mascot_list.insert(swap2_index, swap1)

print("The final list is....", mascot_list)

'''bfast_list = ["Waffles", "Pancakes", "French Toast", "Bacon", "Cereal"]
for food in bfast_list:
    print("(-:",food, ":-)")
print("Bacon is the best though...")'''

'''circle_list = [2, 3, 5, 7, 9, 11]
for radius in circle_list:
    area = 3.14159 * (radius ** 2)
    print("The area of a circle with radius", radius, "is", area)'''

number_mult_list = [10400, 10660, 12285, 12480, 13118, 13832, 14560, 17045, 17521, 17680, 18200, 18718, 19054, 20839, 21359]
mult_7_list = []
mult_13_list = []
mult_both_list = []

for numbers in number_mult_list: 
    rem_by_7 = numbers % 7
    rem_by_13 = numbers % 13
    if (rem_by_7 == 0) and (rem_by_13 != 0):
        mult_7_list.append(numbers)
    if (rem_by_13 == 0) and (rem_by_7 != 0):
        mult_13_list.append(numbers)
    if (rem_by_7 == 0) and (rem_by_13 == 0):
        mult_both_list.append(numbers)

print("These numbers are divisble by 7:", mult_7_list)
print("These numbers are divisble by 13:", mult_13_list)
print("These numbers are divisble by both 7 and 13:", mult_both_list)


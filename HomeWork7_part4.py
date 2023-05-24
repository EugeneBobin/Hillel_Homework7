def common_elements(count1, count2):
    multiples_of_3 = set(range(3, count1 * 3 + 1, 3))
    multiples_of_5 = set(range(5, count2 * 5 + 1, 5))
    result = multiples_of_3.intersection(multiples_of_5)
    return result
count1 = int(input("enter first range :"))
count2 = int(input("enter second range :"))
print(common_elements(count1, count2))

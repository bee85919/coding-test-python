def stringify(list):
    string = ''
    for l in list:
        string += str(l)
    return int(string)


def solution(num_list):
    list1 = [x for x in num_list if x%2 == 1]
    list2 = [x for x in num_list if x%2 == 0]
    string1 = stringify(list1)
    string2 = stringify(list2)
    return string1 + string2
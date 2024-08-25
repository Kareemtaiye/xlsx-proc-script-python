def find_max(num_list) -> int:
    maximum = 0
    for number in num_list :
        maximum = number if number > maximum else maximum
    return  maximum

def unique(item_list) -> list:
    unique_list = []
    for item in item_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


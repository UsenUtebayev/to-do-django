def divide_dict_by_3(dictionary):
    result = []
    temp_dict = {}
    counter = 0
    for key, value in dictionary.items():
        temp_dict[key] = value
        counter += 1
        if counter % 3 == 0:
            result.append(temp_dict)
            temp_dict = {}
    if temp_dict:
        result.append(temp_dict)
    return result

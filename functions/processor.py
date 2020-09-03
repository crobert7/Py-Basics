def process_numbers(unproccesed_list):
    numbers = []
    if isinstance(unproccesed_list, list) == False:
        return numbers
    for item in unproccesed_list:
        if isinstance(item, int):
            numbers.append(item)
        elif isinstance(item, str):
            if item.isnumeric():
                item = int(item)
                numbers.append(item)
    numbers.sort()
    return numbers


def process_names(unproccessed_list):
    names = []
    if isinstance(unproccessed_list, list) == False:
        return names
    for item in unproccessed_list:
        if isinstance(item, str):
            if item.isnumeric() == True:
                continue
            else:
                names.append(item)
        elif isinstance(item, int):
            continue
    names.sort()
    return names
    

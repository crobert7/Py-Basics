def linear_search(search_list, key):
    for i in search_list:
        if i == key:
            return f"{ key }"
    else:
        return "The element is not in the list"

my_list = (1,2,4,5,6,7)

print(linear_search(my_list, 4))

def linearSearch(data, key):
    for index, value in enumerate(data):
        if value == key:
            return f"The value { value } is in the position { index }"
    return -1

list_data = (1,2,3,5,6,7,9,10,30,1)

print(linearSearch(list_data, 8))
def binary(data, key):
    low = 0
    high = len(data) - 1
    middle = (low + high)

    while low <= high:
        if key == data[middle]:
            return middle
        elif data[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
        
        middle = (low + high)
    return None

my_data = [1,7,10,35,44,67,80,120]
print(binary(my_data,120))
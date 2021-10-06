def binary_search(data, key):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = low + high
        guess = data[mid]
        if guess == key:
            return mid
        if guess > key:
            high = mid - 1
        if guess < key:
            low = mid + 1
    return None

my_list = [1,3,5,7,9,13,33]
my_search = binary_search(my_list, 33)
print(my_search)

def binarySearch(data, key):
    low = 0 # low end of search area
    high = len(data) - 1 # high end of search area
    middle = (low + high) # middle element index
    location = -1 # return value of -1 if not found 

    while low <= high and location == -1:
        print(remaining_elements(data, low, high))
        print(' ' * middle, end = '') # output spaces for  alignment
        print('*') # indidcate current middle

        # if the element is found at the middle
        if key == data[middle]:
          location = middle # location is the current middle
        elif data[middle] > key: # middle element is too high
          high = middle - 1 # eliminate the higher half
        else: # middle element is too low
          low = middle + 1 # eliminate lower half

        middle = (low + high) # recalculate the middle 
    return location

def remaining_elements(data, low, high):
    return ' ' * low + ' '.join(str(s) for s in data[low:high + 1])

def main():
    data_array = [1,2,7,9,11,13,17,24,35,40]

    search_key = int(input('Enter an integer value: '))

    while search_key != -1:
        location = binarySearch(data_array, search_key)

        if location == -1:
            print(f'{search_key} was not found \n')
        else:
            print(f'{search_key} found in position {location}')

        search_key = int(input('Enter an integer value: '))

if __name__ == '__main__':
    main()
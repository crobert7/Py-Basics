def compareTriplets(a, b):
    results =  {"a": 0, "b": 0}
    i = 0
    j = 0
    n = len(a)

    while i < n and j < n: 
        if a[i] < b[j]:
            results["b"] += 1
            print(f'i: {a[i]} j:{b[j]}')
            i += 1
            j += 1
        elif a[i] == b[j]:
            results["b"] += 0
            results["a"] += 0
            i += 1
            j += 1
        else:
            results["a"] += 1
            print(f'i: {a[i]} j:{b[j]}')
            i += 1
            j += 1
                
    return results.values()


result =  compareTriplets([1,2,3], [2,2,4])
print(result)
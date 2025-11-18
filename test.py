def getMinimumCost(arr):
    total_cost = 0

    while len(arr) > 1:
        arr.sort()
        print(arr)
        a = arr.pop(0)
        b = arr.pop(0)
        merge_cost = a+b
        print(total_cost)
        total_cost += merge_cost
        print(total_cost)
        arr.append(a+b)

    return total_cost


a = [5, 3, 5, 2]
print(getMinimumCost(a))

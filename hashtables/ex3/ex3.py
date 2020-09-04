

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #to flatten arrays
    flat = [i for sub in arrays for i in sub]

    count = {}
    for num in flat:
        if num not in count:
            count[num] = 1
        else:
            count[num] +=1
    
    result = [i[0] for i in list(count.items()) if i[1] == len(arrays)]


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

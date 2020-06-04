def intersection(arrays): # O(2kn) => O(n)
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = {'intersection': []}
    #find longest array in arrays
    k = len(arrays)
    n = 0
    for i in range(k):
        if len(arrays[i]) > n:
            n = len(arrays[i])
    # iterate through that loop
    for i in range(n):
        # at each iteration, add the number at that index from all other arrays to numbers with a value of 1
        for j in range(k):
            if i > len(arrays[j]) - 1:
                continue
            num = arrays[j][i]
            if num in numbers:
                # increase the value of a number in numbers if the number is found again
                numbers[num] += 1
                # if the amount of a number reaches the number of arrays it is added to numbers.intersection
                if numbers[num] == k:
                    numbers['intersection'].append(num)
            else:
                numbers[num] = 1
    #return numbers.'intersection'
    return numbers['intersection']


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # arrays = [
    #     [1, 2, 3, 4, 5],
    #     [12, 7, 2, 9, 1],
    #     [99, 2, 7, 1,]
    # ]

    # print(arrays)

    print(intersection(arrays))

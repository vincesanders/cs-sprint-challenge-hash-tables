def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    duplicates = []
    numbers = {}
    for num in a:
        if num < 0:
            num_absolute = num * -1
            if num_absolute in numbers:
                duplicates.append(num_absolute)
            else:
                numbers[num_absolute] = 1
        else:
            if num in numbers:
                duplicates.append(num)
            else:
                numbers[num] = 1
    return duplicates


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

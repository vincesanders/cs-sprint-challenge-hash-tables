def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    values = {}
    for i in range(len(weights)):
        if weights[i] not in values:
            values[weights[i]] = i
        co_key = limit - weights[i]
        if co_key in values and values[co_key] is not i:
            co_index = values[co_key]
            if i >= co_index:
                return [i, co_index]
            else:
                return [values[co_key], i]
    return None

weights_4 = [4,4]
print(get_indices_of_item_weights(weights_4, 4, 8))
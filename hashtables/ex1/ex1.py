def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    wei_indexes = {}

    for i in range(0, length):
        wei_indexes[weights[i]] = i

    for i in range(0, length):
        if (limit - weights[i]) in wei_indexes:
            wei = i
            wei2 = wei_indexes[limit - weights[i]]
            if wei <wei2:
                wei, wei2 = wei2, wei
            return (wei, wei2)


    return None

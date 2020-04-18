#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        target = limit - weights[i]
        found = hash_table_retrieve(ht, target)
        if found is None:
            hash_table_insert(ht, weights[i], i)
        elif found is not None:
            return [i, found]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

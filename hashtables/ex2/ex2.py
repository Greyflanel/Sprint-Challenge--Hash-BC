#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for flight in tickets:
        hash_table_insert(hashtable, flight.source, flight.destination)
        source = "NONE"
    for i in range(length):
        destined = hash_table_retrieve(hashtable, source)
        route[i] = destined
        source = destined
    del route[-1]
    return route

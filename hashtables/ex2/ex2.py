#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    flights = {}
    for i in tickets:
        flights[i.source] = i.destination

    #creating the array for the trip
    route = []
    #starting point
    cur = flights["NONE"]

    while cur != "NONE":
        route.append(cur)
        cur = flights[cur]
    route.append("NONE")


    return route


#to test with different info 
ticket_1 = Ticket("NONE", "LAX")
ticket_2 = Ticket("LAX", "SFO")
ticket_3 = Ticket("SFO", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
# expected = ["LAX", "SFO", "NONE"]
print(reconstruct_trip(tickets, 3))
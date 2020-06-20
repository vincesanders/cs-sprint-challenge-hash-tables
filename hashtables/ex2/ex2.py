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
    route = []
    for ticket in tickets:
        flights[ticket.source] = ticket.destination
    current_flight = flights['NONE']
    while current_flight != 'NONE':
        route.append(current_flight)
        current_flight = flights[current_flight]
    route.append(current_flight)
    return route

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# print(reconstruct_trip(tickets, len(tickets)))
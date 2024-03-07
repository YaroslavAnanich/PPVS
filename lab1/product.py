class Ticket:
    number = None
    name = None

    def __init__(self, number, name):
        self.number = number
        self.name = name

    def get_ticket_number(self):
        return self.number

    def get_ticket_name(self):
        return self.name



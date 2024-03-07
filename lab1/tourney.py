import active_player, product, service_personnel, track


class Tournament:
    name = None
    ticket_price: int = None
    participants = []
    judge = None
    track = None
    tickets = []
    ticket_seller = None
    places = {}

    def __init__(self, name, ticket_price):
        try:
            if not isinstance(name, str):
                raise TypeError("Name should be a string.")
            if not isinstance(ticket_price, int):
                raise TypeError("Ticket price should be an integer.")
            self.name = name
            self.ticket_price = ticket_price
        except TypeError as e:
            print(f"Error in constructor: {e}")

    def register_participant(self, name, horse=None, speed=None):
        participant = active_player.Participant(name, active_player.Horse(horse, speed))
        self.participants.append(participant)

    def register_ticket_seller(self, name):
        ticket_seller = service_personnel.TicketSeller(name)
        self.ticket_seller = ticket_seller

    def register_judge(self, name):
        judge = service_personnel.Judge(name)
        self.judge = judge

    def register_ticket(self, number, name):
        ticket = product.Ticket(number, name)
        self.tickets.append(ticket)

    def register_track(self, name=None, track_length=None):
        self.track = track.Track(name, track_length)

    def sell_ticket(self):
        if self.ticket_seller:
            self.ticket_seller.sell_ticket(self.tickets, self.ticket_price)
        else:
            print("Ticket seller is not registered.")

    def set_places(self):
        if self.judge:
            self.judge.set_places(self.places, self.participants, self.name, self.track)
        else:
            print("Judge is not registered.")


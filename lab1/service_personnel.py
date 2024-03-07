import random


class Assistant:
    name = None

    def __init__(self, name):
        self.name = name

    def get_assistant_name(self):
        return self.name


class TicketSeller(Assistant):
    def __init__(self, name):
        super().__init__(name)

    def sell_ticket(self, tickets, ticket_price):
        if len(tickets) != 0:
            print(f"The ticket {tickets[0].get_ticket_number()} was sold ", end='')
            print(f"{tickets[0].get_ticket_name()} for {ticket_price} by {self.name}")
            del tickets[0]
        else:
            print("All tickets are sold out!")


class Judge(Assistant):
    def __init__(self, name):
        super().__init__(name)

    def is_have_horse(self, participants):
        if len(participants) > 1:
            for participant in participants:
                if participant.horse.name and participant.horse.speed:
                    continue
                else:
                    print(f"participant number {participant.name} does not have a horse")
                    return False
            return True
    def is_have_track(self, track):
        if track.track_lenght and track.name:
            return True
        else:
            print("Track name or length not found!")
            return False

    def set_places(self, places, participants, name, track):
        if not self.is_have_horse(participants):
            return None
        if not self.is_have_track(track):
            return None
        random.shuffle(participants)
        places = {participant: place for place, participant in enumerate(participants, start=1)}
        for participant, place in places.items():
            print(f"{participant.name} on a {participant.horse.name} took a {place} place in the {name}", end='')
            print(f" with a speed of {participant.horse.speed}")
        print(f"{self.name}'s decision is final!")




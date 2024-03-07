class Participant:
    name = None
    horse = None

    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

    def get_participant_name(self):
        return self.name

    def get_participant_horse(self):
        return self.horse


class Horse:
    name = None
    speed = None

    def __init__(self, name=None, speed=None):
        self.name = name
        self.speed = speed

    def get_horse_name(self):
        return self.name

    def get_horse_speed(self):
        return self.speed
class Track:
    name = None
    track_lenght = None

    def __init__(self, name=None, track_length=None):
        self.name = name
        self.track_lenght = track_length

    def get_name(self):
        return self.name

    def get_length(self):
        return self.track_lenght

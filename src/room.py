class Room:
    def __init__(self, name, cap, entry, till):
        self.name = name
        self.capacity = cap
        self.song_list = []
        self.guest = []
        self.entry_fee = entry
        self.till = till

    def number_of_guests(self):
        return len(self.guest)

    def get_capacity(self):
        return self.capacity

    def add_to_till(self, amount):
        self.till += amount

    def sign_in_guest(self, guest):
        self.guest.append(guest)

    def sign_out_guest(self, guest):
        if guest in self.guest:
            self.guest.remove(guest)

    def add_toons(self, song):
        self.song_list.append(song)

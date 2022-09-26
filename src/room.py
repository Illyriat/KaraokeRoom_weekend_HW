class Room:
    def __init__(self, name, cap):
        self.name = name
        self.capacity = cap
        self.song_list =[]
        self.guest = []

    def sign_in_guest(self, guest):
        self.guest.append(guest)

    def sign_out_guest(self, guest):
        for guest in self.guest:
            if guest == guest:
                self.guest.remove(guest)

    def add_toons(self, song_list):
        self.song_list.append(song_list)
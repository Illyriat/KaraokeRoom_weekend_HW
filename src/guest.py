class Guest:
    def __init__(self, name, funds, fav_song):
        self.name = name
        self.funds = funds
        self.favourite_song = fav_song

    def can_afford(self, amount):
        return amount <= self.funds

    def pay_amount(self, amount):
        self.funds -= amount

    def cheer_for_song(self, songs):
        for song in songs:
            if song.title == self.favourite_song:
                return "Whoo!"
        return None

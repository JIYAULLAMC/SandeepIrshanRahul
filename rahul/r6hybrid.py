class marvels:
    def __init__(self):
        self.hero1 = "ironman"
        self.hero2 = 'Captain americ '
    def heros(self):
        print("we have so many super man")
class ironman(marvels):
    def __init__(self):
        super().__init__()
        self.strength = "iron suit"
    def tony_stark(self):
        print("i have a plan of attack , call captain")
        print("do you trust me ")
class captain_america(marvels):
    def __init__(self):
        self.strength1 = "shield"
    def steve_rogers(self):
        print("i can do this for all day ")
        print("i doooooo!!!")
class Avengers_endgame(ironman, captain_america):
    def __init__(self):
        ironman.__init__(self)
        captain_america.__init__(self)
        self.strength2 = "hulk"
        self.stringth3 = "thor"
    def endgame(self):
        print("we have finished the end game ")
    def __call__(self):
        return "hello heros "


avg = Avengers_endgame()
print(avg())


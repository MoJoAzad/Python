class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    
    def sleep(self):
        self.energy+=25
        print("I'm sleepy")
        return self

    def eat(self):
        self.energy+=5
        self.health+=10
        print("I'm full")
        return self

    def play(self):
        self.health+=5
        print("let's play")
        return self

    def noise(self):
        print("Bark")
        return self
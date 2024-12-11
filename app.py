class Bird:
    def speak(self):
        print("Chirp")

class Parrot(Bird):
    def speak(self):
        print("Squawk")

def make_bird_speak(bird):
    bird.speak()

parrot = Parrot()
make_bird_speak(parrot)

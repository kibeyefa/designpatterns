class TheaterLights:

    def on(self):
        pass

    def off(self):
        pass

    def dim(self, degree:int):
        print("Dimming light to {}%".format(degree))


class PopcornPopper:

    def on(self):
        print("Turning on popcorn popper")

    def off(self):
        print("Turning off popcorn popper")

    def pop(self):
        print("Popcorn popper popping corn")


class Screen:

    def up(self):
        print("Screen going up")

    def down(self):
        print("Screen going down")


class CdPlayer:

    def on(self):
        pass

    def off(self):
        pass

    def eject(self):
        pass


class DVDPlayer:

    def on(self):
        print("Turning on Dvd")

    def off(self):
        print("Turning off Dvd")

    def play(self, movie: str):
        print(f"Playing {movie}")

    def stop(self):
        print("Stopping Dvd")

    def eject(self):
        print("Ejecting")


class Projector:

    def on(self):
        print("Turning on Projector")

    def off(self):
        print("Turning off Projector")

    def tvMode(self):
        pass

    def wideScreenMode(self):
        print("Wide screen mode set")


class Tuner:

    def on(self):
        print("Turning on Tuner")

    def off(self):
        print("Turning off Tuner")

    def setAM(self):
        pass

    def setFm(self):
        pass

    def setFrequency(self):
        pass


class Amplifier:

    def on(self):
        print("Turning on Amplifier")

    def off(self):
        print("Turning off Amplifier")

    def setDvd(self, dvd):
        self.dvd = dvd
        print("Setting Dvd")

    def setSurroundSound(self):
        print("Setting Surround Sound")

    def setVolume(self, volume):
        print("Setting volume to {}".format(volume))


class HomeTheaterFacade:

    def __init__(self, amp: Amplifier, tuner:Tuner, dvd: DVDPlayer, cd: CdPlayer, projector: Projector, lights: TheaterLights, screen: Screen, popper: PopcornPopper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper


    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setDvd(self.dvd)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def endMovie(self):
        print("Shutting down home theater...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()


dvd = DVDPlayer()
amp = Amplifier()
tuner = Tuner()
cd = CdPlayer()
lights = TheaterLights()
projector = Projector()
screen = Screen()
popper =PopcornPopper()

x = HomeTheaterFacade(amp, tuner, dvd, cd, projector, lights, screen, popper)
x.watchMovie("Harry Potter and the Half blood prince")
x.endMovie()
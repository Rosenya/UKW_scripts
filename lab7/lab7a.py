#import math

pi=3,14

class Figura:

    def nazwa(self):

        return "Figura"

    def pole(self):

        pass

    def obwod(self):

        pass


class Kwadrat(Figura):

    def __init__(self, a):

        self.a = a

    def nazwa(self):

        return "Kwadrat"

    def pole(self):

        return self.a ** 2

    def obwod(self):

        return 4 * self.a


class Prostokat(Figura):

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def nazwa(self):

        return "Prostokąt"

    def pole(self):

        return self.a * self.b

    def obwod(self):

        return 2 * (self.a + self.b)


class Kolo(Figura):

    def __init__(self, r):

        self.r = r

    def nazwa(self):

        return "Koło"

    def pole(self):

        return pi * self.r ** 2

    def obwod(self):

        return 2 * pi * self.r


figury = [

    Kwadrat(4),

    Prostokat(2, 5),

    Kolo(3)

]


for figura in figury:

    tekst = (f"{figura.nazwa()}\nPole: {figura.pole()}\nObwód: {figura.obwod()}\n")

    print(tekst)

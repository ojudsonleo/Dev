class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 77, 78, 78, 79, 79, 80, 81, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 90,]


    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a Dog")

    def talk(self):
        print("Bark!")



    def add_weight(self, weight):
        self.weight = weight

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow  Hi i am", self.name, "and i am", self.age, "years old and i am a Cat")

    def talk(self):
        print("Meow!")

        # time = 2:57:08 / 6:21:12

class Lion(object):
    # TODO: Lion class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 77, 78, 78, 79, 79, 80, 81, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 90,]


    def talk(self):
        print("kkkk!")

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a Lion i will eat every animal")

    def add_weight(self, weight):
        self.weight = weight


    def talk(self):
        print("Bark!")


class snake(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 77, 78, 78, 79, 79, 80, 81, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 90,]


    def speak(self):
        print("sss Hi i am", self.name, "and i am", self.age, "years old and i am a snake")

    def add_weight(self, weight):
        self.weight = weight


    def talk(self):
        print("ssssssss!")



class tiger(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.data = [name]


    def talk(self):
        print("KKKKKKKKKK!")



    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a tiger and i will also eat every animal")

    def add_weight(self, weight):
        self.weight = weight


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x + self.y + p.x)

    def __sub__(self, p):
        return Point(self.x - p.x - self.y - p.x)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self):
        return "Point(x=" + str(self.x) + "," + "y=",  str(self.y) + ")"

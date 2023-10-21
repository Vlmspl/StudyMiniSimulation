import random


class Student:

    def __init__(self, name=None):
        self.name = name
        self.studies = True
        self.hapiness = 50
        self.progress = 0
        self.passed = False
        self.Day = 0

    def study(self):
        print("time to study")
        self.progress += 0.12
        self.hapiness -= 5

    def chill(self):
        print("time to chill")
        self.hapiness += 10
        self.progress -= 0.01

    def sleep(self):
        print("time to sleep")
        self.hapiness += 3

    def is_alive(self):
        if self.progress < 0.5:
            print("Cast out")
            self.studies = False
        elif 0.5 < self.progress < 1:
            print("studied well")
        elif self.progress >= 1:
            print("passed")
            self.studies = False
            self.passed = True

    def live(self):
        print(self.Day)
        for i in range(1,3):
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.study()
            elif live_cube == 2:
                self.chill()
            elif live_cube == 3:
                self.sleep()

        self.sleep()
        self.Day += 1
        print("-------------------------------------------------------------------------------------------------------")


new_student = Student("Nick")
for i in range(0, 356+1):
    new_student.live()
new_student.is_alive()
print("passed:",new_student.passed)

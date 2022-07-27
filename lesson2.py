class ItSchool:
    bootcamp = 15000
    time = "8:30"


kunduz = ItSchool()
yasir = ItSchool()
aliya = ItSchool()
yasir.bootcamp = 15000
yasir.free = True
# print(yasir.__dict__)
# # print()
# print(aliya.__dict__)
# print(ItSchool.__dict__)
# print(yasir.bootcamp)
# print(aliya.bootcamp)


class CarCarolla:
    wheels = 4
    volume = 1.8
    engine = "v6"
    kuzov = "sedan"

    def __init__(self, bumper, color, otdelka):
        self.bumpeq = color
        self.otdelka = otdelka

    def get_info(self):
        print(f" {self.bumper} , цвет машины: {self.color} ,"
              f"отделка машины {self.otdelka}")

    def change_otdelka(self, new_otdelka):
        self.otdelka = new_otdelka

    def get_hello(self):
        print("hello world")


# mirlan = CarCarolla("m obes", "white", "alcantara")
# mirlan.get_info()
# mirlan.change_otdelka("alpaka")
# mirlan =CarCarolla("v obves","dark blue", "krocodile")

# mirlan.get_info()

# mirlan.get_hello()
lessons_timur = {
    "peremennye": 100,
    "loop": 87,
    "func": 58,
}
lessons_nasyikat = {
    "peremennye": 100,
    "loop": 90,
    "func": 79,
}
lessons_aliya = {
    "peremennye": 100,
    "loop": 78,
    "func": 98,
}


class Student:
    group = "python_bootcamp_8:30"

    def __init__(self, full_name, age, phone_number, lesson):
        self.full_name = full_name
        self.age = age
        self.phone_number = phone_number
        self.lesson = lesson
        self.avg = 0

    def get_info(self):
        print(f"Группа {self.group},\nЗовут: {self.full_name},\nвозраст:{self.age},\n"
              f"номер телефона: {self.phone_number},\nсредний балл: {self.avg}")

    def set_avg(self):
        result = sum(self.lesson.values()) / len(self.lesson)
        self.avg = round(result)

    def set_avg_2(self):
        count = 0
        for i in self.lesson.values():
            count += i
        self.avg = round(count/len(self.lesson))


timur = Student("Nasirdinov Timur", 18, "+996700688288", lessons_timur)
nasyikat = Student("Arzybaeva Nasyikat", 38, "+996700688288", lessons_nasyikat)
aliya = Student("Narynbekova Alya", 21, "+996700688299", lessons_aliya)
# timur.get_info()
# timur.set_avg()
# timur.get_info()

# nasyikat.set_avg()
# nasyikat.get_info()


# aliya.set_avg_2()
# aliya.get_info()
# print("-----")
# aliya.set_avg()
# aliya.get_info()

class Example:
    pen_a = 'pen A'
    pen_b = 'pen B'

    def __init__(self, a):
        self.a = a
        self.b = 0

    def what_is_it(self, new):
        self.b = new
        return self.b

    def change(self):
        return self.pen_a + self.pen_b

# get global together

    def ozuno_koboit(self):
        result_a = self.a ** self.b
        result_b = self.b ** self.a
        return result_a, result_b
# return result of each selfa**selfb and selfb**selfaa


try_one = Example(3)
x = try_one.what_is_it(2)
y = try_one.change()
z = try_one.ozuno_koboit()
# print('pena:', try_one.pen_a)
# print('penb:', try_one.pen_b)

# print(x)
# print(y)
# print(z)


class Calculator:

    def __init__(self):
        self.number_one = float(input("Enter number 1: "))
        self.number_two = float(input("Enter number 2: "))

    @property
    def plus_number(self):
        return self.number_one + self.number_two

    @property
    def minus_number(self):
        return self.number_one - self.number_two

    @property
    def multiply_number(self):
        return self.number_one * self.number_two

    @property
    def devision_number(self):
        return self.number_one / self.number_two


money = Calculator()
print(money.plus_number)
print(money.minus_number)
print(money.multiply_number)
print(money.devision_number)

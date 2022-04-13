
def main():
    print("What fractions do you wish to compute? For Example: '1/2 * 3_3/4'")
    equation = input()
    print(compute(equation))


class Fraction:
    def __init__(self, whole, numerator, denominator):
        self.whole = whole
        self.numerator = numerator
        self.denominator = denominator

    @classmethod
    def from_string(cls, num):
        if '/' not in num:
            return cls.__init__(int(num), None, None)
        else:
            numerator, denominator = num.split('/')
            return None, int(numerator), int(denominator)

    def __add__(self, other):
        return whole, numerator1 + numerator2, denominator1


def compute(equation):
    num1, operator, num2 = equation.split(' ')
    if operator == '+':
        whole, numerator, denominator = Fraction(parse_num(num1)) + Fraction(parse_num(num2))
    return f"{numerator}/{denominator}"


def parse_num(num):
    """ Returns (whole, numerator, denominator)"""



if __name__ == '__main__':
    main()

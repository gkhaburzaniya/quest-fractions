from fractions import Fraction


def main():
    print("What fractions do you wish to compute? For Example: '1/2 * 3_3/4'")
    equation = input()
    print(compute(equation))


def compute(equation):
    num1, operator, num2 = equation.split(' ')
    num1, num2 = parse_num(num1), parse_num(num2)
    answer = None
    if operator == '+':
        answer = num1 + num2
    elif operator == '*':
        answer = num1 * num2
    if answer is None:
        return f"Invalid operator: {operator}"

    return format_answer(answer)


def parse_num(num):
    if '/' not in num:
        numerator, denominator = int(num), 1
    elif '_' not in num:
        numerator, denominator = num.split('/')
        numerator, denominator = int(numerator), int(denominator)
    else:
        whole, fraction = num.split('_')
        numerator, denominator = fraction.split('/')
        whole, denominator = int(whole), int(denominator)
        sign = -1 if whole < 0 else 1
        # so that -1_2/3 is -1 + -1 * 2/3
        numerator = int(whole) * denominator + sign * int(numerator)
    return Fraction(numerator, denominator)


def format_answer(answer):
    if answer.denominator == 1:
        return str(answer.numerator)
    elif abs(answer.numerator) < answer.denominator:
        return f"{answer.numerator}/{answer.denominator}"
    elif abs(answer.numerator) > answer.denominator:
        # -3//2 gives -2, so have to correct for that
        sign = -1 if answer.numerator < 0 else 1
        whole = sign * (abs(answer.numerator) // answer.denominator)

        remainder = abs(answer.numerator) % answer.denominator
        return f"{whole}_{remainder}/{answer.denominator}"


if __name__ == '__main__':
    main()

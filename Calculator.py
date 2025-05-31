def main():
    num1 = int(input("Enter the first number:\n"))
    num2 = int(input("Enter the second number:\n"))
    calc = input("Choose the calculation : [ + , - , * , / ]\n")
    do_calc = 0
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    if calc == "+":
        do_calc = add
    elif calc == "-":
        do_calc = sub
    elif calc == "*":
        do_calc = mul
    elif calc == "/":
        do_calc = div
    else:
        do_calc = "NULL"
        print("Choose the correct calculation method from above !!!")
    print(f"The answer is :{do_calc}")
if __name__ == "__main__":
    main()

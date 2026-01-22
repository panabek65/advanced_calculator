import math

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error: Negative number"
    return math.factorial(int(a))

def logarithm(a, base=10):
    if a <= 0:
        return "Error: Non-positive number"
    return math.log(a, base)

def trig_function(a, func):
    if func == "sin":
        return math.sin(math.radians(a))
    elif func == "cos":
        return math.cos(math.radians(a))
    elif func == "tan":
        return math.tan(math.radians(a))

operations = {
    "1": ("Add", add, 2),
    "2": ("Subtract", subtract, 2),
    "3": ("Multiply", multiply, 2),
    "4": ("Divide", divide, 2),
    "5": ("Power", power, 2),
    "6": ("Square Root", sqrt, 1),
    "7": ("Factorial", factorial, 1),
    "8": ("Logarithm (base 10)", logarithm, 1),
    "9": ("Sine", trig_function, 1),
    "10": ("Cosine", trig_function, 1),
    "11": ("Tangent", trig_function, 1)
}

def main():
    print("🌟 Advanced Python Calculator 🌟")
    while True:
        print("\nSelect operation:")
        for key, (name, _, _) in operations.items():
            print(f"{key}. {name}")
        print("12. View History")
        print("13. Exit")

        choice = input("Enter choice (1-13): ")

        if choice == "13":
            print("Goodbye!")
            break
        elif choice == "12":
            print("\nHistory:")
            for h in history:
                print(h)
            continue

        if choice not in operations:
            print("Invalid choice!")
            continue

        name, func, num_args = operations[choice]

        if num_args == 1:
            num = float(input("Enter number: "))
            if name in ["Sine", "Cosine", "Tangent"]:
                result = func(num, name.lower())
            elif name == "Logarithm (base 10)":
                result = func(num)
            else:
                result = func(num)
            history.append(f"{name}({num}) = {result}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = func(num1, num2)
            history.append(f"{name}({num1}, {num2}) = {result}")

        print("Result:", result)

if __name__ == "__main__":
    main()

import math


def calculate(expression):
    try:
        expression = expression.replace("^", "**")

        allowed = {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "factorial": math.factorial
        }

        result = eval(expression, {"__builtins__": {}}, allowed)
        return result

    except:
        return "Error"
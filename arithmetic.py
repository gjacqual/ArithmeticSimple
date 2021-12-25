def arithmetic(expression):
    def separator(symb, str):
        find = str.find(symb)
        if find != -1:
            argums = str.split(symb)
            return argums
        else:
            return False

    operations = ['+', '-', '%', '/', '*']

    for op in operations:
        if expression.find(op):
            argums = separator(op, expression)
            if op == '+':
                if argums:
                    return int(argums[0]) + int(argums[1])
            elif op == '-':
                if argums:
                    return int(argums[0]) - int(argums[1])
            elif op == '%':
                if argums:
                    return int(argums[0]) / 100
            elif op == '/':
                if argums:
                    return int(argums[0]) / int(argums[1])
            elif op == '*':
                stars = 0
                for c in expression:
                    if c == "*":
                        stars += 1
                if stars == 1:
                    argums = separator("*", expression)
                    if argums:
                        return int(argums[0]) * int(argums[1])
                    else:
                        return "None"
                elif stars == 2:
                    argums = separator("**", expression)
                    if argums:
                        if argums[1] == '':
                            return int(argums[0]) * int(argums[0])
                        else:
                            res = int(argums[0])
                            i = 1
                            while i < int(argums[1]):
                                res *= int(argums[0])
                                i += 1
                            return res
                    else:
                        return "None"
expression = input("Enter arithmetic expression: ")
print(arithmetic(expression))




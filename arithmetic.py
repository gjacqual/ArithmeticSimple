def arithmetic(operation):
    def separator(symb, str):
        find = str.find(symb)
        if find != -1:
            argums = str.split(symb)
            return argums
        else:
            return False

    argums = separator("+", operation)
    if argums:
        return int(argums[0]) + int(argums[1])
    else:
        argums = separator("-", operation)
        if argums:
            return int(argums[0]) - int(argums[1])
        else:
            argums = separator("%", operation)
            if argums:
                return int(argums[0]) / 100
            else:
                argums = separator("/", operation)
                if argums:
                    return int(argums[0]) / int(argums[1])
                else:
                    stars = 0
                    for c in operation:
                        if c == "*":
                            stars += 1
                    if stars == 1:
                        argums = separator("*", operation)
                        if argums:
                            return int(argums[0]) * int(argums[1])
                        else:
                            return "None"
                    elif stars == 2:
                        argums = separator("**", operation)
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
expresssion = input("Enter arithmetic expression: ")
print(arithmetic(expresssion))




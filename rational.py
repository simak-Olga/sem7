def calc(l, r, op):
    match op:             # since python 3.10
        case '+':
            res = l + r
        case '-':
            res = l - r
        case '/':
            res = l / r
        case '*':
            res = l * r
    return round(res, 2)


def parse_all(string):
    print (f"Parsing: {string}...\n")
    string = parse(string, ["*", "/"])
    string = parse(string, ["+", "-"])
    return string


def parse(string, opers):
    br1 = string.find("(")
    if br1 >= 0:
        br2 = string.rfind(")")
        string = string.replace(string[br1:br2 + 1], parse_all(string[br1 + 1:br2]))
        return parse_all(string)

    i = 0
    while i < len(string):
        if string[i] in opers:
            if not i:
                i += 1
                continue
            oper = string[i]
            try:
                count = 1
                if string[i + count] == "-":
                    count += 1
                while string[i + count].isdigit() or string[i + count] == ".":
                    count += 1
            except:
                1
            right = string[i + 1:i + count]

            count = 1
            while (string[i - count - 1].isdigit() or string[i - count - 1] == ".") and i - count > 0:
                count += 1
                #print (f"count = {count}, i = {i}")
            if (not string[i - count - 2].isdigit() or not string[0].isdigit()) and i - count > 0:
                count += 1
            left = string[i - count:i]
            print(f"left = {left}, right = {right}, oper = {oper}")
            res = calc(float(left), float(right), oper)
            string = string.replace(f"{left}{oper}{right}", str(res), 1)
            print(f"Res = {string}")
            i = 0
        i += 1
    return string
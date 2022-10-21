from re import findall
from winreg import REG_EXPAND_SZ


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
    return res


def parse(vals, opers):
    if len(vals) < 3:
        return vals
    i = 0
    while 1:
        if vals[i] in opers:
            vals[i - 1] = calc(vals[i - 1],
                               vals[i + 1], vals[i])
            vals.pop(i + 1)
            vals.pop(i)
            i = -1
        i += 1
        if i == len(vals) - 1:
            break
    return vals


def re_parse(string):
    complex_vals = []
    oper_pos = 0

    for i in findall(r"\(.*?\)", string):
        complex_vals.append((complex(sum(map(lambda x: float(x), findall(r"\-?\d+(?:[\.,]\d+)?\b(?!j|\.)", i))),
                                     sum(map(lambda x: float(x), findall(r"-?[\d\.]+(?=j)", i))))))
        if oper_pos + len(i) < len(string):
            complex_vals.append(string[len(i) + oper_pos])
            oper_pos += len(i) + 1
    complex_vals = parse(complex_vals, ("*", "/"))
    complex_vals = parse(complex_vals, ("+", "-"))
    return complex_vals[0]


# string = "(2-0j)+(1+0j)"

# print (re_parse(string))
from pyparsing import *


def tokenize_expression(exp: str):
    expr = Forward()

    double = Word(nums + ".").setParseAction(lambda t: float(t[0]))
    integer = Word(nums).setParseAction(lambda t: int(t[0]))
    variable = Word(alphas)
    string = dblQuotedString
    funccall = Group(variable + "(" + Group(Optional(delimitedList(expr))) + ")")
    array_func = Group(funccall + "[" + Group(delimitedList(expr, "][")) + "]")
    array_var = Group(variable + "[" + Group(delimitedList(expr, "][")) + "]")

    operand = double | string | array_func | funccall | array_var | variable

    expop = Literal("^")
    signop = oneOf("+ -")
    multop = oneOf("* /")
    plusop = oneOf("+ -")

    expr << infix_notation(
        operand,
        [
            ("^", 2, opAssoc.RIGHT),
            (signop, 1, opAssoc.RIGHT),
            (multop, 2, opAssoc.LEFT),
            (plusop, 2, opAssoc.LEFT),
        ],
    )
    return expr.parse_string(exp)


x = tokenize_expression("sin(2*x + y^2)")

print(x)

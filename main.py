from expression_tokenizer import tokenize_expression

# [['sin', '(', [[[2.0, '*', 'x'], '+', ['y', '^', 2.0]]], ')']]
# [[['sin', '(', [[[2.0, '*', 'x'], '+', ['y', '^', 2.0]]], ')'], '/', 2.0]]
# ['log', '(', [2.0, [3.0, '*', 'x']], ')']
# [2.0, '+', 2.0]
# 2.0

string = "2^2+2*x"

tokens = tokenize_expression(string)[0]


def get_derivative(tokens):
    # Just a number
    if type(tokens) == float:
        return 0
    # Function call
    elif type(tokens[0]) == str:
        function_name = tokens[0]
        functions_argument = tokens[2]
    #     match function_name:
    #         case "log":

    #         case "ln":

    #         case "sin":

    #         case "asin":

    #         case "cos":

    #         case "acos":

    #         case "tan":

    #         case "atan":
    #
    #         case "cot":

    #         case "acot":

    #         case _:
    #             print("Not implemented :(")
    # Regular expression
    else:
        argument_one = tokens[0]
        argument_two = tokens[2]
        print(argument_one)
        print(argument_two)
        derivate_one = get_derivative(argument_one)
        derivate_two = get_derivative(argument_two)
        print(derivate_one)
        print(derivate_two)
        arithmetic_operator = tokens[1]

        match arithmetic_operator:
            case "+":
                return [derivate_one, "+", derivate_two]
            case "-":
                return [derivate_one, "-", derivate_two]
            case "*":
                return [
                    [derivate_one, "*", argument_two],
                    "+",
                    [argument_one, "*", derivate_two],
                ]
            case "/":
                return [
                    [
                        [derivate_one, "*", argument_two],
                        "-",
                        [argument_one, "*", derivate_two],
                    ],
                    "/",
                    [argument_two, "^", 2.0],
                ]
            case "^":
                return


print(get_derivative(tokens))

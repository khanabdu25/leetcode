from stack import Stack



def eval_rpn(tokens):
    stack = Stack()
    for tok in tokens:
        if tok == "+":
            second = stack.pop()
            first = stack.pop()
            
            if not second is None and not first is None:
                stack.push(first+second)
            else:
                stack.push(second)
        elif tok == "-":
            second = stack.pop()
            first = stack.pop()
            
            if not second is None and not first is None:
                stack.push(first-second)
            else:
                stack.push(second)
        elif tok == "/":
            second = stack.pop()
            first = stack.pop()
            
            if not second is None and not first is None:
                stack.push(int(first/second))
            else:
                stack.push(second)
        elif tok == "*":
            second = stack.pop()
            first = stack.pop()
            
            if not second is None and not first is None:
                stack.push(first*second)
            else:
                stack.push(second)
        else:
            stack.push(int(tok))
            
    return stack.pop()
    
print(eval_rpn(["2", "1", "+"]))  # 3
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
print(eval_rpn(["2", "3", "*"]))  # 6
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22

# Subtraction order
print(eval_rpn(["7", "3", "-"]))  # 4
print(eval_rpn(["3", "7", "-"]))  # -4

# Division and truncation toward zero
print(eval_rpn(["7", "2", "/"]))  # 3
print(eval_rpn(["-7", "2", "/"]))  # -3
print(eval_rpn(["7", "-2", "/"]))  # -3
print(eval_rpn(["-7", "-2", "/"]))  # 3

# Single operand
print(eval_rpn(["5"]))  # 5
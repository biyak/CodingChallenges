##Author Biya Kazmi
'''
The reverse polish notation is used to evaluate a list of expressions,
operators (+,-,/,*) are listed after the operands (any int or float)
ie postfix notation
'''

def polishNotation(list):
    stack = []
    #We will use a stack to keep track of which operations still need to be done

    operators = ["+", "-", "/", "*"]
    #This helps us distinguish b/w operands and operators

    for i in list:
        if i not in operators:
            stack.append(i)
            #The cool thing about python is that a lot of things
            #dont need to be explained because its written just the way
            #I would explain it!!
        else:
            #The else is if this character IS an operator,
            #In which case, we pop the last two things, which must be
            #numbers, and evaluate them 
            b = eval(stack.pop())
            a = eval(stack.pop())

            #Depending on which operator we have, we evaluate
            if i == "+":
                value = a + b
                #and pop it back onto the stack to further evaluate 
                stack.append(str(value))

            if i == "-":
                value = a - b
                stack.append(str(value))

            if i == "/":
                value = a // b
                stack.append(str(value))

            if i == "*":
                value = a * b
                stack.append(str(value))
                
    #We should be left with one thing on the stack and thats our answer. 
    print(stack[0])
            

polishNotation(["2", "1", "+", "3", "*"])
polishNotation(["4", "13", "5", "/", "+"])

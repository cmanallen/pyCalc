def pyCalc():
	if parCheck(equation) == True:
		solution = postfixSolver(infixToPostfix(equation))
		print(solution)

	else:
		print("Your parenthesis do not match.  Please try again.")


def parCheck(string):
	stack = []
	balanced = True
	index = 0

	while index < len(string) and balanced:

		symbol = string[index]
		
		if symbol == "(":
			stack.append(symbol)
		
		elif symbol == ")":
			if not stack:
				balanced = False
			else:
				stack.pop()

		else:
			pass

		index = index + 1

	if balanced and not stack:
		return True
	else:
		return False


def infixToPostfix(string):

	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1

	operator_stack = []
	output_queue = []
	
	string = list(string)

	for element in string:
		
		if element not in "()+-*/":
			output_queue.append(element)

		elif element == "(":
			operator_stack.append(element)

		elif element in "+-*/" and not operator_stack:
			operator_stack.append(element)

		elif element in "+-*/" and operator_stack:
			
			while operator_stack and prec[operator_stack[-1]] >= prec[element]:
				output_queue.append(operator_stack.pop())
			
			operator_stack.append(element)

		elif element == ")":			
			
			while prec[operator_stack[-1]] > 1:
				output_queue.append(operator_stack.pop())
			
			operator_stack.pop()

		else:
			pass

	while operator_stack:
		output_queue.append(operator_stack[-1])
		operator_stack.pop()

	return ' '.join(output_queue)


def postfixSolver(string):

	string = string.split()
	operand_stack = []

	for element in string:
		if element not in "+-*/":
			operand_stack.append(element)

		elif element == "+":
			new_element = float(operand_stack[-2]) + float(operand_stack[-1])
			operand_stack.pop()
			operand_stack.pop()
			operand_stack.append(new_element)

		elif element == "-":
			new_element = float(operand_stack[-2]) - float(operand_stack[-1])
			operand_stack.pop()
			operand_stack.pop()
			operand_stack.append(new_element)

		elif element == "*":
			new_element = float(operand_stack[-2]) * float(operand_stack[-1])
			operand_stack.pop()
			operand_stack.pop()
			operand_stack.append(new_element)

		elif element == "/":
			new_element = float(operand_stack[-2]) / float(operand_stack[-1])
			operand_stack.pop()
			operand_stack.pop()
			operand_stack.append(new_element)


	return operand_stack



print("Welcome to PyCalc 0.0.0.0.0.2")
print("Please enter your equation to begin.")
print("Everything needs to be space seperated.")
print("You may only use +, -, *, and / as operators.")
equation = input(">> ")
pyCalc()
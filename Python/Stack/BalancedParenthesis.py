# @author
# Aakash.Verma

# In this particular code, we'll be using inbuilt Stack Class because you are already familiar with
# the procedure that Stack works.

# Problem: Check whether the given string forms a set of Balanced Parenthesis or not.

# For example:

# Input: expression = "[[({})]]"
# Output: true

# Input: expression = "[[))"
# Output: false

# Input: expression = "[{]}"
# Output: false

# Approach:

# 1. Whenever we encounter an openning bracket, we'll push it into the stack.
# 2. Whenever we encounter a closing bracket, we'll pop the element out of the stack and
#    we will check whether the popped element is same as the opening bracket of the category of
#    popped element.
# 3. If it satisfies for the complete process until the stack becomes empty, then the parenthesis
#    will be called as balanced, otherwise, if anywhere there is a mismatch, we'll directlty return false.



# this function will return true only when the popped element matches the category of the closing 
# bracket.
# Otherwise, we will return false.
	
def isMatching(openingBracket, closingBracket):
	if(openingBracket is '{' and closingBracket is '}'):
		return True
	if(openingBracket is '(' and closingBracket is ')'):
		return True
	if(openingBracket is '[' and closingBracket is ']'):
		return True
	return False


# function which will return whether the expression is balanced or not */
def isBalanced(expression):

	# initialization of stack of characters
	stack = []
		
	# start iterating over the string
	for i in range(len(expression)):
		# if expression is any of the opening brackets, push it onto the stack */
		if(expression[i] is '{' or expression[i] is '(' or expression[i] is '['):
			stack.append(expression[i])
		else:
			# check if stack is empty, return false directly.
			# Because, having a closing bracket without any opening bracket doesn't mean balanced.
			if(len(stack) == 0):
				return False

			# otherwise check if, current closing brackets matches with the 
			# category of top element of stack, if it so we pop the element.
			# Otherwise, we directly return false.
			if(isMatching(stack.pop(), expression[i]) is not True):
				return False

		# print(stack)
		# if everything is perfect till here and stack becomes empty, means the expression is balanced
		# otherwise, if stack doesn't become empty, then return false.
	if(len(stack) == 0):
		return True
	return False

if __name__ == '__main__':

	expression1 = "[[()]]"
	expression2 = "[[))"
	print(isBalanced(expression1))
	print(isBalanced(expression2))

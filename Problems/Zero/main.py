try:
	n = int(input())
	denominator = int(input())
	print(n // denominator)
except ValueError:
	print("Please enter 2 integers")
except ZeroDivisionError:
	print("Division by zero is not supported")
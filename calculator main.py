# main.py

# Import the custom calculator module
import calculator

# Define test numbers
num1 = 12
num2 = 4

# Perform and display operations
print(f"Addition: {num1} + {num2} = {calculator.add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {calculator.subtract(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {calculator.multiply(num1, num2)}")
print(f"Division: {num1} / {num2} = {calculator.divide(num1, num2)}")

# Test division by zero
print(f"Division by Zero: {num1} / 0 = {calculator.divide(num1, 0)}")

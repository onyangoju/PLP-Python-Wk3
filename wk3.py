# Else example
temperature = 20.5

if temperature > 20:
    print("It's hotter today.")
else:
    print("It's a cold day.")

# Elif example
marks = 85  # You can change the marks value

if marks > 90:
    print("Grade A")
elif marks > 80:
    print("Grade B")
elif marks > 70:
    print("Grade C")
elif marks > 60:
    print("Grade D")
else:
    print("Grade F")

# Elif with input example
# Prompt the user to enter their marks
marks = int(input("Enter your marks: "))

if marks > 90:
    print("Grade A")
elif marks > 80:
    print("Grade B")
elif marks > 70:
    print("Grade C")
elif marks > 60:
    print("Grade D")
else:
    print("Grade F")

# For loop example
basket_of_fruits = ["apple", "mangoes", "oranges", "bananas", "cherry", "kiwi"]

for fruit in basket_of_fruits:
    print(fruit)

# While loop example
count = 1
while count <= 5:
    print(count)
    count += 1

# Def example
def add(a, b):
    sum = a + b
    print("The sum is", sum)

# Calling the function
add(5, 10)

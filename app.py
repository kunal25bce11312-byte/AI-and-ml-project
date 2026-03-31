age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
goal = input("Enter goal (gain/loss/maintain): ")

# Simple calorie formula
bmr = 10 * weight + 6.25 * height - 5 * age + 5

if goal == "gain":
    calories = bmr + 500
elif goal == "loss":
    calories = bmr - 500
else:
    calories = bmr

print("Recommended daily calories:", int(calories))

# Simple diet suggestion
if goal == "gain":
    print("Eat more protein, milk, rice, eggs, bananas")
elif goal == "loss":
    print("Eat fruits, vegetables, avoid sugar, reduce carbs")
else:
    print("Maintain balanced diet")

bmi = weight / ((height/100) ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
else:
    print("You are overweight")

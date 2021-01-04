print("Happy 2021!!!")

# variables
# integers, floats, booleans and strings
secret_of_life = 42
gst_percentage = 0.07
sentence = "The quick brown fox jumps over the lazy dog"
is_raining = True

# BMI calculator
# print is used for output
print("2021 New Year Resolution BMI Calculator")
weight = float(input("Please enter your weight in kg:"))
height = float(input("Please enter your height in metres"))
bmi = weight / (height * height)
print("Your BMI is", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")


# weight = float(weight)
# height = float(height)
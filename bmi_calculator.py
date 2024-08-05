# bmi_calculator.py

# Function to calculate BMI
def calculate_bmi(weight, height):
    """
    This function calculates Body Mass Index (BMI) based on weight and height.
    
    Parameters:
    weight (float): weight in kilograms
    height (float): height in meters

    Returns:
    float: BMI value
    """
    bmi = weight / (height ** 2)
    return bmi

# Function to determine BMI category
def determine_bmi_category(bmi):
    """
    This function determines the BMI category.
    
    Parameters:
    bmi (float): BMI value

    Returns:
    str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main code to interact with the user
try:
    # Input weight and height from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Determine BMI category
    category = determine_bmi_category(bmi)

    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

except ValueError:
    # Handle the error if the input values are not valid numbers
    print("Please enter valid numerical values for weight and height.")

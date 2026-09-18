# TASK 2 - BMI Calculator - Oasis Infobyte

def bmi_calculator():
    print("--- BMI Calculator ---")
    
    try:
        # Take input
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))

        # Validation
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than 0")
            return

        # Calculation
        bmi = weight / (height * height)

        # Classification
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Output
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Error: Please enter numbers only (e.g., 70, 1.75)")

bmi_calculator()

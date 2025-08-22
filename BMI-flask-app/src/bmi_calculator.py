from utils import calculate_bmi, bmi_category

def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

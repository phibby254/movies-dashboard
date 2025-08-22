def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI)
    :param weight_kg: Weight in kilograms
    :param height_m: Height in meters
    :return: BMI value
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than 0")
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    """
    Return BMI category based on WHO standard
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

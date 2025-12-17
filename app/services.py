from typing import Tuple


def calculate_bmi(weight: float, height: float) -> Tuple[float, str, str]:
    """
    Calculate BMI value, category, and display color.

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters or centimeters

    Returns:
        tuple: BMI value, category, and color
    """
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif bmi < 25:
        category = "Normal weight"
        color = "green"
    elif bmi < 30:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"

    return round(bmi, 2), category, color

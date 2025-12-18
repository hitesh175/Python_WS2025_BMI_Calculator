from typing import Tuple


def calculate_bmi(weight: float, height: float) -> Tuple[float, str, str, str]:
    """
    Calculate Body Mass Index (BMI) and return
    BMI value, category, color indicator, and health recommendation.
    """
    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        return (
            bmi,
            "Underweight",
            "blue",
            "Consider a nutritious diet and consult a healthcare professional."
        )
    elif bmi < 25:
        return (
            bmi,
            "Normal weight",
            "green",
            "Maintain a balanced diet and regular physical activity."
        )
    elif bmi < 30:
        return (
            bmi,
            "Overweight",
            "orange",
            "Consider regular exercise and mindful eating habits."
        )
    else:
        return (
            bmi,
            "Obese",
            "red",
            "Consult a healthcare provider for personalized advice."
        )

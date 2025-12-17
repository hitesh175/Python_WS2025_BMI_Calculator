from flask import Blueprint, render_template, request, jsonify
from app.services import calculate_bmi

main = Blueprint("main", __name__)


@main.route("/")
def index() -> str:
    return render_template(
        "index.html",
        bmi=None,
        category=None,
        color=None,
        indicator_position=0,
        error=None
    )



@main.route("/calculate", methods=["POST"])
def calculate() -> str:
    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        if weight <= 0 or height <= 0:
            raise ValueError

        # Convert cm → m if needed
        if height > 3:
            height = height / 100

        bmi, category, color = calculate_bmi(weight, height)

        
        scale_bmi = max(10, min(bmi, 40))

        indicator_position = ((scale_bmi - 10) / (40 - 10)) * 100

        return render_template(
            "index.html",
            bmi=bmi,
            category=category,
            color=color,
            indicator_position=indicator_position
        )

    except ValueError:
        return render_template(
            "index.html",
            error="Please enter valid positive numbers for weight and height.",
            bmi=None,
            category=None,
            color=None
        )


@main.route("/api/bmi", methods=["POST"])
def bmi_api():
    data = request.get_json()

    weight = float(data["weight"])
    height = float(data["height"])

    if height > 3:
        height = height / 100

    bmi, category, color = calculate_bmi(weight, height)

    return jsonify({
        "bmi": bmi,
        "category": category,
        "color": color
    })

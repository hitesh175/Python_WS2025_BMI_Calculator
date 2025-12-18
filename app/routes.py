from flask import Blueprint, render_template, request, jsonify, send_file
from app.services import calculate_bmi
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from typing import Dict, List

main = Blueprint("main", __name__)

# Global in-memory storage (Resets when server restarts)
bmi_history: List[Dict] = []
last_bmi_result: Dict = {}

@main.route("/")
def index() -> str:
    return render_template(
        "index.html",
        bmi=None,
        category=None,
        color=None,
        recommendation=None,
        indicator_position=0,
        error=None,
        history=bmi_history  # Pass history even on load
    )

@main.route("/calculate", methods=["POST"])
def calculate() -> str:
    # Access the global lists to modify them
    global bmi_history
    global last_bmi_result

    try:
        weight_input = request.form["weight"]
        height_input = request.form["height"]
        unit = request.form.get("unit", "metric")

        if not weight_input or not height_input:
            raise ValueError

        weight = float(weight_input)
        height = float(height_input)

        if weight <= 0 or height <= 0:
            raise ValueError

        # Convert imperial → metric for calculation
        calc_weight = weight
        calc_height = height
        if unit == "imperial":
            calc_weight = weight * 0.453592
            calc_height = height * 0.0254

        # Convert cm → m if user entered cm (e.g., 170 instead of 1.7)
        if calc_height > 3:
            calc_height /= 100

        bmi, category, color, recommendation = calculate_bmi(calc_weight, calc_height)

        # Update last result for PDF download
        last_bmi_result = {
            "bmi": bmi,
            "category": category,
            "recommendation": recommendation
        }

        # Add to history list
        bmi_history.append({
            "weight": weight,  # Original input weight
            "height": height,  # Original input height
            "bmi": bmi,
            "category": category
        })

        # Indicator position for UI (scale 10–40)
        scale_bmi = max(10, min(bmi, 40))
        indicator_position = ((scale_bmi - 10) / 30) * 100

        return render_template(
            "index.html",
            bmi=bmi,
            category=category,
            color=color,
            recommendation=recommendation,
            indicator_position=indicator_position,
            history=bmi_history # Passing the updated list
        )

    except ValueError:
        return render_template(
            "index.html",
            bmi=None,
            category=None,
            color=None,
            recommendation=None,
            indicator_position=0,
            history=bmi_history,
            error="Please enter valid positive numbers for weight and height."
        )

@main.route("/history")
def history():
    # Pass the global list to your history.html
    return render_template("history.html", history=bmi_history)

@main.route("/download-pdf")
def download_pdf():
    if not last_bmi_result:
        return "No BMI data available to generate PDF.", 400

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 750, "BMI REPORT")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 710, f"BMI Value: {last_bmi_result['bmi']}")
    pdf.drawString(100, 690, f"Category: {last_bmi_result['category']}")
    pdf.drawString(100, 650, "Health Recommendation:")
    pdf.drawString(120, 630, last_bmi_result["recommendation"])
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="bmi_report.pdf",
        mimetype="application/pdf"
    )
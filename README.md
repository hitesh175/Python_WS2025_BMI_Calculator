BMI Calculator – Flask Web Application

Project Overview
This project is a BMI (Body Mass Index) Calculator Web Application developed as part of the
Python Web Services – Winter Semester 2025 module.

The application allows users to enter their weight and height, and validates the input.
calculates BMI and displays the result, along with a corresponding health category and visual colour indicators.

The project demonstrates:
- Frontend and backend integration using Flask
- Clean code and separation of concerns
- REST API usage
- Docker containerization
- Collaborative development using GitHub



Problem Statement & Motivation
The Body Mass Index (BMI) is a commonly used indicator to assess health risks associated with body weight.
This application provides a simple and user-friendly way to calculate BMI while preventing
invalid inputs and offering clear visual feedback.



Features
- Web-based user interface for BMI calculation
- Input validation with error messages
- BMI category classification with colour indicators
- REST API endpoint for programmatic access
- Dockerized deployment for portability
- Clean, modular code following PEP-8 standards
- View Calculation History
- Download BMI Report.



Technology Stack
- Backend: Python 3.11, Flask
- Frontend: HTML, CSS
- Containerization: Docker
- Version Control: Git & GitHub


<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/0b04bdb3-4217-405b-9e2e-b56d713a28e5" />



How to Run the Application

Option 1: Run Locally (Without Docker)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Open in Browser: http://127.0.0.1:5000



Option 2: 
Run Using Docker (Recommended)

->docker build -t bmi-app .
->docker run -p 5000:5000 bmi-app

Open in browser:

http://localhost:5000



Demo Video

A demo video showing the running application, features, and Docker execution is included
in this repository:

📁 demo_video.mp4



Contributors
Hitesh Kanagala Rajendra Prasad
Vinay Somala

Conclusion
This project demonstrates the development of a complete Python web application
with clean architecture, validation, API support, and containerised deployment.
It follows best practices taught in the course and reflects collaborative development.




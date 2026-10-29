# BMI Calculator — Flask Web Application

A Python Web Services course project for Winter Semester 2025, developed by **Hitesh Kanagala Rajendra Prasad** and **Vinay Somala**.

The application accepts height and weight, validates inputs, calculates BMI, and displays a category with visual feedback.

## Features

- Flask web interface with HTML/CSS templates.
- Input validation and calculation service.
- Programmatic calculation endpoint.
- Calculation history and downloadable reports in the root application.
- Docker configuration.

## Run locally

From the repository root, create and activate an environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python run.py
```

On macOS/Linux, activate with `source .venv/bin/activate`. Open the address printed by Flask, normally `http://127.0.0.1:5000`.

## Run with Docker

```bash
docker build -t bmi-app .
docker run --rm -p 5000:5000 bmi-app
```

Open `http://localhost:5000`.

## Project guide

| Path | Purpose |
| --- | --- |
| [app/routes.py](app/routes.py) | Web routes and request handling |
| [app/services.py](app/services.py) | Calculation logic |
| [app/templates](app/templates/) | Web pages |
| [app/static](app/static/) | Styles and images |
| [run.py](run.py) | Application entry point |
| [Dockerfile](Dockerfile) | Container configuration |
| [Demo video](BMI-WEB_APP_Demo_video.mp4) | Recorded walkthrough |

The repository also retains a nested copy under `BMI Calculator/`. Use the root application for the history/report features described here.

## Scope

This is an educational calculation tool. Displayed categories use the application's programmed thresholds; a numerical result does not provide an individual medical assessment.

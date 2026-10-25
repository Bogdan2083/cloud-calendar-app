from datetime import datetime
from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
  # Отримуємо поточну дату та день тижня
  today = datetime.now().strftime("%d.%m.%Y")
  day_of_week = datetime.now().strftime("%A")

  # HTML-сторінка прямо в коді для зручності
  html = """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Календар - Лабораторна робота</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #74b9ff, #dfe6e9);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.15);
                text-align: center;
                max-width: 400px;
                width: 100%;
            }
            h1 { color: #0984e3; margin-bottom: 10px; font-size: 24px; }
            .date-box {
                font-size: 32px;
                font-weight: bold;
                color: #2d3436;
                margin: 20px 0;
                background: #f1f2f6;
                padding: 15px;
                border-radius: 8px;
            }
            .day { color: #636e72; font-size: 18px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🗓 Інтерактивний календар</h1>
            <p class="day">Сьогодні:</p>
            <div class="date-box">{{ today }}</div>
            <p class="day">{{ day_of_week }}</p>
        </div>
    </body>
    </html>
    """
  return render_template_string(html, today=today, day_of_week=day_of_week)


if __name__ == "__main__":
  app.run(debug=True)
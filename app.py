"""
Health Dashboard - Flask Application Starter
Your task: Follow LAB_GUIDE.md to add form handling!
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


user_data = {}


@app.route('/')
def index():
    """Home page with time/weekend counter"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day_num = datetime.now().weekday()  # Monday=0, Sunday=6
    days_to_weekend = 5 - day_num if day_num < 5 else 0
    
    return render_template('index.html', 
                         time=current_time, 
                         days_to_weekend=days_to_weekend,
                         user_data=user_data,)



@app.route('/submit', methods=['POST'])

def submit():
    """Handle form submission"""
    # Get form data
    name = request.form.get('name', '')
    sleep_hours = request.form.get('sleep_hours', '')
    water_intake = request.form.get('water_intake', '')
    exercise_hours = request.form.get('exercise_hours', '')
    
    
    # Store it
    user_data['name'] = name
    user_data['sleep_hours'] = sleep_hours

    # Water Data
    user_data['water_intake'] = water_intake

    # Excercise Data
    user_data['exercise_hours'] = exercise_hours
    
    # Sleep feedback
    try:
        hours = float(sleep_hours)
        if hours < 7:
            user_data['sleep_feedback'] = "⚠️ Try to get more sleep!"
        else:
            user_data['sleep_feedback'] = "✅ Great sleep!"
    except ValueError:
        user_data['sleep_feedback'] = "Please enter valid hours."
    
    # Water feedback
    try:
        glasses = int(water_intake) if water_intake else 0
        if glasses < 8:
            user_data['water_feedback'] = "💧 Try to drink more water!"
        else:
            user_data['water_feedback'] = "✅ Great hydration!"
    except ValueError:
        user_data['water_feedback'] = "Please enter valid water amount."
    
    # Exercise feedback
    try:
        exercise = float(exercise_hours) if exercise_hours else 0
        if exercise < 1:
            user_data['exercise_feedback'] = "🏃‍♂️ Try to exercise more!"
        else:
            user_data['exercise_feedback'] = "✅ Great workout!"
    except ValueError:
        user_data['exercise_feedback'] = "Please enter valid exercise hours."
    
    print("DEBUG - Data stored:", user_data) 

    # Redirect back to home
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
"""
Health Dashboard - Flask Application Starter
Your task: Follow LAB_GUIDE.md to add form handling!
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for user data (we'll add to this during the lab!)
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
                         user_data=user_data,) # < - NEW!


# TODO: Add /submit route here (see LAB_GUIDE.md Part 3)

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
    user_data['exercise_hours'] = exercise_hours
    
    # Generate feedback
    try:
        hours = float(sleep_hours)
        if hours < 7:
            user_data['feedback'] = "⚠️ Try to get more sleep!"
        else:
            user_data['feedback'] = "✅ Great sleep!"
    except ValueError:
        user_data['feedback'] = "Please enter valid hours."
    
    print("DEBUG - Data stored:", user_data) # <-- Show your collected variable in terminal.
    # ... it's being stored as an in-memory Python dict... it's not going to an API or database yet! 
    # We'll work on that in a future lecture.

    # Redirect back to home
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
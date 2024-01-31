
# Import required modules
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define the routes

# Home page
@app.route('/')
def index():
    """ Render the home page. """
    return render_template('index.html')

# Lessons page
@app.route('/lessons')
def lessons():
    """ Render the lessons page. """
    return render_template('lessons.html')

# Lessons by level page
@app.route('/lessons/<lesson_level>')
def lessons_by_level(lesson_level):
    """ Render the lessons page for a specific level. """
    return render_template('lessons.html', lesson_level=lesson_level)

# Resources page
@app.route('/resources')
def resources():
    """ Render the resources page. """
    return render_template('resources.html')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

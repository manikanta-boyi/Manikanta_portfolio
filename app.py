from flask import Flask, render_template

app = Flask(__name__)


projects = [
    {
        "title": "Recycling Ideas Blog",
        "description": "Users share household waste stories. AI bot gives recycling ideas.",
        "tech": ["Flask", "SQLite", "Flask-Login"],
        "github": "https://github.com/manikanta-boyi/Flask_recycle_project.git",
        "link" : "https://flask-recycle-project.onrender.com",
        "image": "recycling.png"
    },
    {
        "title": "Family Health Records App",
        "description": "Secure family health management with emergency mode.",
        "tech": ["Flask", "JWT", "SQLite","Flask-Login"],
        "github": "https://github.com/manikanta-boyi/Family_Health_App",
        "link" : "https://family-health-app.onrender.com",
        "image" : "health.png"
    },
    {
        "title": "SkillConnect",
        "description": "Voice-driven job platform with secure agreements and tracking.",
        "tech": ["Flask", "Speech-to-Text"],
        "github": "https://github.com/manikanta-boyi/Skill_connect.git",
        "link" : "https://skill-connect.onrender.com",
        "image": "skillconnect.png"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def project_list():
    return render_template('projects.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

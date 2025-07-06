from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mail import Mail, Message
import os
from forms import ContactForm


app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')

mail = Mail(app) # Initialize Flask-Mail


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

@app.route('/contact',methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        user_msg = form.message.data

        msg = Message(subject=f"New Portfolio Contact from {name} ({email})",
                      recipients=[os.environ.get('EMAIL_USER')],
                      html=f"""
                        <p>You have received a new message from your portfolio contact form:</p>
                        <p><strong>Name:</strong> {name}</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p><strong>Message:</strong></p>
                        <p>{user_msg}</p>""")
        try:
            print(f"Attempting to send email from: {app.config.get('MAIL_USERNAME')}")
            print(f"Using server: {app.config.get('MAIL_SERVER')}:{app.config.get('MAIL_PORT')}")
            # DO NOT print app.config.get('MAIL_PASSWORD') in production, only for debugging!
            # print(f"Using password: {app.config.get('MAIL_PASSWORD')}")
            mail.send(msg)
            flash('Meassage sent successfully','success')
            return redirect(url_for('contact'))
        except Exception as e:
            print(f'Message not sent {e}')
            flash('Message sending failed','error')
            return redirect(url_for('contact'))
    return render_template('contact.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)

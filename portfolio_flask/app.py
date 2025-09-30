from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# --- Personal Info ---
about = {
    "name": "Gummadidala Sai Krishna",
    "summary": """Enthusiastic B.Tech CSE (AIML) student at Parul University with a strong foundation 
    in Python, Java, SQL, HTML, CSS, and JavaScript. Skilled in problem-solving, data structures, 
    and AI/ML concepts with hands-on project experience. Passionate about building scalable 
    applications and aiming to grow as a Software Engineer.""",
    "cgpa": "8.01",
    "email": "saikrishnagummadidala34@gmail.com",
    "github": "https://github.com/Saikrishna1124",
    "linkedin": "https://www.linkedin.com/in/sai-krishna-gummadidala-261984354/",
    "profile_img": "images/profile.jpg"
}

# --- Projects ---
projects = [
    {"title": "Infinity", "desc": "Expense manager for shopping, transport, and food. Built with HTML, CSS, JavaScript."},
    {"title": "CampusPro", "desc": "College management system. Built with Django, HTML, CSS, JavaScript."},
    {"title": "Web Portfolio", "desc": "Responsive portfolio website with projects, skills, and contact info."}
]

# --- Certificates ---
certificates = [
    "Python Essential-1 (Cisco)",
    "Data Science (Cisco)",
    "AWS Academy",
    "Algorithm Thinking – Mastering DSA",
    "Internship Offer - Python Developer Intern at Elevate Labs"
]

@app.route("/")
def home():
    return render_template("index.html", about=about, projects=projects, certificates=certificates)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        flash(f"Thanks {name}, I received your message! I’ll reply soon at {email}.")
        return redirect(url_for("contact"))

    return render_template("contact.html", about=about)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    projects = [
        {
            "title": "Python Projects",
            "description": "A collection of scripts and applications in Python.",
            "icon": "icons/python.svg",
            "url": "/python-projects"
        },
        {
            "title": "Unity3D and C# Projects",
            "description": "Games made with Unity3D and desktop/mobile applications made with C#, WPF and .NET MAUI.",
            "icon": "icons/unity.svg",
            "url": "/unity-projects"
        },
        {
            "title": "Photoshop Skills",
            "description": "Graphic design and photo editing using Photoshop.",
            "icon": "icons/photoshop.svg",
            "url": "/photoshop-projects"
        },
    ]
    return render_template("index.html", year=datetime.now().year, projects=projects)

@app.route("/python-projects")
def python():
    return render_template("python_projects.html")

@app.route("/unity-projects")
def unity():
    return render_template("unity_projects.html")

@app.route("/photoshop-projects")
def photoshop():
    return render_template("photoshop_projects.html")


if __name__ == "__main__":
    app.run(debug=True)
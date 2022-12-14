import os
from flask import render_template

from src import config
from src.models import Person


app = config.connex_app
app.add_api(os.path.join(config.basedir, "swagger.yml"))


@app.route("/")
def home():
    people = Person.query.all()
    print(os.listdir('.'))
    return render_template("home.html", people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

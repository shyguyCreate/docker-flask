from flask import Flask, render_template

app = Flask(__name__)

# Anadir a los miembros manualmente
member1 = "Integrante 1"
member2 = "Integrante 2"
member3 = "Integrante 3"


@app.route("/")
def hello_world():
    return render_template(
        "index.html", member1=member1, member2=member2, member3=member3
    )


# Run app
if __name__ == "__main__":
    app.run()

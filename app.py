from flask import Flask, render_template, request

app = Flask(__name__)

heroes = [
    {"name": "Universal Man", "image": "/static/universalman.jpg", "info": "Controls molecular density"},
    {"name": "Psycwave", "image": "/static/psycwave.jpg", "info": "Psychic waves"},
    {"name": "Everseer", "image": "/static/everseer.jpg", "info": "Sees future"},
    {"name": "Macroburst", "image": "/static/macroburst.jpg", "info": "Energy blast"},
    {"name": "Phylange", "image": "/static/phylange.jpg", "info": "Fire control"},
    {"name": "Blazestone", "image": "/static/blazestone.jpg", "info": "Lava body"},
    {"name": "Dynaguy", "image": "/static/dynaguy.jpg", "info": "Explosions"},
    {"name": "Downburst", "image": "/static/downburst.jpg", "info": "Wind waves"},
    {"name": "Hypershock", "image": "/static/hypershock.jpg", "info": "Seismic waves"},
    {"name": "Apogee", "image": "/static/apogee.jpg", "info": "Gravity control"},
    {"name": "Blitzerman", "image": "/static/blitzerman.jpg", "info": "Electricity"},
    {"name": "Tradewind", "image": "/static/tradewind.jpg", "info": "Air control"},
    {"name": "Vectress", "image": "/static/vectress.jpg", "info": "Energy beams"},
    {"name": "Gazerbeam", "image": "/static/gazerbeam.jpg", "info": "Laser eyes"},
    {"name": "Stormicide", "image": "/static/stormicide.jpg", "info": "Storm control"},
    {"name": "Gamma Jack", "image": "/static/gammajack.jpg", "info": "Gamma radiation"},
    {"name": "Splashdown", "image": "/static/splashdown.jpg", "info": "Water control"},
    {"name": "Plasmabolt", "image": "/static/plasmabolt.jpg", "info": "Plasma blasts"},
    {"name": "Metaman", "image": "/static/metaman.jpg", "info": "Metal body"},
    {"name": "Mr. Incredible", "image": "/static/mrincredible.jpg", "info": "Super strength"}
]

@app.route("/island")
def island():
    return render_template("island.html")

@app.route("/finances")
def finances():
    return render_template("finances.html")

@app.route("/omnidroid")
def omnidroid():
    return render_template("omnidroid.html")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == "Kronos":
            return render_template("kronos.html")
        else:
            return render_template("login.html", error="Неверный пароль")
    return render_template("login.html")


@app.route("/supers")
def supers():
    return render_template("supers.html")


@app.route("/supers/table")
def supers_table():
    return render_template("heroes_table.html", heroes=heroes)


@app.route("/watch")
def watch():
    return render_template("watch.html")


@app.route("/supers/search", methods=["GET", "POST"])
def supers_search():
    results = []
    if request.method == "POST":
        query = request.form.get("name", "").lower()
        results = [h for h in heroes if query in h["name"].lower()]
    return render_template("heroes_search.html", results=results)



if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000 ,debug=True)
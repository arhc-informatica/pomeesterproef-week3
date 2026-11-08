from flask import Flask, render_template, redirect, url_for
import database

app = Flask(__name__)

# Zorg dat de tabel bestaat zodra de app start.
database.init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/laad-basisdata")
def laad_basisdata():
    """Route om basis-data in de database te laden."""
    database.laad_basisdata()
    return redirect(url_for("data"))


@app.route("/data")
def data():
    """Pagina die data uit de database toont (SELECT *)."""
    items = database.get_items()
    return render_template("data.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
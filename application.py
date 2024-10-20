from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


class CatalogItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Language name
    category = db.Column(db.String(50), nullable=False)  # Region where it's spoken
    speakers = db.Column(db.Integer)  # Number of speakers
    countries = db.Column(db.String(200))  # Countries where it's spoken
    language_family = db.Column(db.String(100))  # e.g., Niger-Congo, Afroasiatic
    writing_system = db.Column(db.String(100))  # e.g., Latin, Arabic, Ge'ez
    iso_code = db.Column(db.String(3))  # ISO 639-3 code
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Language {self.name}>"


@app.route("/")
def view_index():
    featured_languages = CatalogItem.query.limit(3).all()
    categories = CatalogItem.query.with_entities(CatalogItem.category).distinct().all()
    categories = [category[0] for category in categories]
    return render_template("index.html", featured_languages=featured_languages, categories=categories)


@app.template_filter("format_number")
def format_number(value):
    return f"{value:,}"


@app.route("/category/<string:category>")
def view_category(category):
    languages = CatalogItem.query.filter_by(category=category).all()
    return render_template("category.html", category=category, languages=languages)


@app.route("/language/<int:language_id>")
def view_language(language_id):
    language = CatalogItem.query.get_or_404(language_id)
    return render_template("language.html", language=language)


@app.route("/about")
def view_about():
    return render_template("about.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

import os
from datetime import datetime

from flask import Flask, flash, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
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


class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    contribution_type = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(200))
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="pending")  # pending, approved, rejected

    def __repr__(self):
        return f"<Contribution {self.id} - {self.language}>"


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


@app.route("/contribute", methods=["GET"])
def contribute():
    return render_template("contribute.html")


@app.route("/submit_contribution", methods=["POST"])
def submit_contribution():
    # Extract data from form
    name = request.form.get("name")
    email = request.form.get("email")
    language = request.form.get("language")
    contribution_type = request.form.get("contribution_type")
    content = request.form.get("content")
    source = request.form.get("source")

    # Create new Contribution object
    new_contribution = Contribution(
        name=name, email=email, language=language, contribution_type=contribution_type, content=content, source=source
    )

    try:
        # Add to database
        db.session.add(new_contribution)
        db.session.commit()
        flash("Thank you for your contribution! Our team will review it shortly.", "success")
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while submitting your contribution. Please try again.", "error")
        print(f"Error: {str(e)}")  # Log the error for debugging

    return redirect(url_for("contribute"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

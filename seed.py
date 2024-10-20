from application import CatalogItem, db, app

# # Create a Flask app and configure the database
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use your actual database URI
# db = SQLAlchemy(app)

def seed_database():
    languages = [
        {
            "name": "Swahili",
            "category": "East Africa",
            "speakers": 100000000,
            "countries": "Tanzania, Kenya, Uganda, Rwanda, Burundi, DRC",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "swa"
        },
        {
            "name": "Hausa",
            "category": "West Africa",
            "speakers": 70000000,
            "countries": "Nigeria, Niger, Ghana, Cameroon",
            "language_family": "Afroasiatic",
            "writing_system": "Latin, Arabic",
            "iso_code": "hau"
        },
        {
            "name": "Yoruba",
            "category": "West Africa",
            "speakers": 30000000,
            "countries": "Nigeria, Benin, Togo",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "yor"
        },
        {
            "name": "Amharic",
            "category": "Horn of Africa",
            "speakers": 22000000,
            "countries": "Ethiopia",
            "language_family": "Afroasiatic",
            "writing_system": "Ge'ez",
            "iso_code": "amh"
        },
        {
            "name": "Oromo",
            "category": "Horn of Africa",
            "speakers": 30000000,
            "countries": "Ethiopia, Kenya",
            "language_family": "Afroasiatic",
            "writing_system": "Latin",
            "iso_code": "orm"
        },
        # Add more languages here...
    ]

    # Create all tables
    db.create_all()

    # Check if the database is already populated
    if CatalogItem.query.first() is None:
        for lang in languages:
            language = CatalogItem(**lang)
            db.session.add(language)
        
        db.session.commit()
        print(f"Added {len(languages)} languages to the database.")
    else:
        print("Database already contains data. Skipping seed.")

if __name__ == '__main__':
    with app.app_context():
        seed_database()
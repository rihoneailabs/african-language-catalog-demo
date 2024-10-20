from application import CatalogItem, db, app


def seed_database():
    languages = [
        {
            "name": "Swahili",
            "category": "East Africa",
            "speakers": 100000000,
            "countries": "Tanzania, Kenya, Uganda, Rwanda, Burundi, DRC",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "swa",
        },
        {
            "name": "Hausa",
            "category": "West Africa",
            "speakers": 70000000,
            "countries": "Nigeria, Niger, Ghana, Cameroon",
            "language_family": "Afroasiatic",
            "writing_system": "Latin, Arabic",
            "iso_code": "hau",
        },
        {
            "name": "Yoruba",
            "category": "West Africa",
            "speakers": 30000000,
            "countries": "Nigeria, Benin, Togo",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "yor",
        },
        {
            "name": "Amharic",
            "category": "Horn of Africa",
            "speakers": 22000000,
            "countries": "Ethiopia",
            "language_family": "Afroasiatic",
            "writing_system": "Ge'ez",
            "iso_code": "amh",
        },
        {
            "name": "Oromo",
            "category": "Horn of Africa",
            "speakers": 30000000,
            "countries": "Ethiopia, Kenya",
            "language_family": "Afroasiatic",
            "writing_system": "Latin",
            "iso_code": "orm",
        },
        # South African Bantu languages
        {
            "name": "Zulu",
            "category": "Southern Africa",
            "speakers": 12000000,
            "countries": "South Africa, Zimbabwe",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "zul",
        },
        {
            "name": "Xhosa",
            "category": "Southern Africa",
            "speakers": 8200000,
            "countries": "South Africa",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "xho",
        },
        {
            "name": "Tswana",
            "category": "Southern Africa",
            "speakers": 5000000,
            "countries": "South Africa, Botswana, Namibia",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "tsn",
        },
        {
            "name": "Sesotho",
            "category": "Southern Africa",
            "speakers": 4600000,
            "countries": "South Africa, Lesotho",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "sot",
        },
        {
            "name": "Tshivenda",
            "category": "Southern Africa",
            "speakers": 1000000,
            "countries": "South Africa, Zimbabwe",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "ven",
        },
        {
            "name": "Sepedi (Northern Sotho)",
            "category": "Southern Africa",
            "speakers": 4400000,
            "countries": "South Africa",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "nso",
        },
        {
            "name": "Setswana",
            "category": "Southern Africa",
            "speakers": 5000000,
            "countries": "South Africa, Botswana",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "tsn",
        },
        {
            "name": "Siswati (Swazi)",
            "category": "Southern Africa",
            "speakers": 1400000,
            "countries": "South Africa, Eswatini",
            "language_family": "Niger-Congo",
            "writing_system": "Latin",
            "iso_code": "ssw",
        },
    ]
    
    try:
        db.drop_all()
    except Exception as e:
        print(f"Error dropping tables: {e}")

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


if __name__ == "__main__":
    with app.app_context():
        seed_database()
        print("Database seeding completed successfully.")

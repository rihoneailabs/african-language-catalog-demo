# African Languages Catalog

## Description

The African Languages Catalog is a web application designed to showcase and provide information about the diverse languages spoken across the African continent. This project aims to celebrate linguistic diversity, promote language preservation, and serve as an educational resource for anyone interested in African languages.

## Features

- Browse languages by region
- Detailed information pages for individual languages
- Search functionality (planned)
- User-friendly interface built with Flask and styled with Tailwind CSS

## Technologies Used

- Python 3.11+
- Flask
- SQLAlchemy
- SQLite (can be configured for other databases)
- Tailwind CSS
- HTML5

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/african-languages-catalog.git
   cd african-languages-catalog
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   python seed.py
   ```

5. Run the application:
   ```
   flask run
   ```

6. Open a web browser and navigate to `http://localhost:5000`

## Project Structure

```
african-languages-catalog/
│
├── app.py
├── models.py
├── seed.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── category.html
│   └── language.html
│
└── static/
    └── css/
        └── styles.css
```

## Contributing

If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

- Email: [Rihone AI Labs](mailto:info@rihonegroup.com)

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Wikipedia - African Languages](https://en.wikipedia.org/wiki/Languages_of_Africa)

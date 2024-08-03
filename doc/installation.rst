Installation
============

Start by cloning the Github repository ::

    git clone https://github.com/Antinii/Projet_13_orange_county_lettings.git

Move to the project directory with the command::

    cd Projet_13_orange_county_lettings

Create the virtual environment ::

    python -m venv venv

Activate the virtual environment ::

    For Mac / Linux: source venv/bin/activate
    For Windows: venv/Scripts/activate

Install dependencies using the command::

    pip install -r requirements.txt

Create a .env file in the project directory containing::

    SECRET_KEY=your_secret_key
    SENTRY_DSN=your_sentry_key

If the static files aren't loaded properly type that command::

    python manage.py collectstatic
    
Launch the server using::

    python manage.py runserver

You can now access the wedsite localy at that address http://127.0.0.1:8000


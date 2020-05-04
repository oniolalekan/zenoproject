# zenoproject
Zeno Developer Challenge

An sql file is in the root of this project. Create a db (zenobackend) and run the sql file script to create the tables and data

Create a virtual environment and run the dependencies in the requirements file. On Windows run: "mkvirtualenv virtualenvNAME" 
and do pip install the dependencies.

Activate the virtual environment. On Windows: change the directory to 'src' and run 'workon virtualenvNAME'

Start the server by running: python manage.py runserver 7000 --settings=zenobackend.settings.test
The endpoints are exposed on port 7000.

# Backend Test
Just a lil' test for BOSC
### Running the project
Using pipenv
```bash
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py loaddata ingredients
pipenv run python manage.py runserver
```
Using pip & venv
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata ingredients
python manage.py runserver
```
**Happy coding!**

![alt text][logo]

[logo]: https://media.giphy.com/media/1EaY3GTjg20fe/giphy.gif "Happy coding"

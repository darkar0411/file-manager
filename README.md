python3 -m pip install -r requirements.txt

pip freeze > requirements.txt

pyinstaller --clean -w main.py

pyinstaller --clean -w --add-data "conf/*.json;conf" main.py
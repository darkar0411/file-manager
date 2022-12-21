### dev
[task list](https://github.com/luisdanielta/file-manager/tree/task-list)

### requirements
python3 -m pip install -r requirements.txt
pip freeze > requirements.txt

### build
pyinstaller --clean -w main.py
pyinstaller --clean -w --add-data "conf/*.json;conf" main.py
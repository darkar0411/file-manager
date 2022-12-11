        # strucutre app
        # - menu
        # - select folder
        # - path folder
        # - groups of buttons
        # - groups of plugins
        # - treeview of path folder
        # - treeview buttons selected and delete
        # extras
        # - search
        # - filter
        # - sort
        # - copy or move, all tipyes files, subfolders
        # - rename
        # - menu buttons selected - menu buttons types files
        # - actions recents

python3 -m pip install -r requirements.txt

pip freeze > requirements.txt

pyinstaller --clean -w main.py

pyinstaller --clean -w --add-data "conf/*.json;conf" main.py
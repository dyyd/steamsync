import os

EXT = os.environ['EXT'] or ''
VERSION = "0.3.0"
filename = f"steamsync-{VERSION}{EXT}"

os.system(
    f"pyinstaller --onefile .\main.py --name {filename} --noconsole --icon logo.ico"
)

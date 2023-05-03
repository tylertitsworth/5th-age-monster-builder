python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt
pyinstaller .\src\app.py --onefile --clean --noconsole
cp -r data dist\data
Compress-Archive -LiteralPath dist -DestinationPath 5th-age-monster-builder.zip

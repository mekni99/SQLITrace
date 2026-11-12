@echo off
cd /d "%~dp0output"
start "" "http://127.0.0.1:8765/index.html"
echo Serveur TNtrace actif sur http://127.0.0.1:8765/index.html (Ctrl+C pour arreter)
python -m http.server 8765

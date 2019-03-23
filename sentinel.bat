cd C:\sentinel & C:\sentinel\venv\Scripts\activate.bat & start /B python .\run.py & timeout 5 >nul & cd sentinelfrontend & python .\main.py && deactivate && exit

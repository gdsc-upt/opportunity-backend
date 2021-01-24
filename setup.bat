@echo off

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
call set PATH=%PATH%;%USERPROFILE%\.poetry\bin;
call set PATH=%USERPROFILE%\AppData\Local\Programs\Python\Python39;%PATH%;
call set PATH=%USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts;%PATH%;
echo Python system interpreter:
where python
python --version || goto :error
echo Checking variables configuration
pip install pyyaml
python src/check_config_vars.py || goto :error

echo Activating venv
call poetry shell
for /f %%p in ('poetry env info --path') do set POETRYPATH=%%p
call %POETRYPATH%\Scripts\activate.bat
echo Python version:
python -VV

echo installing requirements...
call poetry install || goto :error

echo Setting up database...
python src/manage.py migrate || goto :error
echo Ensuring admin user...
python src/manage.py shell -c "import createsuperuser"
goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%

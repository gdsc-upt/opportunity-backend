@echo off

IF NOT EXIST venv (
    echo Python system interpreter:
    where python
    python --version || goto :error
    echo Checking variables configuration
    python src/check_config_vars.py || goto :error
    echo Creating new virtualenv...
    python -m venv venv || goto :error
)

echo Activating venv
call deactivate >NUL 2>NUL
call venv\Scripts\activate.bat
echo Python version:
python -VV
echo pip version:
pip --version

if "%1" == "--no-pip" goto :no-pip
echo installing requirements...
python -m pip install -U pip || goto :error
pip install -U -r requirements.txt || goto :error

:no-pip
echo Setting up database...
python src/manage.py migrate || goto :error
echo Ensuring admin user...
python src/manage.py shell -c "import createsuperuser"
goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%

@echo off

IF NOT EXIST venv (
    echo Python system interpreter:
    where python
    python --version || goto :error
    pip install pyyaml
    pip install poetry
    echo Checking variables configuration
    python src/check_config_vars.py || goto :error
)

echo Activating venv
poetry shell || goto :error
echo Python version:
python -VV

echo installing requirements...
poetry install || goto :error

echo Setting up database...
python src/manage.py migrate || goto :error
echo Ensuring admin user...
python src/manage.py shell -c "import createsuperuser"
goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%

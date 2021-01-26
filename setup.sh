curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
export PATH="$HOME/.poetry/bin:$PATH"

echo "Create shell..."
poetry env use 3.9

poetry env info --path
echo "Activating virtual environment..."
source "$( poetry env info --path )/bin/activate"
echo "Installing requirements..."
poetry install

echo "Checking config.yml exists and has basic setup..."
python src/manage.py shell -c "import check_config_vars"

echo "Setting up database..."
python src/manage.py migrate

echo "Ensuring admin user..."
python src/manage.py shell -c "import createsuperuser"

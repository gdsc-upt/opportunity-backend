if [ -z "$1" ]
  then
    python src/manage.py makemigrations
elif [ -z "$2" ]; then
    python src/manage.py makemigrations "$1"
    else python src/manage.py makemigrations -n "$1" "$2"
fi

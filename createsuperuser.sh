#!/usr/bin/env bash

imports='from administration.models import User;'
create_superuser='User.objects.create_superuser("admin", "admin@example.com", "admin")'

echo "$imports $create_superuser" | python src/manage.py shell

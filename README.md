# Django Template Project

This project is intended to provide a nice and comfortable way to start a
new project with Django and it's common settings.

### Project setup (Windows)
* Install a database(use only one of these methods):
    1. Bare metal install:
        * download and install [PostgreSQL]
        * open your database client (such as **pgAdmin**) and create a user with a password, such as ``root`` and password
         ``toor``
        * create a new database and give it a name (for example ``template``) and set **collation** to ``UTF-8``
    1. Using **Docker** (if you have Windows **Home** edition then install [Docker for Win 10 Home]):
        * download and install [Docker]
        * open a **CMD** or **Git Bash Shell** and go (change directory / cd) to the ``database`` folder of this project
        * run ``dir`` in **CMD** or ``ls`` in **Git Bash Shell** and if you don't see ``docker-compose.yml`` file then you're in the wrong
         directory. Try again...
        * if you see ``docker-compose.yml`` file, then run ``docker network create pdb`` and then ``docker-compose up -d``
        * open in browser ``localhost:8085``, log in with ``admin@example.com`` username and ``admin`` password
        * create a new database and give it a name (for example ``template``) and set **collation** to ``UTF-8``
* Install [Python] and make sure to select **Add Python 3.9 to PATH**
when installation wizard appears
* Copy ``template.config.yml`` to ``config.yml`` and add your specific configuration. The most important ones are ``SECRET_KEY``, ``DB_NAME
``,``DB_PASSWORD``
* Run ``setup.bat``

[MariaDB]: https://mariadb.org/download/
[PostgreSQL]: https://www.postgresql.org/download/
[Docker]: https://www.docker.com/products/docker-desktop
[Python]: https://www.python.org/downloads/
[Docker for Win 10 Home]: https://docs.docker.com/docker-for-windows/install-windows-home/?fbclid=IwAR3x-_z4-B3RbAfNliOfogpqVcZlOzQLmpOc5kgU4p0d4Tbfa43TDruWrmw

# Ambiente de Desenvolvimento

PostgreSQL
=======
* Classic install
~~~
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
sudo psql -U postgres
create database parking;
~~~

* Docker container
~~~
sudo docker run -it --rm --network some-network postgres psql -h some-postgres -U postgres
sudo docker start some-postgres
sudo docker exec -it some-postgres /bin/bash
psql -U postgres
create database parking;
~~~

Python
=======
~~~
curl https://pyenv.run | bash
exec $SHELL
pyenv install 3.8.5
~~~

Dependences
=======

At the root of the project

* Create Virtualenv

Python 3
~~~
pip3 install virtualenv
~~~
or Python 2
~~~
pip install virtualenv
~~~

* install dependences
~~~
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
~~~

* Start Project
~~~
python manage.py migrate
python manage.py runserver
~~~

Testings
=======

Into path
~~~
cd test_api/
chmod +x execute.sh
./execute.sh
~~~

* Run GET testings
~~~
python test_get.py
~~~
* Run POST testings
~~~
python test_post.py
~~~
* Run DELETE testings
~~~
python test_delete.py
~~~
* Run PUT testings
~~~
python test_put.py
~~~

Swagger docs
http://localhost:8000/swagger
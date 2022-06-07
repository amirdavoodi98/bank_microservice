# create a virtual enviroment
> python -m venv env
# active venv
# on linux :
> source env/bin/activate
#on windows : 
> env/script/activate
# install requirements
> pip install -r requirements.txt
# create database
> python manage.py migrate
#runserver on port 7000
> python manage.py runserver 7000
#run grpcserver on port 50052
> python manage.py grpcrunserver 127.0.0.1:50052


# CelleryPro

A script that uses celery to execute a task asynchronously.


## How to run:

open the the terminal and activate virtual environment using the command: "source env/bin/activate"

open another erminal and start the celery worker using the command : "celery -A your_project_name worker --loglevel=info"

open another terminal to connect to the redis server using the command: "redis-server"

in the terminal you opened the virtual environment, open the python shell and import the function and run it by adding ".delay()", check the celery terminal for your result
## required packages

pip3 install requests

pip3 install lxml

pip3 install bs4

brew install redis

pip3 install celery

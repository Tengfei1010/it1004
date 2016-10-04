## What is It1004 ?
    It1004 is a web site for collecting security news from top security web sites,
    which is developed by django framework. 

##  How to deploy it ?
##### 1. update system
    
    Let’s get started by making sure our system is up to date.
    
     $ sudo apt-get update
     $ sudo apt-get upgrade
    

##### 2. install virtualenv and create an environment for your app
    
     $ sudo aptitude install -y python-virtualenv supervisor nginx gunicorn
     $ virtualenv ~/Env/mysite 
     $ source ~/Env/myiste/bin/active
     $ pip install -r requiremnets.txt

##### 3. deploy it

    $ python manage.py creatsuperuser
    $ python manage.py syncdb
    $ gunicorn mysite.wsgi:application --bind example.com:80
 
## please enjoy it ~ 
    
    



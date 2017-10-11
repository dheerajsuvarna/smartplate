##Techfest Munich Github Project

## Set environment

```
conda create -n techfest_munich python=3.6
source activate techfest_munich
```

```
pip install tensorflow python-socketio
conda install -c flask gunicorn
conda install scikit-learn nb_conda pandas matplotlib pickleshare

pip freeze > requirements.txt

```
Create Procfile file in root with:

	web: gunicorn --pythonpath ./webapp/ webapp:app --log-file=-


Create Heroku app
https://progblog.io/How-to-deploy-a-Flask-App-to-Heroku/
heroku login
cd root
heroku git:remote -a appname

git add .
git commit -am 
git push heroku master

1. Create github repository

	git init
	git add README.md
	git commit -m "first commit"
	git remote add origin https://github.com/alexmach77/techfest_smartplate.git
	git push -u origin master

2. Install Heroku

		brew install heroku/brew/heroku
		cd root project path
		heroku create
		git remote -v
		git remote rename heroku techfest_munich#rename app
		git push techfest_munich master



####Socket io
webapp.py
###########################
#socket io:
###########################
import socketio
import eventlet
import eventlet.wsgi
sio = socketio.Server()

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('chat message', namespace='/chat')
def message(sid, data):
    print("message ", data)
    sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

###########################


if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

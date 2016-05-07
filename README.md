# FileViewer
A image web server

1. Installation Example:
VirtualEnv jingweih
source jingweih/bin/active
pip install django

2. Connect local port to server port
ssh -N -f -L localhost:8000:localhost:8000 jingweih@orionp

3. Start Server
python manage.py runserver

4. View the website with the url:
http://127.0.0.1:8000/files/

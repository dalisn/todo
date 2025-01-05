
install python 
install virtual env : 
pip install virtualenv

locate el folder : cd /folder/projet/todolist

then creation we activation :
python -m venv env
env\Scripts\activate    (if you got an error here, run this command : Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned )

install project dependecies : 
pip install -r requirements.txt

set up mta3 el database : 
python manage.py migrate


run the program : python manage.py runserver
5alli el terminal running , we visit http://127.0.0.1:8000/


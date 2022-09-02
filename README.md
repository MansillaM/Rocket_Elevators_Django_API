# Rocket Elevators Django API

##Dependencies:
-face recognition
-django frameworks
-cmake
-dlib
-gunicorn

##How to use:

  Run locally or go on this website => https://rocket-elevators-django-api-py.herokuapp.com/

  To make a new employee with new facial_keypoints go in Rocket_Elevators_Django_API/quickstart/employee/recognize.py and change the image path for one that you add in   the employee folder. Run the page with 'python Rocket_Elevators_Django_API/quickstart/employee/recognize.py', get the tensor json data, go to 'https://rocket-elevators-django-api-py.herokuapp.com/employees/'   scroll down and there you have a post method so just insert the data you want to create a new employee.

  To GET the employee from facial_keypoints go to postman, type down 'https://rocket-elevators-django-api-py.herokuapp.com/getEmployee/', click on BODY,'form-data' and in KEY type 'file'(near it dropdown menu pick 'file' not 'text') and in value input a picture of employee(Patrick, Eileen or Francis).
  
  If you want to retrieve all the employees go to 'https://rocket-elevators-django-api-py.herokuapp.com/employees/'.
  
   If you have to login the framework use this => Username: 'Mat' and Password: 'Riotgames514'

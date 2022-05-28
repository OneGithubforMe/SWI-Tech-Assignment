# SWI-Tech-Assignment

Steps to run the code - 
1. after install and activating the virtual environment, run `pip install -r requirements.txt` to install all the dependency in the project.
2. run migrations - `python manange.py migrate`
3. upload the csv files data in the database by running - `python manage.py runscript loadcsv`
4. Run the project -  `python manage.py runserver`

a.	**API-1: Retrieve Sales by Drug Classification:**
  1. URL to get the output as html file :  `http://127.0.0.1:8000/pharma/sales?year=<year>&classification=<Drug Classification>`
     eg - http://127.0.0.1:8000/pharma/sales?year=2014&classification=N
  2. URL to get the output as csv file :  `http://127.0.0.1:8000/pharma/sales/csv?year=<year>&classification=<Drug Classification>`
     eg - http://127.0.0.1:8000/pharma/sales/csv?year=2014&classification=N
     
b.	**API-2: Retrieve Drug Reviews for a given Drug:**
  1. URL to get the output as html file :  `http://127.0.0.1:8000/drug/review?year=<year>&drug=<Drug>`
     eg - [http://127.0.0.1:8000/drug/review?year=2015&drug=Erlotinib](http://127.0.0.1:8000/drug/review?year=2015&drug=Erlotinib)
  2. URL to get the output as csv file :  `http://127.0.0.1:8000/drug/review/csv?year=<year>&drug=<Drug>`
     eg - [http://127.0.0.1:8000/drug/review/csv?year=2015&drug=Erlotinib](http://127.0.0.1:8000/drug/review/csv?year=2015&drug=Erlotinib)
     
  

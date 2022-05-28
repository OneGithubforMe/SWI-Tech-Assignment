from pharma.models import PharmaSales
from drug_review.models import DrugReview
import csv

def python_date(date):
    import datetime
    timestamp = datetime.datetime.strptime(date,"%Y-%m-%d")
    return timestamp.date()

# python manage.py runscript loadcsv

def run():
    with open('drug_review/csv/DrugReview.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        DrugReview.objects.all().delete()
        for row in reader:
            DrugReview.objects.create(id =row[0] , condition =row[1] , date = python_date(row[2]) , drug_name = row[3], rating= row[4], review= row[5], unique_id=row[6] , useful_count=row[7])

    with open('pharma/csv/PharmaSales.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        PharmaSales.objects.all().delete()
        for row in reader:
            PharmaSales.objects.create(id=row[0], datum=python_date(row[1]), mo1ab=row[2], mo1ae=row[3], no2ba=row[4], n02be=row[5], n05b =row[6] , n05c=row[7], r03=row[8] , r06=row[9] , year=row[10])



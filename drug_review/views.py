from django.shortcuts import render
from .models import DrugReview

def get_drug_review(request):
	year = request.GET.get('year')
	drug = request.GET.get('drug')
	# drug_types = ['Melatonin', 'Rituximab', 'Disulfiram', 'Erlotinib', 'Pazopanib', 'Eribulin']
	
	drug_details = DrugReview.objects.filter(drug_name = drug, date__year=year).order_by('drug_name', 'condition', 'date')
	context = {
		'drug_details': drug_details,
	}
	return render(request, 'drug_review.html', context) 


import csv
from django.http import HttpResponse
def get_drug_review_as_csv(request):
	# Create the HttpResponse object with the appropriate CSV header.
	response = HttpResponse(
	    content_type='text/csv',
	    headers={'Content-Disposition': 'attachment; filename="drug_review.csv"'},
	)

	year = request.GET.get('year')
	drug = request.GET.get('drug')
	drug_details = DrugReview.objects.filter(drug_name = drug, date__year=year).order_by('drug_name', 'condition', 'date')

	writer = csv.writer(response)
	writer.writerow(['Drug Name', 'Condition', 'Date', 'Review'])
	for detail in drug_details: 
	    writer.writerow([detail.drug_name, detail.condition, detail.date, detail.review])

	return response
from django.shortcuts import render
from .models import PharmaSales
from django.http import JsonResponse


def get_pharma_sales(request):
	year = int(request.GET.get('year'))
	prev_year = year - 1
	drug_class = request.GET.get('drug_classification')
	if drug_class == "M":
		this_year_sales = PharmaSales.objects.filter(year = year)
		sales = {}
		for data in this_year_sales:
			try:
				sales['mo1ab'] += data.mo1ab
			except:
				sales['mo1ab'] = data.mo1ab
			try:
				sales['mo1ae'] += data.mo1ae
			except:
				sales['mo1ae'] = data.mo1ae


		prev_year_sales = PharmaSales.objects.filter(year = prev_year)
		prev_sales = {}
		for data in prev_year_sales:
			try:
				prev_sales['mo1ab'] += data.mo1ab
			except:
				prev_sales['mo1ab'] = data.mo1ab
			try:
				prev_sales['mo1ae'] += data.mo1ae
			except:
				prev_sales['mo1ae'] = data.mo1ae

		if not prev_year_sales:
			prev_sales['mo1ab'] = "NA"
			prev_sales['mo1ae'] = "NA"
		
		output = [
			['Musculo-Skeletal System Drugs', 'Acetic acid derivatives and related substances (M01AB)', sales['mo1ab'], prev_sales['mo1ab']],
			['Musculo-Skeletal System Drugs', 'Propionic acid derivatives, antiinflammatory and antirheumatic products (M01AE)',sales['mo1ae'], prev_sales['mo1ae']]
		]

	elif drug_class == "N":
		this_year_sales = PharmaSales.objects.filter(year = year)
		sales = {}
		for data in this_year_sales:
			try:
				sales['no2ba'] += data.no2ba
			except:
				sales['no2ba'] = data.no2ba
			try:
				sales['n02be'] += data.n02be
			except:
				sales['n02be'] = data.n02be
			try:
				sales['n05b'] += data.n05b
			except:
				sales['n05b'] = data.n05b
			try:
				sales['n05c'] += data.n05c
			except:
				sales['n05c'] = data.n05c


		prev_year_sales = PharmaSales.objects.filter(year = prev_year)
		prev_sales = {}
		for data in prev_year_sales:
			try:
				prev_sales['no2ba'] += data.no2ba
			except:
				prev_sales['no2ba'] = data.no2ba
			try:
				prev_sales['n02be'] += data.n02be
			except:
				prev_sales['n02be'] = data.n02be
			try:
				prev_sales['n05b'] += data.n05b
			except:
				prev_sales['n05b'] = data.n05b
			try:
				prev_sales['n05c'] += data.n05c
			except:
				prev_sales['n05c'] = data.n05c

		if not prev_year_sales:
			prev_sales['no2ba'] = "NA"
			prev_sales['n02be'] = "NA"
			prev_sales['n05b'] = "NA"
			prev_sales['n05c'] = "NA"


		output = [
			['Nervous System Drugs', 'Salicylic acid and derivatives, analgesics and antipyretics (N02BA)', sales['no2ba'], prev_sales['no2ba']],
			['Nervous System Drugs', 'Anilide analgesics and antipyretics (N02BE)',sales['n02be'], prev_sales['n02be']],
			['Nervous System Drugs', 'ANXIOLYTICS (N05B)',sales['n05b'], prev_sales['n05b']],
			['Nervous System Drugs', 'HYPNOTICS AND SEDATIVES (N05C)',sales['n05c'], prev_sales['n05c']],
		]

	else:
		this_year_sales = PharmaSales.objects.filter(year = year)
		sales = {}
		for data in this_year_sales:
			try:
				sales['r03'] += data.r03
			except:
				sales['r03'] = data.r03
			try:
				sales['r06'] += data.r06
			except:
				sales['r06'] = data.r06


		prev_year_sales = PharmaSales.objects.filter(year = prev_year)
		prev_sales = {}
		for data in prev_year_sales:
			try:
				prev_sales['r03'] += data.r03
			except:
				prev_sales['r03'] = data.r03
			try:
				prev_sales['r06'] += data.r06
			except:
				prev_sales['r06'] = data.r06

		if not prev_year_sales:
			prev_sales['r03'] = "NA"
			prev_sales['r06'] = "NA"

		output = [
			['Respiratory System Drugs', 'DRUGS FOR OBSTRUCTIVE AIRWAY DISEASES (R03)', sales['r03'], prev_sales['r03']],
			['Respiratory System Drugs', 'ANTIHISTAMINES FOR SYSTEMIC USE (R06)',sales['r06'], prev_sales['r06']]
		]

	context = {
		'output': output,
		'this_year': year,
		'last_year': prev_year,
	}

	return render(request, 'pharmaSales.html', context)




import csv
from django.http import HttpResponse
def get_pharma_sales_csv(request):
	year = int(request.GET.get('year'))
	prev_year = year - 1
	drug_class = request.GET.get('drug_classification')

	response = HttpResponse(
	    content_type='text/csv',
	    headers={'Content-Disposition': 'attachment; filename="drug_review.csv"'},
	)

	if drug_class == "M":
		this_year_sales = PharmaSales.objects.filter(year = year)
		sales = {}
		for data in this_year_sales:
			try:
				sales['mo1ab'] += data.mo1ab
			except:
				sales['mo1ab'] = data.mo1ab
			try:
				sales['mo1ae'] += data.mo1ae
			except:
				sales['mo1ae'] = data.mo1ae


		prev_year_sales = PharmaSales.objects.filter(year = prev_year)
		prev_sales = {}
		for data in prev_year_sales:
			try:
				prev_sales['mo1ab'] += data.mo1ab
			except:
				prev_sales['mo1ab'] = data.mo1ab
			try:
				prev_sales['mo1ae'] += data.mo1ae
			except:
				prev_sales['mo1ae'] = data.mo1ae

		if not prev_year_sales:
			prev_sales['mo1ab'] = "NA"
			prev_sales['mo1ae'] = "NA"
		
		output = [
			['Musculo-Skeletal System Drugs', 'Acetic acid derivatives and related substances (M01AB)', sales['mo1ab'], prev_sales['mo1ab']],
			['Musculo-Skeletal System Drugs', 'Propionic acid derivatives, antiinflammatory and antirheumatic products (M01AE)',sales['mo1ae'], prev_sales['mo1ae']]
		]

	elif drug_class == "N":
		this_year_sales = PharmaSales.objects.filter(year = year)
		sales = {}
		for data in this_year_sales:
			try:
				sales['no2ba'] += data.no2ba
			except:
				sales['no2ba'] = data.no2ba
			try:
				sales['n02be'] += data.n02be
			except:
				sales['n02be'] = data.n02be
			try:
				sales['n05b'] += data.n05b
			except:
				sales['n05b'] = data.n05b
			try:
				sales['n05c'] += data.n05c
			except:
				sales['n05c'] = data.n05c


		prev_year_sales = PharmaSales.objects.filter(year = prev_year)
		prev_sales = {}
		for data in prev_year_sales:
			try:
				prev_sales['no2ba'] += data.no2ba
			except:
				prev_sales['no2ba'] = data.no2ba
			try:
				prev_sales['n02be'] += data.n02be
			except:
				prev_sales['n02be'] = data.n02be
			try:
				prev_sales['n05b'] += data.n05b
			except:
				prev_sales['n05b'] = data.n05b
			try:
				prev_sales['n05c'] += data.n05c
			except:
				prev_sales['n05c'] = data.n05c

		if not prev_year_sales:
			prev_sales['no2ba'] = "NA"
			prev_sales['n02be'] = "NA"
			prev_sales['n05b'] = "NA"
			prev_sales['n05c'] = "NA"


		output = [
			['Nervous System Drugs', 'Salicylic acid and derivatives, analgesics and antipyretics (N02BA)', sales['no2ba'], prev_sales['no2ba']],
			['Nervous System Drugs', 'Anilide analgesics and antipyretics (N02BE)',sales['n02be'], prev_sales['n02be']],
			['Nervous System Drugs', 'ANXIOLYTICS (N05B)',sales['n05b'], prev_sales['n05b']],
			['Nervous System Drugs', 'HYPNOTICS AND SEDATIVES (N05C)',sales['n05c'], prev_sales['n05c']],
		]

	else:
		this_year_sales = PharmaSales.objects.filter(year = year)
		sales = {}
		for data in this_year_sales:
			try:
				sales['r03'] += data.r03
			except:
				sales['r03'] = data.r03
			try:
				sales['r06'] += data.r06
			except:
				sales['r06'] = data.r06


		prev_year_sales = PharmaSales.objects.filter(year = prev_year)
		prev_sales = {}
		for data in prev_year_sales:
			try:
				prev_sales['r03'] += data.r03
			except:
				prev_sales['r03'] = data.r03
			try:
				prev_sales['r06'] += data.r06
			except:
				prev_sales['r06'] = data.r06

		if not prev_year_sales:
			prev_sales['r03'] = "NA"
			prev_sales['r06'] = "NA"

		output = [
			['Respiratory System Drugs', 'DRUGS FOR OBSTRUCTIVE AIRWAY DISEASES (R03)', sales['r03'], prev_sales['r03']],
			['Respiratory System Drugs', 'ANTIHISTAMINES FOR SYSTEMIC USE (R06)',sales['r06'], prev_sales['r06']]
		]


	writer = csv.writer(response)
	writer.writerow(['Drug Classification', 'ATC Classification', 'Sales - '+str(year), 'Sales - '+str(prev_year)])
	for o in output: 
	    writer.writerow([o[0], o[1], o[2], o[3]])
	
	return response

from django.db import models

class PharmaSales(models.Model):
	id 		= models.PositiveIntegerField(primary_key=True, unique=True)
	datum 	= models.DateField()
	mo1ab 	= models.FloatField() 
	mo1ae 	= models.FloatField() 
	no2ba 	= models.FloatField()
	n02be 	= models.FloatField()
	n05b 	= models.FloatField()
	n05c 	= models.FloatField()
	r03 	= models.FloatField()
	r06 	= models.FloatField()
	year 	= models.PositiveIntegerField()	

	def __str__(self):
		return str(self.id)


	# id=, datum=, mo1ab=, mo1ae=, no2ba=, n02be=, n05b = , n05c=, r03= , r06= , year
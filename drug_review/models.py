from django.db import models

class DrugReview(models.Model):
	id 			= models.PositiveIntegerField(primary_key=True, unique=True)
	condition 	= models.CharField(max_length=200)
	date 		= models.DateField() 
	drug_name 	= models.CharField(max_length=200)
	rating 		= models.PositiveIntegerField() 
	review 		= models.TextField()
	unique_id 	= models.PositiveIntegerField()
	useful_count = models.PositiveIntegerField()

	def __str__(self):
		return str(self.id)


	# id = , condition = , date = , drug_name = , rating= , review= , unique_id= , useful_count=
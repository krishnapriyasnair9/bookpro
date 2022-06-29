from django.db import models

class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    amount=models.PositiveBigIntegerField()
    copies=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    def __str__(self):
        return self.book_name
    @property
    def m_reviews(self):
        return self.products.all()





#ref=modelname(property=value,property=value,property=value)
#ref.save()
#qs=b00ks(book_name="arachar",auther="kr mera",amount=23)
#qs.save()
#fetching all recordss
#select * from Books
#Books.object.all()
#model form



#refname=modelname.objects.all()




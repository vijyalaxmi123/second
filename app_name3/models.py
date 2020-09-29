from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.
class Student_info(models.Model):
    user = models.CharField(max_length=30)
    student_name=models.CharField(max_length=50)
    class_name =models.CharField(max_length=30)
    branch =models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    country =models.CharField(max_length=40)
    book_needed=models.CharField(max_length=40)

    def __str__(self):
        return self.user

#from django.db import models

# Create your models here.
class Book_info(models.Model):
    user = models.CharField(max_length=30)
    book_name =models.CharField(max_length=30)
    author =models.CharField(max_length=30)
    book_copies = models.IntegerField()
    #district = models.CharField(max_length=30)

    def __str__(self):
        return self.user


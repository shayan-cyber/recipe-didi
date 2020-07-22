from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content =  models.TextField()
    author = models.TextField()
    timeStamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to='static/images', default="")
    image1 = models.ImageField(upload_to='static/images', default="")
    image2 = models.ImageField(upload_to='static/images', default="")
    slug = models.CharField(max_length=150)
    def __str__(self):
        return 'Recipe of  ' +self.title
class Contact(models.Model):
    sno1 = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    email = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return 'Message from  ' +self.name


        
   
    
   

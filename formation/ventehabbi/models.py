from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Article(models.Model):
    title= models.CharField(max_length=30)
    desc= models.TextField()
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField()
    user =models.ForeignKey(User ,on_delete=models.CASCADE,null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    class Meta():
        verbose_name= ('Article')
        verbose_name_plural=('Articles')

class comment(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,null=True,blank=True)
    post =models.ForeignKey(Article ,related_name ="comments"  ,on_delete=models.CASCADE,null=True )
    name=models.CharField(max_length=200)
    email =models.EmailField()
    body =models.TextField()
    created_add =models.DateTimeField(auto_now_add=True)

  
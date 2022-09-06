from django.db import models
from froala_editor.fields import FroalaField
from datetime import datetime

class Review(models.Model): 
    name = models.CharField(blank=False, max_length=100)
    
    STARS = [
        ("ONE", '1'),
        ("TWO", '2'),
        ("THREE", '3'),
        ("FOUR", '4'),
        ('FIVE','5'),
    ]

    star = models.CharField(max_length=10 ,choices=STARS)
    text_review = models.CharField(blank=False, max_length=1000)
    issued = models.DateField(default=datetime.now, blank=True)
    user_photo_review = models.ImageField(upload_to='uploads/user_photo')
    favourite_site_review = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Call_back(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(blank=False, max_length=17)
    question = models.CharField(blank=False, max_length=1000)
    
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(blank=False, max_length=200)
    content = FroalaField()
    issued = models.DateField(default=datetime.now, blank=True)
    image_news = models.ImageField(upload_to='uploads/news_photo')
    category = models.ForeignKey('Category_news', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category_news(models.Model):
    category_name = models.CharField(blank=False, max_length=100)
    category_id = models.DecimalField(blank=False, max_digits=3, decimal_places=0, primary_key=True)
    category_name_en = models.CharField(blank=False, max_length=130)

    def __str__(self):
        return self.category_name




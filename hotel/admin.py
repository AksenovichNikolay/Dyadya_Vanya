from django.contrib import admin
from .models import News, Review, Call_back, Category_news

admin.site.register(News)
admin.site.register(Review)
admin.site.register(Call_back)
admin.site.register(Category_news)

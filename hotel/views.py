from django.shortcuts import render
from .models import News, Review, Call_back, Category_news
from .forms import add_model_callback
import telebot
import requests


def send_msg(text):
    token = "5489523883:AAHUCxtzO8fYdLjBszq7FU5iMW3kYgxsMZ0"
    bot = telebot.TeleBot(token)
    chat_id = "147314968"
    bot.send_message(chat_id, text)

def index(request):
    fav_reviews = Review.objects.filter(favourite_site_review=True)
    title = "Главная"
    
    form = add_model_callback()

    if request.method == "POST":
        
        form = add_model_callback(request.POST)
    
        if form.is_valid():
            call_back = form.save()
            send_msg(f"Имя: {call_back.name}\nEmail: {call_back.email}\nНомер телефона: {call_back.phone_number}\nСообщение: {call_back.question}")
            form.clean()
            return render(request, 'index.html', {'fav_reviews':fav_reviews, 'form':form, 'contact':'index_content\contact_great.html', 'title':title})
        else:
            return render(request, 'index.html', {'fav_reviews':fav_reviews, 'form':form, 'contact':'index_content\contact.html', 'title':title})
    return render(request, 'index.html', {'fav_reviews':fav_reviews, 'form':form, 'contact':'index_content\contact.html', 'title':title})


def newss(request):
    newss = News.objects.all()
    category = Category_news.objects.all()
    title = "Новости"
    return render(request, 'newss.html', {'newss':newss, 'title':title, "category":category})

def news(request, news_id):
    news = News.objects.get(id=news_id)
    title = f"{news.title}"
    return render(request, 'news.html', {'news':news, 'title':title})



# def reviews(request):
#     title = "Отзывы"
#     reviews = Review.objects.all().order_by('-issued')
#     if request.method == "POST":
#         form = add_model_reviews(request.POST, request.FILES)
#         if form.is_valid():
#             review = form.save()
#             send_msg(f"На сайте новый отзыв\nИмя: {review.name}\nЗвёзд: {review.star}\nОтзыв: {review.text_review}")
#             form.clean()
#     else:
#         form = add_model_reviews()
#     return render(request, 'reviews.html', {'reviews':reviews, 'form':form, 'title':title})



# def error_404(request, exception):
#     return render(request, '404.html')

# def error_500(request):
#     return render(request, '404.html')

# def error_400(request, exception):
#     return render(request, '404.html')
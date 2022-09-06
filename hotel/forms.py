from cProfile import label
from dataclasses import field
from django import forms
from matplotlib import widgets
from .models import Call_back, Review
import re
    

class add_model_callback(forms.ModelForm):

    class Meta:
        model = Call_back
        fields = ('name', 'email', 'phone_number', 'question')

        widgets = {
            'name':forms.TextInput(attrs={'type':"text", 'name':"name", 'class':"form-control", 'id':"name", 'placeholder':"Ваше имя"}),
            'email':forms.TextInput(attrs={"type":"email", "class":"form-control", "name":"email", "id":"email", "placeholder":"example@uncleVanya.by"}),
            'phone_number':forms.TextInput(attrs={"type":"text", "class":"form-control rfield", "name":"subject", "id":"subject", "placeholder":"+375(__)___-__-__"}),
            'question':forms.Textarea(attrs={"class":"form-control", "name":"message", "rows":"5", "placeholder":"Сообщение"})
        }


# class add_model_reviews(forms.Form):

#     name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type':"text", 'name':"name", 'class':"form-control", 'id':"name", 'placeholder':"Ваше имя"}))
#     star = forms.ChoiceField(choices=Review.STARS, label='Звезды')
#     text_review = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "name":"message", "rows":"5", "placeholder":"Ваш отзыв"}))
#     user_photo_review = forms.ImageField(label='Ваше фото')

# class add_model_reviews(forms.ModelForm):
#     class Meta:
#         model = Review 
#         fields = ('name', 'star', 'text_review', 'user_photo_review')
#         label = ()
#         widgets = {
#             'name':forms.TextInput(attrs={'type':"text", 'name':"name", 'class':"form-control", 'id':"name", 'placeholder':"Ваше имя"}),
#             'text_review':forms.Textarea(attrs={"class":"form-control", "name":"message", "rows":"5", "placeholder":"Ваш отзыв"}),
#         }
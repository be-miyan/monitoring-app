from django.urls import path
from .views import RecordPost, PhotoPost

app_name = 'post'
urlpatterns = [
    path('record/', RecordPost.as_view()),
    path('photo/', PhotoPost.as_view()),
]


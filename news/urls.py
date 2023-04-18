from .views import *
from django.urls import path, include

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create'),
    path('<int:pk>', NewsDetailView.as_view(), name="news-detail"),
    path('<int:pk>/update', NewsUpdateView.as_view(), name="news-update"),
    path("<int:pk>/delete", NewsDeleteView.as_view(), name="news-delete")
]

from django.contrib import admin
from django.urls import path
import appA.allviews.views
# from appA import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appA.allviews.views.index),
    path('excel/', appA.allviews.views.excel),
]

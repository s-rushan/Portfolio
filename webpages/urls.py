from django.contrib import admin
from django.urls import path,include
from . import views
from .views import downloadpdf
urlpatterns = [
    # path('',views.base,name='base'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('mdetail',views.mdetail,name='mdetail'),
    path("portfolio",views.portfolio, name="portfolio"),
    path("contact",views.contact_view, name="contact"),
    path('downloadpdf/<path:file_path>/', downloadpdf.as_view(), name='downloadpdf'),
    path('form',views.form,name='form'),
]
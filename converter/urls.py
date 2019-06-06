from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homepage, name='home'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.details, name='details'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('convert_length/',views.convert_length,name='convert_length')
]
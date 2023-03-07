from django.urls import path
from . import views

urlpatterns = [
    path('polling-unit/<int:polling_unit_id>/',
         views.polling_unit_results, name='polling_unit_results'),
]

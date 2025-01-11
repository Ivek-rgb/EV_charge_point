from django.urls import path
from .views import process_request, process_charger_request_id

urlpatterns = [
    path('<int:charger_id>/', process_charger_request_id),
    path('', process_request)
]

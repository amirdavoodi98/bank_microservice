from django.urls import path, include

from .views import EmployeeViewSet

urlpatterns = [
    path('createEmployee/', EmployeeViewSet.as_view({'post': 'create'})),
]
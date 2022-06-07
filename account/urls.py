from django.urls import path
from .views import CreateAccountViewSet

urlpatterns = [
    path('createAccount/', CreateAccountViewSet.as_view({'post': 'create'}), name='createAccount'),
]
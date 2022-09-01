from django.urls import include, path

urlpatterns = [
    path('', include('yatube_api/urls.py'))
]

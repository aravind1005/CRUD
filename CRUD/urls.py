from django.urls import path 
from .views import Crud

urlpatterns=[
    path("create/", Crud.create, name="create"),
    path("readall/", Crud.readall, name="readall"),
    path("read/<int:id>/", Crud.read, name="read"),
    path("update/<int:id>/", Crud.update, name="update"),
    path("delete/<int:id>/", Crud.delete, name="delete"),
]
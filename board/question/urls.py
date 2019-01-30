from django.urls import path
from .import views

# 밑에꺼 이렇게 쓸 수도 있다.
# from .views import index
# urlpatterns = [
#     path("",index), 
# ]

urlpatterns = [
    path("", views.index),
    path("new/", views.new),
    path("create/", views.create),
    path("<int:id>/",views.read),
    path("<int:id>/comment/create/",views.comment_create)
]
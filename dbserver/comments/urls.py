from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path("postdis/", views.postdis, name='postdis'),
    path("postdis", views.postdis, name='postdis'),

    path("postcomment", views.postcomment, name='postcomment'),
    path("postcomment/", views.postcomment, name='postcomment'),

    path("getDiscuss", views.getDiscuss, name='getDiscuss'),
    path("getDiscuss/", views.getDiscuss, name='getDiscuss'),

    path("addlike", views.addlike, name='addlike'),
    path("addlike/", views.addlike, name='addlike'),

    path("getComment/<int:pk>", views.getComment, name='getComment'),
    path("getComment/<int:pk>/", views.getComment, name='getComment'),

    path("deletedis/<int:pk>", views.deletedis, name='deletedis'),
    path("deletedis/<int:pk>/", views.deletedis, name='deletedis'),
]

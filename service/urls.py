from django.urls import path

from .views import UserComment

urlpatterns = [
    path('user/comment/', UserComment.as_view(), name='user-comment'),
    path('user/comment/<int:id>', UserComment.as_view(), name='user-comments'),
    path('user/<int:pk>comment/', UserComment.as_view(), name='comment-all-users'),
    path('user/<int:pk>comment/<int:id>', UserComment.as_view(), name='all-comments-all-users'),

]

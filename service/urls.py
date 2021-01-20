from django.urls import path

from .views import UserComment, AllCommentsFromAllUsers, AllUserComments, CommentFromAllUsers

urlpatterns = [
    path('user/comment/', UserComment.as_view(), name='user-comment'),
    path('user/comment/<int:id>', AllUserComments.as_view(), name='user-comments'),
    path('user/<int:pk>comment/', CommentFromAllUsers.as_view(), name='comment-all-users'),
    path('user/<int:pk>comment/<int:id>', AllCommentsFromAllUsers.as_view(), name='all-comments-all-users'),

]

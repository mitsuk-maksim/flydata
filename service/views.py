from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

from .models import Comment
from .serializers import UserCommentSerializer


class UserComment(APIView):
    "Комментарии пользователя"

    def get(self, request, pk=0, id=0):
        # comments = Comment.objects.raw('SELECT * FROM service_comments.user_comment_get(%s, %s)', [pk, id])
        with connection.cursor() as cursor:
            # Это если мы не используем модели, но тогда нужен ли serializer? Ведь он использует модели
            cursor.execute("SELECT * FROM service_comments.user_comment_get(%s, %s)", [pk, id])
            comments = cursor.fetchone()

        serializer = UserCommentSerializer(comments, many=True)
        return Response({'comments': serializer.data})

    def post(self, request, pk=0):
        comment = request.data.get('comment')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM service_comments.user_comment_ins(%s, 0, %s)", [pk, comment])
            ins_comment = cursor.fetchone()

        serializer = UserCommentSerializer(data=ins_comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({'success': 'comment: {}, created'.format(comment_saved.comments)})

    def put(self, request, pk=0, id=0):
        data = request.data.get('comment')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM service_comments.user_comment_upd(%s, %s, %s)", [pk, id, data])
            upd_comment = cursor.fetchone()

        serializer = UserCommentSerializer(instance=upd_comment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({'success': 'comment: {}, updated'.format(comment_saved.comments)})

    def delete(self, request, pk=0, id=0):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM service_comments.user_comment_del(%s, %s, %s)", [pk, id])
            upd_comment = cursor.fetchone()

        return Response({
            'message': 'comments with id {} delete'.format(id),
        }, status=204)

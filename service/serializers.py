from rest_framework import serializers

from .models import Comment


class UserCommentSerializer(serializers.Serializer):
    comments = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comments = validated_data.get('comments', instance.comments)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance

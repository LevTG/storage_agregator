from rest_framework import serializers
from .models import StorageFeedback

from comment.models import Comment
from comment.api.serializers import CommentSerializer


class StorageFeedbackRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFeedback
        fields = [
            "text",
            "rating",
            "username",
            'email',
            'phone_number',
            "text",
            'status'
        ]


class StorageFeedbackSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = StorageFeedback
        fields = [
            'id',
            "grade",
            "username",
            'email',
            'phone_number',
            "text",
            "storage",
            'status',
            'created_on',
            'comments'
        ]

    def get_comments(self, obj):
        comments_qs = Comment.objects.filter_parents_by_object(obj)
        return CommentSerializer(comments_qs, many=True).data

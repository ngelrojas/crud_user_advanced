from rest_framework import serializers
from core.models import Comment, SubComment, User


class UserCommentSerializer(serializers.ModelSerializer):
    """serializer comment-user"""
    class Meta:
        model = User
        fields = (
                'name',
                'last_name',
        )
        read_only_fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    """serializer for comments"""
    class Meta:
        model = Comment
        fields = (
                'id',
                'description',
                'created_at',
                'status',
        )
        read_only_fields = ('id',)


class CommentPublicS(serializers.ModelSerializer):
    """serializer public comments"""
    user = UserCommentSerializer()
    class Meta:
        model = Comment
        fields = (
                'id',
                'description',
                'created_at',
                'status',
                'user',
        )
        read_only_fields = ('id',)


class SubCommentSerializer(serializers.ModelSerializer):
    """serializer for subcomments"""
    class Meta:
        model = SubComment
        fields = (
                'id',
                'description',
                'created_at',
                'status',
                'comment',
        )
        read_only_fields = ('id',)


class SubCommentUpS(serializers.ModelSerializer):
    """serializer update subcommnents"""
    class Meta:
        model = SubComment
        fields = (
                'id',
                'description',
                'created_at',
                'status',
        )
        read_only_fields = ('id',)


class SubCommentPublicS(serializers.ModelSerializer):
    """serializer for subcomments"""
    comment = CommentPublicS()

    class Meta:
        model = SubComment
        fields = (
                'id',
                'description',
                'created_at',
                'status',
                'comment',
        )
        read_only_fields = ('id',)

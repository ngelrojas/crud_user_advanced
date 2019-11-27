from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Comment, SubComment
from comment import serializers


class CommentPrivate(viewsets.ModelViewSet):
    """
    list:
        show comments about campaing
    create:
        create a comment
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(
                user=self.request.user
        )
        return queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def update(self, request, pk=None):
        try:
            comments = {
                    'comment': request.data.get('comment'),
                    'status': request.data.get('status')
            }
            current_comment = Comment.objects.get(id=request.data.get('comment'))
            serializer = self.serializer_class(current_comment, data=comments)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': 'comment updated'},
                        status=status.HTTP_200_OK
                )

        except Comment.DoesNotexist as err:
            return Response(
                    {'error': 'data not match.'},
                    status=status.HTTP_404_NOT_FOUND
            )


class SubCommentPrivate(viewsets.ModelViewSet):
    """
    create:
        create subcomment
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SubCommentSerializer
    serialzier_class_u = serializers.SubCommentUpS
    queryset = SubComment.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, pk=None):
        try:
            subcomments = {
                    'status': request.data.get('status')
            }
            current_subc = SubComment.objects.get(id=request.data.get('subcomment'))
            serializer = serializers.SubCommentUpS(current_subc, data=subcomments)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': 'status updated'},
                        status=status.HTTP_200_OK
                )
        except SubComment.DoesNotExist as err:
            return Response(
                    {'error': 'data not match.'},
                    status=status.HTTP_404_NOT_FOUND
            )


class SubCommentPublic(viewsets.ModelViewSet):
    """
    list:
        show all about campaing
    """
    serializer_class = serializers.SubCommentPublicS
    queryset = SubComment.objects.all()

    def retrieve(self, request, pk):
        status_public = 2
        sub_comment = SubComment.objects.filter(
                comment=pk,
                status=status_public
        )
        serializer = self.serializer_class(sub_comment, many=True)
        return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
        )

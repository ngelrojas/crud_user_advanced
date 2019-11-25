from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import News, Campaing
from newscampaing import serializers


class NewsPrivate(viewsets.ModelViewSet):
    """
    list:
        show all news related campaing
    retrieve:
       display all news related campaing
    create:
        create a news related campaing
    update:
        updated a news related campaing
    destroy:
        delete a news
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer

    def list(self, request, pk):
        current_camp = Campaing.objects.get(
                user=request.user,
                id=pk
        )
        current_news = News.objects.filter(campaing=current_camp.id)
        serializer = self.serializer_class(current_news, many=True)
        return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, pk=None):
        try:
            current_news = News.objects.get(id=request.data.get('pk'))
            print(current_news.campaing.id)
            current_camp = Campaing.objects.get(user=request.user, id=current_news.campaing.id)
            serializer = self.serializer_class(
                    current_news,
                    data=request.data
            )

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': 'news updated.'},
                        status=status.HTTP_200_OK
                )
        except News.DoesNotExist as err:
            return Response(
                    {'error': f'{err}'},
                    status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        try:
            if not request.data.get('id'):
                return Response(
                        {'error': 'ID is required.'},
                        status=status.HTTP_400_BAD_REQUEST
                )

            current_news = News.objects.get(id=request.data.get('id'))
            current_news.delete()
            return Response(
                    {'data': 'news deleted.'},
                    status=status.HTTP_200_OK
            )

        except News.DoesNotexist as err:
            return Response(
                    {'error': f'{err}'},
                    status=status.HTTP_404_NOT_FOUND
            )

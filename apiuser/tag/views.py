from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import TagCampaing, Campaing
from tag import serializers
from campaing import serializers as serializers_camp


class TagViewSet(viewsets.ModelViewSet):
    """
    list:
        show all tags
    retrieve:
        show all campaings related tags
    create:
        create a current tag
    delete:
        deleted a current tag
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = TagCampaing.objects.all()
    serializer_class = serializers.TagCampaingSerializer
    serializer_class_camp = serializers_camp.CampaingSerializer

    def get_queryset(self):
        return self.queryset.order_by('-name')

    def retrieve(self, request, pk):
        queryset_c = Campaing.objects.filter(user=request.user, tags=pk)
        serializer = self.serializer_class_camp(queryset_c, many=True)
        return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data': 'tag created successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors})

    def destroy(self, request, *args, **kwargs):
        instance_tag = TagCampaing.objects.get(name=request.data.get('name'))
        instance_tag.delete()
        return Response({'data': True}, status=status.HTTP_200_OK)


class TagPublic(viewsets.ModelViewSet):
    """
    list:
        show all tags
    retrieve:
        display all campaings related tags
    """
    serializer_class = serializers.TagCampaingSerializer
    serializer_class_camp = serializers_camp.CampaingSerializer
    queryset = TagCampaing.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('-name')

    def retrieve(self, request, pk):
        queryset_tp = Campaing.objects.filter(tags=pk)
        serializer = self.serializer_class_camp(queryset_tp, many=True)
        return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
        )

from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import TagCampaing
from tag import serializers


class TagViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.DestroyModelMixin):
    """manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = TagCampaing.objects.all()
    serializer_class = serializers.TagCampaingSerializer

    def get_queryset(self):
        """return objects for the current authenticated user only"""
        return self.queryset.all().order_by('-name')

    def create(self, request, *args, **kwargs):
        """create tag"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance_tag = TagCampaing.objects.get(name=request.data.get('name'))
        instance_tag.delete()
        return Response(status=status.HTTP_200_OK)

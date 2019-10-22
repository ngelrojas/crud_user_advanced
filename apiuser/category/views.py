from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import CategoryCampaing
from category import serializers


class CategoryViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin):
    """manage category in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CategoryCampaing.objects.all()
    serializer_class = serializers.CategoryCampaingSerializer

    def get_queryset(self):
        return self.queryset.all().order_by('-name')

    def create(self, request, *args, **kwargs):
        """create category"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'error': 'somthing error'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance_category = CategoryCampaing.objects.get(name=request.data.get('name'))
        instance_category.delete()
        return Response({'data': True}, status=status.HTTP_200_OK)

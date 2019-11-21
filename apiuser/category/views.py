from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import CategoryCampaing, Campaing
from category import serializers


class CategoryViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin):
    """
    list:
        show all categories
    create:
        create a category
    retrieve:
        show a category
    update:
        update a category
    destroy:
        delete a category
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CategoryCampaing.objects.all()
    serializer_class = serializers.CategoryCampaingSerializer

    def get_queryset(self):
        return self.queryset.all().order_by('-name')

    def retrieve(self, request, pk):
       queryset = CategoryCampaing.objects.all()
       current_category = get_object_or_404(queryset, pk=pk)
       serializer = self.serializer_class(current_category)
       return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'error': 'somthing error'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            current_category = CategoryCampaing.objects.get(id=request.data.get('id'))
            serializer = self.serializer_class(current_category, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': 'category update successfully.'}, status=status.HTTP_200_OK)
        except CategoryCampaing.DoesNotExist as err:
            return Response({'error': 'something wrong.'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance_category = CategoryCampaing.objects.get(id=request.data.get('id'))
        instance_category.delete()
        return Response({'data': True}, status=status.HTTP_200_OK)


class CategoryPublic(viewsets.GenericViewSet,
                    mixins.ListModelMixin):
    """
    list:
        display all categories
    retrieve:
        display detail category
    """
    serializer_class = serializers.CategoryPublicSerializer
    queryset = CategoryCampaing.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('-name')

    def retrieve(self, request, name):
        current_cc = get_object_or_404(self.queryset, name=name)
        serializer = self.serializer_class(current_cc)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

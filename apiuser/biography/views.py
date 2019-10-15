from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, authentication, \
        permissions, status, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import User, Biography
from biography.serializers import BiographySerializer


class BiographyView(viewsets.ViewSet):
    """manage biography in the data base"""
    serializer_class = BiographySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


    def retrieve(self, request, pk=None):
        """retrieve biography to the current user"""
        try:
            current_user = Biography.objects.get(user=request.user)
            return Response(BiographySerializer(current_user).data, status=status.HTTP_200_OK)
        except Biography.DoesNotExist as err:
            return Response({'error': "current user have not biography"},
                            status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """update biography to the current user"""
        try:
            current_user = Biography.objects.get(user=request.user)
            serializer = BiographySerializer(current_user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'data': "biography updated sucessfuly"}, status=status.HTTP_200_OK)
        except Biography.DoesNotExist as err:
            return Response({'error': "something wrong in update biography user"},
                            status=status.HTTP_400_BAD_REQUEST)

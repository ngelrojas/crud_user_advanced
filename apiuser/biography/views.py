from django.shortcuts import render
from rest_framework import generics, authentication, \
        permissions, status, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import User, Biography
from biography.serializers import BiographySerializer


class BiographyViewSet(generics.CreateAPIView):
    """manage biography in the data base"""
    serializer_class = BiographySerializer

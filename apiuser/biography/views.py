from django.shortcuts import render
from rest_framework import generics, authentication, \
        permissions, status, mixins
from core.models import User, Biography
from biography.serializers import BiographySerializer




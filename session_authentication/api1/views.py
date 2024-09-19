from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import (AllowAny, DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly,
                                        IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Student
from .serializers import StudentSerializer

# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

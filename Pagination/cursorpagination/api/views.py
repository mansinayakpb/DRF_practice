from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Student
from .mypaginations import MyCursorPagination
from .serializers import StudentSerializer

# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination

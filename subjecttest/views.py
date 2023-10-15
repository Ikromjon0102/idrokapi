from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Questions,Pupils, Parents,Teachers,Theme
from .serializes import QuestionSerial,PupilSerial,ParentSerial,TeacherSerial,ThemeSerial

from rest_framework import generics

class ThemeListView(generics.ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerial

class PupilsListView(generics.ListAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilSerial

class TeachersListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerial

class ParentsListView(generics.ListAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentSerial

class QuesTestApiView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerial

class QuesTestDetailApiView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerial

class QuesTestUpdateApiView(generics.UpdateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerial

class QuesTestDeleteApiView(generics.DestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerial

class QuesTestCreateApiView(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerial


# @api_view(['GET'])
# def question_list_view(request, *args, **kwargs):
#     questions = Questions.objects.all()
#     serializer = QuestionSerial(questions, many=True)
#
#     return Response(serializer.data)
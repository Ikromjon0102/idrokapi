from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Questions
from .serializes import QuestionSerial

from rest_framework import generics

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
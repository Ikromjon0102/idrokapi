from rest_framework import serializers
from .models import Teachers, Subjects, Questions, Theme,Pupils,Parents,Class,Schools,Rate


class QuestionSerial(serializers.ModelSerializer):
    class Meta():
        model = Questions
        fields = ('id','subject','title','optionA','optionB','optionC','optionD','answeroptions','levels')


class PupilSerial(serializers.ModelSerializer):
    class Meta():
        model = Pupils
        fields = ('first_name','last_name','gender','phone','birthday','school','clas','teacher','parents','subjects')


class ParentSerial(serializers.ModelSerializer):
    class Meta():
        model = Parents
        fields = ('name',)

class TeacherSerial(serializers.ModelSerializer):
    class Meta():
        model = Teachers
        fields = ('fullname','phone','school')


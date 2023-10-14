from rest_framework import serializers
from .models import Teachers, Subjects, Questions


class QuestionSerial(serializers.ModelSerializer):

    class Meta():
        model = Questions
        fields = ('id','subject','title','optionA','optionB','optionC','optionD','answeroptions','levels')

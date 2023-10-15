from django.db import models

# Create your models here.



class Schools(models.Model):
    name = models.CharField(max_length=200, default='maktab 1')

    def __str__(self):
        return self.name

class Teachers(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)


    def __str__(self):
        return self.fullname

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Class(models.Model):
    title = models.CharField(max_length=200)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Parents(models.Model):
    name = models.CharField(verbose_name='Otasi yoki onasi ismi', max_length=200, default="O'quvchining ota-onasi")

    def __str__(self):
        return self.name

class Pupils(models.Model):
    class Gender(models.TextChoices):
        Erkak = 'm', 'Male'
        Ayol = 'f', 'Female'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,
                              choices=Gender.choices)
    birthday = models.DateField()
    phone = models.CharField(verbose_name = 'Telefon raqami',max_length=14, default='999797367')
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, default='5-sinf')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    parents = models.ForeignKey(Parents, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)



class Questions(models.Model):
    class Levels(models.TextChoices):
        Easy = 'easy', 'Easy'
        Middle = 'midl', 'Middle'
        Hard = 'hard', 'Hard'

    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    clas = models.CharField(max_length=200, default='5-sinf')
    theme = models.CharField(max_length=200, default='Qulay va tezkor hisoblash usullari')
    title = models.TextField()
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)
    answeroptions = models.CharField(max_length=200)
    levels = models.CharField(max_length=4,
                              choices=Levels.choices,
                              default=Levels.Easy)

    def __str__(self):
        return self.title


class Rate(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    pupil = models.ForeignKey(Pupils,on_delete=models.CASCADE)
    persentag = models.CharField(max_length=50)

    def __str__(self):
        return self.subject

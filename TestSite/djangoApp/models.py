from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField('Название планеты', max_length= 50)

    def __str__(self):
        return self.name

class Sith(models.Model):
    name = models.CharField('Имя Ситха', max_length= 50)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recruit(models.Model):
    name = models.CharField('Имя рекрута', max_length= 50 )
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.IntegerField('Возраст')
    email = models.CharField('Email', max_length= 50)
    mentor = models.ForeignKey(Sith, null = True, blank = True,on_delete = models.SET_NULL) #, default= None

    def __str__(self):
        return self.name

    def get_answers(self):
        s = ""
        splited = self.answer_set.order_by('question_id').values_list('choice', flat = True)
        for sp in splited:
            s += str(sp) + " "
        return s

class Question(models.Model):
    number = models.IntegerField('Номер вопроса', unique = True)
    text = models.TextField('Вопрос')

    def __str__(self):
        return str(self.number)

class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.BooleanField('Ответ')


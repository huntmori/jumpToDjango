from django.db import models


# Question.objects.all()
# Question.objects.get(id=1)
# Question.objects.filter(id=1)
# Question.objects.filter(subject__contains='장고')
# UPDATE:
#   q = Question.objects.get(id=2)
#   q.subject = 'subject'
#   q.save()
# DELETE:
#   q = Question.objects.get(id=2)
#   q.delete()
# GET_RELATION:
#   q.answer_set.all()
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_datetime = models.DateTimeField()

    def __str__(self):
        return self.subject


from django.utils import timezone;


# CREATE:
#   q = Question.objects.get(id=2)
#   a = Answer(question = q, content='네 자동으로 생성됩니다.', created_datetime=timezone.now())
#   a.save()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    created_datetime = models.DateTimeField()

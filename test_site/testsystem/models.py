from django.db import models
from django.urls import reverse


class Test(models.Model):
    objects = None
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('test', kwargs={'test_id': self.id})

    def get_absolute_url_edit(self):
        return reverse('edit', kwargs={'test_id': self.id})

    def get_absolute_url_deletetest(self):
        return reverse('deletetest', kwargs={'test_id': self.id})


class TestQuestion(models.Model):
    question = models.CharField(max_length=255)
    test = models.ForeignKey('Test', on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('question', kwargs={'question_number': self.id})


class AnswerQuestion(models.Model):
    answer = models.CharField(max_length=255)
    question = models.ForeignKey('TestQuestion', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer




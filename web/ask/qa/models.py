from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                        SELECT *
                        FROM qa_question
                        ORDER BY added_at
                        LIMIT 1""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], question=row[1], poll_date=row[2])
                result_list.append(p)
        return result_list

    def popular(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                        SELECT *
                        FROM qa_question
                        ORDER BY likes
                        LIMIT 1""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], question=row[1], poll_date=row[2])
                result_list.append(p)
        return result_list


class Question(models.Model):
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, default='x', related_name="question_author")
    likes = models.ManyToManyField(User, related_name="question_like")
    objects = QuestionManager()

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return self.text

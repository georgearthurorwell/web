from django.contrib import admin

from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    fields = ['added_at', 'title']

admin.site.register(Question)
admin.site.register(Answer)

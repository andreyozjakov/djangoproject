from django.contrib import admin

from .models import Subject, Question, Choice, Users, Results

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Users)
admin.site.register(Results)

# Register your models here.

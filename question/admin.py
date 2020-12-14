from django.contrib import admin
from .models import Question, Choice, Account, Result
from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline
    ]


class ResultInline(admin.TabularInline):
    model = models.Result


class AccountAdmin(admin.ModelAdmin):
    inlines = [
        ResultInline
    ]


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Account, AccountAdmin)
# admin.site.register(Question)
admin.site.register(Choice)
# admin.site.register(Account)
admin.site.register(Result)

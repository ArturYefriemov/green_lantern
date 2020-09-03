from django.contrib import admin
import nested_admin
from .models import Quiz, Question, QuizTaker, Answer, UsersAnswer


class AnswerInLine(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4


class QuestionInLine(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInLine, ]
    extra = 5


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInLine, ]


class UserAnswerInline(admin.TabularInline):
    model = UsersAnswer


class QuizTakerAdmin(admin.ModelAdmin):
    inlines = [UserAnswerInline, ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, )
admin.site.register(Answer)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(UsersAnswer)

from django.contrib import admin
from .models import Quiz, Question, Option, QuizResult


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "quiz", "order", "question_text")
    list_filter = ("quiz",)
    inlines = [OptionInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    inlines = [QuestionInline]


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "quiz",
        "score",
        "percentage",
        "grade",
        "created_at",
    )
    list_filter = ("quiz", "grade")
    search_fields = ("user__username", "quiz__title")
    readonly_fields = (
        "user", "quiz", "total_questions", "attempted",
        "correct_answers", "wrong_answers", "score",
        "percentage", "grade", "created_at",
    )

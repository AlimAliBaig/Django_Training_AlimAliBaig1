from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignUpForm
from .models import Quiz, QuizResult


def home(request):
    quizzes = Quiz.objects.filter(is_active=True)
    return render(request, "quiz/home.html", {"quizzes": quizzes})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "quiz/signup.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "quiz/login.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass


@login_required
def quiz_page(request, quiz_id):
    quiz = get_object_or_404(
        Quiz.objects.filter(is_active=True),
        id=quiz_id,
    )
    questions = quiz.questions.prefetch_related("options").all()

    return render(
        request,
        "quiz/quiz.html",
        {"quiz": quiz, "questions": questions},
    )


@login_required
def submit_quiz(request, quiz_id):
    if request.method != "POST":
        return redirect("quiz_page", quiz_id=quiz_id)

    quiz = get_object_or_404(
        Quiz.objects.filter(is_active=True),
        id=quiz_id,
    )
    questions = list(quiz.questions.prefetch_related("options").all())

    total_questions = len(questions)
    attempted = 0
    correct_answers = 0
    wrong_answers = 0
    question_results = []

    for question in questions:
        selected_id = request.POST.get(f"question_{question.id}")
        selected_option = None

        if selected_id:
            attempted += 1
            selected_option = question.options.filter(id=selected_id).first()

        correct_option = question.options.filter(is_correct=True).first()
        is_correct = bool(
            selected_option
            and correct_option
            and selected_option.id == correct_option.id
        )

        if selected_option:
            if is_correct:
                correct_answers += 1
            else:
                wrong_answers += 1

        question_results.append(
            {
                "question": question,
                "selected_option": selected_option,
                "correct_option": correct_option,
                "is_correct": is_correct,
            }
        )

    percentage = (
        round((correct_answers / total_questions) * 100, 2)
        if total_questions
        else 0
    )

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    result = QuizResult.objects.create(
        user=request.user,
        quiz=quiz,
        total_questions=total_questions,
        attempted=attempted,
        correct_answers=correct_answers,
        wrong_answers=wrong_answers,
        score=correct_answers,
        percentage=percentage,
        grade=grade,
    )

    return render(
        request,
        "quiz/result.html",
        {
            "quiz": quiz,
            "result": result,
            "question_results": question_results,
        },
    )


@login_required
def dashboard(request):
    results = request.user.quiz_results.select_related("quiz").all()
    return render(request, "quiz/dashboard.html", {"results": results})

import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CppExampleForm
from .models import CppExample, QuizAttempt


def home(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


def add_cpp_example(request):
    if request.method == "POST":
        code = request.POST.get("code")
        status = request.POST.get("status")
        output = request.POST.get("output", "").strip()
        explanation = request.POST.get("explanation")

        # If status requires output, include it in status string
        if status == "the program is guaranteed to output" and output:
            status = f"{status} {output}"

        CppExample.objects.create(code=code, status=status, explanation=explanation)
        return redirect("cpp_explanations")

    return render(request, "add_cpp_example.html")


def cpp_explanations(request):
    examples = CppExample.objects.all()
    return render(request, "cpp_explanations.html", {"examples": examples})


def cpp_quiz(request):
    context = {}
    if request.method == "POST":
        selected_status = request.POST.get("status")
        output_guess = request.POST.get("output_guess", "").strip()
        example_id = request.POST.get("example_id")
        cpp_example = CppExample.objects.get(id=example_id)

        correct_status = cpp_example.status.strip()
        feedback = ""
        explanation = cpp_example.explanation

        user_correct = False
        if selected_status == correct_status:
            if correct_status.startswith("the program is guaranteed to output"):
                # Extract the correct output
                expected_output = (
                    correct_status.replace("the program is guaranteed to output", "")
                    .strip(": ")
                    .strip()
                )
                if output_guess == expected_output:
                    feedback = "Correct! Your output is right."
                    user_correct = True
                else:
                    feedback = f"Partially correct: right status, but the output was expected to be: '{expected_output}'"
            else:
                feedback = "Correct!"
                user_correct = True
        else:
            feedback = f"Incorrect. The correct answer is: '{correct_status}'"
        if request.user.is_authenticated:
            QuizAttempt.objects.create(
                user=request.user,
                cpp_example=cpp_example,
                is_correct=user_correct,
            )

        return render(
            request,
            "cpp_quiz.html",
            {
                "cpp_example": cpp_example,
                "feedback": feedback,
                "explanation": explanation,
            },
        )
    else:
        try:
            cpp_example = random.choice(CppExample.objects.all())
            return render(request, "cpp_quiz.html", {"cpp_example": cpp_example})
        except IndexError:
            return render(request, "cpp_quiz.html", {"cpp_example": {}})


@login_required
def my_score(request):
    attempts = QuizAttempt.objects.filter(user=request.user)
    correct = attempts.filter(is_correct=True).count()
    total = attempts.count()
    return render(request, "my_score.html", {"correct": correct, "total": total})

import random
from django.shortcuts import render, redirect
from .forms import CppExampleForm
from .models import CppExample

def home(request):
    return render(request, 'home.html')

def add_cpp_example(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        status = request.POST.get('status')
        output = request.POST.get('output', '').strip()
        explanation = request.POST.get('explanation')

        # If status requires output, include it in status string
        if status == "the program is guaranteed to output" and output:
            status = f"{status} {output}"

        CppExample.objects.create(
            code=code,
            status=status,
            explanation=explanation
        )
        return redirect('cpp_explanations')

    return render(request, 'add_cpp_example.html')

def cpp_explanations(request):
    examples = CppExample.objects.all()
    return render(request, 'cpp_explanations.html', {'examples': examples})

def cpp_quiz(request):
    context = {}
    if request.method == 'POST':
        selected_status = request.POST.get('status')
        output_guess = request.POST.get('output_guess', '').strip()
        example_id = request.POST.get('example_id')
        cpp_example = CppExample.objects.get(id=example_id)

        correct_status = cpp_example.status.strip()
        feedback = ""
        explanation = cpp_example.explanation

        if selected_status == correct_status:
            if correct_status.startswith("the program is guaranteed to output"):
                # Extract the correct output
                expected_output = correct_status.replace("the program is guaranteed to output", "").strip(': ').strip()
                if output_guess == expected_output:
                    feedback = "Correct! Your output is right."
                else:
                    feedback = f"Partially correct: right status, but the output was expected to be: '{expected_output}'"
            else:
                feedback = "Correct!"
                user_correct = True
        else:
            feedback = f"Incorrect. The correct answer is: '{correct_status}'"

        return render(request, 'cpp_quiz.html', {
            'cpp_example': cpp_example,
            'feedback': feedback,
            'explanation': explanation
        })
    else:
        cpp_example = random.choice(CppExample.objects.all())
        return render(request, 'cpp_quiz.html', {'cpp_example': cpp_example})

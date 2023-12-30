from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.views import View
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "quiz/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        questions = Question.objects.all()
        choices = Choice.objects.all()
        combined_data = []

        for question in questions:
            question_choices = choices.filter(question=question)
            combined_data.append({
                'question': question,
                'choices': question_choices
            })

        return combined_data

class CheckAnswersView(View):
    def post(self, request):
        question_ids = request.POST.getlist('question_id')
        selected_choices = request.POST.getlist('choice')

        score = 0
        for question_id, selected_choice_id in zip(question_ids, selected_choices):
            question = get_object_or_404(Question, pk=question_id)
            selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

            if selected_choice == question.correct_choice:
                score += 1

        context = {
            'score': score,
        }
        return render(request, 'quiz/results.html', context)

    
class DetailView(generic.DetailView):
    model = Question
    template_name = "quiz/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "quiz/results.html"

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("quiz/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "quiz/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "quiz/results.html", {"question": question})

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST["choice"]
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "quiz/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # selected_choice.save()
        return render(request, "quiz/results.html", {"question": question, "selected_choice": selected_choice})


# Create your views here.

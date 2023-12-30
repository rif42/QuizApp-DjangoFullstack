from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "quiz/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
    
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

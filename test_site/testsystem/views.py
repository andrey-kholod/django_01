from django.db.models import Max
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView

from .forms import AddTest, AddQuestion
from .models import Test, TestQuestion, AnswerQuestion

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Результаты", 'url_name': 'result'},
        {'title': "Добавить тест", 'url_name': 'addtest'}]


class TestHome(ListView):
    model = Test
    template_name = 'testsystem/index.html'
    context_object_name = 'tests'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu
    }


def showtest(request, test_id):

    question = TestQuestion.objects.filter(test=test_id)
    question_id = TestQuestion.objects.values_list('id').filter(test=test_id)
    print(test_id)
    print(question_id)
    answer = AnswerQuestion.objects.filter(question__in=question_id)
    print(answer)

    data = {'title': 'Test',
            'menu': menu,
            'question': question,
            'answer': answer
            }

    return render(request, 'testsystem/test.html', data)


def result(request):
    data = {'title': 'Результаты',
            'menu': menu}

    return render(request, 'testsystem/result.html', data)


def addtest(request):
    if request.method == "POST":
        form_test_title = AddTest(request.POST)
        form_question = AddQuestion(request.POST)

        if form_test_title.is_valid:
            form_test_title.save()

            if form_question.is_valid():
                question = form_question.save(commit=False)
                test_id = Test.objects.aggregate(Max('id'))
                question.test_id = str(test_id["id__max"])
                question.save()
    else:
        form_test_title = AddTest
        form_question = AddQuestion

    data = {'title': 'Добавление теста',
            'menu': menu,
            'form_test_title': form_test_title,
            'form_question': form_question
            }

    return render(request, 'testsystem/addtest.html', data)


def update(request, test_id):
    FormQuestionFormSet = modelformset_factory(TestQuestion, fields=('question',))
    test = get_object_or_404(Test, pk=test_id)

    if request.method == "POST":
        form_test_title = AddTest(request.POST, instance=test)

        formset = FormQuestionFormSet(request.POST)

        if form_test_title.is_valid:
            form_test_title.save()

            if formset.is_valid():
                questions = formset.save(commit=False)

                for question in questions:
                    question.test_id = test_id
                    question.save()

    else:
        form_test_title = AddTest(instance=test)
        FormQuestionFormSet = modelformset_factory(TestQuestion, fields=('question',), extra=0)
        formset = FormQuestionFormSet(queryset=TestQuestion.objects.filter(test=test_id))

    data = {'title': 'Добавление теста',
            'menu': menu,
            'form_test_title': form_test_title,
            'formset': formset
            }

    return render(request, 'testsystem/updatetest.html', data)


def deletetest(request, test_id):
    test_delete = Test.objects.filter(id=test_id)
    if test_delete: test_delete.delete()
    return redirect('home')

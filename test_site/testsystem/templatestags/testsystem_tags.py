from django import template
import testsystem.views as views
from testsystem.models import TestsQuestions

register = template.Library()

@register.inclusion_tag('testsystem/test.html')
def show_all_question():

    return {'question': TestsQuestions.object.all()}
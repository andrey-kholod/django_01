from django import forms
from django.forms import inlineformset_factory

from .models import Test, TestQuestion


class AddTest(forms.ModelForm):

    class Meta:
        model = Test
        fields = '__all__'


class AddQuestion(forms.ModelForm):

    class Meta:
        model = TestQuestion
        fields = ('question',)



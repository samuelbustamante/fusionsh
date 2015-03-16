# -*- encoding: utf-8 -*-

from django.forms import ModelForm
from runs.models import Runner


class RunnerForm(ModelForm):
    """
    """
    class Meta:
        model = Runner
        exclude = ('run',)

# -*- encoding: utf-8 -*-

from django.views.generic import ListView, CreateView
from runs.forms import RunnerForm
from runs.models import Run


class RunListView(ListView):
    """
    """
    model = Run


class RunnerCreateView(CreateView):
    """
    """
    form_class = RunnerForm
    template_name = 'runs/runner_form.html'

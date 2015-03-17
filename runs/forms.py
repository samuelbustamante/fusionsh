# -*- encoding: utf-8 -*-

from django import forms
from runs.models import Category, Run, Runner


class RunnerForm(forms.ModelForm):
    """
    """

    def set_categories(self, run_pk):
        run = Run.objects.get(pk=run_pk)
        category_list = [c.pk for c in run.categories.all()]
        queryset = Category.objects.filter(pk__in=category_list)
        self.fields['category'] = forms.ModelChoiceField(queryset=queryset, label='Categoría')

    class Meta:
        model = Runner
        exclude = ('run',)

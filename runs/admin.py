# coding=utf-8

from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from runs.models import Category, Run, Runner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    pass

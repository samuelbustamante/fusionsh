# coding=utf-8

from django.contrib import admin
from runs.models import Category, Run, Runner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    pass


@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    pass

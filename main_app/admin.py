"""File to register models for admin work"""
from django.contrib import admin
from .models import CppExample

admin.site.register(CppExample)
# Register your models here.

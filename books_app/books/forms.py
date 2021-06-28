"""
title – TextInput with class form-control
pages – NumberInput with class form-control
author – TextInput with class form-control
description – Textarea with class form-control
"""
from django import forms

from books_app.books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

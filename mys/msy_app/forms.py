from django import forms

from .models import Ders, Category, Ogrenci


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class DersForm(forms.ModelForm):
    class Meta:
        model = Ders
        fields = [
            'title',
            'hoca',
            'photo_ders',
            'photo_hoca',
            'status',
            'category',
            'date',
            'saat',
            'body',
            'toplam_saat',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'hoca': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_ders': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_hoca': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'saat': forms.TextInput(attrs={'class': 'form-control', 'id': 'mevcutsaati'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'id': 'mevcutbolumler'}),
            'toplam_saat': forms.TextInput(attrs={'class': 'form-control', 'id': 'toplamsaat'}),
        }


class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = ['name', 'number', 'absence_hours', 'dersler', 'date', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'absence_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'dersler': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

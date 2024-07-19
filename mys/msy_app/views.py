from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DersForm, CategoryForm, OgrenciForm
from .models import Category, Ders, Ogrenci


def index(request):
    add_ders = DersForm()
    add_category = CategoryForm()

    if request.method == 'POST':
        if 'add_ders' in request.POST:
            add_ders = DersForm(request.POST, request.FILES)
            if add_ders.is_valid():
                add_ders.save()
                return redirect('index')
        elif 'add_student' in request.POST:
            add_student = OgrenciForm(request.POST, request.FILES)
            if add_student.is_valid():
                add_student.save()
                return redirect('index')
        elif 'add_category' in request.POST:
            add_category = CategoryForm(request.POST)
            if add_category.is_valid():
                add_category.save()
                return redirect('index')

    context = {
        'category': Category.objects.all(),
        'Ders': Ders.objects.all(),
        'form': DersForm(),
        'students': Ogrenci.objects.all(),
        'studentform': OgrenciForm(),
        'formcat': CategoryForm(),
        'allders': Ders.objects.filter(active=True).count(),
        'derstamamlandı': Ders.objects.filter(status='tamamlandı').count(),
        'dersseçildi': Ders.objects.filter(active=True).count(),
        'dersmevcut': Ders.objects.filter(status='mevcut').count(),
    }
    return render(request, 'pages/index.html', context)


def books(request):
    search = Ders.objects.all()
    title = None
    if 'ARA_name' in request.GET:
        title = request.GET['ARA_name']
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'category': Category.objects.all(),
        'Ders': search,
        'formcat': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)


def students(request):
    context = {
        'category': Category.objects.all(),
        'students': Ogrenci.objects.all(),
        'formcat': OgrenciForm(),
    }
    return render(request, 'pages/students.html', context)


def update_book(request, id):
    ders_id = Ders.objects.get(id=id)
    if request.method == 'POST':
        ders_save = DersForm(request.POST, request.FILES, instance=ders_id)
        if ders_save.is_valid():
            ders_save.save()
            return redirect('index')
    else:
        ders_save = DersForm(instance=ders_id)
    context = {
        'form': ders_save,
    }
    return render(request, 'pages/update.html', context)


def delete_book(request, id):
    ders_delete = get_object_or_404(Ders, id=id)
    if request.method == 'POST':
        ders_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')


def update_student(request, id):
    student_id = Ogrenci.objects.get(id=id)
    if request.method == 'POST':
        student_save = OgrenciForm(request.POST, instance=student_id)
        if student_save.is_valid():
            student_save.save()
            return redirect('students')
    else:
        student_save = OgrenciForm(instance=student_id)
    context = {
        'form': student_save,
    }
    return render(request, 'pages/update.html', context)


def delete_student(request, id):
    student_delete = get_object_or_404(Ogrenci, id=id)
    if request.method == 'POST':
        student_delete.delete()
        return redirect('students')
    return render(request, 'pages/delete.html')


def add_category(request):
    if request.method == 'POST' and is_ajax(request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return JsonResponse({'status': 'success', 'category_name': category.name})
        else:
            return JsonResponse({'status': 'fail', 'errors': form.errors})
    return JsonResponse({'status': 'invalid'})


def is_ajax(request):
    return 'HTTP_X_REQUESTED_WITH' in request.META and request.META['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest'


def interface_index(request):
    return render(request, 'interface/index.html')


def dersler_index(request):
    return render(request, 'interface/dersler.html')


def galeri_index(request):
    return render(request, 'interface/galeri.html')


def iletisim_index(request):
    return render(request, 'interface/iletisim.html')


def hocalar_index(request):
    return render(request, 'interface/hocalar.html')


def uyeolmak_index(request):
    return render(request, 'interface/uyeolmak.html')

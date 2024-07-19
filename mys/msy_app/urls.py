from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/update/<int:id>/', views.update_book, name='update_book'),
    path('books/delete/<int:id>/', views.delete_book, name='delete_book'),
    path('students/', views.students, name='students'),

    path('students/update/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    path('add_category/', views.add_category, name='add_category'),  # مسار جديد لإضافة الفئة عبر AJAX
    path('interface/', views.interface_index, name='interface_index'),
    path('dersler/', views.dersler_index, name='dersler_index'),
    path('galeri/', views.galeri_index, name='galeri_index'),  # تحديد مسار لصفحة "galeri"
    path('hocalar/', views.hocalar_index, name='hocalar_index'),
    path('iletisim/', views.iletisim_index, name='letisim_index'),
    path('uyeolmak/', views.uyeolmak_index, name='uyeolmak_index'),
]

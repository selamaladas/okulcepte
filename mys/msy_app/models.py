from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ders(models.Model):
    status_ders = [
        ('mevcut', 'mevcut'),
        ('seçildi', 'seçildi'),
        ('tamamlandı', 'tamamlandı'),
    ]
    title = models.CharField(max_length=250)
    hoca = models.CharField(max_length=250, null=True, blank=True)
    photo_ders = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_hoca = models.ImageField(upload_to='photos', null=True, blank=True)
    body = models.IntegerField(null=True, blank=True)
    saat = models.IntegerField(null=True, blank=True)
    toplam_saat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_ders, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Ogrenci(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    absence_hours = models.IntegerField()
    dersler = models.ManyToManyField(Ders)
    date = models.DateTimeField()
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.name

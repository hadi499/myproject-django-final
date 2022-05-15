from calendar import SATURDAY
from django.db import models
from . utils import create_new_ref_number
from django.utils import timezone
import time


class TarifPerKilo(models.Model):
    harga = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Tarif per Kilo'

    def __str__(self):
        return self.harga


class Shipping(models.Model):
    resi = models.CharField(
        max_length=10,
        editable=False,
        unique=True,
        default=create_new_ref_number
    )
    nama_barang = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    nama_pengirim = models.CharField(max_length=255)
    alamat_pengirim = models.TextField()
    nama_tujuan = models.CharField(max_length=255)
    alamat_tujuan = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True)
    berat = models.IntegerField()
    tarif_per_kilo = models.IntegerField()
    date = models.DateField(auto_now=True)

    def tarif(self):
        return self.berat * self.tarif_per_kilo

    class Meta:
        verbose_name_plural = 'Shipping'


class Category(models.Model):
    nama = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.nama

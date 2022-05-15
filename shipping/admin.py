from django.contrib import admin
from .models import Category, Shipping, TarifPerKilo


admin.site.register(Category)


@admin.register(TarifPerKilo)
class TarifAdmin(admin.ModelAdmin):
    list_display = ['id', 'harga', 'created_at', 'updated']


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['resi', 'nama_barang', 'kategori', 'nama_pengirim',
                    'alamat_pengirim', 'nama_tujuan', 'alamat_tujuan', 'created_at', 'berat', 'tarif_per_kilo']

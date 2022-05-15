from django import forms

from .models import Category, Shipping, TarifPerKilo


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['nama_barang', 'kategori', 'nama_pengirim',
                  'alamat_pengirim', 'nama_tujuan', 'alamat_tujuan', 'berat', 'tarif_per_kilo']


class GantiTarifForm(forms.ModelForm):
    class Meta:
        model = TarifPerKilo
        fields = [
            'harga',
        ]


class TambahCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'nama',
        ]

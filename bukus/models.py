from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    judul = models.CharField(max_length=30)
    jumlah_halaman = models.IntegerField(max_length=8)
    penerbit = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='bukus', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='bukus', on_delete=models.CASCADE)

class Peminjaman(models.Model):
    tanggal = models.DateTimeField()
    jumlah_hari = models.IntegerField(max_length=3)
    buku_id = models.ForeignKey(related_name='peminjamans')
    user_id = models.ForeignKey(related_name='peminjamans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='peminjaman', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='peminjaman', on_delete=models.CASCADE)

class Pengembalian(models.Model):
    tanggal = models.DateTimeField()
    peminjaman_id = models.ForeignKey(related_name='pengembalian')
    denda = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='pengembalian', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='pengembalian', on_delete=models.CASCADE)
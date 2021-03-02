from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    id = models.AutoField(primary_key=True,)
    judul = models.CharField('Judul', max_length=30)
    jumlah_halaman = models.IntegerField('Jumlah Halaman')
    penerbit = models.CharField('Penerbit', max_length=30)

    def __str__(self):
        return self.judul

class Peminjaman(models.Model):
    tanggal = models.DateTimeField()
    jumlah_hari = models.IntegerField()
    buku_id = models.ForeignKey('Buku', related_name='peminjamans', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='peminjamans', on_delete=models.CASCADE)

class Pengembalian(models.Model):
    tanggal = models.DateTimeField()
    peminjaman_id = models.ForeignKey(Peminjaman, related_name='pengembalian', on_delete=models.CASCADE)
    denda = models.BigIntegerField(null=True)
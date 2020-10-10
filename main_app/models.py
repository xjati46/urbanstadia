from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):

    # CHOICES
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',
    )
    PILIHAN_JENIS_ID = models.TextChoices(
        'Jenis ID',
        'KTP KIA SIM Paspor',
    )

    # BASE IDENTITY
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    nama_panggilan = models.CharField(max_length=20)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,
    )

    # ADMINISTRATIVE IDENTITY
    jenis_id = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_ID.choices,
        blank=True,
        null=True
    )
    nomor_id = models.CharField(max_length=50, blank=True, null=True)
    tempat_lahir = models.CharField(max_length=50, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    alamat_id = models.CharField('Alamat ID', max_length=200, blank=True, null=True)
    kota_kabupaten_id = models.CharField('Kota/ Kab.', max_length=50, blank=True, null=True)
    provinsi_id = models.CharField('Provinsi', max_length=50, blank=True, null=True)

    # ACTUAL LOCATION
    alamat_tinggal = models.CharField('Alamat Tinggal', max_length=200, blank=True, null=True)
    kota_kabupaten_tinggal = models.CharField('Kota/ Kab.', max_length=50, blank=True, null=True)
    provinsi_tinggal = models.CharField('Provinsi', max_length=50, blank=True, null=True)

    # COMMUNICATION
    nomor_ponsel = models.CharField(max_length=20, blank=True, null=True)
    akun_fb = models.CharField(max_length=100, blank=True, null=True)
    akun_twitter = models.CharField(max_length=100, blank=True, null=True)
    akun_ig = models.CharField(max_length=100, blank=True, null=True)
    akun_youtube = models.CharField(max_length=100, blank=True, null=True)

    # CABOR FAVORIT
    cabor_favorit = models.ManyToManyField('CabangOlahraga')

    class Meta:
        ordering = ['nama_lengkap']

    def __str__(self):
        return self.nama_lengkap

    def usia(self):
        return int((timezone.now().date() - self.tanggal_lahir).days / 365.25)


class CabangOlahraga(models.Model):
    nama_olahraga = models.CharField(max_length=100)

    class Meta:
        ordering = ['nama_olahraga']
        verbose_name_plural = 'Cabang Olahraga'

    def __str__(self):
        return self.nama_olahraga


class KelasPertandingan(models.Model):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',
    )

    cabor = models.ForeignKey(CabangOlahraga, on_delete=models.CASCADE)
    nama_kelas = models.CharField(max_length=200)

    batasan_jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,
        blank=True,
        null=True
    )
    batasan_usia_minimal = models.IntegerField(blank=True, null=True)
    batasan_usia_maksimal = models.IntegerField(blank=True, null=True)
    batasan_berat_minimal = models.IntegerField(blank=True, null=True)
    batasan_berat_maksimal = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['nama_kelas']
        verbose_name_plural = 'Kelas Pertandingan'

    def __str__(self):
        return self.nama_kelas


class Pertandingan(models.Model):
    nama_pertandingan = models.CharField(max_length=200)
    cabor = models.ManyToManyField(CabangOlahraga)
    kelas = models.ManyToManyField(KelasPertandingan)

    class Meta:
        ordering = ['nama_pertandingan']
        verbose_name_plural = 'Pertandingan'

    def __str__(self):
        return self.nama_pertandingan


# LINK MODEL
class PesertaPertandingan(models.Model):
    peserta = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pertandingan = models.ForeignKey(Pertandingan, on_delete=models.CASCADE)
    kelas = models.ForeignKey(KelasPertandingan, on_delete=models.CASCADE)

    class Meta:
        ordering = ['peserta']
        verbose_name_plural = 'Peserta'

    def __str__(self):
        return self.peserta.nama_lengkap

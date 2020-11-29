from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name='Xizmat nomi')
    icon = models.CharField(max_length=150, verbose_name='Ikonkasi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Xizmat'
        verbose_name_plural='Xizmatlar'
        ordering =('title',)


class Yangiliklar(models.Model):
    title = models.CharField(max_length=150, verbose_name='Yangiliklar')
    rasm = models.ImageField(upload_to='Yangiliklar', blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Yangilik'
        verbose_name_plural='Yangiliklar'
        ordering =('title',)

class Galereya(models.Model):
    rasm = models.ImageField(upload_to='Galereya', blank=True)

    class Meta:
        verbose_name='Galereya'
        verbose_name_plural='Galereyalar'
        ordering =('rasm',)
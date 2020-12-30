from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    name = models.CharField(max_length=80, verbose_name='ФИО')
    qualification = models.CharField(max_length=80, null=True, verbose_name='Квалификация')
    organization = models.CharField(max_length=100, verbose_name='Организация')
    photo = models.ImageField(upload_to='images/projects', null=True, blank=True, verbose_name='Фото')
    body = models.TextField(verbose_name='Отзыв')
    active = models.BooleanField(default=False, verbose_name='Активный')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Отзыв'
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return f'Отзыв {self.name} от {self.organization}'

from django.db import models
from django.utils.translation import gettext as _


class Employee(models.Model):
    user_name = models.CharField(_('Имя'), max_length=255)
    mobile = models.CharField(
        _('Номер телефона'),
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = _('Работник')
        verbose_name_plural = _('Работники')

    def __str__(self):
        return self.user_name


class Store(models.Model):
    name = models.CharField(_('Название'), max_length=255)
    user = models.ForeignKey(
        Employee,
        verbose_name='Работник',
        on_delete=models.SET_NULL,
        null=True,
        related_name='stores'
    )

    class Meta:
        verbose_name = _('Торговая точка')
        verbose_name_plural = _('Торговые точки')

    def __str__(self):
        return self.name


class Visit(models.Model):
    store = models.ForeignKey(
        Store,
        verbose_name=_('Торговая точка'),
        related_name='visits',
        on_delete=models.CASCADE
    )
    datetime_visited = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(_('Ширина'))
    longitude = models.FloatField(_('Долгота'))

    class Meta:
        verbose_name = _('Посещение')
        verbose_name_plural = _('Посещения')

    def __str__(self):
        return self.store

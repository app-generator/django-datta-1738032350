# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    sector = models.CharField(max_length=255, null=True, blank=True)
    nroempleado = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Instalaciones(models.Model):

    #__Instalaciones_FIELDS__
    inst_id = models.IntegerField(null=True, blank=True)
    inst_name = models.CharField(max_length=255, null=True, blank=True)
    inst_tipo = models.CharField(max_length=255, null=True, blank=True)

    #__Instalaciones_FIELDS__END

    class Meta:
        verbose_name        = _("Instalaciones")
        verbose_name_plural = _("Instalaciones")


class Empresa(models.Model):

    #__Empresa_FIELDS__
    idempresa = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Empresa_FIELDS__END

    class Meta:
        verbose_name        = _("Empresa")
        verbose_name_plural = _("Empresa")


class Area(models.Model):

    #__Area_FIELDS__
    id_area = models.IntegerField(null=True, blank=True)
    name_area = models.CharField(max_length=255, null=True, blank=True)
    fk_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    #__Area_FIELDS__END

    class Meta:
        verbose_name        = _("Area")
        verbose_name_plural = _("Area")



#__MODELS__END

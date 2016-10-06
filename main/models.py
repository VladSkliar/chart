# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Title',
                             unique=True)
    parameters = models.ManyToManyField('Parameter', related_name='group',
                                        blank=True)

    def __unicode__(self):
        return self.title

    @property
    def parameters_values(self):
        parameters = self.parameters.all().order_by('-value')
        parameters_list = list()
        for parameter in parameters:
            param_dict = dict()
            param_dict['value'] = parameter.value
            param_dict['parameters'] = parameter.title
            parameters_list.append(param_dict)
        return parameters_list


class Parameter(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Title')
    value = models.SmallIntegerField()
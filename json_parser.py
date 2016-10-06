# -*- coding: utf-8 -*-
import json
from main.models import Group, Parameter
Group.objects.all().delete()
Parameter.objects.all().delete()
with open('base.json') as json_file:
    objects = json.load(json_file)
    for obj in objects['data']:
        print obj[u'Область'], obj[u'Город'], obj[u'Значение']
        group = obj[u'Область']
        title, value = obj[u'Город'], obj[u'Значение']
        p = Parameter.objects.create(title=title, value=int(float(value)))
        g = Group.objects.filter(title=group).first()
        if g is None:
            g = Group.objects.create(title=group)
            g.parameters.add(p)
        else:
            g.parameters.add(p)
        g.save()

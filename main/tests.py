from django.test import TestCase
from models import Group, Parameter


class GroupModelTest(TestCase):
    def setUp(self):
        param1 = Parameter.objects.create(title='TEST-1',
                                          value=15)
        param2 = Parameter.objects.create(title='TEST-2',
                                          value=18)
        group = Group.objects.create(title='TEST')
        group.parameters.add(param1)
        group.parameters.add(param2)
        group.save()

    def test_correct_create_group(self):
        """test for object creation"""
        group = Group.objects.last()
        self.assertEqual(unicode(group.title), u'TEST')

    def test_correct_create_parameters(self):
        parameter = Parameter.objects.order_by("title").last()
        self.assertEqual(unicode(parameter.title), u'TEST-2')
        self.assertEqual(parameter.value, 18)

    def test_correct_create_group_foreign_key(self):
        parameter = Parameter.objects.last()
        group = Group.objects.last()
        self.assertEqual(group.parameters_values,
                         [{"parameters": "TEST-1", "value": 15},
                          {"parameters": "TEST-2", "value": 18}])

from django.shortcuts import render
from models import Group
from serializers import GroupSerializer, GroupSimpleSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class GroupViewSet(viewsets.ModelViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSimpleSerializer

    def retrieve(self, request, pk=None):
        queryset = Group.objects.all()
        group = get_object_or_404(queryset, pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)


def index(request):
    return render(request, 'index.html')

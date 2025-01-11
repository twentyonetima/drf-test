from rest_framework.generics import ListCreateAPIView
from .models import Tasks
from .serializers import TasksSerializer


class TasksListCreateView(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from base.models import ToDo


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/todos/',
        'Detail': '/todos/<int:pk>/',
        'Create': 'todos/add/',
        'Update': 'todos/update/<int:pk>/',
        'Delete': 'todos/delete/<int:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def getData(request):
    todos = ToDo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def todoView(request, pk):
    todo = ToDo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateData(request, pk):
    todo = ToDo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request, pk):
    todo = ToDo.objects.get(id=pk)
    todo.delete()

    return Response('Succesfully deleted!')

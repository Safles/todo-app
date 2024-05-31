from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import todoLIST
from todo.serializers import todoListSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def todo(request):
    if request.method == 'GET':
        objs=todoLIST.objects.all()
        serializer=todoListSerializer(objs, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer=todoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Data Added Successfully!'})
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer=todoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = todoLIST.objects.get(id=data['id'])
        serializer=todoListSerializer(obj ,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = todoLIST.objects.get(id=data['id'])
        obj.delete()
        return Response({'message' : 'To Do Deleted'})

@api_view(['GET'])    
def getTodoByID(request, id):
    obj = todoLIST.objects.get(id=id)
    serializer = todoListSerializer(obj)
    return Response(serializer.data)

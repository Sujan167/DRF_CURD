from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class StudentView(APIView):

    def get(self, request):
        std_obj = Student.objects.all()
        serializer = StudentSerializer(std_obj, many=True)
        return Response({'status': True, 'data': serializer.data, 'message': "success"})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'post successful'})
        return Response({'status': False, 'message': 'Serializer data not valid'})

    def patch(self, request, pk, format=None):
        obj = Student.objects.get(pk=pk)
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'update successful'})
        return Response({'status': False, 'message': 'Serializer data not valid'})

    def delete(self, request, pk, format=None):
        try:
            obj = Student.objects.get(id=pk)
            obj.delete()
            return Response({'status': True, 'message': 'Delete successful'})
        except:
            return Response({'status': False, 'message': 'Delete Not successful'})

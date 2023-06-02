from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from .models import Students
from .serializers import StudentSerializer
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics


# Function Based API_view ...........................................................................

@api_view(['GET'])
def home(request):
    student_obj=Students.objects.all()
    serializer=StudentSerializer(student_obj, many=True)
    return Response({
        'status':200,
        'payloads':serializer.data
    })

@api_view(['POST'])
def post_data(request):
    data=request.data
    serializer=StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({
            'status':403,
            'message':'Something went Wrong'
        })
    serializer.save()
    return Response({
        'status':200,
        'payload':serializer.data,
        'message':'You sent the data'
    })

@api_view(['PATCH'])
def update_data(request,id):
    student_obj=Students.objects.get(id=id)
    try:
        serializer=StudentSerializer(student_obj,data=request.data,partial=True)
        if not serializer.is_valid():
            return Response({
                'status':403,
                'message':'Something went Wrong'
            })
        serializer.save()
        return Response({
            'status':200,
            'payload':serializer.data,
            'message':'You sent the data'
        })
    except Exception as e:
        return Response({'status':403,'message':"Invalid id"})

@api_view(['DELETE'])
def delete_data(request,id):
    try:
       student_obj=Students.objects.get(id=id)
       student_obj.delete()
       return Response({'status':200,'message':'Object Delete'})
    except Exception as e:
        print(e)
        return Response({'status':400,'messsage':'Invalid id'}) 


@api_view(['GET','POST'])
def student_data(request,id=None):
    if request.method == 'GET':
        student_obj=Students.objects.all()
        serializer=StudentSerializer(student_obj, many=True)
        return Response({
            'status':200,
            'payloads':serializer.data
        })
    elif request.method == 'POST':
        data=request.data
        serializer=StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status':403,
                'message':'Something went Wrong'
            })
        serializer.save()
        return Response({
            'status':200,
            'payload':serializer.data,
            'message':'You sent the data'
        })
    
        
    
        
@api_view(['PATCH','DELETE'])
def student_detailview(request,id):
    if request.method == 'PATCH':
        student_obj=Students.objects.get(id=id)
        try:
            serializer=StudentSerializer(student_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({
                    'status':403,
                    'message':'Something went Wrong'
                })
            serializer.save()
            return Response({
                'status':200,
                'payload':serializer.data,
                'message':'You sent the data'
            })
        except Exception as e:
            return Response({'status':403,'message':"Invalid id"})
        
    elif request.method == 'DELETE':
        try:
            student_obj=Students.objects.get(id=id)
            student_obj.delete()
            return Response({'status':200,'message':'Object Delete'})
        except Exception as e:
            print(e)
            return Response({'status':400,'messsage':'Invalid id'})
        
# Class Based APIView...........................................................................

class StudentDataView(APIView):
    def get(self, request):
        student_obj = Students.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({
            'status': status.HTTP_200_OK,
            'payloads': serializer.data
        })

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'payload': serializer.data,
                'message': 'You sent the data'
            })
        return Response({
            'status': status.HTTP_403_FORBIDDEN,
            'message': 'Something went wrong'
        })

    def patch(self, request, id):
        try:
            student_obj = Students.objects.get(id=id)
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': status.HTTP_200_OK,
                    'payload': serializer.data,
                    'message': 'You sent the data'
                })
            return Response({
                'status': status.HTTP_403_FORBIDDEN,
                'message': 'Something went wrong'
            })
        except Students.DoesNotExist:
            return Response({
                'status': status.HTTP_403_FORBIDDEN,
                'message': 'Invalid id'
            })

    def delete(self, request, id):
        try:
            student_obj = Students.objects.get(id=id)
            student_obj.delete()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Object deleted'
            })
        except Students.DoesNotExist:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Invalid id'
            })
 
 # Generic Class View...........................................................................
 
class StudentDataView(generics.ListCreateAPIView):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer

class StudentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer
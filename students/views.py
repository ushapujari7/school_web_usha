from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

# ✅ GET all students & POST a new student
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':  # GET all students
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Create a new student
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ GET, PUT, DELETE a specific student
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Get details of a student
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':  # Update a student
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  # Delete a student
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

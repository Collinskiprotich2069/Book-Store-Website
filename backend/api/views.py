from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    
    permission_class = [AllowAny]
    def get(self, request):
        model = Book.objects.all()
        serializer = BookSerializer(model, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer,status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        





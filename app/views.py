from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.



class LogoutView(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                "message": "logout successfully"
            }, status=status.HTTP_205_RESET_CONTENT)
        
        
        except Exception as e:
            return Response({
                "error": "Invalid token"
            }, status=status.HTTP_401_UNAUTHORIZED)


class UserList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(request):
        user = CustomUser.objects.all()
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)


class RegisterView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RegisterSerializers(data = request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User is created"
                    

                }, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class NotesListView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        note = Notes.objects.filter(user = request.user)
        serializer = NotesSerializer(note, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NotesSerializer(request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Notes.objects.get(pk=pk, user=user)
        except Notes.DoesNotExist:
            return None
        
    
    def get(self, pk, request):
        note = self.get_object(pk, request.user)
        if not note:
            return Response({
                "error": "NOtes does not found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = NotesSerializer(note)
        return Response(serializer.data)
    

    def put(self, pk, request):
        note = self.get_object(pk, request.user)
        if not note:
            return Response({
                "error": "Notes does not foudn"
            }, status= status.HTTP_404_NOT_FOUND)
        serializer = NotesSerializer(note, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, pk, request):
        note  = self.get_object(pk, request.user)
        if not note:
            return Response({
                "error": "Notes does not found"
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = NotesSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,pk,request):
        note = self.get_object(pk, request.user)
        if not note:
            return Response({
                "error": "Noes does not found"
            }, status=status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response({
            "status": "success"
        }, status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework import decorators,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serilazers import *

@api_view(['POST'])
def post_user_details(request):
      if (request.method =='POST'):
            serilazer = UserDetailsSerilazer(data=request.data)
            if serilazer.is_valid():
                  serilazer.save()
                  return Response({'data':serilazer.data,},status=status.HTTP_201_CREATED)
            return Response({'error':serilazer.errors},status=status.HTTP_400_BAB_REQUEST)
@api_view(['GET'])
def get_user_details(request):
      if (request.method =='GET'):
             user = UserDetails.objects.all()
             serializer = UserDetailsSerilazer(user,many=True) 
            #  if serializer.is_valid():
             return Response({'data':serializer.data,},status=status.HTTP_200_OK)
            #  else:
            #     return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['DELETE'])
def delete_user_details(request,id):
     if (request.method =="DELETE"):
          user = UserDetails.objects.get(id=id)
          user.delete()
          return Response({'message':'user deleted successfully'},status=status.HTTP_204_NO_CONTENT)
     
@api_view(['PUT'])
def update_user_details(request,id):
      if (request.method =='PUT'):
            user = UserDetails.objects.get(id=id)
            seralizer = UserDetailsSerilazer(user,request.data)
            if seralizer.is_valid():
                  seralizer.save()
                  return Response({'data':seralizer.data},status=status.HTTP_200_OK)

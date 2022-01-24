import email
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vax.app.models import Users
from vax.app.serializers import UserSerializer
import logging

@api_view(['GET'])
def get_user_byEmail(request):
    
    userEmail = request.query_params.get('email')
    logging.debug("Received get byEmail request. Email: {}", userEmail)

    try:
        user = Users.objects.get(email=userEmail)
    except Users.DoesNotExist:
        logging.debug("Failed to find user with email: {}", userEmail)
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)

    return Response(serializer.data)

    
@api_view(['GET'])
def get_user_byCardNum(request):
    cardNum = request.query_params.get('cardNum')
    logging.debug("Received get byCardNum request. cardNum: {}", cardNum)

    try:
        user = Users.objects.get(healthCardNum=cardNum)
    except Users.DoesNotExist:
        logging.debug("Failed to find user with health card num: {}", cardNum)
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)

    return Response(serializer.data)    

@api_view(['POST'])
def put_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        logging.debug("Creating new user: {}", serializer.data)
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

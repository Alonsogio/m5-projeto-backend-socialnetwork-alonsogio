from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_room(request):
    # Code to create a new chat room
    return Response({'room_name': 'my_room'})

@api_view(['POST'])
def join_room(request):
    # Code to join an existing chat room
    return Response({'room_name': 'my_room'})

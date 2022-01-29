from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRouts(request):
    routs=[
    'GET /api',
    'GET /api/rooms',
    'GET /api/rooms/:id',
    ]
    return Response(routs)

@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    serialied = RoomSerializer(rooms, many=True)
    return Response(serialied.data)


@api_view(['GET'])
def getRoom(request, pk):
    room=Room.objects.get(id=pk)
    serialied = RoomSerializer(room, many=False)
    return Response(serialied.data)
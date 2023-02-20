from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from jwt_app.serializers import RegisterSerializer, UserSerializer


# Create your views here.

@api_view(['POST'])
def sign_up(request):
    serializer = RegisterSerializer(data=request.data, many=False)
    if serializer.is_valid(raise_exception=True):
        new_user = serializer.create(serializer.validated_data)
        return Response(data=UserSerializer(instance=new_user, many=False).data)


@api_view(['GET'])
def get_version(request):
    return Response(data={'version': 1.0})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_logged_in_user_data(request):
    if request.user.is_authenticated:
        serializer = UserSerializer(instance=request.user, many=False)
        return Response(serializer.data)
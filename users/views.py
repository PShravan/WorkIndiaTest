from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import status

from django.contrib.auth.backends import ModelBackend
from rest_framework.decorators import api_view, permission_classes

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": "account created"}, status=status.HTTP_201_CREATED, headers=headers)

# class LoginUser(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny, )

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = ModelBackend.authenticate(username=username, password=password)
#         if user:
#             return Response({"status": "success", "userId"=}, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST',])
@permission_classes((AllowAny,))
def login(request):
    data = {}
    user = ModelBackend.authenticate(request, username=request.data["username"], password=request.data["password"])
    if user:
        data['status'] = 'success'
        data[ 'userId']=user.id
    else:
        data['status'] = 'failed'
    return Response(data)
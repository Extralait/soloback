from urllib.request import Request

from django.shortcuts import render
import requests
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, \
    DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .permisions import IsOwnerOrAdmin, IsAdminOrLeader
from .serializers import *
from .models import *

from S import settings

# Create your views here.
class UserActivationView(APIView):
    """
    Представление активации профиля
    """
    permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        """
        Активация профиля и перенаправление на вход в профиль
        """
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/SOLO/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        requests.post(post_url, data=post_data)
        return redirect('http://' + settings.FRONT_HOST)


class PasswordResetConfirmView(APIView):
    """
    Представление смены пароля
    """
    permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        """
        Получение токена и UID и перенаправление на смену пароля
        """
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/SOLO/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        return redirect('http://' + settings.FRONT_HOST + '?uid=' + uid + 'token=' + token)

class LeaderCheck(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        print(self.request.user.position)

        if self.request.user.is_leader:
            return Response(True)
        else:
            return Response(False)

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class PositionsViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class VocationViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Vocation.objects.all()

    def filter_queryset(self, queryset):
        user=self.request.user
        if user.is_staff:
            queryset=queryset
        elif str(user) == 'AnonymousUser':
            return queryset.filter(code=-1)
        elif str(user.position) == "Руководитель офиса":
            return queryset
        else:
            if str(user.position) in ["Старший менеджер по обслуживанию",
                                 "Ведущий менеджер по обслуживанию",
                                 "Менеджер по обслуживанию"]:
                positions = ["Старший менеджер по обслуживанию",
                                 "Ведущий менеджер по обслуживанию",
                                 "Менеджер по обслуживанию"]
                queryset1 = queryset.filter(code=user.code,position=positions[0])
                queryset2 = queryset.filter(code=user.code,position=positions[1])
                queryset3 = queryset.filter(code=user.code,position=positions[2])
                queryset = queryset1 | queryset2 | queryset3
            elif user.position in ["Старший клиентский менеджер", "Клиентский менеджер"]:
                positions = ["Старший клиентский менеджер", "Клиентский менеджер"]
                queryset1 = queryset.filter(code=user.code,position=positions[0])
                queryset2 = queryset.filter(code=user.code,position=positions[1])
                queryset = queryset1 | queryset2
            else:
                positions = "Консультант"
                queryset = queryset.filter(code=user.code).filter(position=positions)
        return queryset

    def get_permissions(self):
        """
        Права доступа
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        elif self.action in ['update', 'partial_update', 'destroy', 'create']:
            permission_classes = (IsOwnerOrAdmin,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        Класс сериализатора
        """
        if self.request.user.is_staff:
            serializer_class = VocationAdminSerializer
        elif self.action in ['list', 'retrieve', 'create']:
            serializer_class = VocationCreateSerializer
        else:
            serializer_class = VocationAdminSerializer

        return serializer_class

class InterestCreateViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()

    def filter_queryset(self, queryset):
        user=self.request.user
        if user.is_staff:
            return queryset
        elif str(user) == 'AnonymousUser':
            return queryset.filter(code=-1)
        elif str(user.position) == "Руководитель офиса":
            return queryset
        else:
            if str(user.position) in ["Старший менеджер по обслуживанию",
                                 "Ведущий менеджер по обслуживанию",
                                 "Менеджер по обслуживанию"]:
                positions = ["Старший менеджер по обслуживанию",
                                 "Ведущий менеджер по обслуживанию",
                                 "Менеджер по обслуживанию"]
                queryset1 = queryset.filter(code=user.code,position=positions[0])
                queryset2 = queryset.filter(code=user.code,position=positions[1])
                queryset3 = queryset.filter(code=user.code,position=positions[2])
                queryset = queryset1 | queryset2 | queryset3
            elif user.position in ["Старший клиентский менеджер", "Клиентский менеджер"]:
                positions = ["Старший клиентский менеджер", "Клиентский менеджер"]
                queryset1 = queryset.filter(code=user.code,position=positions[0])
                queryset2 = queryset.filter(code=user.code,position=positions[1])
                queryset = queryset1 | queryset2
            else:
                positions = "Консультант"
                queryset = queryset.filter(code=user.code).filter(position=positions)
            return queryset

    def get_permissions(self):
        """
        Права доступа
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        elif self.action in [ 'create',]:
            permission_classes = (IsAuthenticated,)
        elif self.action in [ 'destroy',]:
            permission_classes = (IsOwnerOrAdmin,)
        elif self.action in  ['update', 'partial_update']:
            permission_classes = (IsAdminOrLeader,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        Класс сериализатора
        """
        if self.request.user.is_staff:
            serializer_class = InterestAdminSerializer
        elif self.action in ['create']:
            serializer_class =InterestCreateSerializer
        elif self.action in ['update', 'partial_update']:
            serializer_class = InterestUpdateSerializer
        else:
            serializer_class = InterestAdminSerializer

        return serializer_class

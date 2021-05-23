from rest_framework import serializers

from SOLO.models import *

from django.db import models


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ('email','name','surname','code','sub_code','position')

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'

class VocationAdminSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Vocation
        fields = '__all__'


class VocationCreateSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    code = serializers.CharField(read_only=True)
    position = serializers.CharField(read_only=False)
    def _user(self):
            """
            Лидер мероприятия
            """
            user = self.context['request'].user
            return user

    def create(self, validated_data):
        """
        Добавление организатора мероприятия
        """
        user = self._user()
        vocation = (Vocation.objects.create(
            owner = user,
            code = user.code,
            **validated_data
        ))
        return vocation

    class Meta:
        model = Vocation
        fields = '__all__'


class InterestCreateSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    status = serializers.CharField(read_only=True)
    code = VocationCreateSerializer(read_only=True)
    position = serializers.CharField(read_only=True)


    def _user(self):
            """
            Лидер мероприятия
            """
            user = self.context['request'].user
            return user

    def create(self, validated_data):
        """
        Добавление организатора мероприятия
        """
        user = self._user()
        interest = (Interest.objects.create(
            owner = user,
            status = 'wait_confirm',
            **validated_data
        ))
        return interest


    class Meta:
            model = Interest
            fields = '__all__'


class InterestUpdateSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)
    vocation = VocationCreateSerializer(required=True)
    status = serializers.CharField(read_only=False)
    code = VocationCreateSerializer(read_only=True)
    position = serializers.CharField(read_only=False)

    def create(self, validated_data):
        """
        Добавление организатора мероприятия
        """
        interest = (Interest.objects.create(
            code=self.vocation.code,
            position=self.vocation.position,
            **validated_data
        ))
        return interest

    class Meta:
        model = Interest
        fields = '__all__'

class InterestAdminSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Interest
        fields = '__all__'

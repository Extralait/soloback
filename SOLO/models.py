import random
import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMessage
from django.db import models
# Create your models here.

class Division(models.Model):
    code=models.CharField('Код подразделения', max_length=60)
    region=models.CharField('Регион', max_length=100,blank=True, null=True)

    class Meta:
        verbose_name = 'Код подразделения'
        verbose_name_plural = 'Код подразделений'

    def __str__(self):
        return self.region

class Positions(models.Model):
    long_name=models.CharField('Должность', max_length=60)
    name=models.CharField('Краткая должность', max_length=60, default='',blank=True,null=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должностьи'

    def __str__(self):
        return self.long_name

class UserManager(BaseUserManager):
    """
    Модель менеджера пользователя
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Конструктор пользователя
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        password =uuid.uuid4().hex[:6].upper()
        user.set_password(password)
        user.save(using=self._db)
        email = EmailMessage(
            'Вы успешно зарегистрировались!',
            f'Этот код - пароль от вашей учетной записи\n\n{password}',
            'tehnolog1999@gmail.com',to=[email]
        )
        email.send(fail_silently=False)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Создание пользователя
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Создание суперпользователя
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None
    email = models.EmailField('Email', unique=True)
    is_leader = models.BooleanField('Лидер', default=False)
    name = models.CharField('Имя', max_length=256, default='', blank=True,null=True)
    surname = models.CharField('Фамилия', max_length=256, default='', blank=True,null=True)
    fathers_name = models.CharField('Отчество', max_length=256, default='', blank=True,null=True)
    code = models.ForeignKey(Division,on_delete=models.CASCADE, blank=True,null=True)
    sub_code = models.CharField('Доп код', max_length=256, default='', blank=True,null=True)
    position = models.ForeignKey(Positions,verbose_name='Должность', on_delete=models.CASCADE, blank=True,null=True)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name', 'surname', 'code','sub_code','position']
    REQUIRED_FIELDS=[]
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

class Vocation(models.Model):
    owner = models.ForeignKey(User,verbose_name='Пользователь',related_name='owner', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,verbose_name='Дата отправки')
    status = models.BooleanField('Статус', max_length=10, default=False)
    code = models.CharField('Код подразделения', blank=True,null=True, max_length=100)
    position = models.CharField('Должность',blank=True,null=True,max_length=100)

    class Meta:
        verbose_name = 'Вокансия'
        verbose_name_plural = 'Вокансии'

    def __str__(self):
        return self.owner.email

class Interest(models.Model):
    class StatusChoices(models.TextChoices):
        """
        Роль в организации
        """
        wait_confirm = 'wait_confirm', 'Ожидание'
        confirm = 'confirm', 'Подтверждено'
        miss = 'miss', 'Отклонено'


    owner = models.ForeignKey(User,verbose_name='Работник',related_name='worker', on_delete=models.CASCADE)
    vocation = models.ForeignKey(Vocation,verbose_name='Вокансия',on_delete=models.CASCADE)
    status = models.CharField('Статус', max_length=100, choices=StatusChoices.choices,
                            default=StatusChoices.wait_confirm)
    code = models.CharField('Код подразделения', blank=True,null=True, max_length=100)
    position = models.CharField('Должность',blank=True,null=True,max_length=100)

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        constraints = [
            models.UniqueConstraint(fields=['owner', 'vocation'], name='unique_member_in_organization')
        ]
    def __str__(self):
        return self.owner.email

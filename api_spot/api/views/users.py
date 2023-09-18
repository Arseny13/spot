from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from ..serializers.users import (ChangePasswordSerializer,
                                 ConfirmationCodeSerializer,
                                 ResetPasswordSerializer, SendCodeSerializer,
                                 UserMeSerializer, UserSerializer)
from ..services.users import (cache_and_send_confirmation_code,
                              finish_activation_email,
                              get_user_with_email_or_bad_request,
                              registration_email, reset_password_email)

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_permissions(self):
        if self.action == 'create':
            return (AllowAny(),)
        return super().get_permissions()

    def perform_create(self, serializer, *args, **kwargs):
        user = serializer.save(*args, **kwargs)
        cache_and_send_confirmation_code(user, registration_email)

    @action(
        detail=False,
        methods=['post'],
        permission_classes=(AllowAny,),
        serializer_class=ConfirmationCodeSerializer
    )
    def activation(self, request, *args, **kwargs):
        """
        Активация юзера через код подтверждения
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        user = get_user_with_email_or_bad_request(email)
        if confirmation_code == cache.get(user.id):
            user.is_active = True
            user.save()
            finish_activation_email(user.email)
            return Response(
                {'message': 'Электронная почта верифицирована'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'error': 'Не действительный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=False,
        methods=['post'],
        permission_classes=(IsAuthenticated,),
        serializer_class=ChangePasswordSerializer
    )
    def change_password(self, request, *args, **kwargs):
        """
        Cмена пароля.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get('password')
        user = serializer.validated_data.get('user')
        user.set_password(password)
        user.save(update_fields=['password'])
        # надо ли разлогинить пользователя после смены пароля?
        # надо ли отправить письмо на почту?
        return Response(
            {'message': 'Пароль изменен'}, status=status.HTTP_200_OK
        )

    @action(
        detail=False,
        methods=['post'],
        permission_classes=(AllowAny,),
        serializer_class=ResetPasswordSerializer
    )
    def reset_password(self, request, *args, **kwargs):
        """
        Сброс пароля.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        password = serializer.validated_data.get('password')
        user = user = get_user_with_email_or_bad_request(email)
        if confirmation_code == cache.get(user.id):
            user.set_password(password)
            user.save(update_fields=['password'])
            finish_activation_email(user.email)
            return Response(
                {'message': 'Пароль изменен'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'error': 'Не действительный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=False,
        permission_classes=(IsAuthenticated,),
        serializer_class=UserMeSerializer
    )
    def me(self, request, *args, **kwargs):
        """
        Любой пользователь может получить информацию о себе.
        """
        email = request.user.email
        user = User.objects.get(email=email)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @me.mapping.patch
    def patch_me(self, request, *args, **kwargs):
        """
        Любой пользователь может изменить информацию о себе.
        """
        serializer = self.get_serializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['post'],
        permission_classes=(AllowAny,),
        serializer_class=SendCodeSerializer
    )
    def reset_password_confirmation_code(self, request, *args, **kwargs):
        """
        Отправка кода подтверждения для сброса пароля.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user = user = get_user_with_email_or_bad_request(email)
        cache_and_send_confirmation_code(user, reset_password_email)
        return Response(
            {'message': 'Код подтверждения отправлен на почту'},
            status=status.HTTP_200_OK
        )

    @action(
        detail=False,
        methods=['post'],
        permission_classes=(AllowAny,),
        serializer_class=SendCodeSerializer
    )
    def resend_confirmation_code(self, request, *args, **kwargs):
        """
        Повторная отправка кода подтверждения.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user = get_user_with_email_or_bad_request(email)
        if user.is_active:
            return Response(
                {'error': 'Вы уже подтвердили эл. почту'}
            )
        cache_and_send_confirmation_code(user, registration_email)
        return Response(
            {'message': 'Код активации отправлен на почту'},
            status=status.HTTP_200_OK
        )

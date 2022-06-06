from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail
# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    phone_reggex = RegexValidator(
        regex=r'^\??\d{9,10}$', message='Please Enter the number in 9999999999 format.')
    phone = models.CharField(max_length=10, blank=True,
                             validators=[phone_reggex])
    full_name = models.CharField(max_length=100, blank=True)
    is_premium_user = models.BooleanField(default=False)

    def __srt__(self):
        return f"User {self.username}"


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    try:
        email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

        send_mail(
            # title:
            "Password Reset for {title}".format(title="Hamro Cinema"),
            # message:
            email_plaintext_message,
            # from:
            "yogeshlim2001@gmail.com",
            # to:
            [reset_password_token.user.email],
            fail_silently=False
        )
    except Exception as ex:
        print('Something Went Wrong')
    

import firebase_admin
from firebase_admin import credentials
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice
from . import settings

cred = credentials.Certificate(settings.cred)
firebase_admin.initialize_app(cred)

def send_notification(user_id, title, message, data):
    try:
        device = FCMDevice.objects.filter(user=user_id).first()
        response = device.send_message(
            title=title,
            body=message,
            data=data,
            sound=True
        )
        return response
        print("Message sent successfully:", response)
    except:
        pass

def normal_notification(title, message, data):
    try:
        response = device.send_message(
            title=title,
            body=message,
            data=data,
            sound=True
        )
        return response
        print("Message sent successfully:", response)
    except:
        pass
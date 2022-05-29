import firebase_admin
from firebase_admin import credentials, messaging
from fcm_django.models import FCMDevice
from . import settings




def send_booked_notification(topic, title, body):
    device = FCMDevice.objects.all()
    message = messaging.Message(
        data={
            'title': title,
            'body': body
        },
        condition=condition
    )
    response = device.send_message(message, condition=condition)
    print('Sucessfully sent the info:', response)




topic = 'reminder-info'
def send_reminder(topic, title, body):
    device = FCMDevice.objects.all()
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        android=messaging.AndroidConfig(
            priority='normal',
            notification=messaging.AndroidNotification(
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
        topic=topic
    )
    response = device.send_message(message, topic=topic)
    print('Successfully sent the notification:', response)

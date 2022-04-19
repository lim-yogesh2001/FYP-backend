import firebase_admin
from firebase_admin import credentials, messaging
from fcm_django.models import FCMDevice
from . import settings

cred = credentials.Certificate(settings.cred)
firebase_admin.initialize_app(cred)

topics = [
    'booked-info',
    'seat-reserved'
]

condition = "'booked-info' in topics || 'seat-reserved' in topics"


def send_booked_notification(condition, title, body):
    message = messaging.Message(
        data={
            'title': title,
            'body': body
        },
        condition=condition
    )
    response = messaging.send_message(message)
    print('Sucessfully sent the info:', response)


topic = 'reminder-info'


def send_reminder(topic, title, body):
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
    response = messanging.send_message(message)
    print('Successfully sent the notification:', response)

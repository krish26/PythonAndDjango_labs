class Email:
    def send(self):
        return "Sending email"

class SMS:
    def send(self):
        return "Sending SMS"
    
def notify(notification):
    if isinstance(notification, Email):
        print("EMAIL:", notification.send())

    elif isinstance(notification, SMS):
        print("SMS:", notification.send())
    else:
        raise TypeError("Unsupported notification type")
    
email = Email()
sms = SMS()

notify(email)
notify(sms)
    
class PushNotification:
    def send(self):
        return "Sending push notification"
    
def notify(notification):
    if isinstance(notification, Email):
        print("EMAIL:", notification.send())
    elif isinstance(notification, SMS):
        print("SMS:", notification.send())
    elif isinstance(notification, PushNotification):   # new change
        print("PUSH:", notification.send())
    else:
        raise TypeError("Unsupported notification type")


push = PushNotification()
notify(push)


#usig polymorphism


class Notification:
    def send(self):
        raise NotImplementedError("Subclasses must implement send()")


class Email(Notification):
    def send(self):
        return "EMAIL: Sending Email"

class SMS(Notification):
    def send(self):
        return "SMS: Sending SMS"

class PushNotification(Notification):
    def send(self):
        return "PUSH: Sending Push Notification"


def notify(notification):
    print(notification.send())


email = Email()
sms = SMS()
push = PushNotification()

notify(email)
notify(sms)
notify(push)


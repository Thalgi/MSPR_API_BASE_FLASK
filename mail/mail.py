import qrcode
from io import BytesIO
from flask_mail import Message, Mail

global mail


def get_mail(app):
    mail = None
    if mail is not None:
        return mail
    else:
        mail = init_mail(app)
        return mail


def init_mail(app):
    mail = Mail(app)
    return mail


def send_email_with_qr_code(user_email, qr_data):
    img = qrcode.make(qr_data)
    img_buffer = BytesIO()
    img.save(img_buffer, 'PNG')
    img_buffer.seek(0)

    msg = Message(subject="Your QR Code",
                  sender="natsu.974.tm@example.com",
                  recipients=[user_email],
                  body="Please find the QR code attached.")

    msg.attach(filename="qr_code.png", content_type="image/png", data=img_buffer.getvalue())

    mail.send(msg)

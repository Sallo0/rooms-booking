import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.config import settings
from app.tasks.celery_app import celery
from app.tasks.email_templates import create_booking_confirmation_template


@celery.task(name='tasks.resize_image')
def resize_image(image_path: str, size: tuple[int, int]):
    im_path = Path(image_path)
    im = Image.open(im_path)
    im_resized = im.resize(size)
    im_resized.save(f"{im_path.parent / im_path.stem}_resized_{size[0]}x{size[1]}{im_path.suffix}")


# TODO: try to send on real email
@celery.task(name='tasks.send_email')
def send_booking_confirmation_email(
        booking: dict,
        email_to: EmailStr
):
    email_to_mock = settings.SMTP_USER
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.send_message(msg_content)

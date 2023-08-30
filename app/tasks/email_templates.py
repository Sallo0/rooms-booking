from email.message import EmailMessage

from pydantic import EmailStr


def create_booking_confirmation_template(
        booking: dict,
        email_to: EmailStr,
):
    email_message = EmailMessage()
    email_message["Subject"] = "Booking confirmation"
    email_message["From"] = "Hotel Booking Service"
    email_message["To"] = email_to

    email_message.set_content(
        f"""
        <h1>Booking confirmation</h1>
        <p>Dear user!</p>
        <p>You have successfully booked a room in our hotel 
        from  {booking["date_from"]} to {booking["date_to"]}.</p>
        """,
        subtype="html"
    )

    return email_message

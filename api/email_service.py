from django.core.mail import send_mail

def send_email_notification(to_email, evaluation_id):
    """Send an email notification when evaluation is completed."""
    subject = "Evaluation Completed"
    message = f"Your evaluation request (ID: {evaluation_id}) has been completed."
    from_email = "your-email@gmail.com"  # Same as EMAIL_HOST_USER
    recipient_list = [to_email]

    send_mail(subject, message, from_email, recipient_list)

    print(f"Email sent to {to_email}")

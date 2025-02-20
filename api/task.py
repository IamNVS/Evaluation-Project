import time
import random
from celery import shared_task
from .email_service import send_email_notification


@shared_task
@shared_task
def process_evaluation(evaluation_id):
    from .models import EvaluationRequest
    """Simulates an evaluation process and sends an email notification using SMTP."""
    time.sleep(5)  # Simulate processing delay

    # Fetch the evaluation request from the database
    evaluation = EvaluationRequest.objects.get(id_er=evaluation_id)

    # Generate a random evaluation result
    evaluation.result = f"Simulated evaluation result: {random.randint(1, 100)}"
    evaluation.status = "completed"
    evaluation.save()

    # Send email notification using Django's built-in SMTP email
    send_email_notification(evaluation.email, evaluation.id)

    return f"Evaluation {evaluation_id} processed successfully."

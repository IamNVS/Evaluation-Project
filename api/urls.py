from .views import RetrieveEvaluationRequest, SubmitEvaluationRequest
from django.urls import path

# Creating the endpoints
urlpatterns = [
    path("evaluate/", SubmitEvaluationRequest.as_view(), name="submit-evaluation"),  # POST request, where submits an evaluation request and starts an asynchronous Celery task return the evaluation request ID
    path("evaluate/<int:id>/", RetrieveEvaluationRequest.as_view(), name="retrieve-evaluation"),  # GET request ,<id> where you should add real ID to fetches the status and result of the evaluation
]

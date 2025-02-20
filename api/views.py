from django.shortcuts import render
from .models import EvaluationRequest
from .serializers import EvaluationRequestSerializers, EvaluationSubmitSerializers
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .task import process_evaluation


# Create your views here.

# This is Handles retrieval of evaluation request status and result
class RetrieveEvaluationRequest(generics.RetrieveAPIView):
    queryset = EvaluationRequest.objects.all() # For https request all methods 
    serializer_class = EvaluationRequestSerializers

# This is for handles submission of evaluation requests
class SubmitEvaluationRequest(APIView):
    def post(self, request):
        serializer = EvaluationSubmitSerializers(data=request.data)
        if serializer.is_valid():
            evaluation = serializer.save(status="pending")  # Default is "pending"
            process_evaluation.delay(evaluation.id_er)  # Call Celery task asynchronously
            return Response({"id": evaluation.id_er, "message": "Evaluation request submitted."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

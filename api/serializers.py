from .models import EvaluationRequest
from rest_framework import serializers

class EvaluationRequestSerializers(serializers.ModelSerializer):
    evaluationRequest = serializers.ReadOnlyField()
    class Meta:
        model=EvaluationRequest
        fields ="__all__" # All fields from models(Entity)


class EvaluationSubmitSerializers(serializers.ModelSerializer):
    class Meta:
        model=EvaluationRequest
        fields = ['input_prompt', 'email'] # Only expose input_prompt and email fields
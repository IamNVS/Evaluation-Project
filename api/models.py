from django.db import models

# Create your models here.

class EvaluationRequest(models.Model):
    id_er = models.AutoField(primary_key=True)  # Unique ID for each evaluation request
    input_prompt = models.TextField(blank=True, null=True)  
    status = models.CharField( max_length=100, choices=
                              (("completed","completed"),
                                ("pending", "pending")), default="pending") # Giving status and status of the evaluation (default is 'pending')
    result = models.TextField(default="pending") # Stores the evaluation result
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the evaluation request was created (set automatically)
    updated_at = models.DateTimeField(auto_now=True) # Timestamp when the evaluation request was last updated (updated automatically)
    email = models.EmailField() # User's email to send notifications once evaluation is completed

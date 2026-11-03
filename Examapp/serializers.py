
from rest_framework import serializers
from Examapp.models import Question


class QuestionSerializer(serializers.Serializer):

    Question = serializers.CharField(max_length=200)
    option_a = serializers.CharField(max_length=100)
    option_b = serializers.CharField(max_length=100)
    option_c = serializers.CharField(max_length=100)
    option_d = serializers.CharField(max_length=100)
    correct_answer = serializers.CharField(max_length=100)



class SubmissionSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=100)
    question_id = serializers.IntegerField()
    selected_answer = serializers.CharField(max_length=100)
    submitted_at = serializers.DateTimeField(read_only=True)

    def validate(self, validated_data):
        question_id = validated_data.get("question_id")

        if not Question.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exist.")

        return validated_data
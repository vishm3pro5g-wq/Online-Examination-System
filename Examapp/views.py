from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Examapp.models import Question,Submission
from Examapp.serializers import QuestionSerializer,SubmissionSerializer


class QuestionListCreateView(APIView):

    def get(self, request):
        qs = Question.objects.all()
        serializer_instance = QuestionSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Question.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        #qs = Question.objects.get(id=pk)
        qs = get_object_or_404(Question, id=pk)
        serializer_instance = QuestionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Question.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        Question.objects.filter(id=pk).delete()
        return Response(data={"message": "Question deleted successfully...!"})



class AnswerSubmissionListCreateView(APIView):
    def get(self,request):
        qs = Submission.objects.all()
        serializer_instance = SubmissionSerializer(qs, many=True)
        return Response(data=serializer_instance.data)  


    def post(self,request):
        form_data=request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Submission.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)




class SubmissionRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(Submission, id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        qs = get_object_or_404(Submission, id=pk)
        serializer_instance = SubmissionSerializer(qs, data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors, status=400)

    def delete(self, request, pk):
        qs = get_object_or_404(Submission, id=pk)
        qs.delete()
        return Response(data={"message": "Submission deleted successfully!"})



class EvaluateSubmissionView(APIView):
    def put(self, request, pk):
        form_data = request.data

        Submission.objects.filter(id=pk).update(**form_data)

        return Response(data={
            "message": "updated.."
        })

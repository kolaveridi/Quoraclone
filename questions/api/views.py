from rest_framework import viewsets
from questions.api.serializers import QuestionSerializer
from questions.models import Question
from questions.api.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
class QuestionViewSet(viewsets.ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        # log the request here
        print("request",request)
        return super().dispatch(request, *args, **kwargs)
    queryset=Question.objects.all()
    lookup_field="slug"
    serializer_class=QuestionSerializer
    permission_classes=[IsAuthorOrReadOnly,IsAuthenticated]
    def perform_create(self, serializer):
        print("user is", self.request.user)
        serializer.save(author=self.request.user)
    
    
    
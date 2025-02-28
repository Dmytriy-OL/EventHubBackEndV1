from rest_framework import  generics

from user.api.serializers import AutorSerializer
from user.models import Author


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AutorSerializer

class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AutorSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from rest_framework.views import APIView

from event.models import Event, Category
from event.api.serializers import EventSerializer, CategorySerializer


class EventListAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response({"events": serializer.data})


class EventDetailAPIView(APIView):

    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response({"event": serializer.data})


class EventCreateAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        request_body=EventSerializer,
        manual_parameters=[
            openapi.Parameter(
                name="image",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description="Файл-зображення події",
                required=True,
            )
        ]
    )
    def post(self, request):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            event = serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response({"category": serializer.data})


class CategoryCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=CategorySerializer,
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

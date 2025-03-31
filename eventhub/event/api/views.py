from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from rest_framework.views import APIView

from event.models import Event, Category
from event.api.serializers import EventSerializer, CategorySerializer


class EventListAPIView(APIView):
    """
       Handles GET requests to retrieve a list of all events.

       This class provides an API to fetch all events in the system.
       It returns a list of events in JSON format.

       Methods:
           GET: Returns a list of all events.
       """

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response({"events": serializer.data})


class EventDetailAPIView(APIView):
    """
        Handles GET requests to retrieve detailed information about a specific event.

        This class provides an API to fetch details of a specific event by its primary key (id).

        Methods:
            GET: Returns the details of an event with the specified id.
        """

    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response({"event": serializer.data})


class EventCreateAPIView(APIView):
    """
        Handles POST requests to create a new event.

        This class provides an API to create a new event with data sent in the request.
        Supports file uploads (e.g., event images).

        Methods:
            POST: Creates a new event, accepting event data and an image file via a form.
        """
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
    """
        Handles GET requests to retrieve a list of all categories.

        This class provides an API to fetch all categories in the system.

        Attributes:
            queryset: Contains all categories.
            serializer_class: Used for serializing category data.
        """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(APIView):
    """
        Handles GET requests to retrieve detailed information about a category.

        This class provides an API to fetch details of a specific category by its primary key (id).

        Methods:
            GET: Returns the details of a category with the specified id.
        """

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response({"category": serializer.data})


class CategoryCreateAPIView(APIView):
    """
       Handles POST requests to create a new category.

       This class provides an API to create a new category in the system.

       Methods:
           POST: Creates a new category, accepting category data.
       """
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        request_body=CategorySerializer,
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

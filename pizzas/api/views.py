from .serializers import SizeSerializer, ToppingSerializer, PizzaSerializer, PizzaReadSerializer
from pizzas.models import Pizza, Size, Topping
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

# Api to get list of pizzas and create a new pizza
class PizzaList(APIView):

    serializer_class = PizzaSerializer

    def get(self, request,format=None):
        try:
            pizza = Pizza.objects.all()
            serializer=PizzaReadSerializer(pizza,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise Http404

    def post(self, request, format=None):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Api to get,update and delete a particular pizza .
class PizzaDetail(APIView):

    def get_object(self, pk):
        try:
            return Pizza.objects.get(pk=pk)
        except Pizza.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pizza = self.get_object(pk)
        serializer = PizzaReadSerializer(pizza)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pizza = self.get_object(pk)
        serializer = PizzaSerializer(
            pizza, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pizza = self.get_object(pk)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Api to get list of pizza sizes and add a new size
class SizeList(APIView):

    serializer_class = SizeSerializer

    def get(self, request,format=None):
        try:
            size = Size.objects.all()
            serializer=SizeSerializer(size,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise Http404

    def post(self, request, format=None):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Api to get list of pizza topping and add a new topping
class ToppingList(APIView):

    serializer_class = ToppingSerializer

    def get(self, request,format=None):
        try:
            topping = Topping.objects.all()
            serializer=SizeSerializer(topping,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            raise Http404

    def post(self, request, format=None):
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


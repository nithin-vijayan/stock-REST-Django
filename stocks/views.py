from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from models import Stock
from serializers import StockSerializer

class StockListCreate(CreateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

class StockList(ListAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

class StockRetrieve(RetrieveAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

class StockRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

class StockRetrieveDelete(RetrieveDestroyAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

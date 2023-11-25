from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin 
from rest_framework import viewsets
from .serializer import ProductSerialiazer, BillSerialiazer, SellDetailSerializer
from .models import Product, Bill, SellDetail
# Create your views here.
class ProductGenericView(viewsets.GenericViewSet,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):

    serializer_class = ProductSerialiazer
    queryset = Product.objects.all() 
    lookup_field = "id"

    def get(self, request, id=None):

        if not (id):
            return self.list(request)
        else:
            return self.retrieve(request)

    def post(self, request, id= None):
        return self.create(request)
    
    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, request, id= None):
        return self.destroy(request, id)
    
    def get_queryset(self): 
        queryset = self.queryset.order_by('-id')
        return queryset
    
class BillGenericView(viewsets.GenericViewSet,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):

    serializer_class = BillSerialiazer
    queryset = Bill.objects.all() 
    lookup_field = "id"

    def get(self, request, id=None):

        if not (id):
            return self.list(request)
        else:
            return self.retrieve(request)

    def perform_create(self, serializer):
        sellsdetails = self.request.data.get('sellsdetails', [])
        sellsdetailssaved = []
        for selldetail in sellsdetails:
            selldetailserializer = SellDetailSerializer(data=selldetail)
            selldetailserializer.is_valid(raise_exception=True)
            selldetailinstance = selldetailserializer.save()
            sellsdetailssaved.append(selldetailinstance)

        serializer.save(selldetail=sellsdetailssaved)

    def post(self, request, id= None):
        return self.create(request)
    
    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, request, id= None):
        return self.destroy(request, id)
    
    def get_queryset(self):
        queryset = self.queryset.order_by('-id')
        return queryset

class SellDetailGenericView(viewsets.GenericViewSet,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):

    serializer_class = SellDetailSerializer
    queryset = SellDetail.objects.all() 
    lookup_field = "id"

    def get(self, request, id=None):

        if not (id):
            return self.list(request)
        else:
            return self.retrieve(request)

    def post(self, request, id= None):
        return self.create(request)
    
    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, request, id= None):
        return self.destroy(request, id)
    
    def get_queryset(self): 
        queryset = self.queryset.order_by('-id')
        return queryset
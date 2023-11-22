from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin 
from rest_framework import viewsets
from .serializer import ProductSerialiazer
from .models import Product
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
    
    def get_queryset(self): #Este metodo se llama dentro del get
        queryset = self.queryset.order_by('-id')
        return queryset
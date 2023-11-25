from rest_framework import fields, serializers
from .models import Product, Bill, SellDetail

class ProductSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
    
    def to_representation(self,instance):
        return super(ProductSerialiazer,self).to_representation(instance)

class SellDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellDetail
        fields = '__all__'
    
    def to_representation(self,instance):
        self.fields["product"]= ProductSerialiazer(read_only=True)
        return super(SellDetailSerializer,self).to_representation(instance)
    
class BillSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'
    
    def to_representation(self,instance):
        self.fields["selldetail"]= SellDetailSerializer(read_only=True, many=True)
        return super(BillSerialiazer,self).to_representation(instance)

    
    

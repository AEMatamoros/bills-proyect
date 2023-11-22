from rest_framework import fields, serializers
from .models import Product

class ProductSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
    
    def to_representation(self,instance):
        ##Remember to use later
        # self.fields["related_field"]= RelatedSerialiazer(read_only=True)
        return super(ProductSerialiazer,self).to_representation(instance)


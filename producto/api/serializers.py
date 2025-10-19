from producto.models import Producto
from rest_framework import serializers

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' #Aqui por seguridad se pone todo, pero en produccion se recomienda poner los campos que se van a usar.
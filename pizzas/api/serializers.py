from rest_framework import serializers
from pizzas.models import Pizza, Topping, Size

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('__all__')

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('__all__')

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('__all__')

class PizzaReadSerializer(serializers.ModelSerializer):
    size = SizeSerializer(read_only=True)
    topping = ToppingSerializer(read_only=True)
    class Meta:
        model = Pizza
        fields = ('__all__')
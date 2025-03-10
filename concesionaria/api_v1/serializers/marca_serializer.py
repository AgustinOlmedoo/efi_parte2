from rest_framework import serializers
from vehiculos.models import Marca


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
        ref_name = 'MarcaSerializer'  # Otro nombre único para evitar conflictos


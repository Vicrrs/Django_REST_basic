from rest_framework import serializers
from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}  # email nao vai ser apresentado
        }  # email exigido apenas para cadastro, por questao de seguranca
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )

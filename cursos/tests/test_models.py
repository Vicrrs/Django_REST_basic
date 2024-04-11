from django.test import TestCase
from ..models import Curso
from django.db import IntegrityError


class CursoTestCase(TestCase):
    def setUp(self) -> None:
        self.curso = Curso.objects.create(
            titulo="Curso Django", url="http://curso001Django.com")

    def test_curso_creation(self):
        """
        Testa a criacao de um curso e verifica se os campos estao corretos
        """
        self.assertEqual(self.curso.titulo, "Curso Django")
        self.assertFalse(self.curso.ativo,
                         "O curso deve ser inativo por padrão")
        self.assertIsNotNone(self.curso.publicacao,
                             "Deveria ter uma data de publicação")

    def test_curso_unique_url(self):
        """Testa se a URL do curso é única."""
        with self.assertRaises(IntegrityError):
            Curso.objects.create(titulo="Curso de Flask",
                                 url="http://curso001Django.com")

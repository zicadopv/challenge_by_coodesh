from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializer import ArticlesSerializer
from voos.models import Voo


def index(request):
    return JsonResponse({
        "status": "ok",
        "message": "Back-end Challenge 2021 🏅 - Space Flight News"
    })


@api_view(['GET'])
def articles(request):
    """[GET]/articles/: Listar todos os artigos da base de dados,
        utilizar o sistema de paginação para não sobrecarregar a REQUEST
    """
    articles = Voo.objects.all()
    serializer = ArticlesSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_key(request, key):
    """[GET]/articles/id: Obter a informação somente de um artigo"""
    if request.method == 'GET':
        try:
            article = Voo.objects.filter(key=key)
            serializer = ArticlesSerializer(article, many=True)
            return Response(serializer.data)
        except Voo.DoesNotExist:
            return Response(
                f'Artigo com este key..:{key} não existe!',
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_new(request):
    """[POST]/articles/: Adicionar um novo artigo"""
    if request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def article_update(request, key):
    """[PUT]/articles/{id}: Atualizar um artigo baseado no id"""
    if request.method == 'PUT':
        try:
            article = Voo.objects.get(key=key)
            request_data = request.data
            serializer_class = ArticlesSerializer(
                article, data=request_data, partial=True
            )
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(
                    serializer_class.data, status=status.HTTP_200_OK
                )
            return Response(
                serializer_class.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except Voo.DoesNotExist as err:
            return Response(
                f"O artigo de key..:{key} não existe na base",
                status.HTTP_404_NOT_FOUND
            )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def article_delete(request, key):
    """[DELETE]/articles/{id}: Remover um artigo baseado no id"""
    if request.method == 'DELETE':
        try:
            article = Voo.objects.get(key=key)
            article.delete()
            return Response(status.HTTP_200_OK)
        except Exception as err:
            return Response(
                f"O artigo de key..:{key} não existe na base",
                status.HTTP_404_NOT_FOUND
            )

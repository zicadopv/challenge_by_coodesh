from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializer import ArticlesSerializer
from voos.models import Voo


@api_view(['GET'])
def articles(request):
    """[GET]/articles/: Listar todos os artigos da base de dados,
        utilizar o sistema de paginação para não sobrecarregar a REQUEST
    """
    articles = Voo.objects.all()
    serializer = ArticlesSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_id(request, id):
    """[GET]/articles/id: Obter a informação somente de um artigo"""
    if request.method == 'GET':
        try:
            article = Voo.objects.filter(id=id)
            serializer = ArticlesSerializer(article, many=True)
            return Response(serializer.data)
        except Voo.DoesNotExist:
            return Response(
                f'Artigo com este ID..:{id} não existe!',
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['POST'])
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
def article_update(request, id):
    """[PUT]/articles/{id}: Atualizar um artigo baseado no id"""
    if request.method == 'PUT':
        article = Voo.objects.get(id=id)
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


@api_view(['DELETE'])
def article_delete(request, id):
    """[DELETE]/articles/{id}: Remover um artigo baseado no id"""
    if request.method == 'DELETE':
        try:
            article = Voo.objects.get(id=id)
            article.delete()
            return Response(status.HTTP_200_OK)
        except Exception as err:
            return Response(f"Error delete.: {err}", status.HTTP_404_NOT_FOUND)

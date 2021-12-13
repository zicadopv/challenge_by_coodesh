from django.http import HttpResponse, JsonResponse

from rest_framework import generics

from voos.models import Voo


class DatabaseHealth(generics.ListAPIView):
    """
        Retornar um Status: 200 e uma Mensagem "Back-end Challenge 2021 🏅 - Space Flight News
    """
    def get(self, request):
        try:
            Voo.objects.get(id=1)
            return JsonResponse({"status": "ok"})
        except Exception:
            return HttpResponse(status=503)

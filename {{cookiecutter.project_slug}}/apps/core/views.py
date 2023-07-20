from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class StatusAPIView(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request):
        return Response({"status": "ok"})

    def post(self, request):
        print(request.user)
        return Response({"authenticated": True})

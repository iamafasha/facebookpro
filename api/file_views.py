from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .file_serializers import FileSerializers
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class MyUploadView(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        mymodel.my_file_field.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        mymodel.my_file_field.delete(save=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
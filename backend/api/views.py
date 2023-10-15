from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from api.serializers import CleanReportSerializer, WorkReportSerializer


@api_view(['POST'])
def work_report_list(request: Request) -> Response:  # type: ignore
    if request.method == 'POST':
        serializer = WorkReportSerializer(data=request.data)  # type: ignore
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def clean_report_list(request: Request) -> Response:  # type: ignore
    if request.method == 'POST':
        serializer = CleanReportSerializer(data=request.data)  # type: ignore
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

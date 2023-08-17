from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import WorkReportSerializer


@api_view(['POST'])
def report_list(request):
    if request.method == 'POST':
        serializer = WorkReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

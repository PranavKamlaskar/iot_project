from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SensorDataView(APIView):
    def post(self, request):
        temp = request.data.get("temperature")
        hum = request.data.get("humidity")
        print(f"Received - Temp: {temp}, Humidity: {hum}")
        return Response({"message": "Data received"}, status=status.HTTP_200_OK)


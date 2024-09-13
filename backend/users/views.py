import json
from django.shortcuts import render # type: ignore

from rest_framework import status # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from .models import CustomUser
from .serializers import RegistrationSerializer
from django.core.mail import send_mail # type: ignore

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Send activation email
            return Response({'message': 'User registered successfully! Please check your email for activation link.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def register(request):
        if request.method == 'POST':
            data = json.loads(request.body)
        # Implement registration logic
            return JsonResponse({'message': 'Registration successful!'}, status=201) # type: ignore
        else:
            return JsonResponse({'error': 'Invalid request method.'}, status=400) # type: ignore


from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
       serializer = UserSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)

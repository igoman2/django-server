from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

@api_view(['POST'])
def helloAPI(request):

    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        print("Invalid")
        serializer.save()
    print("Valide")
    print(request.data)
    return Response(request.data)
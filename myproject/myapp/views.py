from django.shortcuts import render
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

class IndexView(View):
    def index(request):
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})

class ApiLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # TODO: LOGIN LOGIC HERE
        token = "the_generated_jwt_token"
        return Response({'token': token})

class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListPostsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

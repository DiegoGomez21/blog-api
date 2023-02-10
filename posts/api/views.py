from django.db.models import Q #Funciona con consulta de filtro avanzado,  permite crear consultas complejas
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination

class PostApiViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        userr = self.request.user
        if userr.is_superuser:
            return self.queryset
        else:
            #Va a retornar los post que estan publicados y que le pertenecen al usuario
            return self.queryset.filter(Q(published=True) | Q(user=userr.id))
        

    
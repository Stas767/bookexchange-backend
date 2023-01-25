# from django.shortcuts import get_object_or_404
# from django.core.exceptions import PermissionDenied
from books.models import BookAuthor, Book, Genre  # , User
from rest_framework import viewsets, permissions, filters
# , permissions, mixins, filters, serializers

from .serializers import (
    BookSerializer,
    BookAuthorSerializer,
    GenreSerializer
)
from .permissions import IsAuthorOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'author__last_name',
        'author__first_name',
        'title',
        'creation_date',
        )

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    # def perform_update(self, serializer):
    #     if serializer.instance.author != self.request.user:
    #         raise PermissionDenied('Изменение чужого контента запрещено!')
    #     serializer.save()

    # def perform_destroy(self, serializer):
    #     if serializer.author != self.request.user:
    #         raise PermissionDenied('Удаление чужого контента запрещено!')
    #     serializer.delete()


class BookAuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     # permission_classes = [
#     #     permissions.IsAuthenticated, IsAuthorOrReadOnly
#     # ]

#     def get_queryset(self):
#         post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
#         return post.comments

#     def perform_create(self, serializer):
#         post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
#         serializer.save(post=post, author=self.request.user)


# class FollowViewSet(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     viewsets.GenericViewSet):
#     # queryset = Follow.objects.all()
#     serializer_class = FollowSerializer
#     permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly,]
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('following__username',)

#     def get_queryset(self):
#         user = get_object_or_404(User, pk=self.request.user.id)
#         return user.follower

#     def perform_create(self, serializer):
#         user = self.request.user
#         following = serializer.validated_data['following']

#         if Follow.objects.filter(user=user, following=following).exists():
#             raise serializers.ValidationError

#         if user != following:
#             serializer.save(user=self.request.user)
#         else:
#             raise serializers.ValidationError('Нельзя подписаться на себя самого!')

#         # return super().perform_create(serializer)

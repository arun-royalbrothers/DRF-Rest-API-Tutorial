from .models import *
from .serializer import *
from rest_framework import mixins, generics

class MovieListGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#Concrete API View
class MovieCreateConcreteView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewCreateConcreteView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieListConcreteView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListConcreteView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieDetailConcreteView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewDetailConcreteView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieDeleteConcreteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewDeleteConcreteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieUpdateConcreteView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewUpdateConcreteView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieListCreateConcreteView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListCreateConcreteView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieDetailUpdateConcreteView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewDetailUpdateConcreteView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieDetailDeleteConcreteView(generics.RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewDetailDeleteConcreteView(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieDetailUpdateDeleteConcreteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewDetailUpdateDeleteConcreteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions, response, status, views

from car.models import Car, Comment
from .serializers import (
    CarSerializer,
    CarCreateSerializer,
    CommentSerializer,
    CommentCreateSerializer,
)


class ViewMixin(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        abstract = True


class CarListView(ViewMixin):
    def get(self, request, *args, **kwargs):
        cars = Car.objects.all().prefetch_related("comments")
        serializer = CarSerializer(cars, many=True)

        return response.Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = CarCreateSerializer(data=data)
        if serializer.is_valid():
            car = serializer.save(owner=request.user)

            return response.Response(CarSerializer(car).data, status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CarDetailView(ViewMixin):
    def get(self, request, car_id, *args, **kwargs):
        car = get_object_or_404(Car, id=car_id)

        return response.Response(CarSerializer(car).data, status.HTTP_200_OK)

    def put(self, requst, car_id, *args, **kwargs):
        car = get_object_or_404(Car, id=car_id)
        serializer = CarCreateSerializer(car, data=requst.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return response.Response(CarSerializer(car).data, status.HTTP_200_OK)

        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, car_id, *args, **kwargs):
        car = get_object_or_404(Car, id=car_id)
        car.delete()

        return response.Response({"msg": "Succesfully deleted."}, status.HTTP_200_OK)


class CommentView(ViewMixin):
    def get(self, request, car_id, *args, **kwargs):
        car = get_object_or_404(Car, id=car_id)
        comments = Comment.objects.filter(car=car).all()
        serializer = CommentSerializer(comments, many=True)

        return response.Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, car_id, *args, **kwargs):
        car = get_object_or_404(Car, id=car_id)

        data = request.data.copy()
        serializer = CommentCreateSerializer(data=data)
        if serializer.is_valid():
            comment = serializer.save(author=request.user, car=car)

            return response.Response(CommentSerializer(comment).data, status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

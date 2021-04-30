from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.serializers import UserSerializer, RegisterUserSerializer


class RegisterUserViewSet(CreateAPIView):
    model = get_user_model()
    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)


class CurrentUserAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = RegisterUserSerializer  # UserSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = get_object_or_404(queryset, id=self.request.user.id)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    # def update(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(request.user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)

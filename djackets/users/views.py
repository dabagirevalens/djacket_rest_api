from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProfileSerializer
from .forms import CustomUserCreationForm


class ProfileRegister(APIView):
    def register(self, request):

        form = CustomUserCreationForm()

        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)

            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()

                serializer = ProfileSerializer(user, many=False)

                return Response(serializer.data)

            else:
                return Http404

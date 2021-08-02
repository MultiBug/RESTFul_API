from rest_framework import generics
from Quest.serializers import QuestDetailSerializer, QuestListSerializer
from Quest.models import Quest
from Quest.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class QuestCreateView(generics.CreateAPIView):
    serializer_class = QuestDetailSerializer


class QuestListView(generics.ListAPIView):
    serializer_class = QuestListSerializer
    queryset = Quest.objects.all()
    permission_classes = (IsAuthenticated, )


class QuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestDetailSerializer
    queryset = Quest.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
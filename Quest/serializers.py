from rest_framework import serializers
from Quest.models import Quest


class QuestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id')


class QuestDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Quest
        fields = '__all__'

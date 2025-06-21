from rest_framework import serializers
from .models import *
import datetime
from rest_framework.validators import UniqueTogetherValidator


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')
    class Meta:
        model = Achievement
        fields = ['id', 'achievement_name']

class CatSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    achievement = AchievementSerializer(many=True, required=False)
    class Meta:
        model = Cat
        fields = ['id', 'name', 'color', 'birth_year', 'owner', 'age', 'achievement']
        read_only_fields = ['owner']

    validators = [
            UniqueTogetherValidator(
                queryset=Cat.objects.all(),
                fields=('name', 'owner')
            )
        ]

    def validate(self, data):
        if data['name'] == data['color']:
            raise serializers.ValidationError('It cant be same')
        return data
        
    def get_age(self, obj):
        return datetime.datetime.now().year - obj.birth_year 

    def create(self, validated_data):
        if 'achievement' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat
        else:
            achievement = validated_data.pop('achievement')
            cat = Cat.objects.create(**validated_data)
            for achievements in achievement:
                current_achievement, status=Achievement.objects.get_or_create(**achievements)
                AchievementCat.objects.create(name=current_achievement, cat=cat)
            return cat

class AchievementCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementCat
        fields = ['id', 'name', 'cat']
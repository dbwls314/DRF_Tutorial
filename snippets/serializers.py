# 직렬화 & 역직렬화 방법 제공하기
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# ModelSerializer class 사용 -> 직렬 변환기 클래스를 생성하기 위한 클래스
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet 
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style'] # Snippet 모델의 필드명
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
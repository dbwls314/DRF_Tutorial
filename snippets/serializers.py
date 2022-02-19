# 직렬화 & 역직렬화 방법 제공하기
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# ModelSerializer class 사용 -> 직렬 변환기 클래스를 생성하기 위한 클래스
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet 
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style'] # Snippet 모델의 필드명

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
from rest_framework import serializers
from questionbank.models import Category,Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields =(
            'question_text',
            'question_link'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category_name',
            )

class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'question-detail'
    )
    class Meta:
        model = Category
        fields = (
            'category_name',
            'category_description',
            'questions'
        )


class QuestionDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question_text',
            'question_link'
        )
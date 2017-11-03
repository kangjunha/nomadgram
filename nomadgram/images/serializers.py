from rest_framework import serializers
from . import models
# serializer -> Framework와 Python world의 다리

class ImageSerializer(serializers.Serializer):

    class Meta:
        model = models.Image
        fields = '__all__'

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.Serializer):

    class Meta:
        model = models.Like
        fields = '__all__'

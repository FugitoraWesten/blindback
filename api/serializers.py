from rest_framework import serializers
from image_processing.models import Image, Description

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id', 'description_text', 'created_at']

class ImageSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'image_file', 'uploaded_at', 'descriptions']

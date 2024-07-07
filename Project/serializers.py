from rest_framework import serializers
from .models import Technology, Project

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'project_link', 'slug', 'description', 'role', 'technologies', 'image', 'created_at']

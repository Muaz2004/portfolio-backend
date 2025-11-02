from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    tech_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
        'id', 'title', 'description', 'tech_stack', 'tech_list',
        'github_link', 'live_link', 'video_demo', 'image_preview', 'created_at'
         ]

    def get_tech_list(self, obj):
        return obj.tech_list

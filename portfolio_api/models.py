from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)

    # 🎥 YouTube demo and image fallback
    video_demo = models.URLField(blank=True, null=True)
    image_preview = models.ImageField(upload_to='project_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in (self.tech_stack or "").split(',') if t.strip()]

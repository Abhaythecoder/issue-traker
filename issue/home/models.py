from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Issue(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
        
    ]
    is_completed = models.BooleanField(default=False)

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='open')
    project = models.ForeignKey(Project, related_name='issues',

                                on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='issues_created',
                                   on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='issues_assigned',
                                    on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    issue = models.ForeignKey(Issue, related_name='comments',
                              on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments',
                               on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.issue}'

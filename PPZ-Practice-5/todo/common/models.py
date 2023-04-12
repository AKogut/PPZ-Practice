from django.db import models

class Task(models.Model):
    HIGH_PRIORITY = 'H'
    MEDIUM_PRIORITY = 'M'
    LOW_PRIORITY = 'L'
    PRIORITY_CHOICES = (
        (HIGH_PRIORITY, 'High'),
        (MEDIUM_PRIORITY, 'Medium'),
        (LOW_PRIORITY, 'Low')
    )

    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=MEDIUM_PRIORITY)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

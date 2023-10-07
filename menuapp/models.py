from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    url = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    menu_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_descendants(self):
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants

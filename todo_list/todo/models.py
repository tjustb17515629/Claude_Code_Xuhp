from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    completed = models.BooleanField(default=False, verbose_name='已完成')
    category = models.CharField(
        max_length=20,
        choices=[
            ('study', '学习'),
            ('entertainment', '娱乐'),
            ('work', '工作'),
            ('life', '生活'),
        ],
        default='study',
        verbose_name='类型',
    )
    due_date = models.DateField(null=True, blank=True, verbose_name='截止日期')
    tags = models.CharField(max_length=200, blank=True, verbose_name='标签')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

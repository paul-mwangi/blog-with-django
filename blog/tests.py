from django.test import TestCase
from blog.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Big', body='unique unique', author_id='1')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
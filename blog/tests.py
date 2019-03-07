from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='big', body='unique unique', author_id='1')

    def test_title_max_length(self):
        post = post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 250)
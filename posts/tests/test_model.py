from django.test import TestCase
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'accounts.User'
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = "vpdiongzon@gmail.com"


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'posts.Post'
    
    text = "default text"
    user = factory.SubFactory(UserFactory)


class PostTestCase(TestCase):

    def test_post_text_field(self):
        
        post = PostFactory()
        user = UserFactory()
        
        self.assertEqual(post.text, "default text")
        self.assertEqual(post.user, user)

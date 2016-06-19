import factory
from django_factory_boy import auth as auth_factories


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Post'

    author = auth_factories.UserFactory()
    title = "Test Title"
    content = "Here is some test content."

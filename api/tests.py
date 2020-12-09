from django.test import TestCase, Client
import json
from rest_framework import status
from django.urls import reverse
from post.models import Post
from .post_serializers import PostSerializers

# Create your tests here.

# initialize the APIClient app
client = Client()

class CreateNewPostTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'text': 'Hello',
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_post(self):
        response = client.post(
            reverse('post_api'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_post(self):
        response = client.post(
            reverse('post_api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
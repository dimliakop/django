import os
from django.core.files import File
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
import mock

from versioning.models import Document, Revision


class RevisionModelTests(TestCase):

    def setUp(self):
        get_user_model().objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def tearDown(self):
        # pass
        from base import settings
        path = os.path.join(settings.BASE_DIR, 'users\\temporary\\test-file.0.jpg')
        if os.path.isfile(path):
            os.remove(path)


    def test_revision_index(self):
        """
        """
        document = Document.objects.create(url='some-url', owner=User.objects.get(username='temporary'))
        revision0 = Revision.objects.create(document=document)
        revision1 = Revision.objects.create(document=document)
        revision2 = Revision.objects.create(document=document)

        self.assertEqual(revision0.index, 0)
        self.assertEqual(revision1.index, 1)
        self.assertEqual(revision2.index, 2)


    def test_revision_revision_url(self):
        """
        """
        mock_file = mock.MagicMock(spec=File)
        mock_file.name = 'test-file.jpg'
        document = Document.objects.create(url='some/url', owner=User.objects.get(username='temporary'))
        revision = Revision.objects.create(document=document, file=mock_file)
        self.assertEqual(revision.url, "users/temporary/test-file.0.jpg")
        self.assertEqual(revision.revision_url, "some/url?revision=0")

    def test_upload_to(self):
        pass

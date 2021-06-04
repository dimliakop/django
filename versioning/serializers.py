from django.contrib.auth.models import User
from rest_framework import serializers

from base import settings
from versioning.models import Revision, Document


class RevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revision
        fields = ['id', 'created', 'file', 'index', 'revision_url']


class DocumentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    url = serializers.CharField(allow_blank=False)
    revisions = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='revision-detail')
    file = serializers.FileField(write_only=True)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')

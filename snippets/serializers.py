from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# For User Authentication
from django.contrib.auth.models import User


# The first part of the serializer class defines the fields that get serialized/deserialized. 
# The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()

# Good Way to do it
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # or CharField(read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')
# Bad Way to do it

# class SnippetSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#    code = serializers.CharField(style={'base_template': 'textarea.html'})
#    linenos = serializers.BooleanField(required=False)
#    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#    def create(self, validated_data):
#        """
#        Create and return a new `Snippet` instance, given the validated data.
#        """
#        return Snippet.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#       """
#        Update and return an existing `Snippet` instance, given the validated data.
#        """
#        instance.title = validated_data.get('title', instance.title)
#        instance.code = validated_data.get('code', instance.code)
#        instance.linenos = validated_data.get('linenos', instance.linenos)
#        instance.language = validated_data.get('language', instance.language)
#        instance.style = validated_data.get('style', instance.style)
#        instance.save()
#        return instance


# For user authentication

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,view_name='snippet-detail',read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
#  Because 'snippets' is a reverse relationship on the User model, it will not be included by default
#  when using the ModelSerializer class, so we needed to add an explicit field for it.
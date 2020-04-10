from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from blog.models import Comment


class BlogCommentTreeSerializer(ModelSerializer):
    children = SerializerMethodField(source='get_children')

    class Meta:
        models = Comment
        fields = ('children', 'id', 'author', 'body',)  # add here rest of the fields from model

    def get_children(self, obj):
        children = self.context['children'].get(obj.id, [])
        serializer = BlogCommentTreeSerializer(children, many=True, context=self.context)
        return serializer.data

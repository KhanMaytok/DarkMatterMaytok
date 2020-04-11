from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from blog.models import Comment
from core.models import User


class UserForCommentSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', ]


class BlogCommentTreeSerializer(ModelSerializer):
    leaf_nodes = SerializerMethodField()
    user = UserForCommentSerializer()

    def get_leaf_nodes(self, obj):
        return BlogCommentTreeSerializer(obj.get_children(), many=True).data

    class Meta:
        depth = 1
        model = Comment
        fields = ('leaf_nodes', 'id', 'user', 'body',)  # add here rest of the fields from model

from rest_framework import serializers
from gifts.models import Gift, User, GiftAddress, Category, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Comment
        fields = "__all__"


class GiftAddressSerializer(serializers.ModelSerializer):
    """Полный адрес"""

    class Meta:
        model = GiftAddress
        fields = "__all__"


class GiftListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    address = GiftAddressSerializer(many=True)
    gift_comments = CommentCreateSerializer(many=True)
    class Meta:
        model = Gift
        fields = "__all__"


# class GiftDetailSerializer(serializers.ModelSerializer):
#     """Полный фильм"""
#     category = serializers.SlugRelatedField(slug_field="name", read_only=True)
#     user = serializers.SlugRelatedField(slug_field="username", read_only=True)
#     address = GiftAddressSerializer(many=True)
#     gift_comments = CommentCreateSerializer(many=True)
# 
#     class Meta:
#         model = Gift
#         exclude = ("new", )

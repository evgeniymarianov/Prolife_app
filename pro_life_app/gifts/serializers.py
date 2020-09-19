from rest_framework import serializers
from gifts.models import Gift, User, GiftAddress, Category, Comment


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftAddress
        fields = "__all__"

class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Comment
        fields = "__all__"


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("name", "text", "children")


class GiftAddressSerializer(serializers.ModelSerializer):
    """Полный адрес"""

    class Meta:
        model = GiftAddress
        fields = "__all__"


class GiftListSerializer(serializers.ModelSerializer):
    #category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    #user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    #address = GiftAddressSerializer(many=True)
    #gift_comments = CommentSerializer(many=True)
    class Meta:
        model = Gift
        fields = "__all__"


class GiftDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    address = GiftAddressSerializer(many=True)
    gift_comments = CommentSerializer(many=True)
    class Meta:
        model = Gift
        exclude = ("photo",)

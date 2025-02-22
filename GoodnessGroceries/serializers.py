from rest_framework import serializers
from .models import CashierTicketProducts, ProductReviews, Users


class CashierTicketProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashierTicketProducts
        fields = (
            'product_ean',
            'timestamp',
        )


class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviews
        fields = (
            'participant',
            'product_ean',
            'timestamp',
            'selected_indicator_main_id',
            'selected_indicator_secondary_id',
            'free_text_indicator',
            'price_checkbox_selected',
        )


class UsersStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'status',
        )


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'participant_id',
            'platform',
            'product_category_1',
            'product_category_2',
            'product_category_3',
            'product_category_4',
            'indicator_category_1',
            'indicator_category_2',
            'indicator_category_3',
            'indicator_category_4',
        )

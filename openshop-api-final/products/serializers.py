from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Product.

    Menambahkan atribut `_links` yang berisi tautan HATEOAS (Hypermedia
    as the Engine of Application State) sehingga client API dapat
    mengetahui aksi apa saja (POST, GET, PUT, DELETE) yang tersedia
    terkait resource produk tanpa perlu dokumentasi terpisah.
    """
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'sku', 'description', 'shop', 'location',
            'price', 'discount', 'category', 'stock', 'is_available',
            'picture', 'is_delete', '_links',
        ]

    def get__links(self, obj):
        """Menghasilkan daftar tautan HATEOAS terkait resource produk."""
        return [
            {"rel": "self", "href": "/products", "action": "POST", "types": ["application/json"]},
            {"rel": "self", "href": f"/products/{obj.id}/", "action": "GET", "types": ["application/json"]},
            {"rel": "self", "href": f"/products/{obj.id}/", "action": "PUT", "types": ["application/json"]},
            {"rel": "self", "href": f"/products/{obj.id}/", "action": "DELETE", "types": ["application/json"]},
        ]
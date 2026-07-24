from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(APIView):
    """
    View untuk menampilkan daftar produk dan menambahkan produk baru.

    GET  /products/  : mengembalikan daftar produk aktif (tidak dihapus),
                        dengan dukungan filter opsional `name` dan `location`.
    POST /products/  : membuat produk baru berdasarkan data yang dikirim.
    """

    def get(self, request):
        """Mengembalikan daftar produk, opsional difilter berdasarkan nama/lokasi."""
        name = request.query_params.get("name")
        location = request.query_params.get("location")

        queryset = Product.objects.filter(is_delete=False)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)

        serializer = ProductSerializer(queryset, many=True)
        return Response({"products": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """Membuat produk baru setelah melalui validasi serializer."""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    """
    View untuk menampilkan, mengubah, dan menghapus (soft delete)
    satu produk berdasarkan id (UUID).
    """

    def get_object(self, pk):
        """Mengambil instance Product berdasarkan primary key, atau None jika tidak ditemukan."""
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        """Menampilkan detail satu produk berdasarkan id."""
        product = self.get_object(pk)
        if not product:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Memperbarui data produk berdasarkan id."""
        product = self.get_object(pk)
        if not product:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Menghapus produk secara soft delete: data tidak benar-benar
        dihapus dari database, hanya ditandai `is_delete=True`.
        """
        product = self.get_object(pk)
        if not product:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        product.is_delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
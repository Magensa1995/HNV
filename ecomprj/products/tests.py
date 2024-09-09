from django.test import TestCase
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from decimal import Decimal

class ProductModelTest(TestCase):
    
    def setUp(self):
        # This method is run before every test.
        Product.objects.create(
            name="Test Product",
            description="A test product",
            price=10.99,
            stock=100,
            available=True
        )

    def test_product_creation(self):
        # Test if the product is created successfully
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "A test product")
        self.assertEqual(product.price, Decimal('10.99'))
        self.assertEqual(product.stock, 100)
        self.assertTrue(product.available)

    def test_product_string_representation(self):
        # Test the string representation of the Product model
        product = Product.objects.get(name="Test Product")
        self.assertEqual(str(product), product.name)

    # def test_product_form_valid_data(self):
    #     form = ProductForm(data={
    #         'name': 'Test Product',
    #         'description': 'A test product description',
    #         'price': 20.99,
    #         'stock': 50,
    #         'available': True
    #     })

    #     # Check if form is valid
    #     self.assertTrue(form.is_valid())

    # def test_product_form_invalid_price(self):
    #     form = ProductForm(data={
    #         'name': 'Test Product',
    #         'description': 'A test product description',
    #         'price': -10.99,  # Invalid price
    #         'stock': 50,
    #         'available': True
    #     })

    #     # Form should be invalid because price is negative
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('price', form.errors)

    # def test_product_form_missing_required_fields(self):
    #     form = ProductForm(data={})

    #     # Form should be invalid because required fields are missing
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('name', form.errors)
    #     self.assertIn('description', form.errors)
    #     self.assertIn('price', form.errors)
    #     self.assertIn('stock', form.errors)

    # def test_product_list_view(self):
    #     # Test if product list view works correctly
    #     response = self.client.get(reverse('product_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Test Product")
    #     self.assertTemplateUsed(response, 'product_list.html')

    # def test_product_detail_view(self):
    #     # Test if product detail view works correctly
    #     response = self.client.get(reverse('product_detail', args=[self.product.id]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Test Product")
    #     self.assertTemplateUsed(response, 'product_detail.html')

    # def test_product_create_view(self):
    #     # Test creating a new product via the view
    #     response = self.client.post(reverse('product_create'), {
    #         'name': 'New Product',
    #         'description': 'A new product description',
    #         'price': 15.99,
    #         'stock': 30,
    #         'available': True
    #     })
    #     self.assertEqual(response.status_code, 302)  # Redirect after success
    #     self.assertEqual(Product.objects.last().name, 'New Product')

    # def test_product_update_view(self):
    #     # Test updating an existing product
    #     response = self.client.post(reverse('product_update', args=[self.product.id]), {
    #         'name': 'Updated Product',
    #         'description': 'Updated product description',
    #         'price': 20.99,
    #         'stock': 200,
    #         'available': True
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.product.refresh_from_db()
    #     self.assertEqual(self.product.name, 'Updated Product')

    # def test_product_delete_view(self):
    #     # Test deleting a product
    #     response = self.client.post(reverse('product_delete', args=[self.product.id]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(Product.objects.filter(id=self.product.id).exists())
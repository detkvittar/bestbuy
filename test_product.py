import pytest
from products import Product

def test_product_creation():
    product = Product("Test Product", price=10, quantity=100)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 100
    assert product.is_active() == True

def test_invalid_product_creation():
    with pytest.raises(Exception):
        Product("", price=10, quantity=100)  # empty name

    with pytest.raises(Exception):
        Product("Test Product", price=-10, quantity=100)  # negative price

    with pytest.raises(Exception):
        Product("Test Product", price=10, quantity=-100)  # negative quantity

def test_product_becomes_inactive():
    product = Product("Test Product", price=10, quantity=1)
    product.buy(1)
    assert product.is_active() == False

def test_product_purchase():
    product = Product("Test Product", price=10, quantity=100)
    total_price = product.buy(10)
    assert total_price == 100  # 10 items * $10 each
    assert product.quantity == 90  # 100 original - 10 bought

def test_buying_too_much():
    product = Product("Test Product", price=10, quantity=10)
    with pytest.raises(Exception):
        product.buy(20)  # More than available

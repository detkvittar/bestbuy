import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def test_product_creation():
    product = Product("Test Product", price=10, quantity=100)
    assert product.name == "Test Product"
    assert product.price == 10
    assert product.quantity == 100
    assert product.is_active() is True


def test_invalid_product_creation():
    with pytest.raises(ValueError):
        Product("", price=10, quantity=100)  # empty name

    with pytest.raises(ValueError):
        Product("Test Product", price=-10, quantity=100)  # negative price

    with pytest.raises(ValueError):
        Product("Test Product", price=10, quantity=-100)  # negative quantity


def test_product_becomes_inactive():
    product = Product("Test Product", price=10, quantity=1)
    product.buy(1)
    assert product.is_active() is False


def test_product_purchase():
    product = Product("Test Product", price=10, quantity=100)
    total_price = product.buy(10)
    assert total_price == 100  # 10 items * $10 each
    assert product.quantity == 90  # 100 original - 10 bought


def test_buying_too_much():
    product = Product("Test Product", price=10, quantity=10)
    with pytest.raises(ValueError):
        product.buy(20)  # More than available


def test_non_stocked_product_creation():
    product = NonStockedProduct("Windows License", price=125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.quantity == 0
    assert product.is_active() is True


def test_non_stocked_product_purchase():
    product = NonStockedProduct("Windows License", price=125)
    total_price = product.buy(10)
    assert total_price == 1250  # 10 licenses * $125 each
    assert product.quantity == 0  # quantity should stay 0


def test_limited_product_creation():
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 250
    assert product.maximum == 1
    assert product.is_active() is True


def test_limited_product_purchase_within_limit():
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    total_price = product.buy(1)
    assert total_price == 10  # 1 shipping fee * $10
    assert product.quantity == 249  # 250 original - 1 bought


def test_limited_product_purchase_exceeds_limit():
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError):
        product.buy(2)  # More than maximum limit


# Creates a reusable product for testing
@pytest.fixture
def product():
    return Product("Test Product", price=100, quantity=10)


def test_percent_discount(product):
    promotion = PercentDiscount("30% off!", percent=30)
    product.set_promotion(promotion)

    assert product.buy(1) == 70  # 30% off $100 is $70
    assert product.buy(2) == 140  # 30% off $200 is $140


def test_second_half_price(product):
    promotion = SecondHalfPrice("Second Half price!")
    product.set_promotion(promotion)

    assert product.buy(1) == 100  # Single product is full price
    assert product.buy(2) == 150  # Second product is half price
    assert product.buy(3) == 250  # Third product is full price


def test_third_one_free(product):
    promotion = ThirdOneFree("Third One Free!")
    product.set_promotion(promotion)

    assert product.buy(1) == 100  # Single product is full price
    assert product.buy(2) == 200  # Second product is full price
    assert product.buy(3) == 200  # Third product is free

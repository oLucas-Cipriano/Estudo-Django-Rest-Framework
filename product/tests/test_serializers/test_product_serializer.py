import pytest
from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    # Usando factory para criar a categoria
    category = CategoryFactory(title="technology")
    
    # Usando factory para criar o produto com a categoria associada
    product = ProductFactory(
        title="mouse", price=100, category=[category]
    )
    
    # Instanciando o serializer
    product_serializer = ProductSerializer(product)
    
    # Pegando os dados serializados
    serializer_data = product_serializer.data

    # Verificando se os dados serializados estão corretos
    assert serializer_data["price"] == 100
    assert serializer_data["title"] == "mouse"
    assert serializer_data["category"][0]["title"] == "technology"

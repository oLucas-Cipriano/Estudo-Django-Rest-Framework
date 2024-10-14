import pytest
from product.factories import CategoryFactory
from product.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    # Usando factory para criar a categoria
    category = CategoryFactory(title="food")

    # Instanciando o serializer
    category_serializer = CategorySerializer(category)

    # Pegando os dados serializados
    serializer_data = category_serializer.data

    # Verificando se o título da categoria serializada está correto
    assert serializer_data["title"] == "food"

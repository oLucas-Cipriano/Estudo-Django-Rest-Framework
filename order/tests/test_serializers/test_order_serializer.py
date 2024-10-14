import pytest
from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    # Usando factories para criar os produtos
    product_1 = ProductFactory()
    product_2 = ProductFactory()

    # Criando um pedido que utiliza os dois produtos
    order = OrderFactory(product=(product_1, product_2))

    # Instanciando o serializer
    order_serializer = OrderSerializer(order)

    # Pegando os dados serializados
    serializer_data = order_serializer.data

    # Verificando se os títulos dos produtos serializados estão corretos
    assert serializer_data["product"][0]["title"] == product_1.title
    assert serializer_data["product"][1]["title"] == product_2.title

from sqlalchemy import text

import product_pb2_grpc
import product_pb2

from connection import session_scope


class ProductManager(product_pb2_grpc.ProductAPIServicer):
    def GetAllProducts(self, request, context):
        with session_scope() as session:
            results = session.execute(text("SELECT * FROM PRODUCTS;"))
            products = []
            for product in results.fetchall():
                id, name, price, quantity = product
                products.append(product_pb2.Product(
                    name=name,
                    price=price,
                    quantity=quantity
                ))
        return product_pb2.Products(
            data=products
        )

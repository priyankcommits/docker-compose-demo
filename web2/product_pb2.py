# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='product.proto',
  package='core.product',
  syntax='proto3',
  serialized_options=_b('H\001'),
  serialized_pb=_b('\n\rproduct.proto\x12\x0c\x63ore.product\"\x0e\n\x0c\x45mptyRequest\"8\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x03\"/\n\x08Products\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.core.product.Product2T\n\nProductAPI\x12\x46\n\x0eGetAllProducts\x12\x1a.core.product.EmptyRequest\x1a\x16.core.product.Products\"\x00\x42\x02H\x01\x62\x06proto3')
)




_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='core.product.EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=45,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='core.product.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.product.Product.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='core.product.Product.price', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='core.product.Product.quantity', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=103,
)


_PRODUCTS = _descriptor.Descriptor(
  name='Products',
  full_name='core.product.Products',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='core.product.Products.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=152,
)

_PRODUCTS.fields_by_name['data'].message_type = _PRODUCT
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Products'] = _PRODUCTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYREQUEST,
  __module__ = 'product_pb2'
  # @@protoc_insertion_point(class_scope:core.product.EmptyRequest)
  ))
_sym_db.RegisterMessage(EmptyRequest)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT,
  __module__ = 'product_pb2'
  # @@protoc_insertion_point(class_scope:core.product.Product)
  ))
_sym_db.RegisterMessage(Product)

Products = _reflection.GeneratedProtocolMessageType('Products', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTS,
  __module__ = 'product_pb2'
  # @@protoc_insertion_point(class_scope:core.product.Products)
  ))
_sym_db.RegisterMessage(Products)


DESCRIPTOR._options = None

_PRODUCTAPI = _descriptor.ServiceDescriptor(
  name='ProductAPI',
  full_name='core.product.ProductAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=154,
  serialized_end=238,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllProducts',
    full_name='core.product.ProductAPI.GetAllProducts',
    index=0,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_PRODUCTS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRODUCTAPI)

DESCRIPTOR.services_by_name['ProductAPI'] = _PRODUCTAPI

# @@protoc_insertion_point(module_scope)

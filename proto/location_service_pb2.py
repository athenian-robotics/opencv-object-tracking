# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/location_service.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='proto/location_service.proto',
    package='opencv_object_tracking',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x1cproto/location_service.proto\x12\x16opencv_object_tracking\"\x1a\n\nClientInfo\x12\x0c\n\x04info\x18\x01 \x01(\t\"\x1a\n\nServerInfo\x12\x0c\n\x04info\x18\x01 \x01(\t\"_\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12\x12\n\nmiddle_inc\x18\x06 \x01(\x05\x32\xc7\x01\n\x0fLocationService\x12Z\n\x0eregisterClient\x12\".opencv_object_tracking.ClientInfo\x1a\".opencv_object_tracking.ServerInfo\"\x00\x12X\n\x0cgetLocations\x12\".opencv_object_tracking.ClientInfo\x1a .opencv_object_tracking.Location\"\x00\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CLIENTINFO = _descriptor.Descriptor(
    name='ClientInfo',
    full_name='opencv_object_tracking.ClientInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='info', full_name='opencv_object_tracking.ClientInfo.info', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=56,
    serialized_end=82,
)

_SERVERINFO = _descriptor.Descriptor(
    name='ServerInfo',
    full_name='opencv_object_tracking.ServerInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='info', full_name='opencv_object_tracking.ServerInfo.info', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=84,
    serialized_end=110,
)

_LOCATION = _descriptor.Descriptor(
    name='Location',
    full_name='opencv_object_tracking.Location',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='opencv_object_tracking.Location.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='x', full_name='opencv_object_tracking.Location.x', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='y', full_name='opencv_object_tracking.Location.y', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='width', full_name='opencv_object_tracking.Location.width', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='height', full_name='opencv_object_tracking.Location.height', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='middle_inc', full_name='opencv_object_tracking.Location.middle_inc', index=5,
            number=6, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=112,
    serialized_end=207,
)

DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), dict(
    DESCRIPTOR=_CLIENTINFO,
    __module__='proto.location_service_pb2'
    # @@protoc_insertion_point(class_scope:opencv_object_tracking.ClientInfo)
))
_sym_db.RegisterMessage(ClientInfo)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
    DESCRIPTOR=_SERVERINFO,
    __module__='proto.location_service_pb2'
    # @@protoc_insertion_point(class_scope:opencv_object_tracking.ServerInfo)
))
_sym_db.RegisterMessage(ServerInfo)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
    DESCRIPTOR=_LOCATION,
    __module__='proto.location_service_pb2'
    # @@protoc_insertion_point(class_scope:opencv_object_tracking.Location)
))
_sym_db.RegisterMessage(Location)

try:
    # THESE ELEMENTS WILL BE DEPRECATED.
    # Please use the generated *_pb2_grpc.py files instead.
    import grpc
    from grpc.framework.common import cardinality
    from grpc.framework.interfaces.face import utilities as face_utilities
    from grpc.beta import implementations as beta_implementations
    from grpc.beta import interfaces as beta_interfaces


    class LocationServiceStub(object):

        def __init__(self, channel):
            """Constructor.
      
            Args:
              channel: A grpc.Channel.
            """
            self.registerClient = channel.unary_unary(
                '/opencv_object_tracking.LocationService/registerClient',
                request_serializer=ClientInfo.SerializeToString,
                response_deserializer=ServerInfo.FromString,
            )
            self.getLocations = channel.unary_stream(
                '/opencv_object_tracking.LocationService/getLocations',
                request_serializer=ClientInfo.SerializeToString,
                response_deserializer=Location.FromString,
            )


    class LocationServiceServicer(object):

        def registerClient(self, request, context):
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def getLocations(self, request, context):
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')


    def add_LocationServiceServicer_to_server(servicer, server):
        rpc_method_handlers = {
            'registerClient': grpc.unary_unary_rpc_method_handler(
                servicer.registerClient,
                request_deserializer=ClientInfo.FromString,
                response_serializer=ServerInfo.SerializeToString,
            ),
            'getLocations': grpc.unary_stream_rpc_method_handler(
                servicer.getLocations,
                request_deserializer=ClientInfo.FromString,
                response_serializer=Location.SerializeToString,
            ),
        }
        generic_handler = grpc.method_handlers_generic_handler(
            'opencv_object_tracking.LocationService', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler,))


    class BetaLocationServiceServicer(object):
        """The Beta API is deprecated for 0.15.0 and later.
    
        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""

        def registerClient(self, request, context):
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

        def getLocations(self, request, context):
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


    class BetaLocationServiceStub(object):
        """The Beta API is deprecated for 0.15.0 and later.
    
        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""

        def registerClient(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            raise NotImplementedError()

        registerClient.future = None

        def getLocations(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            raise NotImplementedError()


    def beta_create_LocationService_server(servicer, pool=None, pool_size=None, default_timeout=None,
                                           maximum_timeout=None):
        """The Beta API is deprecated for 0.15.0 and later.
    
        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_deserializers = {
            ('opencv_object_tracking.LocationService', 'getLocations'): ClientInfo.FromString,
            ('opencv_object_tracking.LocationService', 'registerClient'): ClientInfo.FromString,
        }
        response_serializers = {
            ('opencv_object_tracking.LocationService', 'getLocations'): Location.SerializeToString,
            ('opencv_object_tracking.LocationService', 'registerClient'): ServerInfo.SerializeToString,
        }
        method_implementations = {
            ('opencv_object_tracking.LocationService', 'getLocations'): face_utilities.unary_stream_inline(
                servicer.getLocations),
            ('opencv_object_tracking.LocationService', 'registerClient'): face_utilities.unary_unary_inline(
                servicer.registerClient),
        }
        server_options = beta_implementations.server_options(request_deserializers=request_deserializers,
                                                             response_serializers=response_serializers,
                                                             thread_pool=pool, thread_pool_size=pool_size,
                                                             default_timeout=default_timeout,
                                                             maximum_timeout=maximum_timeout)
        return beta_implementations.server(method_implementations, options=server_options)


    def beta_create_LocationService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
        """The Beta API is deprecated for 0.15.0 and later.
    
        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_serializers = {
            ('opencv_object_tracking.LocationService', 'getLocations'): ClientInfo.SerializeToString,
            ('opencv_object_tracking.LocationService', 'registerClient'): ClientInfo.SerializeToString,
        }
        response_deserializers = {
            ('opencv_object_tracking.LocationService', 'getLocations'): Location.FromString,
            ('opencv_object_tracking.LocationService', 'registerClient'): ServerInfo.FromString,
        }
        cardinalities = {
            'getLocations': cardinality.Cardinality.UNARY_STREAM,
            'registerClient': cardinality.Cardinality.UNARY_UNARY,
        }
        stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer,
                                                         request_serializers=request_serializers,
                                                         response_deserializers=response_deserializers,
                                                         thread_pool=pool, thread_pool_size=pool_size)
        return beta_implementations.dynamic_stub(channel, 'opencv_object_tracking.LocationService', cardinalities,
                                                 options=stub_options)
except ImportError:
    pass
# @@protoc_insertion_point(module_scope)

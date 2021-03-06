# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/analyzer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/analyzer.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n\"rastervision/protos/analyzer.proto\x12\trv.protos\x1a\x1cgoogle/protobuf/struct.proto\"\x9a\x02\n\x0e\x41nalyzerConfig\x12\x15\n\ranalyzer_type\x18\x01 \x02(\t\x12N\n\x15stats_analyzer_config\x18\x04 \x01(\x0b\x32-.rv.protos.AnalyzerConfig.StatsAnalyzerConfigH\x00\x12\x13\n\tstats_uri\x18\x05 \x01(\tH\x00\x12\x30\n\rcustom_config\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x1a=\n\x13StatsAnalyzerConfig\x12\x11\n\tstats_uri\x18\x01 \x02(\t\x12\x13\n\x0bsample_prob\x18\x02 \x01(\x02\x42\x1b\n\x19raster_transformer_config')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ANALYZERCONFIG_STATSANALYZERCONFIG = _descriptor.Descriptor(
  name='StatsAnalyzerConfig',
  full_name='rv.protos.AnalyzerConfig.StatsAnalyzerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stats_uri', full_name='rv.protos.AnalyzerConfig.StatsAnalyzerConfig.stats_uri', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample_prob', full_name='rv.protos.AnalyzerConfig.StatsAnalyzerConfig.sample_prob', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=333,
)

_ANALYZERCONFIG = _descriptor.Descriptor(
  name='AnalyzerConfig',
  full_name='rv.protos.AnalyzerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyzer_type', full_name='rv.protos.AnalyzerConfig.analyzer_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats_analyzer_config', full_name='rv.protos.AnalyzerConfig.stats_analyzer_config', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats_uri', full_name='rv.protos.AnalyzerConfig.stats_uri', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='rv.protos.AnalyzerConfig.custom_config', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZERCONFIG_STATSANALYZERCONFIG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='raster_transformer_config', full_name='rv.protos.AnalyzerConfig.raster_transformer_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=80,
  serialized_end=362,
)

_ANALYZERCONFIG_STATSANALYZERCONFIG.containing_type = _ANALYZERCONFIG
_ANALYZERCONFIG.fields_by_name['stats_analyzer_config'].message_type = _ANALYZERCONFIG_STATSANALYZERCONFIG
_ANALYZERCONFIG.fields_by_name['custom_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ANALYZERCONFIG.oneofs_by_name['raster_transformer_config'].fields.append(
  _ANALYZERCONFIG.fields_by_name['stats_analyzer_config'])
_ANALYZERCONFIG.fields_by_name['stats_analyzer_config'].containing_oneof = _ANALYZERCONFIG.oneofs_by_name['raster_transformer_config']
_ANALYZERCONFIG.oneofs_by_name['raster_transformer_config'].fields.append(
  _ANALYZERCONFIG.fields_by_name['stats_uri'])
_ANALYZERCONFIG.fields_by_name['stats_uri'].containing_oneof = _ANALYZERCONFIG.oneofs_by_name['raster_transformer_config']
_ANALYZERCONFIG.oneofs_by_name['raster_transformer_config'].fields.append(
  _ANALYZERCONFIG.fields_by_name['custom_config'])
_ANALYZERCONFIG.fields_by_name['custom_config'].containing_oneof = _ANALYZERCONFIG.oneofs_by_name['raster_transformer_config']
DESCRIPTOR.message_types_by_name['AnalyzerConfig'] = _ANALYZERCONFIG

AnalyzerConfig = _reflection.GeneratedProtocolMessageType('AnalyzerConfig', (_message.Message,), dict(

  StatsAnalyzerConfig = _reflection.GeneratedProtocolMessageType('StatsAnalyzerConfig', (_message.Message,), dict(
    DESCRIPTOR = _ANALYZERCONFIG_STATSANALYZERCONFIG,
    __module__ = 'rastervision.protos.analyzer_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.AnalyzerConfig.StatsAnalyzerConfig)
    ))
  ,
  DESCRIPTOR = _ANALYZERCONFIG,
  __module__ = 'rastervision.protos.analyzer_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.AnalyzerConfig)
  ))
_sym_db.RegisterMessage(AnalyzerConfig)
_sym_db.RegisterMessage(AnalyzerConfig.StatsAnalyzerConfig)


# @@protoc_insertion_point(module_scope)

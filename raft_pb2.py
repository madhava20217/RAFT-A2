# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"t\n\nPutMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12$\n\x07payload\x18\x02 \x01(\x0b\x32\x13.PutMessage.Payload\x1a\x32\n\x07Payload\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x81\x01\n\x08PutReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\"\n\x07payload\x18\x02 \x01(\x0b\x32\x11.PutReply.Payload\x1a\x43\n\x07Payload\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\"t\n\nGetMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12$\n\x07payload\x18\x02 \x01(\x0b\x32\x13.GetMessage.Payload\x1a\x32\n\x07Payload\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x81\x01\n\x08GetReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\"\n\x07payload\x18\x02 \x01(\x0b\x32\x11.GetReply.Payload\x1a\x43\n\x07Payload\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\"\x98\x01\n\x0bVoteMessage\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tcommitIdx\x18\x02 \x01(\x05\x12#\n\x06staged\x18\x03 \x01(\x0b\x32\x13.VoteMessage.Staged\x12\x10\n\x08LeaderID\x18\x04 \x01(\t\x1a\x31\n\x06Staged\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\")\n\tVoteReply\x12\x0e\n\x06\x63hoice\x18\x01 \x01(\x08\x12\x0c\n\x04term\x18\x02 \x01(\x05\"\xb9\x01\n\tAEMessage\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12#\n\x07payload\x18\x03 \x01(\x0b\x32\x12.AEMessage.Payload\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\t\x12\x11\n\tcommitIdx\x18\x05 \x01(\x05\x12\x14\n\x0clease_expiry\x18\x06 \x01(\x03\x1a\x32\n\x07Payload\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"*\n\x07\x41\x45Reply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tcommitIdx\x18\x02 \x01(\x05\"\xa4\x01\n\nLogMessage\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12#\n\x06staged\x18\x03 \x01(\x0b\x32\x13.LogMessage.Payload\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\t\x12\x11\n\tcommitIdx\x18\x05 \x01(\x05\x1a\x32\n\x07Payload\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"+\n\x08LogReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tcommitIdx\x18\x02 \x01(\x05\"\x97\x01\n\rCommitMessage\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12&\n\x06staged\x18\x03 \x01(\x0b\x32\x16.CommitMessage.Payload\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\t\x1a\x32\n\x07Payload\x12\x0b\n\x03\x61\x63t\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\".\n\x0b\x43ommitReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tcommitIdx\x18\x02 \x01(\x05\"\r\n\x0bJoinRequest\"\x1a\n\x0cJoinResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\"\"\n\x0fServeClientArgs\x12\x0f\n\x07Request\x18\x01 \x01(\t\"C\n\x10ServeClientReply\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\t\x12\x10\n\x08LeaderID\x18\x02 \x01(\t\x12\x0f\n\x07Success\x18\x03 \x01(\x08\x32\xde\x02\n\x04Raft\x12%\n\x04Join\x12\x0c.JoinRequest\x1a\r.JoinResponse\"\x00\x12&\n\nPutRequest\x12\x0b.PutMessage\x1a\t.PutReply\"\x00\x12&\n\nGetRequest\x12\x0b.GetMessage\x1a\t.GetReply\"\x00\x12)\n\x0bRequestVote\x12\x0c.VoteMessage\x1a\n.VoteReply\"\x00\x12\'\n\rAppendEntries\x12\n.AEMessage\x1a\x08.AEReply\"\x00\x12%\n\tSpreadLog\x12\x0b.LogMessage\x1a\t.LogReply\"\x00\x12.\n\x0cSpreadCommit\x12\x0e.CommitMessage\x1a\x0c.CommitReply\"\x00\x12\x34\n\x0bServeClient\x12\x10.ServeClientArgs\x1a\x11.ServeClientReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PUTMESSAGE']._serialized_start=14
  _globals['_PUTMESSAGE']._serialized_end=130
  _globals['_PUTMESSAGE_PAYLOAD']._serialized_start=80
  _globals['_PUTMESSAGE_PAYLOAD']._serialized_end=130
  _globals['_PUTREPLY']._serialized_start=133
  _globals['_PUTREPLY']._serialized_end=262
  _globals['_PUTREPLY_PAYLOAD']._serialized_start=195
  _globals['_PUTREPLY_PAYLOAD']._serialized_end=262
  _globals['_GETMESSAGE']._serialized_start=264
  _globals['_GETMESSAGE']._serialized_end=380
  _globals['_GETMESSAGE_PAYLOAD']._serialized_start=80
  _globals['_GETMESSAGE_PAYLOAD']._serialized_end=130
  _globals['_GETREPLY']._serialized_start=383
  _globals['_GETREPLY']._serialized_end=512
  _globals['_GETREPLY_PAYLOAD']._serialized_start=195
  _globals['_GETREPLY_PAYLOAD']._serialized_end=262
  _globals['_VOTEMESSAGE']._serialized_start=515
  _globals['_VOTEMESSAGE']._serialized_end=667
  _globals['_VOTEMESSAGE_STAGED']._serialized_start=618
  _globals['_VOTEMESSAGE_STAGED']._serialized_end=667
  _globals['_VOTEREPLY']._serialized_start=669
  _globals['_VOTEREPLY']._serialized_end=710
  _globals['_AEMESSAGE']._serialized_start=713
  _globals['_AEMESSAGE']._serialized_end=898
  _globals['_AEMESSAGE_PAYLOAD']._serialized_start=80
  _globals['_AEMESSAGE_PAYLOAD']._serialized_end=130
  _globals['_AEREPLY']._serialized_start=900
  _globals['_AEREPLY']._serialized_end=942
  _globals['_LOGMESSAGE']._serialized_start=945
  _globals['_LOGMESSAGE']._serialized_end=1109
  _globals['_LOGMESSAGE_PAYLOAD']._serialized_start=80
  _globals['_LOGMESSAGE_PAYLOAD']._serialized_end=130
  _globals['_LOGREPLY']._serialized_start=1111
  _globals['_LOGREPLY']._serialized_end=1154
  _globals['_COMMITMESSAGE']._serialized_start=1157
  _globals['_COMMITMESSAGE']._serialized_end=1308
  _globals['_COMMITMESSAGE_PAYLOAD']._serialized_start=80
  _globals['_COMMITMESSAGE_PAYLOAD']._serialized_end=130
  _globals['_COMMITREPLY']._serialized_start=1310
  _globals['_COMMITREPLY']._serialized_end=1356
  _globals['_JOINREQUEST']._serialized_start=1358
  _globals['_JOINREQUEST']._serialized_end=1371
  _globals['_JOINRESPONSE']._serialized_start=1373
  _globals['_JOINRESPONSE']._serialized_end=1399
  _globals['_SERVECLIENTARGS']._serialized_start=1401
  _globals['_SERVECLIENTARGS']._serialized_end=1435
  _globals['_SERVECLIENTREPLY']._serialized_start=1437
  _globals['_SERVECLIENTREPLY']._serialized_end=1504
  _globals['_RAFT']._serialized_start=1507
  _globals['_RAFT']._serialized_end=1857
# @@protoc_insertion_point(module_scope)

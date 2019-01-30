# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import heartbeat_pb2 as heartbeat__pb2


class HeartbeatStub(object):
  """Service for receiving hearbeats.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Beat = channel.unary_unary(
        '/Heartbeat/Beat',
        request_serializer=heartbeat__pb2.HeartbeatRequest.SerializeToString,
        response_deserializer=heartbeat__pb2.HeartbeatResponse.FromString,
        )


class HeartbeatServicer(object):
  """Service for receiving hearbeats.
  """

  def Beat(self, request, context):
    """Send a beat.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HeartbeatServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Beat': grpc.unary_unary_rpc_method_handler(
          servicer.Beat,
          request_deserializer=heartbeat__pb2.HeartbeatRequest.FromString,
          response_serializer=heartbeat__pb2.HeartbeatResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Heartbeat', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
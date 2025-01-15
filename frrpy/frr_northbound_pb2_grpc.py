# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import frrpy.frr_northbound_pb2 as frr__northbound__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    first_version_is_lower = lambda v1, v2: False
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in frr_northbound_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NorthboundStub(object):
    """Service specification for the FRR northbound interface.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCapabilities = channel.unary_unary(
                '/frr.Northbound/GetCapabilities',
                request_serializer=frr__northbound__pb2.GetCapabilitiesRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.GetCapabilitiesResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_stream(
                '/frr.Northbound/Get',
                request_serializer=frr__northbound__pb2.GetRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.GetResponse.FromString,
                _registered_method=True)
        self.CreateCandidate = channel.unary_unary(
                '/frr.Northbound/CreateCandidate',
                request_serializer=frr__northbound__pb2.CreateCandidateRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.CreateCandidateResponse.FromString,
                _registered_method=True)
        self.DeleteCandidate = channel.unary_unary(
                '/frr.Northbound/DeleteCandidate',
                request_serializer=frr__northbound__pb2.DeleteCandidateRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.DeleteCandidateResponse.FromString,
                _registered_method=True)
        self.UpdateCandidate = channel.unary_unary(
                '/frr.Northbound/UpdateCandidate',
                request_serializer=frr__northbound__pb2.UpdateCandidateRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.UpdateCandidateResponse.FromString,
                _registered_method=True)
        self.EditCandidate = channel.unary_unary(
                '/frr.Northbound/EditCandidate',
                request_serializer=frr__northbound__pb2.EditCandidateRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.EditCandidateResponse.FromString,
                _registered_method=True)
        self.LoadToCandidate = channel.unary_unary(
                '/frr.Northbound/LoadToCandidate',
                request_serializer=frr__northbound__pb2.LoadToCandidateRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.LoadToCandidateResponse.FromString,
                _registered_method=True)
        self.Commit = channel.unary_unary(
                '/frr.Northbound/Commit',
                request_serializer=frr__northbound__pb2.CommitRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.CommitResponse.FromString,
                _registered_method=True)
        self.ListTransactions = channel.unary_stream(
                '/frr.Northbound/ListTransactions',
                request_serializer=frr__northbound__pb2.ListTransactionsRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.ListTransactionsResponse.FromString,
                _registered_method=True)
        self.GetTransaction = channel.unary_unary(
                '/frr.Northbound/GetTransaction',
                request_serializer=frr__northbound__pb2.GetTransactionRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.GetTransactionResponse.FromString,
                _registered_method=True)
        self.LockConfig = channel.unary_unary(
                '/frr.Northbound/LockConfig',
                request_serializer=frr__northbound__pb2.LockConfigRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.LockConfigResponse.FromString,
                _registered_method=True)
        self.UnlockConfig = channel.unary_unary(
                '/frr.Northbound/UnlockConfig',
                request_serializer=frr__northbound__pb2.UnlockConfigRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.UnlockConfigResponse.FromString,
                _registered_method=True)
        self.Execute = channel.unary_unary(
                '/frr.Northbound/Execute',
                request_serializer=frr__northbound__pb2.ExecuteRequest.SerializeToString,
                response_deserializer=frr__northbound__pb2.ExecuteResponse.FromString,
                _registered_method=True)


class NorthboundServicer(object):
    """Service specification for the FRR northbound interface.
    """

    def GetCapabilities(self, request, context):
        """Retrieve the capabilities supported by the target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Retrieve configuration data, state data or both from the target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCandidate(self, request, context):
        """Create a new candidate configuration and return a reference to it. The
        created candidate is a copy of the running configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCandidate(self, request, context):
        """Delete a candidate configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCandidate(self, request, context):
        """Update a candidate configuration by rebasing the changes on top of the
        latest running configuration. Resolve conflicts automatically by giving
        preference to the changes done in the candidate configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditCandidate(self, request, context):
        """Edit a candidate configuration. All changes are discarded if any error
        happens.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadToCandidate(self, request, context):
        """Load configuration data into a candidate configuration. Both merge and
        replace semantics are supported.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Create a new configuration transaction using a two-phase commit protocol.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransactions(self, request, context):
        """List the metadata of all configuration transactions recorded in the
        transactions database.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransaction(self, request, context):
        """Fetch a configuration (identified by its transaction ID) from the
        transactions database.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LockConfig(self, request, context):
        """Lock the running configuration, preventing other users from changing it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlockConfig(self, request, context):
        """Unlock the running configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Execute(self, request, context):
        """Execute a YANG RPC.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NorthboundServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCapabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCapabilities,
                    request_deserializer=frr__northbound__pb2.GetCapabilitiesRequest.FromString,
                    response_serializer=frr__northbound__pb2.GetCapabilitiesResponse.SerializeToString,
            ),
            'Get': grpc.unary_stream_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=frr__northbound__pb2.GetRequest.FromString,
                    response_serializer=frr__northbound__pb2.GetResponse.SerializeToString,
            ),
            'CreateCandidate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCandidate,
                    request_deserializer=frr__northbound__pb2.CreateCandidateRequest.FromString,
                    response_serializer=frr__northbound__pb2.CreateCandidateResponse.SerializeToString,
            ),
            'DeleteCandidate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCandidate,
                    request_deserializer=frr__northbound__pb2.DeleteCandidateRequest.FromString,
                    response_serializer=frr__northbound__pb2.DeleteCandidateResponse.SerializeToString,
            ),
            'UpdateCandidate': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCandidate,
                    request_deserializer=frr__northbound__pb2.UpdateCandidateRequest.FromString,
                    response_serializer=frr__northbound__pb2.UpdateCandidateResponse.SerializeToString,
            ),
            'EditCandidate': grpc.unary_unary_rpc_method_handler(
                    servicer.EditCandidate,
                    request_deserializer=frr__northbound__pb2.EditCandidateRequest.FromString,
                    response_serializer=frr__northbound__pb2.EditCandidateResponse.SerializeToString,
            ),
            'LoadToCandidate': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadToCandidate,
                    request_deserializer=frr__northbound__pb2.LoadToCandidateRequest.FromString,
                    response_serializer=frr__northbound__pb2.LoadToCandidateResponse.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=frr__northbound__pb2.CommitRequest.FromString,
                    response_serializer=frr__northbound__pb2.CommitResponse.SerializeToString,
            ),
            'ListTransactions': grpc.unary_stream_rpc_method_handler(
                    servicer.ListTransactions,
                    request_deserializer=frr__northbound__pb2.ListTransactionsRequest.FromString,
                    response_serializer=frr__northbound__pb2.ListTransactionsResponse.SerializeToString,
            ),
            'GetTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransaction,
                    request_deserializer=frr__northbound__pb2.GetTransactionRequest.FromString,
                    response_serializer=frr__northbound__pb2.GetTransactionResponse.SerializeToString,
            ),
            'LockConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.LockConfig,
                    request_deserializer=frr__northbound__pb2.LockConfigRequest.FromString,
                    response_serializer=frr__northbound__pb2.LockConfigResponse.SerializeToString,
            ),
            'UnlockConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlockConfig,
                    request_deserializer=frr__northbound__pb2.UnlockConfigRequest.FromString,
                    response_serializer=frr__northbound__pb2.UnlockConfigResponse.SerializeToString,
            ),
            'Execute': grpc.unary_unary_rpc_method_handler(
                    servicer.Execute,
                    request_deserializer=frr__northbound__pb2.ExecuteRequest.FromString,
                    response_serializer=frr__northbound__pb2.ExecuteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'frr.Northbound', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('frr.Northbound', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Northbound(object):
    """Service specification for the FRR northbound interface.
    """

    @staticmethod
    def GetCapabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/GetCapabilities',
            frr__northbound__pb2.GetCapabilitiesRequest.SerializeToString,
            frr__northbound__pb2.GetCapabilitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/frr.Northbound/Get',
            frr__northbound__pb2.GetRequest.SerializeToString,
            frr__northbound__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateCandidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/CreateCandidate',
            frr__northbound__pb2.CreateCandidateRequest.SerializeToString,
            frr__northbound__pb2.CreateCandidateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteCandidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/DeleteCandidate',
            frr__northbound__pb2.DeleteCandidateRequest.SerializeToString,
            frr__northbound__pb2.DeleteCandidateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateCandidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/UpdateCandidate',
            frr__northbound__pb2.UpdateCandidateRequest.SerializeToString,
            frr__northbound__pb2.UpdateCandidateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EditCandidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/EditCandidate',
            frr__northbound__pb2.EditCandidateRequest.SerializeToString,
            frr__northbound__pb2.EditCandidateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LoadToCandidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/LoadToCandidate',
            frr__northbound__pb2.LoadToCandidateRequest.SerializeToString,
            frr__northbound__pb2.LoadToCandidateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Commit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/Commit',
            frr__northbound__pb2.CommitRequest.SerializeToString,
            frr__northbound__pb2.CommitResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListTransactions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/frr.Northbound/ListTransactions',
            frr__northbound__pb2.ListTransactionsRequest.SerializeToString,
            frr__northbound__pb2.ListTransactionsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/GetTransaction',
            frr__northbound__pb2.GetTransactionRequest.SerializeToString,
            frr__northbound__pb2.GetTransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LockConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/LockConfig',
            frr__northbound__pb2.LockConfigRequest.SerializeToString,
            frr__northbound__pb2.LockConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UnlockConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/UnlockConfig',
            frr__northbound__pb2.UnlockConfigRequest.SerializeToString,
            frr__northbound__pb2.UnlockConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/frr.Northbound/Execute',
            frr__northbound__pb2.ExecuteRequest.SerializeToString,
            frr__northbound__pb2.ExecuteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

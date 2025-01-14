import json
import grpc
import frrpy.frr_northbound_pb2
import frrpy.frr_northbound_pb2_grpc


def flat_xpaths(xpaths):
    flat_list = []

    for entry in xpaths:
        print(entry)
        xpath = entry.to_xpath()
        if type(xpath) is list:
            flat_list.extend(xpath)
        else:
            flat_list.append(xpath)

    return flat_list


class FrrConnection:
    "FRR gRPC connection."

    def __init__(self, server='localhost', port=57001):
        self.channel = grpc.insecure_channel(f"{server}:{port}")
        self.stub = frrpy.frr_northbound_pb2_grpc.NorthboundStub(self.channel)

    def configuration(self, xpath):
        "Gets configuration from FRR"
        request = frrpy.frr_northbound_pb2.GetRequest()
        request.path.append(xpath)
        request.type = frrpy.frr_northbound_pb2.GetRequest.CONFIG
        request.encoding = frrpy.frr_northbound_pb2.JSON

        result = ''
        try:
            for r in self.stub.Get(request):
                result += r.data.data
        except grpc.RpcError as error:
            if error.code() == grpc.StatusCode.UNAVAILABLE:
                result = '{}'

        return json.loads(result)

    def commit(self, xpaths, comment='No comment'):
        new_candidate = self.stub.CreateCandidate(
            frrpy.frr_northbound_pb2.CreateCandidateRequest())

        edit_request = frrpy.frr_northbound_pb2.EditCandidateRequest()
        edit_request.candidate_id = new_candidate.candidate_id
        print(xpaths)
        xpaths = flat_xpaths(xpaths)
        for xpath in xpaths:
            edit_request.update.append(xpath)
        self.stub.EditCandidate(edit_request)

        commit_request = frrpy.frr_northbound_pb2.CommitRequest()
        commit_request.candidate_id = new_candidate.candidate_id
        commit_request.phase = frrpy.frr_northbound_pb2.CommitRequest.ALL
        commit_request.comment = comment
        try:
            self.stub.Commit(commit_request)
        except grpc.RpcError as error:
            if error.code() == grpc.StatusCode.ABORTED:
                print(f"gRPC commit aborted: {error.details()}")

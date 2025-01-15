"""
frrpy.connection
================

This module provides a simplified interface for interacting with FRR (Free Range Routing) using gRPC.

Classes:
--------
- FrrConnection: Manages the gRPC connection to the FRR server and provides methods to get configuration and commit changes.

Functions:
----------
- flat_xpaths(xpaths): Flattens a list of xpaths.

Class FrrConnection:
---------------------
- __init__(self, server='localhost', port=57001): Initializes the gRPC connection to the FRR server.
- configuration(self, xpath): Retrieves the configuration from FRR for a given xpath.
- commit(self, xpaths, comment='No comment'): Commits changes to the FRR configuration.

Function flat_xpaths:
---------------------
- flat_xpaths(xpaths): Flattens a list of xpaths into a single list.

"""

import json
import grpc
import frrpy.frr_northbound_pb2
import frrpy.frr_northbound_pb2_grpc


"""
frrpy.connection
================

This module provides a simplified interface for interacting with FRR (Free Range Routing) using gRPC.

Classes:
--------
- FrrConnection: Manages the gRPC connection to the FRR server and provides methods to get configuration and commit changes.

Functions:
----------
- flat_xpaths(xpaths): Flattens a list of xpaths.

Class FrrConnection:
---------------------
- __init__(self, server='localhost', port=57001): Initializes the gRPC connection to the FRR server.
- configuration(self, xpath): Retrieves the configuration from FRR for a given xpath.
- commit(self, xpaths, comment='No comment'): Commits changes to the FRR configuration.

Function flat_xpaths:
---------------------
- flat_xpaths(xpaths): Flattens a list of xpaths into a single list.

"""
def flat_xpaths(xpaths):
    flat_list = []

    for entry in xpaths:
        print(entry)
        xpath = entry.to_xpath()

        flat_list.extend(xpath) if type(xpath) is list else flat_list.append(xpath)

    return flat_list


class FrrConnection:
    """
    Manages the gRPC connection to the FRR server and provides methods to get configuration and commit changes.

    Methods:
    --------
    __init__(self, server='localhost', port=57001):
        Initializes the gRPC connection to the FRR server.

    configuration(self, xpath):
        Retrieves the configuration from FRR for a given xpath.

    commit(self, xpaths, comment='No comment'):
        Commits changes to the FRR configuration.
    """

    def __init__(self, server='localhost', port=57001):
        """
        Initializes the gRPC connection to the FRR server.

        Parameters:
        -----------
        server : str, optional
            The server address (default is 'localhost').
        port : int, optional
            The server port (default is 57001).
        """

        self.channel = grpc.insecure_channel(f"{server}:{port}")
        self.stub = frrpy.frr_northbound_pb2_grpc.NorthboundStub(self.channel)

    def configuration(self, xpath):
        """
        Retrieves the configuration from FRR for a given xpath.

        Parameters:
        -----------
        xpath : str
            The xpath for which the configuration is to be retrieved.

        Returns:
        --------
        dict
            The configuration data in JSON format.
        """
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
        """
        Commits changes to the FRR configuration.

        Parameters:
        -----------
        xpaths : list
            A list of xpaths to be committed.
        comment : str, optional
            A comment for the commit (default is 'No comment').

        Returns:
        --------
        None
        """
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

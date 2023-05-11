import grpc
import filelisting_pb2
import filelisting_pb2_grpc

def list_files():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = filelisting_pb2_grpc.FileListingServiceStub(channel)
        response = stub.ListFiles(filelisting_pb2.Empty())
        files = [{'name': f.name, 'size': f.size} for f in response.files]
        return files
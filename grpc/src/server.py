from concurrent import futures
import grpc
import os

import filelisting_pb2
import filelisting_pb2_grpc

class FileListingServicer(filelisting_pb2_grpc.FileListingServiceServicer):
    def ListFiles(self, request, context):
        file_list = []
        for filename in os.listdir("."):
            if os.path.isfile(filename):
                file_size = os.path.getsize(filename)
                file_list.append(filelisting_pb2.File(name=filename, size=file_size))
        return filelisting_pb2.FileList(files=file_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    filelisting_pb2_grpc.add_FileListingServiceServicer_to_server(FileListingServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

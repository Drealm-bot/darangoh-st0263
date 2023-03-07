from concurrent import futures
import grpc
import os

import filelisting_pb2
import filelisting_pb2_grpc

dir = "/home/ubuntu/darangoh-st0263/dir"
#current_dir = os.path.abspath(os.curdir)
#dir_path = os.path.abspath(os.path.join(current_dir, "dir"))

class FileListingServicer(filelisting_pb2_grpc.FileListingServiceServicer):
    def ListFiles(self, request, context):
        file_list = []
        for filename in os.listdir(dir):
            files = dir+'/'+filename
            if os.path.isfile(files):
                file_size = os.path.getsize(files)
                file_list.append(filelisting_pb2.File(name=filename, size=file_size))
        return filelisting_pb2.FileList(files=file_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    filelisting_pb2_grpc.add_FileListingServiceServicer_to_server(FileListingServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Esperando por mensajes...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

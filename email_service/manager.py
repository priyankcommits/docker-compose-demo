import email_pb2_grpc
import email_pb2


class EmailManager(email_pb2_grpc.EmailServicer):
    def SendEmail(self, request, context):
        print("Got email request")
        return email_pb2.OperationStatus(
            status="Email Sent"
        )

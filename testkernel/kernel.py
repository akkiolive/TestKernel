from ipykernel.kernelbase import Kernel

class CKernel(Kernel):
    implementation = 'testkernel'
    implementation_version = "0.1"
    banner = None
    
    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=True):
        self.send_response(self.iopub_socket, 'stream', {'name': 'stdout', 'text': f'Test output for {code}'})
        return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [], 'user_expressions': {}}
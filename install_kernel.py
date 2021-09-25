import json
import os
import sys

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory


kernel_name = "testkernel" # this is also used for package name in kernel_json
display_name = "test kernel"
language_name = "test language"

kernel_json = {
    "argv": [
        "python3",
        "-m",
        kernel_name,
        "-f",
        "{connection_file}"
    ],
    "display_name": display_name,
    "language": language_name
}


def install_my_kernel_spec(kernel_name, user=False, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        # TODO: Copy resources once they're specified

        print('Installing IPython kernel spec')
        KernelSpecManager().install_kernel_spec(td, kernel_name, user=user, prefix=prefix)
        
install_my_kernel_spec(kernel_name=kernel_name)
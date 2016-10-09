"""
Utilities for starting Py4J servers.
"""
import atexit
import os
import glob
from subprocess import Popen, PIPE
from py4j.java_gateway import JavaGateway, GatewayClient, java_import


MODULE_DIR = os.path.dirname(__file__)
LIB_DIR = os.path.join(MODULE_DIR, 'lib')
JARS = ':'.join(glob.glob(LIB_DIR + '/*.jar'))
CLASSPATH = MODULE_DIR + ':' + LIB_DIR + ':' + JARS


def launch_py4j_server():
    """
    Launch a py4j server process on an ephemeral port.  Returns a Py4J gateway
    connected to the server.  The server is configured to shut down when the
    Python process exits.  The classpath is set to the lib folder in this
    project, giving the server access to the Java libraries bundled with the
    project.

    >>> gateway = launch_py4j_server()
    >>> gateway.jvm #doctest +ELLIPSIS
    <py4j.java_gateway.JVMView object at 0x...>
    """
    # Launch the server on an ephemeral in a subprocess.
    _pid = Popen(["java", "-classpath", CLASSPATH, "Py4JServer", "0"],
        stdout=PIPE, stdin=PIPE)

    # Determine which ephemeral port the server started on.
    _port = int(_pid.stdout.readline())

    # Configure the subprocess to be killed when the program exits.
    atexit.register(_pid.kill)

    # Setup the gateway.
    gateway = JavaGateway(GatewayClient(port=_port))
    return gateway

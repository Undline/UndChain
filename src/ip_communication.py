import socket
import asyncio
import multiprocessing

from abstract_communication import AbstractCommunication

class IPCommunication(AbstractCommunication):
    # Keep track of our active connections for debug purpose
    active_connections = 0

    
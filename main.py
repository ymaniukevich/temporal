import asyncio
import os 

from temporalio import activity
from temporalio.worker import Worker
from temporalio.client import Client
from temporalio.service import TLSConfig

from activities import say_hello
from workflows import SayHello


def setup_tls_config() -> TLSConfig:
    """Helper func to build TLSConfig struct."""
    with open("tls/client.crt", "rb") as f:
        client_cert = f.read()
    with open("tls/client.key", "rb") as f:
        client_private_key = f.read()
    with open("tls/ca.crt", "rb") as f:
        server_root_ca_cert = f.read()
    return TLSConfig(
        client_cert=client_cert,
        client_private_key=client_private_key,
        server_root_ca_cert=server_root_ca_cert,
        domain = "staging.goconsensus.com"
    )


async def main():

    client = await Client.connect("localhost:51282", namespace="mps", tls = setup_tls_config())
    print(client)
    result = await client.execute_workflow(
        SayHello.run, "Temporal", id="hello-world-1", task_queue="hello-task-queue"
    )


if __name__ == "__main__":
    asyncio.run(main())

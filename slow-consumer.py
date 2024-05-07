import asyncio
import nats
from time import sleep

async def run():
    # Connect to NATS server
    nc = await nats.connect("nats://nats:4222")

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print(f"Received a message on '{subject} {reply}': {data}")
        sleep(0.0006)  # Using sleep for simplicity, though asyncio.sleep is preferred in async code

    # Subscribe to a subject with the above message handler
    await nc.subscribe("updates", cb=message_handler)

    # Wait indefinitely until the script is manually stopped or an exit condition is triggered
    stop_event = asyncio.Event()
    await stop_event.wait()

if __name__ == '__main__':
    print("Starting slow consumer")
    asyncio.run(run())
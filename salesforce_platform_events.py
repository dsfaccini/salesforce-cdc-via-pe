import asyncio
from aiosfstream import SalesforceStreamingClient

from dotenv import dotenv_values
# https://medium.com/tech-force/subscribe-to-salesforce-platform-events-with-python-2a3acbe9743c
# https://github.com/robertmrk/aiocometd/pull/20

config = dotenv_values(".env")
consumer_key = config["consumerkey"]
consumer_secret = config["consumersecret"]
username = config["username"]
password = config["password"]
security_token = config["security_token"]

channel_replay_id = {
    "HR_Shipping_Address_PE__e": -1,
}

async def subscribeToSalesforce():
    async with SalesforceStreamingClient(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            username=username,
            password=password+security_token,
            sandbox=True,
    ) as client:
        
        for channel, replayid in channel_replay_id.items():
            await client.subscribe(f"/event/{channel}")
        
        # listen for incoming messages
        async for message in client:
            topic = message["channel"]
            data = message["data"]
            print(f"{topic}: {data}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribeToSalesforce())
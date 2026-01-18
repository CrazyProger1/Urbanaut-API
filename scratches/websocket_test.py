#!/usr/bin/env python
"""
WebSocket script for AsyncUserConsumer with token authentication via WebsocketQueryAuthMiddleware.
"""
import asyncio
import json
import websockets
from datetime import datetime


async def test_websocket():
    """Connect to AsyncUserConsumer with token authentication."""

    # WebSocket server URL
    ws_url = "ws://localhost:8001/ws/"

    # Token from the provided JWT
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU5ZDJjYjJlLTMwYmQtNDAzZi04MDRhLTZlZjdmZmU3N2I2NCIsImV4cCI6MTc2ODczNTcyMywiaWF0IjoxNzY4NzMyMTIzfQ.e9pS6xSb9jAHgoOsWkxGt7ugv1Jq-Jv1cDpqYD4BvKw"

    # Construct WebSocket URL with token as query parameter
    ws_full_url = f"{ws_url}?{token}"

    print(f"[{datetime.now()}] Connecting to: {ws_url}")
    print(f"[{datetime.now()}] Token: {token[:50]}...")

    try:
        # Pass origin header that matches ALLOWED_HOSTS
        async with websockets.connect(ws_full_url, origin="http://localhost") as websocket:

            # Listen for messages forever
            print(f"[{datetime.now()}] ✓ Connected and listening for messages...")
            while True:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=2)
                    print(f"[{datetime.now()}] ← Received: {message}")
                except asyncio.TimeoutError:
                    print(f"[{datetime.now()}] (no messages for 2s)")

    except asyncio.TimeoutError:
        print(f"[{datetime.now()}] ✗ Timeout waiting for message")
    except ConnectionRefusedError:
        print(f"[{datetime.now()}] ✗ Connection refused - is the server running?")
    except Exception as e:
        print(f"[{datetime.now()}] ✗ Error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    asyncio.run(test_websocket())
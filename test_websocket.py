#!/usr/bin/env python
"""
WebSocket test script for AsyncUserConsumer with token authentication.
"""
import json
import time
import websocket


def on_message(ws, message):
    """Handle incoming messages."""
    print(f"Received: {message}")
    try:
        data = json.loads(message)
        print(f"Parsed JSON: {data}")
    except json.JSONDecodeError:
        print("Failed to parse as JSON")


def on_error(ws, error):
    """Handle errors."""
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    """Handle connection close."""
    print(f"Connection closed: {close_status_code} - {close_msg}")


def on_open(ws):
    """Handle connection open."""
    print("Connection opened")

    # Send a status check message
    status_check_msg = {
        "type": "status_check"
    }
    ws.send(json.dumps(status_check_msg))
    print(f"Sent: {status_check_msg}")

    # Send a notification
    time.sleep(1)
    notification_msg = {
        "type": "send_notification",
        "message": "Test notification from Python script"
    }
    ws.send(json.dumps(notification_msg))
    print(f"Sent: {notification_msg}")


def main():
    # WebSocket server URL
    ws_url = "ws://localhost:8000/ws/"

    # Token from the provided JWT
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImU5ZDJjYjJlLTMwYmQtNDAzZi04MDRhLTZlZjdmZmU3N2I2NCIsImV4cCI6MTc2ODczNTcyMywiaWF0IjoxNzY4NzMyMTIzfQ.e9pS6xSb9jAHgoOsWkxGt7ugv1Jq-Jv1cDpqYD4BvKw"

    # Construct WebSocket URL with token as query parameter
    ws_full_url = f"{ws_url}?{token}"

    print(f"Connecting to: {ws_url}")
    print(f"Token: {token[:50]}...")

    # Create WebSocket connection
    ws = websocket.WebSocketApp(
        ws_full_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    # Run the connection (blocks until connection closes)
    ws.run_forever()


if __name__ == "__main__":
    main()
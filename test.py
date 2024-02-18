import webview
import json
import time

def send_data_to_html():
    # Data to send to HTML
    data = {
        'message': 'Hello from Python!'
    }

    # Convert data to JSON string
    data_str = json.dumps(data)

    # Execute JavaScript code to update HTML with data
    webview.windows[0].evaluate_js(f"updateDataFromPython({data_str})")

if __name__ == '__main__':
    # Create a webview window with an HTML file
    webview.create_window('Data Transfer', './ui/index.html')

    # Call function to send data to HTML
    send_data_to_html()

    # Start the PyWebview event loop
    webview.start()

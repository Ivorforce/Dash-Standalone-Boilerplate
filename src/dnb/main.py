import os
import time
from multiprocessing import Process, Condition

import setproctitle
import webview
from dnb.domino import terminate_when_process_dies

from dnb.server import start_dash


def start():
    port = int(os.getenv("PORT", "8050"))
    host = os.getenv("HOST", "127.0.0.1")

    server_is_started = Condition()

    # Set the process title.
    setproctitle.setproctitle('dnb-webview')

    # Spawn the dash process.
    p = Process(target=start_dash, args=(host, port, server_is_started,))
    p.start()
    # If the dash process dies, follow along.
    terminate_when_process_dies(p)

    # Wait until dash process is ready.
    with server_is_started:
        server_is_started.wait()
    # FIXME this should not be needed, if server_is_started was triggered after app runs.
    #  idk if that is possible.
    time.sleep(0.2)

    # Create the webview.
    webview.create_window('Dash', f'http://{host}:{port}')
    webview.start()

    # Unreachable.
    print("Web view stopped? Killing backend.")
    p.terminate()
    exit(1)


if __name__ == '__main__':
    start()

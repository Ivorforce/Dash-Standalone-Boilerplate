import multiprocessing
import os
import signal
import threading


def join_process_and_terminate(process: multiprocessing.process.BaseProcess):
    """
    Whenever the given process exits, send SIGTERM to self.
    This function is synchronous; for async usage see the other two.
    """
    process.join()
    # sys.exit() raises, killing only the current thread
    # os._exit() is private, and also doesn't allow the thread to gracefully exit
    os.kill(os.getpid(), signal.SIGTERM)


def terminate_when_process_dies(process: multiprocessing.process.BaseProcess):
    """
    Whenever the given process exits, send SIGTERM to self.
    This function is asynchronous.
    """
    threading.Thread(target=join_process_and_terminate, args=(process,)).start()


def terminate_when_parent_process_dies():
    """
    Whenever the parent process exits, send SIGTERM to self.
    This function is asynchronous.
    """
    terminate_when_process_dies(multiprocessing.parent_process())

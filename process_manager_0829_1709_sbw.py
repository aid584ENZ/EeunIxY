# 代码生成时间: 2025-08-29 17:09:38
import psutil
import signal

# ProcessManager class to manage processes using psutil
class ProcessManager:
    """
    Manages system processes.

    Attributes:
        None

    Methods:
        list_processes: Lists all running processes.
        terminate_process: Terminates a process by its PID.
    """

    def list_processes(self):
        """
        Lists all running processes.

        Returns:
            list: A list of tuples containing process info.
        """
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'status']):
                processes.append(proc.info)
            return processes
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def terminate_process(self, pid):
        """
        Terminates a process by its PID.

        Args:
            pid (int): The process ID to terminate.

        Returns:
            bool: True if the process was terminated successfully, False otherwise.
        """
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()
            return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Failed to terminate process {pid}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return False

# Example usage
if __name__ == '__main__':
    manager = ProcessManager()
    processes = manager.list_processes()
    for proc in processes:
        print(proc)

    # Replace <pid> with the actual process ID you want to terminate
    # pid = <pid>
    # success = manager.terminate_process(pid)
    # if success:
    #     print(f"Process {pid} terminated successfully.")
    # else:
    #     print(f"Failed to terminate process {pid}.")
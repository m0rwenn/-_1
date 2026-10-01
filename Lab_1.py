import platform
import socket
import os
import sys
import json
from datetime import datetime

def get_system_info():
    print("Start..")
    
    try:
        system_info = {
            'os_name': platform.system(),
            'os_release': platform.release(),
            'os_version': platform.version(),
        }
    except Exception as e:
        system_info = {'error': f"It was not possible to gather the information.: {e}"}

    try:
        hardware_info = {
            'architecture': platform.machine(),
            'processor': platform.processor(),
            'cpu_cores': os.cpu_count(),
        }
    except Exception as e:
        hardware_info = {'error': f"It was not possible to gather the information.: {e}"}

    try:
        hostname = socket.gethostname()
        try:
            local_ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            local_ip = "127.0.0.1 (There is no active network connection.)"

        network_info = {
            'hostname': hostname,
            'local_ip': local_ip,
        }
    except Exception as e:
        network_info = {'error': f"It was not possible to gather the information.: {e}"}

    try:
        try:
            login_name = os.getlogin()
        except OSError:
            login_name = "It was not possible to determine"
            
        home_dir_key = 'HOME' if platform.system() != 'Windows' else 'USERPROFILE'
        home_directory = os.environ.get(home_dir_key, "not found")

        environment_info = {
            'current_user': login_name,
            'home_directory': home_directory,
            'python_version': sys.version,
            'python_executable': sys.executable,
        }
    except Exception as e:
        environment_info = {'error': f"It was not possible to gather the information.: {e}"}
    
    all_info = {
        'report_generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'system': system_info,
        'hardware': hardware_info,
        'network': network_info,
        'environment': environment_info,
    }
    
    print("Done")
    return all_info


def save_to_json(data, filename="system_info.json"):
    print(f"The data is being save... '{filename}'...")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"The file '{filename}' has been successfully created.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    collected_data = get_system_info()
    save_to_json(collected_data)
    
    print("Complete")
    

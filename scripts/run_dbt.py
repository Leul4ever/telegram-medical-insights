import os
import subprocess
from dotenv import load_dotenv

def run_dbt(command):
    # Load .env from root
    load_dotenv(os.path.join(os.getcwd(), '.env'))
    
    dbt_exe = r'C:\Users\dell\AppData\Roaming\Python\Python313\Scripts\dbt.exe'
    
    # Run from medical_warehouse directory
    cwd = os.path.join(os.getcwd(), 'medical_warehouse')
    
    full_command = f"{dbt_exe} {command}"
    print(f"Running: {full_command}")
    
    result = subprocess.run(full_command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"dbt command failed with return code {result.returncode}")
    else:
        print("dbt command finished successfully")

if __name__ == "__main__":
    import sys
    cmd = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "run"
    run_dbt(cmd)

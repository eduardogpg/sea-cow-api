import subprocess

def create_invoice():
    node = 1
    response = {
        'id': 0,
        'wallet': 'Wallet',
        'balance': 0
    }
    
    try:
        process = subprocess.run(
            [
                f'cd /home/eduardo/projects/sea-cow-api && ./wallets.sh {node}'
            ],
            shell=True,
            capture_output=True
        )
        stdout_as_str = process.stdout.decode("utf-8").strip()
        
        # Save wallet in table
        response['wallet'] = stdout_as_str
        
    except Exception as err:
        pass
    
    finally:
        return response
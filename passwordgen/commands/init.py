
from pathlib import Path
import os
from passwordgen.infra.clock import curr_date
from passwordgen.infra.account_store import  save

#---json read/write path---
BASE_DIR = Path(__file__).resolve().parent
vault_file_path = BASE_DIR / "vault.json.enc"
meta_file_path = BASE_DIR / "vault.meta.json"
policy_file_path = BASE_DIR / "policy.json"


def init_vault()->None:
    '''
    create vault version and hash metadata
    create default password policy parameters.
    create new vault and encrypt
    save
    '''
    vault_meta()

    
def vault_meta():
    
    count = 0.1
    vault_version = count
    kdf = key_params()
    date = curr_date()
    default_params = {
        "vault_version": vault_version,
        "key_params": kdf,
        "created_at": date
    }
    save(default_params)



def key_params()-> dict:
   
    salt = os.urandom(16)
    hash_params = {
        "algorithm": "argon2id",
        "salt": salt,
        "time_cost": 3,
        "memory_cost": 65536,
        "parallelism": 2,
        "hash_length": 32,
    }

    return hash_params
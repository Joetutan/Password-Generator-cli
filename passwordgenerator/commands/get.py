
def get(account:str)->None:
    '''
    validate account is in vault
    get master password if not unlocked
    derive master_key
    derive account_key
    return formated password
    '''
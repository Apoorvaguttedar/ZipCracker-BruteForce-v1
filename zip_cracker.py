# zip_cracker.py
import zipfile

def crack_zip(zip_path, wordlist_path, output_path="uploads/"):
    with zipfile.ZipFile(zip_path) as zf:
        with open(wordlist_path, 'r') as f:
            for attempt, line in enumerate(f, 1):
                password = line.strip()
                try:
                    zf.extractall(path=output_path, pwd=bytes(password, 'utf-8'))
                    return True, password, attempt
                except:
                    continue
    return False, None, attempt

import settings
level = settings.get_setting("logging_level")

def log(type: str, message: str):
    with open("log.txt","a") as f:
        f.write(f"{type} - {message}\n")
    print(f"{type} - {message}")
    
def save_info(info: str):
    with open("log.txt","a") as f:
        f.write(f"{info}\n")
    print(info)
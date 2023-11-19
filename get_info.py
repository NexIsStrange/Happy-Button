data = {"application_version":2,
         "theme_version":1,
         "save_version":1,
         "publish_type":"development"}
    
def application_ver():
    return float(data["application_version"])
def theme_ver():
    return data["theme_version"]
def save_ver():
    return data["save_version"]
def release_type():
    return data["publish_type"]
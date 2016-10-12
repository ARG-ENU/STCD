import ConfigParser as cp
import datetime as dt
import getpass as gp
import optparse as opt
import os
import uuid as u

config_loc = "defaults.cfg"

def init():
    config = cp.ConfigParser()
    config_location = config_loc
    config.read(config_location)
    global user_name 
    user_name = config.get("user", "name")
    global user_email 
    user_email = config.get("user", "email")
    global dataset_path
    dataset_path = config.get("system", "path")
    

def new_resource(url):
    guid = u.uuid4()
    folder_name = str(guid)
    path = dataset_path+folder_name
    now = dt.datetime.now().isoformat()

    guid_string = '"guid":"'+ str(guid) +'"'
    now_string = '"timestamp":"'+ now +'"'
    url_string = '"url":"'+ url +'"'
    user_string = '"name":"'+ user_name +'"'
    email_string = '"email":"'+ user_email +'"'

    data = [guid_string, now_string, url_string, user_string, email_string]

    print path

    if not os.path.exists(path):
        os.makedirs(path)
    with open( path+"/metadata.txt", "wb") as outfile:
        outfile.write("\n".join(data))

def validate_url(url):
    if (url[:7] != 'http://'):
        url = 'http://'+url
    return url  

if __name__ == "__main__":

    parser = opt.OptionParser()
    (options, args) = parser.parse_args()
    if len(args) == 1:
        url = args[0]
        url = url.lower()
        url = validate_url(url)
        init()
        new_resource(url)
    
    elif len(args) == 2:
        
        url = args[0]
        url = url.lower()
        url = validate_url(url)

        new_config = args[1]
        config_loc = new_config

        init()
        new_resource(url)
    else:
        print "Usage: resources.py url config_file"
    

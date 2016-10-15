import ConfigParser as cp
import datetime as dt
import getpass as gp
import optparse as opt
import os
import uuid as u

def init(config_file):
    print config_file
    config = cp.ConfigParser()
    config_location = config_file
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

def main():
    parser = opt.OptionParser(description="STCD Metadata Tool",
        prog="resources.py",
        version="0.1",
        usage="python %prog [config] URL")
    parser.add_option('--config', '-c', default="etc/config/defaults.cfg")
    (options, args) = parser.parse_args()

    init(options.config)
 
    if(len(args)==1):
        new_resource(args[0])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()    


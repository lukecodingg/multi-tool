@echo off
setlocal enabledelayedexpansion

for /F "tokens=2 delims=:" %%a in ('netsh wlan show profiles') do (
    set "ssid=%%a"
    set "ssid=!ssid:~1!"  REM trims the leading space

    set "wifi_pwd="

    for /F "tokens=2 delims=:" %%F in ('netsh wlan show profile name^="!ssid!" key^=clear ^| findstr "Key Content"') do (
        set "wifi_pwd=%%F"
        set "wifi_pwd=!wifi_pwd:~1!"  REM trims leading space
    )

    echo SSID: !ssid! ^| Password: !wifi_pwd!
)
pause

@echo off
:loop
python -u scripts/market_scanner.py
ping -n 61 127.0.0.1 > nul
goto loop
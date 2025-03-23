#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import time
import os

# Attempt to import the googlesearch module
try:
    from googlesearch import search
except ImportError:
    print("\033[91m[ERROR] Missing dependency: googlesearch-python\033[0m")
    print("\033[93m[INFO] Install it using: pip install googlesearch-python\033[0m")
    sys.exit(1)

# Check for Python version
if sys.version_info[0] < 3:
    print("\n\033[91m[ERROR] This script requires Python 3.x\033[0m\n")
    sys.exit(1)

# ANSI color codes for styling output
class Colors:
    RED = "\033[91m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

# Default output filename
log_file = "dorks_output.txt"

def logger(data):
    """Logs data to a file."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(data + "\n")

def dorks():
    """Main function for handling Google Dorking."""
    global log_file
    try:
        dork = input(f"{Colors.BLUE}\n[+] Enter The Dork Search Query: {Colors.RESET}")
        
        user_choice = input(f"{Colors.BLUE}[+] Enter Total Number of Results You Want (or type 'all' to fetch everything): {Colors.RESET}").strip().lower()
        
        if user_choice == "all":
            total_results = float("inf")
        else:
            try:
                total_results = int(user_choice)
                if total_results <= 0:
                    raise ValueError("Number must be greater than zero.")
            except ValueError:
                print(f"{Colors.RED}[ERROR] Invalid number entered! Please enter a positive integer or 'all'.{Colors.RESET}")
                return
        
        save_output = input(f"{Colors.BLUE}\n[+] Do You Want to Save the Output? (Y/N): {Colors.RESET}").strip().lower()
        if save_output == "y":
            log_file = input(f"{Colors.BLUE}[+] Enter Output Filename (default: dorks_output.txt): {Colors.RESET}").strip()
            if not log_file:
                log_file = "dorks_output.txt"
            if not log_file.endswith(".txt"):
                log_file += ".txt"
            
            file_path = input(f"{Colors.BLUE}[+] Enter the full path where you want to save the file (default: current directory): {Colors.RESET}").strip()
            if file_path:
                if not os.path.exists(file_path):
                    print(f"{Colors.RED}[ERROR] The provided path does not exist. Saving in the current directory instead.{Colors.RESET}")
                    file_path = os.getcwd()
                log_file = os.path.join(file_path, log_file)
            else:
                log_file = os.path.join(os.getcwd(), log_file)

        print(f"\n{Colors.GREEN}[INFO] Searching... Please wait...{Colors.RESET}\n")
        
        fetched = 0
        
        for result in search(dork):
            if fetched >= total_results:
                break
            print(f"{Colors.YELLOW}[+] {Colors.RESET}{result}")
            
            if save_output == "y":
                logger(result)
            
            fetched += 1
        
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] User Interruption Detected! Exiting...{Colors.RESET}\n")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}[ERROR] {str(e)}{Colors.RESET}")
    
    print(f"{Colors.GREEN}\n[✔] Automation Done..{Colors.RESET}")
    sys.exit()

if __name__ == "__main__":
    dorks()

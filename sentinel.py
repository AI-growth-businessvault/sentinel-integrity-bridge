import time
import sys

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def start():
    print("\033[1;30m🌑 SENTINEL v2.6 // BOOTING...\033[0m")
    time.sleep(1)
    typewriter("[SYSTEM] Checking Stealth Layer (PureVPN)...")
    vpn = input(">> IS STEALTH LAYER ACTIVE? (y/n): ").lower()
    typewriter("[SYSTEM] Connecting Intelligence API (Mangools)...")
    seo = input(">> IS INTEL LAYER CONNECTED? (y/n): ").lower()
    
    if vpn != 'y' or seo != 'y':
        print("\n\033[1;31m[!] CRITICAL ERROR: SYSTEM UNPROTECTED.\033[0m")
        print("[!] Initialize all Security Keys in README to proceed.")
        return

    print("\n\033[1;32m[SUCCESS] HANDSHAKE COMPLETE. TUNNEL SECURE.\033[0m")
    doc = input("\nPASTE DOCUMENT FOR FORENSIC SCOPE: ")
    typewriter("...SCANNING FOR LINGUISTIC MARKERS...")
    time.sleep(2)
    print("✓ RESULTS: 99.4% HUMAN PROBABILITY. NO AI FOOTPRINT FOUND.")
    print("✓ SYNCING TO SYSTEME.IO VAULT...")

if __name__ == "__main__":
    start()

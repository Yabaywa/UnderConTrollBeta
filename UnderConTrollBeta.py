import os
import re
import sys
import uuid
import time
import socket
import threading
import subprocess

logo = """
\033[38;2;128;0;0m\t   ██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗  ██████╗███╗   ██╗████████╗██████╗  ██████╗ ██╗     ██╗
\033[38;2;128;0;0m\t   ██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     ██║
\033[38;2;128;0;0m\t   ██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝██║     ██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     ██║
\033[38;2;128;0;0m\t   ██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗██║     ██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ██║
\033[38;2;128;0;0m\t   ╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║╚██████╗██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████╗
\033[38;2;128;0;0m\t    ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
\033[0m"""

def internet_verbindung_testen(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return "\033[38;2;0;255;0m\t\t\t\t\tInternetverbindung aktiv"
    except socket.error:
        return "\033[38;2;128;0;0m\t\t\t\t\tKeine Internetverbindung erkannt"

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))

def loading_animation():
    bar_length = 40
    for i in range(101):
        filled = int(bar_length * i / 100)
        bar = '█' * filled + '-' * (bar_length - filled)
        sys.stdout.write(f"\r\033[38;2;0;255;0m{' ' * 30}Loading: [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n" + " " * 45 + "\033[38;2;128;0;0mDone!\033[0m")

loading_animation()

aktuelles_status_info = {}

def system_infos_aktualisieren():
    while True:
        aktuelles_status_info["internet"] = internet_verbindung_testen()
        aktuelles_status_info["ip"] = get_ip_address()
        aktuelles_status_info["mac"] = get_mac_address()
        time.sleep(0.05)

def show_main_menu():
    threading.Thread(target=system_infos_aktualisieren, daemon=True).start()

    while True:
        os.system("title UnderConTroll")
        os.system("cls")
        print(logo)
        print("\033[38;2;0;255;0m\t\t\t\t\tInternet Informationen")
        print()
        print(internet_verbindung_testen())
        print("\t\t\t\t\tIP-Adresse:", get_ip_address())
        print("\t\t\t\t\tMAC-Adresse:", get_mac_address())
        print()
        print("\t\t\t\t\tOptionen die dir zur Auswahl stehen")
        print()
        print("\033[38;2;0;255;0m\t\t\t\t\t[0 ] Drück 0 um die UI zu verlassen")
        print("\033[38;2;0;255;0m\t\t\t\t\t[1 ] Netzwerk und System-Tools")
        print("\033[38;2;0;255;0m\t\t\t\t\t[2 ] Security & Hacking-Tools")
        print("\033[38;2;0;255;0m\t\t\t\t\t[3 ] System-Manipulation & Automatisierung")
        print("\033[38;2;0;255;0m\t\t\t\t\t[4 ] Verschluesselung & Dateimanagement")
        print()
        print("\033[38;2;0;255;0m\t\t\t\t\t[5] Zeige mir alle Optionen")
        print()

        x = input("\033[38;2;0;255;0m\t\t\t\t\tOption: ")

        if x == "1":
            show_network_menu()
        elif x == "2":
            show_security_menu()
        elif x == "3":
            show_system_automation_menu()
        elif x == "4":
            show_encryption_menu()
        elif x == "5":
            show_everything_menu()
        elif x == "0":
            exit()
        else:
            print("Ungültige Eingabe!")
            time.sleep(0.05)

def show_network_menu():
    """ Zeigt das Netzwerk- und System-Tools-Menü an """
    while True:
        os.system("cls")
        print("\n=== Netzwerk & System-Tools ===\n")
        print("Funktion\t\t\t\t\tBeschreibung")
        print("-" * 80)
        print("\033[38;2;128;0;128m[0 ] Zurück zum Hauptmenü")
        print()
        print("\033[38;2;145;0;130m[1 ] Port Scanner\t\t\t\tScannt ein Zielsystem nach offenen Ports.")
        print("\033[38;2;162;0;133m[2 ] Netzwerk-Scanner\t\t\t\tZeigt alle Geräte im aktuellen Netzwerk an.")
        print("\033[38;2;179;0;136m[3 ] IP-Geolocation\t\t\t\tBestimmt die IP-Adresse und deren Position.")
        print("\033[38;2;196;0;139m[4 ] VPN-Status Check\t\t\t\tPrüft, ob ein VPN aktiv ist.")
        print("\033[38;2;213;0;141m[5 ] DNS Resolver\t\t\t\tWandelt eine Domain in eine IP-Adresse um.")
        print("\033[38;2;230;0;144m[6 ] WLAN Deauth Detection\t\t\tErkennt Deauth-Pakete im WLAN-Netzwerk.")
        print("\033[38;2;240;26;157m[7 ] Firewall-Status Check\t\t\tÜberprüft den Status der System-Firewall.")
        print("\033[38;2;245;51;170m[8 ] Netzwerkverkehr-Analyse\t\t\tAnalysiert den eingehenden und ausgehenden Netzwerkverkehr.")
        print("\033[38;2;250;77;182m[9 ] Public IP Checker\t\t\t\tErmittelt die externe IP-Adresse des Geräts.")
        print("\033[38;2;253;102;194m[10] Traceroute-Tool\t\t\t\tZeigt die Route von Paketen zum Zielserver an.")
        print("\033[38;2;254;128;205m[11] Netzwerk-Speedtest\t\t\t\tMisst die aktuelle Internetgeschwindigkeit.")
        print("\033[38;2;255;153;216m[12] Netzwerk-Graph generieren\t\t\tVisualisiert Netzwerke mit einem Diagramm.")
        print("\033[38;2;255;179;226m[13] Ping-Tester\t\t\t\t\tTestet die Erreichbarkeit eines Hosts.")
        print("\033[38;2;255;204;237m[14] Bandbreiten-Monitor\t\t\t\tÜberwacht den Internetverbrauch in Echtzeit.")
        print("\033[38;2;255;255;255m[15] DHCP-Sniffer\t\t\t\tErkennt DHCP-Server im Netzwerk.")

        choice = input("\033[38;2;255;255;255m\nOption: ")

        if choice == "0":
            return  # Zurück zum Hauptmenü
        else:
            print("Option wird noch entwickelt...")

def show_security_menu():
    """ Zeigt das Security & Hacking-Tools-Menü an """
    while True:
        os.system("cls")
        print("\n\033[38;2;128;0;128m=== Security & Hacking-Tools ===\033[0m\n")
        print("Funktion\t\t\t\t\tBeschreibung")
        print("-" * 120)
        print("\033[38;2;204;0;147m[0 ] Zurück zum Hauptmenü")
        print()
        print("\033[38;2;214;13;150m[1 ] ARP-Spoofing\t\t\t\tManipuliert ARP-Tabellen in einem Netzwerk.")
        print("\033[38;2;224;26;154m[2 ] Packet Sniffer\t\t\t\tErfasst und analysiert Netzwerkpakete.")
        print("\033[38;2;234;38;157m[3 ] Hash-Cracking\t\t\t\tBrute-Force-Angriff auf Hash-Werte (MD5, SHA1, etc.).")
        print("\033[38;2;244;51;161m[4 ] Passwort-Generator\t\t\tErstellt sichere Passwörter mit zufälligen Zeichen.")
        print("\033[38;2;251;64;168m[5 ] Bluetooth Sniffing\t\t\tScannt und listet Bluetooth-Geräte in der Nähe auf.")
        print("\033[38;2;253;77;175m[6 ] Phishing-Seiten-Detektor\t\t\tErkennt verdächtige Webseiten basierend auf deren HTML-Code.")
        print("\033[38;2;254;102;182m[7 ] Webcam-Hijack Prevention\t\t\tÜberwacht, ob die Webcam ohne Erlaubnis genutzt wird.")
        print("\033[38;2;255;128;188m[8 ] Keylogger\t\t\t\t\tErfasst Tastatureingaben (Beta).")
        print("\033[38;2;255;153;195m[9 ] Browser-Daten auslesen\t\t\tZeigt gespeicherte Cookies und Passwörter.")
        print("\033[38;2;255;179;202m[10] DNS Spoofing\t\t\t\tManipuliert DNS-Anfragen (nur für legale Tests!).")
        print("\033[38;2;255;204;209m[11] Malware-Scanner\t\t\t\tErkennt und entfernt Schadsoftware.")
        print("\033[38;2;255;217;214m[12] Exploit-Scanner\t\t\t\tIdentifiziert bekannte Schwachstellen im System.")
        print("\033[38;2;255;229;220m[13] Anti-Rootkit-Tool\t\t\t\tFindet versteckte Rootkits auf dem Gerät.")
        print("\033[38;2;255;240;225m[14] USB-Sicherheitsueberwachung\t\tErkennt und warnt vor nicht autorisierten USB-Geräten.")
        print("\033[38;2;255;229;218m[15] Session Hijacking-Erkennung\t\tWarnt vor Angriffen auf offene Sitzungen.")

        choice = input("\033[38;2;255;255;255m\nOption: ")

        if choice == "0":
            return  # Zurück zum Hauptmenü
        else:
            print("Option wird noch entwickelt...")

def show_system_automation_menu():
    """ Zeigt das System-Manipulation & Automatisierung-Menü an """
    while True:
        os.system("cls")
        print("\n\033[35m=== System-Manipulation & Automatisierung ===\033[0m\n")
        print("Funktion\t\t\t\t\tBeschreibung")
        print("-" * 80)
        print("\033[38;2;255;77;179m[0 ] Zurück zum Hauptmenü")
        print()
        print("\033[38;2;255;89;184m[1 ] Prozess-Manager\t\t\tListet laufende Prozesse und ermöglicht das Beenden dieser.")
        print("\033[38;2;255;102;188m[2 ] Startup-Programme bearbeiten\tÄndert Programme, die beim Systemstart ausgeführt werden.")
        print("\033[38;2;255;115;193m[3 ] Datei-Sucher\t\t\tFindet versteckte oder verdächtige Dateien.")
        print("\033[38;2;255;128;197m[4 ] Screenshot-Erstellung\t\tErstellt Screenshots des Bildschirms.")
        print("\033[38;2;255;141;202m[5 ] Auto-Delete Logs\t\t\tLöscht spezifische Systemprotokolle automatisch.")
        print("\033[38;2;255;153;206m[6 ] Registry Viewer & Editor\tZeigt und ändert Registry-Einträge.")
        print("\033[38;2;255;166;211m[7 ] USB-Geräte-Logger\t\tListet alle angeschlossenen USB-Geräte.")
        print("\033[38;2;255;179;216m[8 ] Mac-Switch\t\t\tÄndert die MAC-Adresse eines Netzwerkadapters.")
        print("\033[38;2;255;191;220m[9 ] Clipboard-Manager\t\tZeigt und speichert Zwischenablage-Historie.")
        print("\033[38;2;255;204;225m[10] Automatische Systemwartung\tFührt geplante Wartungsaufgaben durch.")
        print("\033[38;2;255;216;229m[11] Hintergrundprozess-Killer\tSchließt nicht benötigte Hintergrundprozesse.")
        print("\033[38;2;255;229;234m[12] Automatische Software-Updater\tHält installierte Programme auf dem neuesten Stand.")
        print("\033[38;2;255;240;238m[13] Datei-Dupliziererkennung\tFindet doppelte Dateien auf dem System.")
        print("\033[38;2;255;250;243m[14] Energieverbrauchsmonitor\tAnalysiert den Stromverbrauch des Geräts.")
        print("\033[38;2;255;250;244m[15] Terminal-Befehlslogger\tSpeichert ausgeführte Terminal-Befehle.")

        choice = input("\033[38;2;255;255;255m\nOption: ")

        if choice == "0":
            return  # Zurück zum Hauptmenü
        else:
            print("Option wird noch entwickelt...")

def show_encryption_menu():
    """ Zeigt das Verschlüsselung & Dateimanagement-Menü an """
    while True:
        os.system("cls")
        print("\n\033[35m=== Verschluesselung & Dateimanagement ===\033[0m\n")
        print("Funktion\t\t\t\t\t\t\tBeschreibung")
        print("-" * 120)
        print("\033[38;2;255;179;205m[0 ] Zurück zum Hauptmenü")
        print()
        print("\033[38;2;255;186;210m[1 ] Datei-Verschluesselung\t\t\tVerschlüsselt Dateien mit AES oder anderen Algorithmen.")
        print("\033[38;2;255;192;215m[2 ] Verschluesselte Kommunikation\t\tSendet Nachrichten verschlüsselt über Netzwerke.")
        print("\033[38;2;255;198;220m[3 ] Sichere Passwort-Speicherung\t\tSpeichert Passwörter in einer verschlüsselten Datenbank.")
        print("\033[38;2;255;204;225m[4 ] USB-Speicher Verschluesselung\t\tSchützt USB-Laufwerke mit einer Verschlüsselung.")
        print("\033[38;2;255;210;230m[5 ] Secure Delete\t\t\t\tLöscht Dateien dauerhaft und unwiederbringlich.")
        print("\033[38;2;255;210;230m[6 ] Container-Verschluesselung\t\t\tErstellt verschlüsselte Container für Dateien.")
        print("\033[38;2;255;222;240m[7 ] Steganographie-Tool\t\t\tVersteckt Nachrichten in Bildern oder Audiodateien.")
        print("\033[38;2;255;228;245m[8 ] Blockchain-basierte Dateisicherung\t\tSpeichert Dateien manipulationssicher in einer Blockchain.")
        print("\033[38;2;255;234;250m[9 ] One-Time-Pad-Verschluesselung\t\tNutzt unknackbare Einwegschlüssel zur Verschlüsselung.")
        print("\033[38;2;255;239;252m[10] Cloud-Speicher-Verschluesselung\t\tVerschlüsselt Daten vor dem Hochladen in die Cloud.")
        print("\033[38;2;255;244;254m[11] Datei-Verschluesselungs-Automatisierung\tVerschlüsselt automatisch neue Dateien in einem Ordner.")
        print("\033[38;2;255;248;255m[12] ZIP-Verschluesselung\t\t\tErstellt passwortgeschützte ZIP-Dateien.")
        print("\033[38;2;255;251;255m[13] Festplatten-Encryption\t\t\tVerschlüsselt komplette Festplatten für mehr Sicherheit.")
        print("\033[38;2;255;255;255m[14] Digitale Signaturen\t\t\tErstellt und überprüft digitale Signaturen von Dateien.")
        print("\033[38;2;255;255;255m[15] Datei-Zugriffs-Überwachung\t\t\tProtokolliert, welche Benutzer auf welche Dateien zugreifen.")

        choice = input("\033[38;2;255;255;255m\nOption: ")

        if choice == "0":
            return  # Zurück zum Hauptmenü
        else:
            print("Option wird noch entwickelt...")

def show_everything_menu():
    """ Es wird Jede option aufgelistet """
    while True: 
        os.system("cls")
        print("\n\033[35m=== Verschluesselung & Dateimanagement ===\033[0m\n")
        print("Funktion\t\t\t\t\t\t\tBeschreibung")
        print("-" * 120)
        print("\033[38;2;145;0;130m[0 ] Zurück zum Hauptmenü")
        print()
        print("\033[38;2;145;0;130m[1 ] Port Scanner\t\t\t\tScannt ein Zielsystem nach offenen Ports.")
        print("\033[38;2;146;4;132m[2 ] Netzwerk-Scanner\t\t\t\tZeigt alle Geräte im aktuellen Netzwerk an.")
        print("\033[38;2;148;8;134m[3 ] IP-Geolocation\t\t\t\tBestimmt die IP-Adresse und deren Position.")
        print("\033[38;2;150;12;136m[4 ] VPN-Status Check\t\t\t\tPrüft, ob ein VPN aktiv ist.")
        print("\033[38;2;152;17;138m[5 ] DNS Resolver\t\t\t\tWandelt eine Domain in eine IP-Adresse um.")
        print("\033[38;2;154;21;140m[6 ] WLAN Deauth Detection\t\t\tErkennt Deauth-Pakete im WLAN-Netzwerk.")
        print("\033[38;2;156;25;142m[7 ] Firewall-Status Check\t\t\tÜberprüft den Status der System-Firewall.")
        print("\033[38;2;157;29;144m[8 ] Netzwerkverkehr-Analyse\t\t\tAnalysiert den eingehenden und ausgehenden Netzwerkverkehr.")
        print("\033[38;2;159;34;146m[9 ] Public IP Checker\t\t\t\tErmittelt die externe IP-Adresse des Geräts.")
        print("\033[38;2;161;38;148m[10] Traceroute-Tool\t\t\t\tZeigt die Route von Paketen zum Zielserver an.")
        print("\033[38;2;163;42;150m[11] Netzwerk-Speedtest\t\t\t\tMisst die aktuelle Internetgeschwindigkeit.")
        print("\033[38;2;165;46;152m[12] Netzwerk-Graph generieren\t\t\tVisualisiert Netzwerke mit einem Diagramm.")
        print("\033[38;2;167;51;154m[13] Ping-Tester\t\t\t\t\tTestet die Erreichbarkeit eines Hosts.")
        print("\033[38;2;168;55;156m[14] Bandbreiten-Monitor\t\t\t\tÜberwacht den Internetverbrauch in Echtzeit.")
        print("\033[38;2;170;59;158m[15] DHCP-Sniffer\t\t\t\tErkennt DHCP-Server im Netzwerk.")
        print("\033[38;2;172;63;160m[16] ARP-Spoofing\t\t\t\tManipuliert ARP-Tabellen in einem Netzwerk.")
        print("\033[38;2;174;68;162m[17] Packet Sniffer\t\t\t\tErfasst und analysiert Netzwerkpakete.")
        print("\033[38;2;176;72;164m[18] Hash-Cracking\t\t\t\tBrute-Force-Angriff auf Hash-Werte (MD5, SHA1, etc.).")
        print("\033[38;2;177;76;166m[19] Passwort-Generator\t\t\tErstellt sichere Passwörter mit zufälligen Zeichen.")
        print("\033[38;2;179;80;168m[20] Bluetooth Sniffing\t\t\tScannt und listet Bluetooth-Geräte in der Nähe auf.")
        print("\033[38;2;181;85;170m[21] Phishing-Seiten-Detektor\t\t\tErkennt verdächtige Webseiten basierend auf deren HTML-Code.")
        print("\033[38;2;183;89;172m[22] Webcam-Hijack Prevention\t\t\tÜberwacht, ob die Webcam ohne Erlaubnis genutzt wird.")
        print("\033[38;2;185;93;174m[23] Keylogger\t\t\t\t\tErfasst Tastatureingaben (Beta).")
        print("\033[38;2;186;97;176m[24] Browser-Daten auslesen\t\t\tZeigt gespeicherte Cookies und Passwörter.")
        print("\033[38;2;188;102;178m[25] DNS Spoofing\t\t\t\tManipuliert DNS-Anfragen (nur für legale Tests!).")
        print("\033[38;2;190;106;180m[26] Malware-Scanner\t\t\t\tErkennt und entfernt Schadsoftware.")
        print("\033[38;2;192;110;182m[27] Exploit-Scanner\t\t\t\tIdentifiziert bekannte Schwachstellen im System.")
        print("\033[38;2;194;114;184m[28] Anti-Rootkit-Tool\t\t\t\tFindet versteckte Rootkits auf dem Gerät.")
        print("\033[38;2;195;119;186m[29] USB-Sicherheitsueberwachung\t\tErkennt und warnt vor nicht autorisierten USB-Geräten.")
        print("\033[38;2;197;123;188m[30] Session Hijacking-Erkennung\t\tWarnt vor Angriffen auf offene Sitzungen.")
        print("\033[38;2;199;127;190m[31] Prozess-Manager\t\t\tListet laufende Prozesse und ermöglicht das Beenden dieser.")
        print("\033[38;2;201;131;192m[32] Startup-Programme bearbeiten\tÄndert Programme, die beim Systemstart ausgeführt werden.")
        print("\033[38;2;203;136;194m[33] Datei-Sucher\t\t\tFindet versteckte oder verdächtige Dateien.")
        print("\033[38;2;204;140;196m[34] Screenshot-Erstellung\t\tErstellt Screenshots des Bildschirms.")
        print("\033[38;2;206;144;198m[35] Auto-Delete Logs\t\t\tLöscht spezifische Systemprotokolle automatisch.")
        print("\033[38;2;208;148;200m[36] Registry Viewer & Editor\tZeigt und ändert Registry-Einträge.")
        print("\033[38;2;210;153;202m[37] USB-Geräte-Logger\t\tListet alle angeschlossenen USB-Geräte.")
        print("\033[38;2;212;157;204m[38] Mac-Switch\t\t\tÄndert die MAC-Adresse eines Netzwerkadapters.")
        print("\033[38;2;213;161;206m[39] Clipboard-Manager\t\tZeigt und speichert Zwischenablage-Historie.")
        print("\033[38;2;215;165;208m[40] Automatische Systemwartung\tFührt geplante Wartungsaufgaben durch.")
        print("\033[38;2;217;170;210m[41] Hintergrundprozess-Killer\tSchließt nicht benötigte Hintergrundprozesse.")
        print("\033[38;2;219;174;212m[42] Automatische Software-Updater\tHält installierte Programme auf dem neuesten Stand.")
        print("\033[38;2;221;178;214m[43] Datei-Dupliziererkennung\tFindet doppelte Dateien auf dem System.")
        print("\033[38;2;223;182;216m[44] Energieverbrauchsmonitor\tAnalysiert den Stromverbrauch des Geräts.")
        print("\033[38;2;224;187;218m[45] Terminal-Befehlslogger\tSpeichert ausgeführte Terminal-Befehle.")
        print("\033[38;2;226;191;220m[46] Datei-Verschluesselung\t\t\tVerschlüsselt Dateien mit AES oder anderen Algorithmen.")
        print("\033[38;2;228;195;222m[47] Verschluesselte Kommunikation\t\tSendet Nachrichten verschlüsselt über Netzwerke.")
        print("\033[38;2;230;199;224m[48] Sichere Passwort-Speicherung\t\tSpeichert Passwörter in einer verschlüsselten Datenbank.")
        print("\033[38;2;231;204;226m[49] USB-Speicher Verschluesselung\t\tSchützt USB-Laufwerke mit einer Verschlüsselung.")
        print("\033[38;2;233;208;228m[50] Secure Delete\t\t\t\tLöscht Dateien dauerhaft und unwiederbringlich.")
        print("\033[38;2;235;212;230m[51] Container-Verschluesselung\t\t\tErstellt verschlüsselte Container für Dateien.")
        print("\033[38;2;237;216;232m[52] Steganographie-Tool\t\t\tVersteckt Nachrichten in Bildern oder Audiodateien.")
        print("\033[38;2;239;221;234m[53] Blockchain-basierte Dateisicherung\t\tSpeichert Dateien manipulationssicher in einer Blockchain.")
        print("\033[38;2;240;225;236m[54] One-Time-Pad-Verschluesselung\t\tNutzt unknackbare Einwegschlüssel zur Verschlüsselung.")
        print("\033[38;2;242;229;238m[55] Cloud-Speicher-Verschluesselung\t\tVerschlüsselt Daten vor dem Hochladen in die Cloud.")
        print("\033[38;2;244;233;240m[56] Datei-Verschluesselungs-Automatisierung\tVerschlüsselt automatisch neue Dateien in einem Ordner.")
        print("\033[38;2;246;238;242m[57] ZIP-Verschluesselung\t\t\tErstellt passwortgeschützte ZIP-Dateien.")
        print("\033[38;2;248;242;244m[58] Festplatten-Encryption\t\t\tVerschlüsselt komplette Festplatten für mehr Sicherheit.")
        print("\033[38;2;249;246;246m[59] Digitale Signaturen\t\t\tErstellt und überprüft digitale Signaturen von Dateien.")
        print("\033[38;2;255;255;255m[60] Datei-Zugriffs-Überwachung\t\t\tProtokolliert, welche Benutzer auf welche Dateien zugreifen.")



        choice = input("\033[38;2;255;255;255m\nOption: ")

        if choice == "0":
            return  # Zurück zum Hauptmenü
        else:
            print("Option wird noch entwickelt...")
# Startet das Programm
show_main_menu()

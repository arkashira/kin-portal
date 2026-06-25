import json
from dataclasses import dataclass
from typing import List
import argparse

@dataclass
class Service:
    name: str
    url: str
    icon: str
    shareable: bool

class KinPortal:
    def __init__(self):
        self.services = []

    def scan_services(self):
        # Simulate scanning local LAN
        self.services = [
            Service("Nextcloud", "https://nextcloud.local", "nextcloud.png", False),
            Service("Kanboard", "https://kanboard.local", "kanboard.png", False),
        ]

    def get_services(self):
        return self.services

    def toggle_shareable(self, service_name):
        for service in self.services:
            if service.name == service_name:
                service.shareable = not service.shareable
                return service

    def create_tunnel(self, service_name):
        for service in self.services:
            if service.name == service_name and service.shareable:
                # Simulate creating a secure reverse-proxy tunnel
                return f"Tunnel created for {service_name}"
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--toggle", type=str)
    parser.add_argument("--tunnel", type=str)
    args = parser.parse_args()

    portal = KinPortal()

    if args.scan:
        portal.scan_services()
        print(json.dumps([service.__dict__ for service in portal.get_services()]))
    elif args.toggle:
        service = portal.toggle_shareable(args.toggle)
        if service:
            print(json.dumps(service.__dict__))
    elif args.tunnel:
        result = portal.create_tunnel(args.tunnel)
        if result:
            print(result)

if __name__ == "__main__":
    main()

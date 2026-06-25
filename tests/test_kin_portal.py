from kin_portal import KinPortal, Service
import pytest

def test_scan_services():
    portal = KinPortal()
    portal.scan_services()
    services = portal.get_services()
    assert len(services) == 2
    assert services[0].name == "Nextcloud"
    assert services[1].name == "Kanboard"

def test_get_services():
    portal = KinPortal()
    services = portal.get_services()
    assert services == []

def test_toggle_shareable():
    portal = KinPortal()
    portal.scan_services()
    service = portal.toggle_shareable("Nextcloud")
    assert service.shareable

def test_create_tunnel():
    portal = KinPortal()
    portal.scan_services()
    portal.toggle_shareable("Nextcloud")
    result = portal.create_tunnel("Nextcloud")
    assert result == "Tunnel created for Nextcloud"

def test_create_tunnel_unshareable():
    portal = KinPortal()
    portal.scan_services()
    result = portal.create_tunnel("Nextcloud")
    assert result is None

def test_main_scan():
    import sys
    sys.argv = ["kin_portal.py", "--scan"]
    from kin_portal import main
    main()

def test_main_toggle():
    import sys
    sys.argv = ["kin_portal.py", "--toggle", "Nextcloud"]
    from kin_portal import main
    main()

def test_main_tunnel():
    import sys
    sys.argv = ["kin_portal.py", "--tunnel", "Nextcloud"]
    from kin_portal import main
    main()

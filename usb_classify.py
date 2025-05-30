import pyudev

def load_usb_ids(usb_ids_path="/usr/local/share/usb.ids"):
    vendors = {}
    current_vendor = None
    with open(usb_ids_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            if not line.startswith("\t"):
                parts = line.strip().split(None, 1)
                if len(parts) == 2 and len(parts[0]) == 4:
                    current_vendor = parts[0].lower()
                    vendors[current_vendor] = {"name": parts[1], "products": {}}
            else:
                parts = line.strip().split(None, 1)
                if current_vendor and len(parts) == 2 and len(parts[0]) == 4:
                    product_id = parts[0].lower()
                    vendors[current_vendor]["products"][product_id] = parts[1]
    return vendors

def lookup_usb(vendors, vendor_id, product_id):
    vendor_id = vendor_id.lower()
    product_id = product_id.lower()
    vendor = vendors.get(vendor_id)
    if not vendor:
        return None, None
    product = vendor["products"].get(product_id)
    return vendor["name"], product

if __name__ == "__main__":
    usb_vendors = load_usb_ids()
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb', device_type='usb_device')

    print("Đang theo dõi thiết bị USB...")

    for device in iter(monitor.poll, None):
        if device.action == 'add':
            vendor_id = device.get('ID_VENDOR_ID')
            product_id = device.get('ID_MODEL_ID')
            if vendor_id and product_id:
                vendor_name, product_name = lookup_usb(usb_vendors, vendor_id, product_id)
                print(f"Thiết bị mới: {vendor_name or vendor_id} - {product_name or product_id}")
            else:
                print("Thiết bị USB mới không xác định được ID.")
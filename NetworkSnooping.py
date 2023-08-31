import pyshark

target_ip = "192.168.1.100"
capture_file = "capture.pcap"

capture = pyshark.FileCapture(capture_file)
for packet in capture:
    try:
        if 'IP' in packet:
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst
            
            if src_ip == target_ip or dst_ip == target_ip:
                print(f"Source: {src_ip} -> Destination: {dst_ip}")
    except Exception as e:
        pass  # Handle exceptions if needed

capture.close()

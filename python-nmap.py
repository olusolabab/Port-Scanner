import nmap

nm = nmap.PortScanner()

target = "45.33.32.156"
options = "-sV -sC scanResults"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        portInfo = nm[host][protocol]
        for port, state in portInfo.items():
            print("  Port: %s \tState: %s" % (port, state))
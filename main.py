import dns.resolver  # DNS queries
from termcolor import colored

try:
    host = input("\nEnter target: ")
    name_servers = dns.resolver.query(host, "NS")  # (host, tipo_consulta)
    host_ips = dns.resolver.query(host, "A")

    for ip in host_ips:
        print("\nIP: ", ip)

    print("\nName Servers: ")
    for ns in name_servers:
        print(" ", ns)

except Exception as error:
    print("\nError:", colored(error, "red"))

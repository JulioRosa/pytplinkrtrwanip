#!/usr/bin/env python3
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='requests')

import requests
from tplinkrouterc6u import TplinkRouterProvider

# --- Configuration ---
ROUTER_URL = 'http://192.168.1.1 or your rtr ip'
ROUTER_PASSWORD = 'ROUTERPASSWORD'  # Replace with your router admin password
DUCKDNS_TOKEN = 'Insert_your_DUCK_DNS_token_here'  # Replace with your real DuckDNS token
DUCKDNS_DOMAIN = 'YOURSUBDOMAIN.duckdns.org'

def get_wan_info_and_update_dns():
    router = TplinkRouterProvider.get_client(ROUTER_URL, ROUTER_PASSWORD)

    try:
        router.authorize()
        ipv4_status = router.get_ipv4_status()

        # Extract WAN IP
        wan_ip = ipv4_status.wan_ipv4_ipaddr

        # Print WAN info
  #      print("WAN Information:")
  #      print(f"wan_macaddr: {ipv4_status.wan_macaddr}")
  #      print(f"wan_macaddress: {ipv4_status.wan_macaddress}")
         print(f"wan_ipv4_ipaddr: {ipv4_status.wan_ipv4_ipaddr}")
  #      print(f"wan_ipv4_ipaddress: {ipv4_status.wan_ipv4_ipaddress}")
  #      print(f"wan_ipv4_gateway: {ipv4_status.wan_ipv4_gateway}")
  #      print(f"wan_ipv4_gateway_address: {ipv4_status.wan_ipv4_gateway_address}")
  #      print(f"wan_ipv4_conntype: {ipv4_status.wan_ipv4_conntype}")
  #      print(f"wan_ipv4_netmask: {ipv4_status.wan_ipv4_netmask}")
         print("\nUpdating DuckDNS...")
      
        # Send IP to DuckDNS
        duckdns_url = (
            f"https://www.duckdns.org/update?"                                                                                      f"domains={DUCKDNS_DOMAIN}&"
            f"token={DUCKDNS_TOKEN}&"                                                                                               f"ip={wan_ip}"
        )

        response = requests.get(duckdns_url)

        # Confirm result
        if response.status_code == 200 and 'OK' in response.text:
            print(f"DuckDNS update successful. IP: {wan_ip}")
        else:
            print(f"DuckDNS update failed. Response: {response.text}")                                                  
    except Exception as e:                                                                                                      print(f"Error: {e}")

    finally:
        router.logout()                                                                                                 
if __name__ == "__main__":
    get_wan_info_and_update_dns()

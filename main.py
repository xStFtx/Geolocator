import requests

def get_location(ip_address=None):
    # If no IP address is provided, it fetches the location of the requester's IP
    url = f"https://ipinfo.io/{ip_address}/json" if ip_address else "https://ipinfo.io/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'bogon' in data:
            return "This is a reserved or private IP address."

        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        org = data.get('org', 'N/A')
        location = data.get('loc', 'N/A')
        
        return f"IP Address: {ip_address}\nCity: {city}\nRegion: {region}\nCountry: {country}\nOrganization: {org}\nCoordinates: {location}"

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    ip = input("Enter the IP address (or press enter to get info about your IP): ")
    print(get_location(ip))

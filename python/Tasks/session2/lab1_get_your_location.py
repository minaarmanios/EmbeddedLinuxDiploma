"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    #get my ip address
    url_response = requests.get("https://api.ipify.org/?format=json",timeout=1.0)
    url_response_dict = url_response.json()
    ip_address = url_response_dict.get('ip',None)
    if ip_address:
        url_response = requests.get('https://ipinfo.io/'+ip_address+'/geo',timeout=1.0)
        return url_response.json()
    return None

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"

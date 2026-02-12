DOMAIN = "lepro_led"

API_HOSTS = {
    "eu": "api-eu-iot.lepro.com",
    "us": "api-na-iot.lepro.com",
}


def get_api_urls(region):
    """Return a dict of API URLs for the given region."""
    host = API_HOSTS[region]
    base = f"https://{host}"
    return {
        "host": host,
        "login": f"{base}/user/login",
        "family_list": f"{base}/family/list/timestamp/{{timestamp}}",
        "user_profile": f"{base}/user/profile",
        "device_list": f"{base}/v3/device/list/fid/{{fid}}/timestamp/{{timestamp}}",
        "switch": f"{base}/statistic/record",
    }

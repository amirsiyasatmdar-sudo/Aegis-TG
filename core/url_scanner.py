import requests
import os

class URLScanner:
    def __init__(self):
        self.api_key = os.getenv("VIRUSTOTAL_API_KEY")
        self.base_url = "https://www.virustotal.com/api/v3/urls"

    def scan_url(self, url: str) -> bool:
        """بررسی لینک و بازگرداندن True اگر مخرب باشد"""
        if not self.api_key:
            print("WARNING: VIRUSTOTAL_API_KEY is not set.")
            return False
            
        headers = {"x-apikey": self.api_key}
        
        # ارسال لینک به VirusTotal
        response = requests.post(self.base_url, headers=headers, data={"url": url})
        
        if response.status_code == 200:
            analysis_id = response.json()["data"]["id"]
            analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
            result = requests.get(analysis_url, headers=headers).json()
            
            # اگر بیش از ۳ آنتی‌ویروس لینک را مخرب تشخیص داده باشند
            malicious_count = result["data"]["attributes"]["stats"]["malicious"]
            if malicious_count >= 3:
                return True
        return False

import requests
import logging
import os

logger = logging.getLogger(__name__)

class FeishuSync:
    def __init__(self, api_keys):
        self.app_id = api_keys.get('feishu_app_id')
        self.app_secret = api_keys.get('feishu_app_secret')
        self.user_token = api_keys.get('feishu_user_access_token') # Or tenant_access_token logic
        self.app_token = api_keys.get('bitable_app_token')
        self.table_id = api_keys.get('bitable_table_id')
        self.token = None

    def get_tenant_access_token(self):
        # If user provided a specific token, use it. Otherwise get tenant token.
        if self.user_token and self.user_token != "YOUR_USER_ACCESS_TOKEN":
            return self.user_token

        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        headers = {"Content-Type": "application/json; charset=utf-8"}
        data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json().get("tenant_access_token")
        except Exception as e:
            logger.error(f"Failed to get Feishu token: {e}")
            return None

    def upload_image(self, image_path):
        if not os.path.exists(image_path):
            return None
        
        token = self.get_tenant_access_token()
        if not token: return None

        url = "https://open.feishu.cn/open-apis/drive/v1/medias/upload_all"
        headers = {"Authorization": f"Bearer {token}"}
        
        try:
            with open(image_path, 'rb') as f:
                config = {
                    "parent_type": "bitable_image",
                    "parent_node": self.app_token,
                    "size": os.path.getsize(image_path)
                }
                files = {'file': (os.path.basename(image_path), f)}
                data = {'params': str(config)} # This might need json encoding if passing as param? 
                # Feishu API is specific. Usually multipart/form-data with 'file_name', 'parent_type', 'parent_node', 'size', 'file'
                # Corrections for "upload_all":
                data = {
                    'parent_type': 'bitable_image',
                    'parent_node': self.app_token,
                    'size': os.path.getsize(image_path),
                    'file_name': os.path.basename(image_path)
                }
                response = requests.post(url, headers=headers, data=data, files=files)
                response.raise_for_status()
                return response.json().get('data', {}).get('file_token')
        except Exception as e:
            logger.error(f"Failed to upload image: {e}")
            return None

    def sync_to_bitable(self, record_data, table_id=None):
        """
        record_data: dict compatible with Bitable fields
        table_id: Optional ID to override default
        """
        token = self.get_tenant_access_token()
        if not token: return False

        target_table_id = table_id if table_id else self.table_id
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{target_table_id}/records"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, headers=headers, json={"fields": record_data})
            
            res_json = response.json()
            if response.status_code == 200 and res_json.get('code') == 0:
                return True
            else:
                logger.error(f"Feishu Sync Error: {response.text}")
                return False
        except Exception as e:
            return False

    def upload_file(self, file_path, parent_type="bitable_file"):
        if not os.path.exists(file_path):
            return None
        
        token = self.get_tenant_access_token()
        if not token: return None

        url = "https://open.feishu.cn/open-apis/drive/v1/medias/upload_all"
        headers = {"Authorization": f"Bearer {token}"}
        
        try:
            with open(file_path, 'rb') as f:
                size = os.path.getsize(file_path)
                data = {
                    'parent_type': parent_type,
                    'parent_node': self.app_token,
                    'size': size,
                    'file_name': os.path.basename(file_path)
                }
                files = {'file': (os.path.basename(file_path), f)}
                
                response = requests.post(url, headers=headers, data=data, files=files)
                response.raise_for_status()
                return response.json().get('data', {}).get('file_token')
        except Exception as e:
            logger.error(f"Failed to upload file: {e}")
            return None

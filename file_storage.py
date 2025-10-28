import os
import uuid
import json
import base64
from datetime import datetime, timedelta

class FileStorage:
    def __init__(self, storage_dir='temp_sessions'):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        self.cleanup_old_files()
    
    def create_session(self):
        session_id = str(uuid.uuid4())
        session_data = {
            'created_at': datetime.now().isoformat(),
            'uploaded_image': None,
            'current_question': 1,
            'answers': {}
        }
        self.save_session(session_id, session_data)
        return session_id
    
    def save_session(self, session_id, data):
        file_path = os.path.join(self.storage_dir, f"{session_id}.json")
        with open(file_path, 'w') as f:
            json.dump(data, f)
    
    def load_session(self, session_id):
        file_path = os.path.join(self.storage_dir, f"{session_id}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return None
    
    def delete_session(self, session_id):
        file_path = os.path.join(self.storage_dir, f"{session_id}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
    
    def cleanup_old_files(self):
        # Remove files older than 1 hour
        for filename in os.listdir(self.storage_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(self.storage_dir, filename)
                if os.path.exists(file_path):
                    file_time = datetime.fromtimestamp(os.path.getctime(file_path))
                    if datetime.now() - file_time > timedelta(hours=1):
                        os.remove(file_path)

# Global storage instance
storage = FileStorage()
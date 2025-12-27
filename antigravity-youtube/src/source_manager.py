import yaml
import os
import logging

logger = logging.getLogger(__name__)

class SourceManager:
    def __init__(self, sources_path, state_path):
        self.sources_path = sources_path
        self.state_path = state_path
        self.config = self._load_config()
        self.state = self._load_state()

    def _load_config(self):
        if not os.path.exists(self.sources_path):
            raise FileNotFoundError(f"Config file not found: {self.sources_path}")
        with open(self.sources_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _load_state(self):
        if not os.path.exists(self.state_path):
            return {'processed_videos': []}
        with open(self.state_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {'processed_videos': []}

    def save_state(self):
        with open(self.state_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.state, f)

    def is_processed(self, video_id):
        return video_id in self.state.get('processed_videos', [])

    def mark_processed(self, video_id):
        if 'processed_videos' not in self.state:
            self.state['processed_videos'] = []
        if video_id not in self.state['processed_videos']:
            self.state['processed_videos'].append(video_id)
            self.save_state()

    def get_channels(self):
        return [c for c in self.config.get('channels', []) if c.get('enable', True)]

    def get_api_keys(self):
        return self.config.get('api_keys', {})

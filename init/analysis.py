class PropertiesReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.properties = {}
        self._load_properties()

    def _load_properties(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    self.properties[key.strip()] = value.strip().strip('\'')

    def get(self, key, default=None):
        return self.properties.get(key, default)

    def get_all(self):
        return self.properties
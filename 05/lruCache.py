class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.first = {}
        self.last = {}
        self.first["future"] = self.last
        self.last["early"] = self.first

    def get(self, key):
        if key in self.cache:
            cell = self.cache[key]
            self.remove_cell(cell)
            self.add_cell(cell)
            return cell["value"]
        return None

    def set(self, key, value):
        if key in self.cache:
            cell = self.cache[key]
            self.remove_cell(cell)
        elif len(self.cache) >= self.limit:
            cell = self.last["early"]
            self.remove_cell(cell)
            del self.cache[cell["key"]]
        cell = {"key": key, "value": value}
        self.cache[key] = cell
        self.add_cell(cell)

    def remove_cell(self, cell):
        early_cell = cell["early"]
        future_cell = cell["future"]
        early_cell["future"] = future_cell
        future_cell["early"] = early_cell

    def add_cell(self, cell):
        future_cell = self.first["future"]
        self.first["future"] = cell
        cell["early"] = self.first
        cell["future"] = future_cell
        future_cell["early"] = cell

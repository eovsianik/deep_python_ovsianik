import argparse
import logging

logger = logging.getLogger("LRUCache")


class EvenWordFilter(logging.Filter):
    def filter(self, record):
        return len(record.msg.split()) % 2 == 0


class LRUCache:
    def __init__(self, limit=42):
        logger.info("")
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
            logger.info("Get existing key: %d", key)
            return cell["value"]
        logger.warning("Get missing key: %d", key)
        return None

    def set(self, key, value):
        if key in self.cache:
            cell = self.cache[key]
            self.remove_cell(cell)
            logger.info("Set existing key: %d", key)
        elif len(self.cache) >= self.limit:
            cell = self.last["early"]
            self.remove_cell(cell)
            del self.cache[cell["key"]]
            logger.critical("Set missing key when capacity reached: %d", key)
        else:
            logger.error("Set missing key: %d", key)
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--stdout", action="store_true", help="Log to stdout")
    parser.add_argument("-f", "--filter", help="Apply a custom filter to the logs")
    args = parser.parse_args()

    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("cache.log")
    if args.stdout:
        handler_stdout = logging.StreamHandler()
        handler_stdout.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))

    logger.addHandler(handler)
    if args.stdout:
        logger.addHandler(handler_stdout)

    if args.filter == "even":
        handler.addFilter(EvenWordFilter())

    cache = LRUCache(100)
    for i in range(100):
        cache.set(i, f"value{i}")
        cache.get(i)
    cache.set(100, "value100")
    cache.get(100)
    cache.set(101, "value101")
    cache.get(101)


if __name__ == "__main__":
    main()

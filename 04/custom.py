class CustomMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith("__"):
                attr_name = "custom_" + attr_name
            new_attrs[attr_name] = attr_value

        new_class = super().__new__(cls, name, bases, new_attrs)

        original_setattr = new_class.__setattr__

        def new_setattr(self, name, value):
            if not name.startswith("__"):
                name = "custom_" + name
            original_setattr(self, name, value)

        new_class.__setattr__ = new_setattr

        return new_class

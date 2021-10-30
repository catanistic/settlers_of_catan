from enum import Enum, auto


class FieldType(Enum):
    Category = auto()
    Integer = auto()
    Float = auto()
    GameObjectReference = auto()


class Schema():
    def __init__(self):
        self.field_names = []
        self.field_types = {}
        self.category_counts = {}
        self.category_mappings = {}

    def append_field(self, field_name, field_type, *argv, **kwargs):
        assert(field_name not in self.field_types)
        if field_type is FieldType.Category:
            self.append_category_field(field_name, *argv, **kwargs)
            return

        assert(type(field_name) is str)
        assert(type(field_type) is FieldType)
        self.field_names.append(field_name)
        self.field_types[field_name] = field_type

    def append_category_field(self, field_name, possible_values):
        assert(type(field_name) is str)
        assert(field_name not in self.field_types)
        assert(len(possible_values) > 0)
        self.field_names.append(field_name)
        self.category_mappings[field_name]= {val:i for i, val in enumerate(possible_values)}
        assert(len(self.category_mappings[field_name]) == len(possible_values))
        self.field_types[field_name] = FieldType.Category

    def _observe(self, idx, *args, **kwargs):
        field_name = self.field_names[idx]
        if len(args) == len(self.field_names):
            value = args[idx]
        else:
            value = kwargs[field_name]

        if self.field_types[field_name] is FieldType.Category:
            return self.category_mappings[field_name][value]
        else:
            return value 

    def __call__(self, *args, **kwargs):
        return [self._observe(idx, *args, **kwargs) for idx in range(len(self.field_names))]
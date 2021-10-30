from ..context import catan

import unittest
from parameterized import parameterized


class TestSchema(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.schema = catan.shared.Schema()

    @parameterized.expand([
        ("test_field", catan.shared.FieldType.Integer),
        ("test_field", catan.shared.FieldType.Float),
        ("test_field", catan.shared.FieldType.GameObjectReference),
    ])
    def testAppendField(self, field_name, field_type):
        self.schema.append_field(field_name, field_type)
        self.assertEqual(len(self.schema.field_names), 1)
        self.assertEqual(len(self.schema.field_types), 1)

    def testAppendWithDuplicatedFieldName(self):
        self.schema.append_field("test_field", catan.shared.FieldType.Integer)
        self.assertRaises(AssertionError, self.schema.append_field,
        "test_field", catan.shared.FieldType.Integer) 

    def testAppendCategoryField(self):
        self.schema.append_field("test_field", catan.shared.FieldType.Category, ["one", "two"])
        self.assertEqual(len(self.schema.field_names), 1)
        self.assertEqual(len(self.schema.field_types), 1)

    def testAppendCategoryFieldWithEnum(self):
        self.schema.append_field("test_field", catan.shared.FieldType.Category, catan.shared.FieldType)
        self.assertEqual(len(self.schema.field_names), 1)
        self.assertEqual(len(self.schema.field_types), 1)

    def testAppendCategoryWithoutPossibleValues(self):
        self.assertRaises(TypeError, self.schema.append_field,
        "test_field", catan.shared.FieldType.Category) 

    def testAppendCategoryWithDuplicates(self):
        self.assertRaises(AssertionError, self.schema.append_field,
            "test_field", catan.shared.FieldType.Category, ["one", "one"]) 
        self.assertRaises(AssertionError, self.schema.append_category_field,
            "test_field", ["one", "one"]) 

    def testCall(self):
        self.schema.append_field("test_field", catan.shared.FieldType.Integer)
        self.assertListEqual(self.schema(0), [0])
        self.assertListEqual(self.schema(0), [0])

    def testCallWithCategory(self):
        self.schema.append_field("test_field", catan.shared.FieldType.Category, ["one", "two"])
        self.assertListEqual(self.schema("one"), [0])
        self.assertListEqual(self.schema("two"), [1])
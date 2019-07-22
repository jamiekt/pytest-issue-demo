import unittest
import mock
from widget import Widget


@mock.patch.dict(
    "widget.os.environ",
    {"SOME_VAR": "qwerty"}
)
class TestWidget(unittest.TestCase):
    def test1(self):
        widget1 = Widget()
        assert widget1.func1() == "qwerty"

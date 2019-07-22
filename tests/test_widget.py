import unittest
import mock
from widget import Widget


env_vars_dict = {
        "SOME_VAR": "qwerty"
    }


@mock.patch.dict(
    "widget.os.environ",
    env_vars_dict
)
class TestWidget(unittest.TestCase):
    def test1(self):
        widget1 = Widget()
        assert widget1.func1() == "qwerty"

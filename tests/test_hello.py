import pytest

from python_package_quickstart import Example

class TestExample:
    def test_string(self):
        obj = Example()
        assert isinstance(obj.hello(), str)

    def test_hello(self):
        obj = Example()
        assert obj.hello() == 'Hello!!'

    def test_exception(self):
        with pytest.raises(NotImplementedError):
            obj = Example()
            obj.raise_exception()

    def test_not_written(self):
        pytest.skip("This should test something that is not writtent yet.")
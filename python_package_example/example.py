
class Example:
    """Class used as an example of how to create a minimal module/package

    Class used as an example of how to create a minimal module/package
    It has no miningful functionality, just a few sample methods.

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    """


    def hello(self):
        """ Sample method, just return "Hello!!"

        Sample method, just return "Hello!!"

        Returns:
            str: "Hello!!!"

        """

        return "Hello!!"


    def raise_exception(self):
        """Sample method, just raise un exception

        Sample method, just raise un exception

        """

        raise NotImplementedError

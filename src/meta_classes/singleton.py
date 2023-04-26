class Singleton(type):
    """Singleton class. Used to avoid duplicate instances of specific classes
    
    Pass as "metaclass" argument when instantiating new class
    
    .. code-block::
    
        class NewClass(metaclass=Singleton):
            
            def __init__(self) -> None:
                self.some_field = "some_value"
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

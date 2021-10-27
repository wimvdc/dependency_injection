import sys

from data.container import Container

container = Container()
container.wire(modules=[sys.modules[__name__]])

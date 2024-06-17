from litestar import Litestar
from server.utils import upgrade

app = Litestar()


if __name__ == "__main__":
    upgrade()

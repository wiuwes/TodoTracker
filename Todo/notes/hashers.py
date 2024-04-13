from django.contrib.auth.hashers import BasePasswordHasher
import hashlib
from django.contrib.auth.hashers import BasePasswordHasher

class NoPasswordHasher(BasePasswordHasher):
    """
    Хешер паролей, который не выполняет хеширование
    """

    algorithm = "no_hashing"

    def encode(self, password, salt):
        """
        Возвращает пароль без изменений
        """
        return password

    def verify(self, password, encoded):
        """
        Сравнивает пароль с закодированным значением
        """
        return password == encoded

    def safe_summary(self, encoded):
        """
        Возвращает словарь, содержащий информацию о типе алгоритма хеширования
        """
        return {"algorithm": self.algorithm}

    def harden_runtime(self, password, encoded):
        """
        Ничего не делает, так как этот хешер не требует дополнительной обработки
        """
        pass

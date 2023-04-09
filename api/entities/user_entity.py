"""User entity module."""


class User:
    """User entity."""

    def __init__(
        self, name: str, email: str, password: str, is_admin: bool, api_key: str
    ) -> None:
        self.__name = name
        self.__email = email
        self.__password = password
        self.__is_admin = is_admin
        self.__api_key = api_key

    @property
    def name(self):
        """Name getter."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Name setter."""
        self.__name = name

    @property
    def email(self) -> str:
        """Email getter."""
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        """Email setter."""
        self.__email = email

    @property
    def password(self) -> str:
        """Password getter."""
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        """Password setter."""
        self.__password = password

    @property
    def is_admin(self) -> bool:
        """Is admin getter."""
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin: bool) -> None:
        """Is admin setter."""
        self.__is_admin = is_admin

    @property
    def api_key(self) -> str:
        """API Key getter."""
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        """API Key setter."""
        self.__api_key = api_key

import json

class FeatureFlags:
    """
    Klasa obsługująca mechanizm Feature Flags.

    Pozwala na dynamiczne włączanie i wyłączanie funkcjonalności w aplikacji
    na podstawie konfiguracji w pliku JSON.
    """

    def __init__(self, config_file="feature_flags.json"):
        """
        Inicjalizuje obiekt FeatureFlags i ładuje konfigurację z pliku.

        Args:
            config_file (str): Ścieżka do pliku JSON z konfiguracją flag.
        """
        self.config_file = config_file
        self.flags = self.load_flags()

    def load_flags(self):
        """
        Ładuje konfigurację flag z pliku JSON.

        Returns:
            dict: Słownik z flagami i ich wartościami (True/False).
        """
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def is_enabled(self, feature_name):
        """
        Sprawdza, czy dana funkcja jest włączona.

        Args:
            feature_name (str): Nazwa flagi funkcji.

        Returns:
            bool: True, jeśli funkcja jest włączona; False w przeciwnym razie.
        """
        return self.flags.get(feature_name, False)

    def enable(self, feature_name):
        """
        Włącza funkcję, ustawiając jej flagę na True.

        Args:
            feature_name (str): Nazwa flagi funkcji.

        Returns:
            None
        """
        self.flags[feature_name] = True
        self.save_flags()

    def disable(self, feature_name):
        """
        Wyłącza funkcję, ustawiając jej flagę na False.

        Args:
            feature_name (str): Nazwa flagi funkcji.

        Returns:
            None
        """
        self.flags[feature_name] = False
        self.save_flags()

    def save_flags(self):
        """
        Zapisuje aktualną konfigurację flag do pliku JSON.

        Returns:
            None
        """
        with open(self.config_file, "w") as file:
            json.dump(self.flags, file, indent=4)

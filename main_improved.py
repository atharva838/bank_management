import json
import random
import string
from datetime import datetime
from pathlib import Path


class Bank:
    """Simple JSON-based bank management backend."""

    database = Path("data.json")

    def __init__(self):
        self.data = self._load_data()

    def _load_data(self):
        if not self.database.exists():
            return []
        try:
            with self.database.open("r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def _save_data(self):
        with self.database.open("w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    @staticmethod
    def _generate_account_number():
        """Generate a unique 10-digit account number."""
        return "".join(random.choices(string.digits, k=10))

    def _find_account(self, account_no):
      account_no = str(account_no).strip()

      return next(
        (
            account
            for account in self.data
            if isinstance(account, dict)
            and str(account.get("account_no", "")).strip() == account_no
        ),
        None,
    )
    def authenticate(self, account_no, pin):
        account = self._find_account(str(account_no).strip())
        if account and account["pin"] == str(pin).strip():
            return account
        return None

    def create_account(self, name, age, email, pin):
        name = name.strip()
        email = email.strip().lower()
        pin = str(pin).strip()

        if not name:
            raise ValueError("Name is required.")
        if age < 18:
            raise ValueError("Account holder must be at least 18 years old.")
        if "@" not in email or "." not in email:
            raise ValueError("Enter a valid email address.")
        if not (pin.isdigit() and len(pin) == 4):
            raise ValueError("PIN must contain exactly 4 digits.")

        account_no = self._generate_account_number()
        while self._find_account(account_no):
            account_no = self._generate_account_number()

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no": account_no,
            "balance": 0.0,
            "transactions": [],
        }

        self.data.append(account)
        self._save_data()
        return account

    def deposit(self, account_no, amount):
        account = self._find_account(account_no)
        amount = float(amount)

        if not account:
            raise ValueError("Account not found.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        if amount > 100000:
            raise ValueError("Maximum single deposit is ₹1,00,000.")

        account["balance"] += amount
        account["transactions"].append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        self._save_data()
        return account["balance"]

    def withdraw(self, account_no, amount):
        account = self._find_account(account_no)
        amount = float(amount)

        if not account:
            raise ValueError("Account not found.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > account["balance"]:
            raise ValueError("Insufficient account balance.")

        account["balance"] -= amount
        account["transactions"].append({
            "type": "Withdrawal",
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        self._save_data()
        return account["balance"]

    def get_account(self, account_no):
        account = self._find_account(account_no)
        if not account:
            raise ValueError("Account not found.")
        return account

    def update_account(self, account_no, name=None, email=None, pin=None):
        account = self._find_account(account_no)
        if not account:
            raise ValueError("Account not found.")

        if name is not None and name.strip():
            account["name"] = name.strip()

        if email is not None and email.strip():
            email = email.strip().lower()
            if "@" not in email or "." not in email:
                raise ValueError("Enter a valid email address.")
            account["email"] = email

        if pin is not None and str(pin).strip():
            pin = str(pin).strip()
            if not (pin.isdigit() and len(pin) == 4):
                raise ValueError("PIN must contain exactly 4 digits.")
            account["pin"] = pin

        self._save_data()
        return account

    def delete_account(self, account_no):
        account = self._find_account(account_no)
        if not account:
            raise ValueError("Account not found.")

        self.data.remove(account)
        self._save_data()
        return True

#1634085070
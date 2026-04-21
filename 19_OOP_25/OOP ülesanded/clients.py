"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        get_earnings_per_day = self.current_amount / self.account_age
        return get_earnings_per_day


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    # Loome objekti ja lisame listi
                    new_client = Client(
                        parts[0].strip(),
                        parts[1].strip(),
                        int(parts[2]),
                        int(parts[3]),
                        int(parts[4])
                    )
                    clients.append(new_client)
    except (FileNotFoundError, ValueError):
        return []
    return clients


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people (Client objects).
    """
    all_clients = read_from_file_into_list(filename)
    # TAGASTAME OBJEKTID, mitte ainult nimed
    return [client for client in all_clients if client.bank == bank]

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) < 2:
                    continue

                current_bank = parts[1].strip()

                if current_bank == bank:
                    clients.append(parts[0].strip())

    except FileNotFoundError:
        print(f"Viga: Faili nimega '{filename}' ei leitud!")
        return []

    return [client.name for client in all_clients if client.bank == bank]


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    clients = read_from_file_into_list(filename)

    best_client = None
    max_rate = -1.0

    for client in clients:
        total_earned = client.current_amount - client.starting_amount

        if total_earned <= 0:
            continue

        current_rate = total_earned / client.account_age

        if (best_client is None) or (current_rate > max_rate) or (current_rate == max_rate and client.account_age < best_client.account_age):

            max_rate = current_rate
            best_client = client

    return best_client


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    clients = read_from_file_into_list(filename)

    worst_client = None
    max_rate = -1.0

    for client in clients:
        total_lost = (client.starting_amount - client.current_amount)

        if total_lost <= 0:
            continue

        current_loss = total_lost / client.account_age

        if (worst_client is None) or (current_loss > max_rate) or (current_loss == max_rate and client.account_age < worst_client.account_age):

            max_rate = current_loss
            worst_client = client

    return worst_client


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz

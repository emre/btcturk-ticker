
import requests

template = """
    {}
    {:8}{:>19}{:>19}{:>19}{:>20}
    \033[01m{:>5} TL\033[0m{:>16} TL{:>16} TL{:>16} TL{:>16} BTC
    {:>80}
    {}  price info fetched from btcturk.com API.
"""

money_bag = "\xF0\x9F\x92\xB0"


def main():
    json_data = requests.get("https://www.btcturk.com/api/ticker").json()
    print template.format(
        "-" * 88,
        "ask",
        "bid",
        "high",
        "low",
        "volume",
        json_data["ask"],
        json_data["bid"],
        json_data["high"],
        json_data["low"],
        json_data["volume"],
        "-" * 88,
        money_bag,
    )

if __name__ == '__main__':
    main()
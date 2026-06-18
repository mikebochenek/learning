"""
https://claude.ai/chat/a836a831-21bd-435a-8205-54539c1aaa2f
World Cup 2026 results checker.

FIFA does not publish a free public API, so this uses two free
third-party sources instead:
  1. openfootball/worldcup.json  — fully free, no API key, open data
     (https://github.com/openfootball/worldcup.json)
  2. football-data.org          — free tier, requires a free API key
     (https://www.football-data.org)

Run with just `python wc2026_results.py` to use source #1.
Set FOOTBALL_DATA_API_KEY to also pull from source #2.
"""
import os
import requests

OPENFOOTBALL_URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"
FOOTBALL_DATA_URL = "https://api.football-data.org/v4/competitions/WC/matches"

def get_results_openfootball():
    """Free, no API key required."""
    resp = requests.get(OPENFOOTBALL_URL, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    results = []
    for m in data.get("matches", []):
        score = m.get("score", {}).get("ft")
        if score:  # only matches that have been played
            results.append({
                "date": m["date"],
                "team1": m["team1"],
                "team2": m["team2"],
                "score": f"{score[0]}-{score[1]}",
                "group": m.get("group", m.get("round")),
            })
    return results

def get_results_football_data(api_key):
    """Requires a free API key from football-data.org."""
    headers = {"X-Auth-Token": api_key}
    resp = requests.get(FOOTBALL_DATA_URL, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    results = []
    for m in data.get("matches", []):
        if m["status"] == "FINISHED":
            home = m["homeTeam"]["name"]
            away = m["awayTeam"]["name"]
            score = m["score"]["fullTime"]
            results.append({
                "date": m["utcDate"][:10],
                "team1": home,
                "team2": away,
                "score": f"{score['home']}-{score['away']}",
                "group": m.get("group"),
            })
    return results

def print_results(results, source_name):
    print(f"\n=== Results from {source_name} ===")
    if not results:
        print("No finished matches found yet.")
        return
    for r in results:
        print(f"{r['date']}  {r['team1']} {r['score']} {r['team2']}  ({r['group']})")

if __name__ == "__main__":
    # Source 1: always free, no key needed
    try:
        results = get_results_openfootball()
        print_results(results, "openfootball/worldcup.json")
    except requests.RequestException as e:
        print(f"openfootball source failed: {e}")

    # Source 2: optional, only runs if you set an API key
    api_key = os.environ.get("FOOTBALL_DATA_API_KEY")
    if api_key:
        try:
            results = get_results_football_data(api_key)
            print_results(results, "football-data.org")
        except requests.RequestException as e:
            print(f"football-data.org source failed: {e}")
    else:
        print("\n(Tip: set FOOTBALL_DATA_API_KEY env var to also check football-data.org)")

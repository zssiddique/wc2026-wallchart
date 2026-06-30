#!/usr/bin/env python3
"""
Fetches live World Cup 2026 scores from one of several sources and
writes them into scores.json at the repo root.

This script is called by .github/workflows/pages.yml with the
source name as argv[1] and the raw response saved at /tmp/raw.json.
"""
import json
import sys
import datetime

NAME_MAP = {
    'United States': 'USA',
    'Bosnia-Herzegovina': 'Bosnia & Herz.',
    'Bosnia & Herzegovina': 'Bosnia & Herz.',
    "Côte d'Ivoire": 'Ivory Coast',
    "Cote d'Ivoire": 'Ivory Coast',
    'Cape Verde Islands': 'Cape Verde',
    'Cabo Verde': 'Cape Verde',
    'Democratic Republic of Congo': 'DR Congo',
    'Congo DR': 'DR Congo',
    'Korea Republic': 'South Korea',
    'Republic of Korea': 'South Korea',
    'Czech Republic': 'Czechia',
}


def norm(name):
    return NAME_MAP.get(name, name) if name else name


def parse_worldcup26ir(data):
    matches = []
    raw_list = data if isinstance(data, list) else data.get('games', data.get('matches', []))
    for m in raw_list:
        stage = (m.get('stage') or m.get('round') or m.get('phase') or '').lower()
        is_ko = any(x in stage for x in ('round', 'quarter', 'semi', 'final', 'knockout'))
        home_name = norm(m.get('homeTeam', {}).get('name') or m.get('home', ''))
        away_name = norm(m.get('awayTeam', {}).get('name') or m.get('away', ''))
        try:
            home_score = int(m.get('homeScore') or m.get('home_score') or
                              (m.get('score') or {}).get('home', -1))
            away_score = int(m.get('awayScore') or m.get('away_score') or
                              (m.get('score') or {}).get('away', -1))
        except (TypeError, ValueError):
            continue
        if home_score < 0 or away_score < 0:
            continue
        entry = {'home': home_name, 'away': away_name, 'hs': home_score, 'as_': away_score}
        if is_ko:
            matches.append(('knockout', entry))
        else:
            matches.append(('group', entry))
    return matches


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_scores.py <source_name>")
        sys.exit(1)

    source = sys.argv[1]

    try:
        with open('/tmp/raw.json') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as exc:
        print(f"Could not parse /tmp/raw.json: {exc}")
        sys.exit(0)

    if source == 'worldcup26.ir':
        parsed = parse_worldcup26ir(data)
    else:
        print(f"No parser implemented for source '{source}', skipping.")
        sys.exit(0)

    group_matches = [e for kind, e in parsed if kind == 'group']
    knockout_matches = [e for kind, e in parsed if kind == 'knockout']

    out = {
        'source': source,
        'fetched': datetime.datetime.utcnow().isoformat() + 'Z',
        'matches': group_matches,
        'knockout': knockout_matches,
    }

    with open('scores.json', 'w') as f:
        json.dump(out, f, indent=2)

    print(f"Wrote {len(group_matches)} group matches and "
          f"{len(knockout_matches)} knockout matches from {source}")


if __name__ == '__main__':
    main()

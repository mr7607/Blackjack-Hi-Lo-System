"""
Blackjack Card Counting — Hi-Lo System
=======================================
Simulates a single-deck blackjack shoe and tracks:
  - Running Count  : raw Hi-Lo tally
  - True Count     : running count ÷ decks remaining
  - Betting Signal : suggested action based on true count

Input: type a card rank (e.g. 2, 3, 10, J, Q, K, A) — suits are not needed.
"""

import random

# ── Card Definitions ──────────────────────────────────────────────────────────

RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def build_deck():
    """Build and return a standard 52-card deck (4 of each rank)."""
    return [r for r in RANKS for _ in range(4)]

def shuffle_deck(deck):
    """Shuffle the deck in-place."""
    random.shuffle(deck)
    return deck

# ── Hi-Lo Count Value ─────────────────────────────────────────────────────────

def hilo_value(rank):
    """Return the Hi-Lo count value for a given card rank."""
    if rank in ['2', '3', '4', '5', '6']:
        return +1
    elif rank in ['7', '8', '9']:
        return 0
    else:          # 10, J, Q, K, A
        return -1

# ── Betting Signal ────────────────────────────────────────────────────────────

def betting_signal(true_count):
    """Return an emoji signal and advice string based on the true count."""
    if true_count < 0:
        return "🔴", "Negative deck  — bet MINIMUM or sit out"
    elif true_count < 1:
        return "⚪", "Neutral deck   — flat bet, no clear edge"
    elif true_count < 2:
        return "🟡", "Slight edge    — consider a small raise"
    elif true_count < 3:
        return "🟢", "Good edge      — raise your bet"
    else:
        return "🔵", "STRONG edge    — MAX BET!"

# ── Display Helpers ───────────────────────────────────────────────────────────

def print_header():
    print("\n" + "=" * 52)
    print("   ♠  BLACKJACK CARD COUNTER  —  Hi-Lo System  ♥")
    print("=" * 52)


def print_reference_table():
    print("\n  Hi-Lo Reference:")
    print("  ┌─────────────────────┬───────┐")
    print("  │ Cards               │ Value │")
    print("  ├─────────────────────┼───────┤")
    print("  │ 2  3  4  5  6       │  +1   │")
    print("  │ 7  8  9             │   0   │")
    print("  │ 10 J  Q  K  A       │  -1   │")
    print("  └─────────────────────┴───────┘")

def print_state(running_count, true_count, cards_dealt, deck_size):
    decks_left = deck_size / 52
    emoji, advice = betting_signal(true_count)
    sign = "+" if running_count >= 0 else ""

    print(f"\n  {'─'*46}")
    print(f"  Running Count : {sign}{running_count}")
    print(f"  True Count    : {'+' if true_count >= 0 else ''}{true_count:.2f}")
    print(f"  Cards Dealt   : {cards_dealt}  |  Decks Left: {decks_left:.2f}")
    print(f"  Signal        : {emoji}  {advice}")
    print(f"  {'─'*46}")

def print_remaining(deck):
    """Show how many of each rank remain in the deck."""
    counts = {r: deck.count(r) for r in RANKS}
    print("\n  Remaining cards:")
    row = "  " + "  ".join(f"{r}:{counts[r]}" for r in RANKS)
    print(row)

# ── Main Session ──────────────────────────────────────────────────────────────

def run_session():
    print_header()
    print_reference_table()

    deck = shuffle_deck(build_deck())
    running_count = 0
    cards_dealt   = 0
    history       = []

    print("\n  Enter a card rank to deal it  (e.g. 2  5  10  J  Q  K  A)")
    print("  Commands:  [r] reset   |  [q] quit   |  [?] show remaining\n")

    while True:
        cmd = input("  > ").strip().upper()

        if cmd == 'Q':
            print("\n  Thanks for playing. Good luck at the tables! ♠\n")
            break

        elif cmd == 'R':
            deck = shuffle_deck(build_deck())
            running_count = 0
            cards_dealt   = 0
            history       = []
            print("\n  ♻  Deck shuffled. New shoe started.")
            print_state(running_count, 0.0, cards_dealt, len(deck))

        elif cmd == '?':
            print_remaining(deck)

        elif cmd in RANKS:
            if cmd not in deck:
                print(f"\n  ⚠  No '{cmd}' cards left in the deck.")
                continue

            deck.remove(cmd)          # remove one instance of that rank
            value = hilo_value(cmd)
            running_count += value
            cards_dealt   += 1
            history.append(cmd)

            decks_left  = max(len(deck) / 52, 0.01)
            true_count  = running_count / decks_left
            sign        = "+" if value > 0 else ("" if value < 0 else "±")
            val_str     = f"{sign}{value}"

            print(f"\n  Card dealt : {cmd:>3}   Count value: [{val_str}]")
            print(f"  Last 5     : {' '.join(history[-5:])}")
            print_state(running_count, true_count, cards_dealt, len(deck))

        else:
            print(f"  Unknown input '{cmd}'. Enter a rank (A 2 3 … 10 J Q K), 'r' to reset, 'q' to quit.")

# ── Demo Mode (auto-deal full deck) ──────────────────────────────────────────

def run_demo(num_cards=20):
    """Auto-deal `num_cards` cards and print the running count progression."""
    print_header()
    print(f"\n  AUTO DEMO — dealing {num_cards} cards from a shuffled deck\n")
    print(f"  {'Card':<6} {'Value':>6} {'Running':>9} {'True':>8}  Signal")
    print(f"  {'─'*55}")

    deck = shuffle_deck(build_deck())
    running = 0

    for i in range(min(num_cards, 52)):
        card  = deck.pop()
        value = hilo_value(card)
        running += value

        cards_dealt = i + 1
        decks_left  = max(len(deck) / 52, 0.01)
        true_count  = running / decks_left
        sign        = "+" if value > 0 else ("" if value < 0 else "±")
        emoji, _    = betting_signal(true_count)
        tc_sign     = "+" if true_count >= 0 else ""

        print(f"  {card:<6} {sign+str(value):>6} {('+' if running>=0 else '')+str(running):>9}"
              f" {tc_sign+f'{true_count:.2f}':>8}  {emoji}")

    print(f"  {'─'*55}")
    print(f"\n  Final running count : {('+' if running>=0 else '')}{running}")
    print(f"  Cards dealt         : {num_cards}")
    decks_left = max(len(deck) / 52, 0.01)
    final_true = running / decks_left
    emoji, advice = betting_signal(final_true)
    print(f"  Final true count    : {('+' if final_true>=0 else '')}{final_true:.2f}")
    print(f"  Verdict             : {emoji}  {advice}\n")

# ── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        run_demo(num_cards=n)
    else:
        run_session()
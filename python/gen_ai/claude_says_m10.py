# https://claude.ai/chat/f4424726-e909-49cf-b7b8-d9ae9e379de0

# What books did alice and bob BOTH read? (&)
# What if we pool them together? (|)
# What books did ONLY ONE of them read? (^ NEW)

alice = Counter({'dune': 3, 'hobbit': 2, 'hyperion': 1})
bob   = Counter({'dune': 1, 'hobbit': 3, 'foundation': 2})

print(alice & bob)   # intersection (min counts)
print(alice | bob)   # union (max counts)
print(alice ^ bob)   # ← NEW: symmetric difference!

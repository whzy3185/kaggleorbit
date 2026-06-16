# Opponent Profile Examples

Date: 2026-06-16

Synthetic test case:

```text
Enemy owns planet 1.
Enemy launches fleet 9 with 30 ships toward our planet.
Profiler observes one new enemy fleet.
```

Expected profile:

```yaml
enemy_id: 1
observed_new_fleets: 1
total_ships_sent: 30
confidence: greater_than_zero
scores:
  enemy_rusher: present
```

Interpretation:

One fleet is not enough to force a counter-strategy. It only raises a weak
signal. Counter policies must multiply profile scores by confidence and use
thresholds before changing reserve, defense, expansion, or attack weights.


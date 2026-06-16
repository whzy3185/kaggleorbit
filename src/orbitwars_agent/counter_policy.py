from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .opponent_profiler import OpponentProfile


@dataclass
class StrategyModifiers:
    reserve_floor_delta: int = 0
    defense_weight_mult: float = 1.0
    expansion_weight_mult: float = 1.0
    attack_weight_mult: float = 1.0
    center_weight_mult: float = 1.0
    comet_weight_mult: float = 1.0
    counterattack_bonus: float = 0.0
    risky_expand_penalty: float = 1.0
    max_commit_ratio_delta: float = 0.0
    target_enemy_bias: float = 1.0


def effective(profile: OpponentProfile, key: str) -> float:
    return profile.scores.get(key, 0.0) * profile.confidence


def build_strategy_modifiers(profiles: Dict[int, OpponentProfile]) -> StrategyModifiers:
    mods = StrategyModifiers()
    if not profiles:
        return mods

    enemy_rush = max(effective(profile, "enemy_rusher") for profile in profiles.values())
    neutral_rush = max(effective(profile, "neutral_rusher") for profile in profiles.values())
    turtle = max(effective(profile, "turtle") for profile in profiles.values())
    big_stack = max(effective(profile, "big_stack") for profile in profiles.values())
    overcommit = max(effective(profile, "overcommitter") for profile in profiles.values())
    comet = max(effective(profile, "comet_greedy") for profile in profiles.values())

    if enemy_rush > 0.55:
        mods.reserve_floor_delta += 6
        mods.defense_weight_mult *= 1.4
        mods.expansion_weight_mult *= 0.9
        mods.risky_expand_penalty *= 1.25
        mods.max_commit_ratio_delta -= 0.10

    if neutral_rush > 0.55:
        mods.counterattack_bonus += 10.0
        mods.expansion_weight_mult *= 0.95
        mods.target_enemy_bias *= 1.08

    if turtle > 0.55:
        mods.attack_weight_mult *= 0.80
        mods.expansion_weight_mult *= 1.25
        mods.comet_weight_mult *= 1.15

    if big_stack > 0.55:
        mods.defense_weight_mult *= 1.25
        mods.counterattack_bonus += 8.0

    if overcommit > 0.55:
        mods.counterattack_bonus += 12.0
        mods.max_commit_ratio_delta += 0.08

    if comet > 0.55:
        mods.comet_weight_mult *= 1.25

    return mods


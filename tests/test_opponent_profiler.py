from orbitwars_agent.opponent_profiler import OpponentProfiler
from orbitwars_agent.world_model import build_game_state


def test_profiler_records_new_enemy_fleet_and_scores():
    profiler = OpponentProfiler()
    prev = build_game_state(
        {
            "player": 0,
            "step": 1,
            "planets": [
                [0, 0, 10.0, 10.0, 2.0, 20, 2],
                [1, 1, 80.0, 80.0, 2.0, 40, 2],
                [2, -1, 60.0, 80.0, 2.0, 6, 4],
            ],
            "initial_planets": [],
            "fleets": [],
            "comet_planet_ids": [],
            "angular_velocity": 0.0,
        }
    )
    profiler.update(prev)

    current = build_game_state(
        {
            "player": 0,
            "step": 2,
            "planets": prev.planets,
            "initial_planets": [],
            "fleets": [
                [9, 1, 79.0, 80.0, 3.1415926535, 1, 30],
            ],
            "comet_planet_ids": [],
            "angular_velocity": 0.0,
        }
    )
    profiles = profiler.update(current)
    profile = profiles[1]
    assert profile.observed_new_fleets == 1
    assert profile.total_ships_sent == 30
    assert profile.confidence > 0
    assert "enemy_rusher" in profile.scores


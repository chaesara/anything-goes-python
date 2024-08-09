import random
import json
from time import sleep


def check_s2_proc(proc_chance: float) -> int:
    return random.random() < proc_chance


# bat: base attack time
def calc_base_attack_speed(base_atk_speed, bat, attr_agi, bonus_atk_speed=0) -> float:
    r = (base_atk_speed + attr_agi + bonus_atk_speed) / (base_atk_speed * bat)
    T = 1 / r

    return T


def main() -> None:
    spirit_breaker_stats: dict = {
        "hp": 120,
        "mana": 75,
        "base_damage": 31,
        "move_speed": 295,
        "attr_str": 28 + 3.3,
        "attr_agi": 17 + 1.7,
        "attr_int": 14 + 1.8,
        "atk_rate": 0.53,
        "atk_range": 170,
        "atk_speed": 100,
        "atk_speed_bat": 1.7,
        "atk_animation": 0.6 + 0.3,
        "s2_proc_chance": 0.17,
        "s2_stun_duration": [0.9, 1.1, 1.3, 1.5],
    }

    spirit_breaker_stats["s2_damage"]: list[float] = [
        (0.25 * spirit_breaker_stats["move_speed"]), (0.3 * spirit_breaker_stats["move_speed"])]

    counter: int = 0
    time_takes_to_bash: float = 0
    total_damage: float = 0
    hero_level: int = 0
    while True:
        # Test the s2_proc_chance
        counter += 1
        time_between_atk = calc_base_attack_speed(
            spirit_breaker_stats["atk_speed"], spirit_breaker_stats["atk_speed_bat"], spirit_breaker_stats["attr_agi"])
        print(f"time between atk: {round(time_between_atk, 2)}s")
        time_takes_to_bash += time_between_atk
        sleep(time_between_atk)
        print(f"Hit no: {counter}")
        if check_s2_proc(spirit_breaker_stats["s2_proc_chance"]):
            total_damage += spirit_breaker_stats["s2_damage"][hero_level]
            print(f'Success! Bash damage: {spirit_breaker_stats["s2_damage"][hero_level]}')
            print(f'Total Damage        : {total_damage}')
            print(f'Time takes to bash  : {time_takes_to_bash}s')
            break
        else:
            total_damage += spirit_breaker_stats['base_damage']
            print("No bash proc this time.")


if __name__ == '__main__':
    main()

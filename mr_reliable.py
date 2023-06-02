import aiohttp
from prettytable import PrettyTable
from fpl import FPL


async def mr_reliable():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

    most_minutes_played = sorted(players, key=lambda x: x.minutes, reverse=True)

    player_table = PrettyTable()
    player_table.field_names = ["Player", "£", "Total Minutes", "Points Per Game"]
    player_table.align["Player"] = "l"

    for player in most_minutes_played[:100]:
        # float_ppg
        if float(player.points_per_game) > 4.0:
            # Filter out goalkeepers
            if player.element_type != 1:
                player_table.add_row(
                    [
                        player.web_name,
                        f"£{player.now_cost / 10}",
                        player.minutes,
                        player.points_per_game,
                    ]
                )

    print(player_table)

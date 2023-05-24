import aiohttp
from prettytable import PrettyTable
from fpl import FPL


async def bargains_in_form():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

    top_performers = sorted(players, key=lambda x: x.form, reverse=True)

    player_table = PrettyTable()
    player_table.field_names = ["Player", "£", "Form"]
    player_table.align["Player"] = "l"

    for player in top_performers[:100]:
        if player.now_cost < 60 and float(player.form) > 4.5:
            # Filter out goalkeepers
            if player.element_type != 1:
                player_table.add_row(
                    [player.web_name, f"£{player.now_cost / 10}", player.form]
                )

    print(player_table)

import aiohttp
from prettytable import PrettyTable
from fpl import FPL


async def most_transferred_players():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

    transfer_menu = int(
        input(
            "Do you want to see the most transferred in or out for the current GW?"
            "\n1 - Transfer Ins"
            "\n2 - Transfer Outs"
            "\n"
        )
    )

    player_table = PrettyTable()

    if transfer_menu == 1:
        most_transferred_in = sorted(
            players, key=lambda x: x.transfers_in_event, reverse=True
        )

        player_table.field_names = ["Player", "Transfers in", "Form", "Total Points"]
        player_table.align["Player"] = "l"

        for player in most_transferred_in[:10]:
            player_table.add_row(
                [
                    player.web_name,
                    player.transfers_in_event,
                    player.form,
                    player.total_points,
                ]
            )

        print(player_table)
    elif transfer_menu == 2:
        most_transferred_out = sorted(
            players, key=lambda x: x.transfers_out_event, reverse=True
        )

        player_table.field_names = ["Player", "Transfers out", "Form", "Total Points"]
        player_table.align["Player"] = "l"

        for player in most_transferred_out[:10]:
            player_table.add_row(
                [
                    player.web_name,
                    player.transfers_out_event,
                    player.form,
                    player.total_points,
                ]
            )

        print(player_table)

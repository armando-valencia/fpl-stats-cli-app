import asyncio
import aiohttp
from prettytable import PrettyTable
from fpl import FPL


async def back_to_menu():
    menu_selection = input("\nWant to go back to the main menu?(y/n) ")

    if menu_selection == "y":
        await main()


async def goals_contribution_leaders():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()

    top_performers = sorted(
        players, key=lambda x: x.goals_scored + x.assists, reverse=True
    )

    player_table = PrettyTable()
    player_table.field_names = ["Player", "£", "G", "A", "G + A"]
    player_table.align["Player"] = "l"

    for player in top_performers[:10]:
        goals = player.goals_scored
        assists = player.assists
        player_table.add_row(
            [
                player.web_name,
                f"£{player.now_cost / 10}",
                goals,
                assists,
                goals + assists,
            ]
        )

    print(player_table)

    await back_to_menu()


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

    await back_to_menu()


async def main():
    menu_selection = int(
        input(
            "What would you like to see?"
            "\n1 - Goal Contribution Leaders"
            "\n2 - Most Transferred Players (this GW)"
            "\n"
        )
    )

    if menu_selection == 1:
        await goals_contribution_leaders()
    elif menu_selection == 2:
        await most_transferred_players()


asyncio.run(main())

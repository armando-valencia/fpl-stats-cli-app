import asyncio
from fpl import FPL

from goal_contributions import goals_contribution_leaders
from most_transferred import most_transferred_players


async def back_to_menu():
    menu_selection = input("\nWant to go back to the main menu?(y/n) ")

    if menu_selection == "y":
        await main()


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

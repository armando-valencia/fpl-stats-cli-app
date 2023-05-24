import asyncio
from fpl import FPL

from goal_contributions import goals_contribution_leaders
from most_transferred import most_transferred_players
from bargains_in_form import bargains_in_form


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
            "\n3 - Bargains in Form"
            "\n"
        )
    )

    if menu_selection == 1:
        # Players with the most goals and assists combined
        await goals_contribution_leaders()
    elif menu_selection == 2:
        # Most transferred players this GW
        await most_transferred_players()
    elif menu_selection == 3:
        # Players in the top 100 in form and under £6.0m (excl GKs)
        await bargains_in_form()


asyncio.run(main())

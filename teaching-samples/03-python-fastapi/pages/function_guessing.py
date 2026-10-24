"""
Functions: a guessing game built from several small functions.

The computer envisions a number, and the player tries to reveal it
in a limited number of guesses.
"""

import random
from typing import Annotated

from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse

from templating import templates

router = APIRouter()

upper_limit = 100

lower_limit = 1

envisioned_number = -1

new_guess = 0

guesses_so_far = 1

max_guesses = 7

message = "Press button 'Start Game'"

user_lost = False

game_started = False


def guess_section_should_be_visible() -> bool:
    return game_started and not user_lost


def start_game_message(ll: int, ul: int, mg: int) -> str:
    return f"I envisioned a number between {ll} and {ul}.\nTry to reveal it in {mg} guesses.\n"


def win_message(ng: int, gsf: int) -> str:
    s = f"CONGRATULATIONS! YOU WIN! Number {ng} is the envisioned one!\n"
    s += f"You revealed it in {gsf} guesses.\n"
    s += "For new game, press button 'Start Game'"
    return s


def lose_message(en: int) -> str:
    s = f"SORRY! YOU LOSE! Number is {en}!\n"
    s += "For new game, press button 'Start Game'"
    return s


@router.get("/function-guessing")
def show(request: Request):
    return templates.TemplateResponse(
        request,
        "function_guessing.html",
        {
            "lower_limit": lower_limit,
            "upper_limit": upper_limit,
            "max_guesses": max_guesses,
            "new_guess": new_guess,
            "message": message,
            "guess_section_visible": guess_section_should_be_visible(),
        },
    )


@router.post("/function-guessing/start")
def start_game(
    lower: Annotated[int, Form()],
    upper: Annotated[int, Form()],
    guesses: Annotated[int, Form()],
):
    global lower_limit, upper_limit, max_guesses
    global game_started, new_guess, guesses_so_far, user_lost, envisioned_number, message

    lower_limit = lower
    upper_limit = upper
    max_guesses = guesses

    game_started = True
    new_guess = 0
    guesses_so_far = 1
    user_lost = False
    envisioned_number = random.randint(lower_limit, upper_limit)  # both limits are included
    message = start_game_message(lower_limit, upper_limit, max_guesses)

    return RedirectResponse("/function-guessing", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/function-guessing/check")
def check_guess(guess: Annotated[int, Form()]):
    global new_guess, guesses_so_far, user_lost, game_started, message

    new_guess = guess
    if envisioned_number == new_guess:
        message += win_message(new_guess, guesses_so_far)
        game_started = False
    elif envisioned_number > new_guess:
        if guesses_so_far >= max_guesses:
            message += lose_message(envisioned_number)
            user_lost = True
        else:
            message += f"Sorry, envisioned number is greater than {new_guess}\n"
    else:
        if guesses_so_far >= max_guesses:
            message += lose_message(envisioned_number)
            user_lost = True
        else:
            message += f"Sorry, envisioned number is less than {new_guess}\n"
    guesses_so_far += 1

    return RedirectResponse("/function-guessing", status_code=status.HTTP_303_SEE_OTHER)

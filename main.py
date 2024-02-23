"""Checks if a number is even or odd in the stupidest way possible"""
import argparse
import sys
import pymsgbox


def even_or_odd(num: int) -> str:
    """Say if a number is even or odd"""
    return "eovdedn"[num % 2:: 2]


if __name__ == "__main__":
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        pymsgbox.alert(
            "The Number is" + even_or_odd(
                int(
                    pymsgbox.prompt(
                        "Enter a number to check",
                        "Enter a number",
                    )
                )
            ),
            "Answer"
        )
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("num", help="Number to check for oddness")
        args = parser.parse_args()
        print(even_or_odd(args.num))

#!/usr/bin/env python3
import sys
from contextlib import suppress
from time import sleep

from plumbum import FG, CommandNotFound, local
from plumbum.cli import Application, Flag
from plumbum.cli.terminal import ask, choose
from plumbum.colors import blue, green, magenta, yellow
from rarbgapi import RarbgAPI


def search(search_terms, adult=False):
    search_args = {'search_string': ' '.join(search_terms), 'extended_response': True}
    if adult:
        search_args['categories'] = [RarbgAPI.CATEGORY_ADULT]
    results = None
    max_attempts = 6
    attempts = max_attempts
    while attempts and not results:
        if attempts < max_attempts:
            print(f"Retrying . . .")
            sleep(1)
        results = {
            ' '.join((
                r.filename,
                str(r.seeders) | green,
                str(r.leechers) | yellow,
                f"{r.size / 1024**3:.2f} GiB" | blue,
                r.pubdate.split()[0] | magenta
            )): r.download
            for r in RarbgAPI().search(**search_args)
        }
        attempts -= 1
    return results


def choose_result(results):
    results.update({"Nothing": 'None'})
    uri = choose("What should we get?" | magenta, results, default='None')
    return {'None': None}.get(uri, uri)


def show_connection():
    try:
        print(local['mullvad']('status', '-l') | yellow)
    except CommandNotFound:
        try:
            print((
                local['nmcli']['-o']
                | local['grep']['-E', '^[^ ]+: connected']
            )() | yellow)
        except CommandNotFound:
            try:
                print(local['https']('--body', 'ipinfo.io') | yellow)
            except CommandNotFound:
                try:
                    print(local['curl']('ipinfo.io') | yellow)
                except CommandNotFound:
                    print(local['wget']('-qO', '-', 'ipinfo.io') | yellow)


def clip(text):
    try:
        (((local['xclip']['-sel', 'clip'] > sys.stdout) >= sys.stderr) << text)()
    except CommandNotFound:
        (((local['pbcopy'] > sys.stdout) >= sys.stderr) << text)()


class NoResults(Exception): pass


class Rawr(Application):

    VERSION = '0.0.1'
    adult = Flag(['a', 'adult'], help="Search (only) in the 'adult' category")

    def main(self, *search_terms):
        try:
            results = search(search_terms, adult=self.adult)
        except KeyboardInterrupt:
            results = None
        if not results:
            raise NoResults

        with suppress(CommandNotFound):
            print(
                f"{local['df']('-h', '-P', '.').splitlines()[-1].split()[3]} available"
            | yellow)
        uri = choose_result(results)
        if not uri:
            return
        try:
            clip(uri)
        except CommandNotFound:
            print(uri | blue)
        else:
            print("Magnet URI copied to clipboard" | green)

        show_connection()
        try:
            aria2c = local['aria2c']
        except CommandNotFound:
            print(
                "If I'd found the 'aria2c' command, I'd have offered to launch it for you."
            | yellow)
        else:
            if ask("Begin download with aria2" | magenta, True):
                # try:
                aria2c['--seed-time=0', uri] &FG
                # except KeyboardInterrupt:
                # TODO: really kill that aria2c proc


Rawr.unbind_switches('help-all')


if __name__ == '__main__':
    Rawr()

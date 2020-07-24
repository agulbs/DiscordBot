from argparse import ArgumentParser as ArgParser
import configparser
from pprint import pprint
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

def main():
    arg_parser = ArgParser()
    arg_parser.add_argument(
        '-s',
        '--config_file',
        help = '.ini config file',
        required = True,
    )

    cfg = configparser.ConfigParser()
    cfg.read(arg_parser.parse_args().config_file)

    token = cfg.get('discord','token')
    bot_attr = {}
    for option in cfg.options('bot'):
        bot_attr[option] = cfg.get('bot', option)


    client.run(token)



if __name__ == '__main__':
    main()

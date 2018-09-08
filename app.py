import json
import random

JOKES = [
    "Two satellites decided to get married. The wedding wasn't much but the reception was incredible.",
    "Last night I dreamt I was a muffler. I woke up exhausted.",
    "Why can't you have a nose that's 12 inches long? Because then it'd be a foot!",
    "Have you heard of the new band 1023MB? They haven't got a gig yet.",
    "I just watched a program about beavers. It was the best dam program I've ever seen.",
    "I hate jokes about German sausages. They're the wurst.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Want to hear a joke about a piece of paper? Never mind... it's tearable",
    "If you see a robbery at an Apple Store does that make you an iWitness?",
    "A ham sandwich walks into a bar and orders a beer. The bartender says, \"Sorry we don’t serve food here.\"",
    "What’s Forrest Gump’s password? 1forrest1",
    "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!",
    "I used to have a job at a calendar factory but I got the sack because I took a couple of days off.",
    "A three-legged dog walks into a bar and says to the bartender, \"I’m looking for the man who shot my paw.\"",
    "Two guys walk into a bar. The third one ducks.",
    "Don't trust atoms. They make up everything!",
    "How many tickles does it take to make an octopus laugh? Ten-tickles.",
    "Why couldn't the bike standup by itself? It was two tired.",
    "What do you call a dog that can do magic? A Labracadabrador.",
    "Who was the fattest knight at King Arthur's round table? Sir Cumference.",
    "What do you get when you cross a snowman with a vampire? Frostbite.",
    "What do you call a deer with no eyes? No idea!",
    "What does a zombie vegetarian eat? \"GRRRAAAAAIIIINNNNS!\"",
    "Why wasn't the woman happy with the velcro she bought? It was a total ripoff.",
    "What did the buffalo say to his son when he dropped him off at school? Bison.",
    "Why do crabs never share? Because they're shellfish",
    "Why don’t skeletons ever go trick or treating? Because they have nobody to go with.",
    "Why do scuba divers fall backwards into the water? Because if they fell forwards they’d still be in the boat.",
    "Why are skeletons so calm? Because nothing gets under their skin.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "I know this great restaurant on the moon. The food is great but there is no atmosphere.",
]


def main(data, context):
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({'text': random.choice(JOKES), 'response_type': 'in_channel'})
    }

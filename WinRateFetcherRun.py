import api_request as api
import matplotlib.pyplot as plt
import time


plt.style.use('ggplot')

REGIONS = {
    "br": "br1",
    "eune": "eun1",
    "euw": "euw1",
    "jp": "jp1",
    "kr": "kr",
    "lan": "la1",
    "las": "la2",
    "na": "na1",
    "oce": "oc1",
    "tr": "tr1",
    "ru": "ru"
}

# Queue codes:
# 400 - 5v5 Draft Pick
# 420 - 5v5 Ranked Solo
# 430 - 5v5 Blind Pick
# 440 - 5v5 Ranked Flex
# 450 - 5v5 ARAM
QUEUES = {
    'draft': 400,
    'solo': 420,
    'blind': 430,
    'flex': 440,
    'aram': 450
}


def routingSelector(region):
    """
    Match history data uses routing regions instead
    """
    if region in ["na", "br", "lan", "las", "oce"]:
        return "americas"
    if region in ["kr", "jp"]:
        return "asia"
    if region in ["eune", "euw", "tr", "ru"]:
        return "europe"
    assert False, "not matched"


if __name__ == "__main__":
    # Prompt user for inputs
    region = ""
    while region not in REGIONS:
        print("Region? (i.e. NA)")
        region = input().lower()

    routing = routingSelector(region)
    region = REGIONS[region]

    # Does not verify input for summoner name
    print("Summoner Name?")
    summonerName = input()

    queue = ""
    # Verify queue input validation
    while queue not in QUEUES:
        print("Which queue?")
        queue = input().lower()

    queueCode = QUEUES[queue]

    print("Loading...")

    # Gets start and end time for the function
    start = time.time()

    # Gets list of champions & their winrates as a pair of lists, in order of number of games played
    summonerId = api.getSummonerId(summonerName, region)
    matchlist = api.getMatchList(summonerId, queueCode, routing)
    api.displayWinrates(summonerId, matchlist, routing)
    api.csKdaGetter(summonerId, matchlist, routing)

    end = time.time()
    print(f"Data acquired in {end-start:.2f} seconds.")


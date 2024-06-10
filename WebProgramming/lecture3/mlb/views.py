from django.shortcuts import render

al_teams = {"EAST": ["Blue Jays", "Yankees", "Orioles", "Red Sox", "Rays"],
         "CENTRAL": ["White Sox", "Tigers", "Twins", "Royals", "Indians"],
         "WEST": ["Astros", "Angels", "Mariners", "Rangers", "Athletics"]}

nl_teams = { "EAST": ["Phillies", "Braves", "Mets", "Marlins", "Nationals"],
            "CENTRAL": ["Brewers", "Pirates", "Cardinals", "Reds"],
            "WEST": ["Dodgers", "Padres", "Rockies", "Giants", "Diamondbacks"]
            }
# Create your views here.
def index(request):
    return render(request, "mlb/index.html", {
        "al_teams": al_teams,
        "nl_teams": nl_teams
    })

def getTeam(request, team):
    return render(request, "mlb/index.html", {
        "teams": al_teams["AL EAST"]
    })
from collections import deque

graph = {}
graph['me'] = ['morg', 'joao', 'matheus', 'pedrao']
graph['morg'] = ['anaju', 'silva', 'kairosg', 'pedrao', 'ju', 'platiny']
graph['matheus'] = ['leticia', 'joao']
graph['joao'] = ['matheus']
graph['silva'] = ['morg']
graph['anaju'] = ['ju']
graph['ju'] = ['anaju']
graph['pedrao'] = ['platiny', 'gabriel', 'torinha']
graph['platiny'] = ['pedrao', 'gabriel', 'torinha', 'morg']
graph['gabriel'] = ['platiny', 'gabriel', 'torinha']
graph['leticia'] = []


person_attributes = {
    'kairos': {'play_lol': False},
    'joao': {'play_lol': True},
    'morg': {'play_lol': True},
    'matheus': {'play_lol': False},
    'pedrao': {'play_lol': True},
    'anaju': {'play_lol': False},
    'silva': {'play_lol': False},
    'ju': {'play_lol': False},
    'leticia': {'play_lol': False},
    'platiny': {'play_lol': True},
    'gabriel': {'play_lol': False},
    'torinha': {'play_lol': True}

}


def person_play_lol(name):
    return person_attributes.get(name, {}).get('play_lol', False)

def search(name):
    queue_search = deque()  
    queue_search += graph[name] 
    verify = []
    lol_players = []

    while queue_search:
        person = queue_search.popleft()
        if not person in verify:
            if person_play_lol(person):
                lol_players.append(person)
            queue_search += graph.get(person, [])
            verify.append(person)
    if lol_players:
        print('These people plays League of Legends:', ', '.join(lol_players))
    else:
        print('No people found who play League of Legends.')
    return lol_players
search('me')
# print(graph)
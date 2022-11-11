import random


INTERACTIVE_MODE = True
DEFAULT_PEOPLE = dict(
        geneve={'alim', 'eva'},
        st_blaise={'fabienne', 'imam'},
        haag={'omar', 'nicole'}
        )

def main():

    print('tirage au sort de noel')
    if INTERACTIVE_MODE:
        answer = input('entrer les noms de tous les foyers, séparés par des espace:\n')
        foyers = set(answer.split())

        people = dict()
        for foyer in foyers:
            answer = input(f'entrer le nom de toutes les personnes présentes dans {foyer}, séparés par des espaces:\n')
            personnes = set(answer.split())
            people[foyer] = personnes
    else:
        people = DEFAULT_PEOPLE

    results = list()

    last_foyer = None
    infra_gifts = 0
    first_foyer = None
    while people:
        people_to_draw = people.copy()
        if last_foyer in people_to_draw:
            if len(people_to_draw) > 1:
                people_to_draw.pop(last_foyer)
            else:
                infra_gifts += 1
        next_foyer = random.choices(list(people_to_draw), [len(val) for val in people_to_draw.values()])[0]
        next_person = people[next_foyer].pop()
        if not people[next_foyer]:
            people.pop(next_foyer)
        results.append(next_person)
        last_foyer = next_foyer
        if first_foyer is None:
            first_foyer = next_foyer
    if first_foyer == last_foyer:
        infra_gifts += 1
    if infra_gifts:
        print(f'il y a {infra_gifts} cadeau intra-foyers. refaite un tirage si nécessaire')
    results.append(results[0])
    for donneur, receveur in zip(results[:-1], results[1:]):
        print(f'{donneur} offre un cadeau à {receveur}')


if __name__ == '__main__':
    main()

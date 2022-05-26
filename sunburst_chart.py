import numpy as np
import matplotlib.pyplot as plt
import json

json_data = {
    "name": "flare",
    "children": [
        {
            "name": "Floral",
            "children": [
                {"name": "BLACK TEA", "value": 1},
                {
                    "name": "FLORAL",
                    "children": [
                        {"name": "CHAMOMILE", "value": 1},
                        {"name": "ROSE", "value": 1},
                        {"name": "JASMINE", "value": 1}
                    ],
                    "value": 3
                }
            ],
            "value": 4
        },
        {
            "name": "Fruit",
            "children": [
                {
                    "name": "BERRY",
                    "children": [
                        {"name": "BLACKBERRY", "value": 1},
                        {"name": "RASPBERRY", "value": 1},
                        {"name": "BLUEBERRY", "value": 1},
                        {"name": "STRAWBERRY", "value": 1}
                    ],
                    "value": 4
                },
                {
                    "name": "DRIED FRUIT",
                    "children": [
                        {"name": "RAISIN", "value": 1},
                        {"name": "PRUNE", "value": 1}
                    ],
                    "value": 2
                },
                {
                    "name": "OTHER FRUIT",
                    "children": [
                        {"name": "COCONUT", "value": 1},
                        {"name": "CHERRY", "value": 1},
                        {"name": "POMEGRANATE", "value": 1}
                    ],
                    "value": 3
                },
                {
                    "name": "CITRUS FRUIT",
                    "children": [
                        {"name": "GRAPEFRUIT", "value": 1},
                        {"name": "GRANGE", "value": 1},
                        {"name": "LEMON", "value": 1},
                        {"name": "LIME", "value": 1}
                    ],
                    "value": 4
                }
            ],
            "value": 13
        },
        {
            "name": "SOUR/FERMENTED",
            "children": [
                {
                    "name": "SOUR",
                    "children": [
                        {"name": "SOUR AROMATICS", "value": 1},
                        {"name": "ACETIC ACID", "value": 1},
                        {"name": "BUTYRIC ACID", "value": 1},
                        {"name": "ISOVALERIC ACID", "value": 1},
                        {"name": "CITRIC ACID", "value": 1},
                        {"name": "MALIC ACID", "value": 1}
                    ],
                    "value": 6
                },
                {
                    "name": "ALCOHOL/FERMENTED",
                    "children": [
                        {"name": "WINEY", "value": 1},
                        {"name": "WHISKEY", "value": 1},
                        {"name": "FERMENTED", "value": 1},
                        {"name": "OVERRIPE", "value": 1}
                    ],
                    "value": 4
                }
            ],
            "value": 10
        },
        {
            "name": "GREEN/VEGETATIVE",
            "children": [
                {"name": "OLIVE OIL", "value": 1},
                {"name": "RAW", "value": 1},
                {"name": "GREEN/VEGETATIVE",
                 "children": [
                     {"name": "UNDER-RIPE", "value": 1},
                     {"name": "PREAPOD", "value": 1},
                     {"name": "FRESH", "value": 1},
                     {"name": "DARK GREEN", "value": 1},
                     {"name": "VEGETATIVE", "value": 1},
                     {"name": "HAY-LIKE", "value": 1},
                     {"name": "HERB-LIKE", "value": 1}
                 ],
                 "value": 7},
                {"name": "BEANY", "value": 1}
            ],
            "value": 10
        },
        {
            "name": "OTHER",
            "children": [
                {
                    "name": "PAPERY/MUSTY",
                    "children": [
                        {"name": "PHENOLIC", "value": 1},
                        {"name": "MEATY BROTHY", "value": 1},
                        {"name": "ANIMALIC", "value": 1},
                        {"name": "MUSTY/EARTHY", "value": 1},
                        {"name": "MUSTY/DUSTY", "value": 1},
                        {"name": "MUSTY/DAMP", "value": 1},
                        {"name": "WOODY", "value": 1},
                        {"name": "PAPERY", "value": 1},
                        {"name": "CARDBOARD", "value": 1},
                        {"name": "STALE", "value": 1}
                    ],
                    "value": 10
                },
                {
                    "name": "CHEMICAL",
                    "children": [
                        {"name": "RUBBER", "value": 1},
                        {"name": "SKUNKY", "value": 1},
                        {"name": "PETROLEUM", "value": 1},
                        {"name": "MEDICINAL", "value": 1},
                        {"name": "SALTY", "value": 1},
                        {"name": "BITTER", "value": 1}
                    ],
                    "value": 6
                }
            ],
            "value": 16
        },
        {
            "name": "ROASTED",
            "children": [
                {"name": "TABACCO", "value": 1},
                {"name": "PIPE TOBACCO", "value": 1},
                {
                    "name": "CEREAL",
                    "children": [
                        {"name": "MALT", "value": 1},
                        {"name": "GRAIN", "value": 1}
                    ],
                    "value": 2
                },
                {
                    "name": "BURNT",
                    "children": [
                        {"name": "BROWN, ROAST", "value": 1},
                        {"name": "SMOKY", "value": 1},
                        {"name": "ASHY", "value": 1},
                        {"name": "ACRID", "value": 1}
                    ],
                    "value": 4
                }
            ],
            "value": 8
        },
        {
            "name": "SPICES",
            "children": [
                {"name": "PUNGENT", "value": 1},
                {"name": "PEPPER", "value": 1},
                {"name": "BROWN SPICE",
                 "children": [
                     {"name": "CLOVE", "value": 1},
                     {"name": "CINNAMON", "value": 1},
                     {"name": "NUTMEG", "value": 1},
                     {"name": "ANISE", "value": 1}
                 ],
                 "value": 4
                 }
            ],
            "value": 6
        },
        {
            "name": "NUTTY/COCOA",
            "children": [
                {
                    "name": "COCOA",
                    "children": [
                        {"name": "DARK CHOCOLATE", "value": 1},
                        {"name": "CHOCOLATE", "value": 1}
                    ],
                    "value": 2
                },
                {
                    "name": "NUTTY",
                    "children": [
                        {"name": "ALMOND", "value": 1},
                        {"name": "HAZELNUT", "value": 1},
                        {"name": "PEANUTS", "value": 1}
                    ],
                    "value": 3
                }
            ],
            "value": 5
        },
        {
            "name": "SWEET",
            "children": [
                {
                    "name": "BROWN SUGAR",
                    "children": [
                        {"name": "HONEY", "value": 1},
                        {"name": "CARAMELIZED", "value": 1},
                        {"name": "MAPLE SYRUP", "value": 1},
                        {"name": "MOLASSES", "value": 1}
                    ],
                    "value": 4
                },
                {"name": "VANILLA", "value": 1},
                {"name": "VANILLIN", "value": 1},
                {"name": "OVERALL SWEET", "value": 1},
                {"name": " SWEET AROMATICS", "value": 1}
            ],
            "value": 8
        }
    ],
    "value": 80
}


def sunburst(nodes, total=np.pi * 2, offset=0, level=0, ax=None):
    ax = ax or plt.subplot(111, projection='polar')

    if level == 0 and len(nodes) == 1:
        label, value, subnodes = nodes[0]
        ax.bar([0], [0.5], [np.pi * 2])
        ax.text(0, 0, label, ha='center', va='center')
        sunburst(subnodes, total=value, level=level + 1, ax=ax)
    elif nodes:
        d = np.pi * 2 / total
        labels = []
        widths = []
        local_offset = offset
        for label, value, subnodes in nodes:
            labels.append(label)
            widths.append(value * d)
            sunburst(subnodes, total=total, offset=local_offset,
                     level=level + 1, ax=ax)
            local_offset += value
        values = np.cumsum([offset * d] + widths[:-1])
        heights = [1] * len(nodes)
        bottoms = np.zeros(len(nodes)) + level - 0.5
        rects = ax.bar(values, heights, widths, bottoms, linewidth=1,
                       edgecolor='white', align='edge')
        for rect, label in zip(rects, labels):
            x = rect.get_x() + rect.get_width() / 2
            y = rect.get_y() + rect.get_height() / 2
            rotation = (90 + (360 - np.degrees(x) % 180)) % 360
            ax.text(x, y, label, rotation=rotation, ha='center', va='center')

    if level == 0:
        ax.set_theta_direction(-1)
        ax.set_theta_zero_location('N')
        ax.set_axis_off()


def json_to_list(json_dict, level=0):
    result_list = list()
    children_list = list()

    try:
        for children_dict in json_dict['children']:
            tmp = json_to_list(children_dict, level=level + 1)
            # print('---------------------------------')
            # print(tmp)
            children_list.append(tmp)
    except KeyError:
        return (json_dict['name'], json_dict['value'], [])
    result_list.append((json_dict['name'], json_dict['value'], children_list))

    # print('------------------------------------')
    # print(result_list)
    if level == 0:
        return result_list
    else:
        return result_list[0]


if __name__ == "__main__":
    print(json.dumps(json_data))
    print(type(json.dumps(json_data)))
    print(type(json_data))
    test_data = json_to_list(json_data)
    sunburst(test_data)
    plt.show()

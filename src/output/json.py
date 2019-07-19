from .. import constants
import json

# Generates a JSON file based on the markov chain


def generate_json(mkv):
    data = {
        "notes": []
    }

    counter = 0
    tonic_hit = False
    while counter < constants.minimum_duration or not tonic_hit:
        note = mkv.get_state()[0]
        data.get("notes").append({
            "relative_value": note,
            "duration": mkv.get_state()[1]
        })
        if counter > constants.minimum_duration and mkv.get_state()[0] == 1:
            tonic_hit = True
        if counter > 10:
            tonic_hit = True
        counter += 1
        mkv.next_state()

    #with open(constants.save_midi_path + 'new_song.json', 'w') as json_file:
    return json.dumps(data)

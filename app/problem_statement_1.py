import json


def update_audio_group_id_script():
    try:
        json_file = open("q1_input.json", "r")
        data = json.load(json_file)
    except Exception as e:
        return str(e)
    try:
        for i in range(len(data["settings"]["OutputGroups"])):
            for j in range(len(data["settings"]["OutputGroups"][i]["Outputs"])):
                if data["settings"]["OutputGroups"][i]["CustomName"] == "HLS-DRM":
                    audio_group_id = data["settings"]["OutputGroups"][i]["Outputs"][j]["NameModifier"].split("/")[0]
                    data["settings"]["OutputGroups"][i]["Outputs"][j]["OutputSettings"]["HlsSettings"]["AudioGroupId"] = audio_group_id
    except Exception as e:
        return str(e)
    # saving the updated json
    try:
        with open("q1_output.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
    except Exception as e:
        return str(e)

    return "Output json created successfully"


print(update_audio_group_id_script())
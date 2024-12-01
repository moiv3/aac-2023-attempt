# Note: This day still needs code cleanup!!!

import argparse

def read_list(filepath):
    with open(filepath, "r") as fp:
        return fp.read().splitlines()
    
def reflect_light(input_list, initial_beam):
    # format of initial_beam:
    #     initial_beam = {
    #     "x": -1,
    #     "y": 0,
    #     "direction": "r"
    # }

    input_y = len(input_list)
    input_x = len(input_list[0])

    # final map initialize
    single_line = []
    energized_map = [["." for i in range(input_x)] for j in range(input_y)]
    # for _ in range(input_x):
    #     single_line.append(".")
    # for _ in range(input_y):
    #     energized_map.append(single_line)
    # print(*all_lines)


    beams_of_light = [initial_beam]
    generated_beams = []
    break_counter = 0
    prev_energy = 0
    # while any(beam["direction"] for beam in beams_of_light):
    for i in range(2000):
        # print("Cycle", i)
        # print("Beams:", beams_of_light)
        energy = sum(x.count("#") for x in energized_map)
        # print(energized_map)
        print(energy)
        if prev_energy == energy:
            break_counter += 1
            if break_counter >= 15:
                return energy
        else:
            break_counter = 0

        prev_energy = energy

        new_beams_of_light = []
        for initial_beam in beams_of_light:
            new_beams_of_light.append(initial_beam)
            x_pos = initial_beam["x"]
            y_pos = initial_beam["y"]
            energized_map[y_pos][x_pos] = "#"
            

            # print("Start:", initial_beam)

            if initial_beam["direction"] is None:
                new_beams_of_light.pop()

            elif initial_beam["direction"] == "r":
                x_pos = initial_beam["x"]
                y_pos = initial_beam["y"]
                if x_pos + 1 >= input_x:
                    initial_beam["direction"] = None
                elif input_list[y_pos][x_pos+1] == "\\" :
                    initial_beam["x"] += 1
                    initial_beam["direction"] = "d"
                elif input_list[y_pos][x_pos+1] == "/" :
                    initial_beam["x"] += 1
                    initial_beam["direction"] = "u"
                elif input_list[y_pos][x_pos+1] in (".", "-"):
                    initial_beam["x"] += 1
                elif input_list[y_pos][x_pos+1] == "|" :
                    initial_beam["x"] += 1
                    initial_beam["direction"] = "d"
                    initial_beam_2 = initial_beam.copy()
                    initial_beam_2["direction"] = "u"
                    if initial_beam_2 not in generated_beams:
                        generated_beams.append(initial_beam_2)
                        new_beams_of_light.append(initial_beam_2)
                    else:
                        continue

                else:
                    print("Else")


            elif initial_beam["direction"] == "l":
                x_pos = initial_beam["x"]
                y_pos = initial_beam["y"]
                if x_pos - 1 < 0:
                    initial_beam["direction"] = None
                elif input_list[y_pos][x_pos-1] == "\\" :
                    initial_beam["x"] -= 1
                    initial_beam["direction"] = "u"
                elif input_list[y_pos][x_pos-1] == "/" :
                    initial_beam["x"] -= 1
                    initial_beam["direction"] = "d"
                elif input_list[y_pos][x_pos-1] in (".", "-"):
                    initial_beam["x"] -= 1
                elif input_list[y_pos][x_pos-1] == "|" :
                    initial_beam["x"] -= 1
                    initial_beam["direction"] = "u"
                    initial_beam_2 = initial_beam.copy()
                    initial_beam_2["direction"] = "d"
                    if initial_beam_2 not in generated_beams:
                        generated_beams.append(initial_beam_2)
                        new_beams_of_light.append(initial_beam_2)
                    else:
                        continue


            elif initial_beam["direction"] == "u":
                x_pos = initial_beam["x"]
                y_pos = initial_beam["y"]
                if y_pos - 1 < 0:
                    initial_beam["direction"] = None
                elif input_list[y_pos-1][x_pos] == "\\" :
                    initial_beam["y"] -= 1
                    initial_beam["direction"] = "l"
                elif input_list[y_pos-1][x_pos] == "/" :
                    initial_beam["y"] -= 1
                    initial_beam["direction"] = "r"
                elif input_list[y_pos-1][x_pos] in (".", "|"):
                    initial_beam["y"] -= 1
                elif input_list[y_pos-1][x_pos] == "-" :
                    initial_beam["y"] -= 1
                    initial_beam["direction"] = "l"
                    initial_beam_2 = initial_beam.copy()
                    initial_beam_2["direction"] = "r"
                    if initial_beam_2 not in generated_beams:
                        generated_beams.append(initial_beam_2)
                        new_beams_of_light.append(initial_beam_2)
                    else:
                        continue


            elif initial_beam["direction"] == "d":
                x_pos = initial_beam["x"]
                y_pos = initial_beam["y"]
                if y_pos + 1 >= input_y:
                    initial_beam["direction"] = None
                elif input_list[y_pos+1][x_pos] == "\\" :
                    initial_beam["y"] += 1
                    initial_beam["direction"] = "r"
                elif input_list[y_pos+1][x_pos] == "/" :
                    initial_beam["y"] += 1
                    initial_beam["direction"] = "l"
                elif input_list[y_pos+1][x_pos] in (".", "|"):
                    initial_beam["y"] += 1
                elif input_list[y_pos+1][x_pos] == "-" :
                    initial_beam["y"] += 1
                    initial_beam["direction"] = "l"
                    initial_beam_2 = initial_beam.copy()
                    initial_beam_2["direction"] = "r"
                    if initial_beam_2 not in generated_beams:
                        generated_beams.append(initial_beam_2)
                        new_beams_of_light.append(initial_beam_2)
                    else:
                        continue

            # print("End:", initial_beam)
        beams_of_light = new_beams_of_light
    # print("Final:", initial_beam)
    return initial_beam
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser("AAC-2023-Day16")
    parser.add_argument("file", help="path to the txt file")
    args = parser.parse_args()
    input_list = read_list(args.file)

    # part_one_result = reflect_light(input_list)
    # print(input_list)

    part_two_result = []

    for a in range(100):
        print("Cycle" ,a)
        initial_beam = {
        "x": -1,
        "y": a,
        "direction": "r"
        }
        sub_result = reflect_light(input_list, initial_beam=initial_beam)
        part_two_result.append(sub_result)
        print("Cycle" ,a , "result:", sub_result)

    for b in range(100):
        print("Cycle" ,b)
        initial_beam = {
        "x": b,
        "y": -1,
        "direction": "d"
        }
        sub_result = reflect_light(input_list, initial_beam=initial_beam)
        part_two_result.append(sub_result)
        print("Cycle" ,b , "result:", sub_result)
        
    for c in range(100):
        print("Cycle" ,c)
        initial_beam = {
        "x": c,
        "y": 100,
        "direction": "u"
        }
        sub_result = reflect_light(input_list, initial_beam=initial_beam)
        part_two_result.append(sub_result)
        print("Cycle" ,c , "result:", sub_result)
        
    for d in range(100):
        print("Cycle" ,d)
        initial_beam = {
        "x": 100,
        "y": d,
        "direction": "l"
        }
        sub_result = reflect_light(input_list, initial_beam=initial_beam)
        part_two_result.append(sub_result)
        print("Cycle" ,d , "result:", sub_result)
        
    print(part_two_result)
    print(max(part_two_result))

    # up: 7926

# [7860, 5, 12, 7930, 51, 8014, 8004, 7907, 76, 7860, 13, 7958, 30, 7958, 17, 7924, 7903, 8004, 7888, 108, 113, 17, 7881, 7964, 7873, 7869, 3, 3, 7911, 7879, 108, 7887, 7867, 98, 67, 7893, 7988, 7860, 7907, 7865, 7876, 7998, 7873, 8331, 40, 268, 7882, 7866, 7945, 7869, 7860, 7908, 36, 7878, 7860, 7868, 7860, 52, 231, 231, 7951, 7875, 40, 7926, 274, 7872, 7868, 185, 7876, 54, 7888, 7894, 7861, 7903, 7880, 272, 233, 39, 7861, 7861, 36, 7861, 37, 169, 7870, 7861, 20, 66, 20, 51, 231, 8123, 7864, 8064, 7887, 7866, 7861, 7863, 7868, 17, 126, 13, 5, 55, 7895, 23, 7932, 101, 12, 42, 126, 69, 7868, 7933, 40, 176, 30, 109, 7940, 7945, 7890, 24, 67, 115, 23, 84, 7928, 7881, 8024, 7861, 79, 67, 7932, 168, 79, 7861, 7866, 7861, 7861, 75, 7861, 156, 7876, 7860, 109, 23, 7934, 7862, 7894, 7861, 7875, 7902, 7914, 8089, 7861, 7860, 8018, 7869, 7860, 80, 23, 7869, 7866, 7877, 7904, 7870, 76, 7861, 7861, 7872, 7864, 7884, 7864, 7936, 7876, 7873, 7886, 7871, 7860, 7927, 7926, 7875, 7978, 7901, 7892, 7900, 7874, 7884, 7878, 7891, 52, 36, 23, 30, 7908, 7861, 7897, 7898, 61, 7907, 10, 52, 5, 129, 35, 7, 25, 32, 7860, 7860, 7860, 45, 7860, 7860, 61, 20, 7860, 7864, 7860, 7860, 66, 7865, 7977, 7860, 7862, 7860, 7860, 43, 8096, 7876, 7886, 8129, 8001, 71, 8014, 168, 7869, 7860, 7860, 7964, 7875, 8005, 56, 71, 7977, 7927, 27, 7978, 7901, 8065, 39, 7860, 7860, 97, 7933, 7860, 7860, 7871, 24, 7872, 8171, 7860, 116, 7882, 7867, 7880, 7890, 7860, 7860, 7957, 131, 7860, 7884, 7860, 7882, 7860, 7969, 45, 7860, 7921, 7860, 7868, 74, 7867, 60, 28, 7860, 7860, 7905, 58, 7865, 18, 77, 7896, 7868, 22, 108, 7872, 41, 72, 7941, 7914, 7865, 6, 13, 7913, 7880, 7860, 7907, 7866, 60, 7884, 20, 7900, 26, 7864, 26, 8076, 29, 7864, 7860, 7875, 7905, 7869, 7860, 7952, 7860, 7873, 7909, 7907, 7870, 7860, 88, 7860, 7956, 80, 7863, 7860, 7873, 7863, 7863, 7916, 7860, 7864, 7906, 33, 7954, 80, 7860, 7860, 7891, 7864, 7860, 7860, 98, 7866, 7860, 7865, 7876, 7869, 7866, 7870, 87, 7860, 7867, 7860, 66, 138, 7867, 7872, 7860, 41, 111, 7904, 7866, 8090, 7868, 115, 7867, 7868, 7860, 7872, 7860, 7865, 7864, 7865, 7860, 38, 87, 60, 7867, 7860, 76, 39, 121, 26, 7860, 34, 7906, 7860]


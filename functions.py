import quick_styles as qs
import keyboard as kb

options = ["HELLO", "THERE", "WORLD"]
selected_index = 0

while True:
    for c, v in enumerate(options):
        if c == selected_index:
            qs.cprint(v, color="white", bgcolor="blue", styles="bold")
        else:
            print(v)
    key = kb.read_key(suppress=True)
    match key:
        case "up":
            if selected_index > 0:
                selected_index -= 1
        case "down":
            if selected_index < len(options)-1: 
                selected_index += 1
import quick_styles as qs
import keyboard as kb

def filtered_key():
    keys = []
    while len(keys) < 2:
        keys.append(kb.read_key())
    return keys[0]

def clear_lines(amt):
    print("\033[F\033[K"*amt, end="")

def select_menu(options):
    selected_index = 0
    last_index = len(options)-1
    while True:
        for c, v in enumerate(options):
            if c == selected_index:
                qs.cprint(v, color="white", bgcolor="blue", styles="bold")
            else:
                print(v)

        key = filtered_key()
        clear_lines(len(options))
        match key:
            case "up":
                if selected_index != 0:
                    selected_index -= 1
                else:
                    selected_index = last_index
            case "down":
                if selected_index != last_index: 
                    selected_index += 1
                else:
                    selected_index = 0
            case "enter":
                print("\033[K", end="")
                return options[selected_index]
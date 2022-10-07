import datetime

with open("schedule_calculator_y-m-d.txt", "r") as rf:
    start_date = rf.readline(10).replace("-", "/")

print("Schedule Calculator v0.1.0")
print("Type / HELP for a list of commands.")
print("Last date:", start_date)
print("Type the schedule accordingly as follows, in MST format")

clock_in = None
clock_out = None
get_command = "normal"
total_hours = 0
total_minutes = 0
date_ = datetime.datetime.strptime(start_date, "%Y/%m/%d")
day_count = 0
n = 1


def get_time(input_):
    if input_.lower() == "off":
        return "Off"
    elif input_.__len__() > 1 and input_[0] == "/":
        return "".join(input_)
    elif input_.__contains__(":") is False:
        print("Invalid time stamp. Must include a colon.")
    else:
        minute = input_[(input_.__len__()) - 2:]
        hour = input_[:(input_.__len__()) - 3]
        try:
            if int(hour) > 24 or int(minute) >= 60 or int(hour) < 1 or int(minute) < 0:
                print("Invalid time stamp. Must be in MST format. (1-24, hours):(00-59, minutes.)")
            else:
                time_ = [(int(hour)), (int(minute))]
                return time_
        except ValueError:
            print("Invalid time stamp. Must be in MST format")


def sixty_minutes(h, m):
    if m >= 60:
        return h + 1, m - 60
    else:
        return h, m


def balance(in_minuets):
    x = 60 - in_minuets
    if x != 0:
        return -1, x  # Remove an hour, and add a few minuets.
    else:
        return 0, x  # Don't change the hours or minuets.


def add_zero(z):
    if str(z).__len__() == 1:
        return "0" + str(z)
    else:
        return z


def calculate_time():
    if clock_in != "Off" and clock_out != "Off":
        change_ = balance(clock_in[1])
        minute_difference_ = (clock_in[1] + (clock_out[1] + change_[1])) - clock_in[1]

        clock_out[0], minute_difference_ = sixty_minutes(clock_out[0], minute_difference_)

        if clock_out[0] < clock_in[0]:
            clock_in[0] += 24 * -1

        hour_difference_ = (clock_in[0] - (clock_out[0] + change_[0])) * -1
        if hour_difference_ < 0:
            hour_difference_ += 24

        minute_difference_ = add_zero(minute_difference_)
        shift_ = str(hour_difference_) + ":" + str(minute_difference_)
    else:
        shift_ = "Off"
    print(" |\nShift is:", shift_)
    return shift_


def commands(input_):  # # / set | / clear | / show | / help
    try:
        if input_.__len__() == 2:
            a, b = input_
            c = "".join(str(a)+str(b))
        else:
            c = "".join(input_)

        if c.lower() == "/ help":
            print("""
COMMANDS:
    / SET YYYY/MM/DD  (Set the the last date.)
    / SHOW  (Show everything in the schedule.)
    / CLEAR  (Clears everything in the schedule) \n""")
            return None
        elif c.lower()[:6] == "/ set ":
            x = (c[6:])
            try:
                datetime.datetime.strptime(x, '%Y/%m/%d')
                return c.lower()
            except ValueError:
                return None
        elif c.lower() == "/ clear":
            x = input("Are you sure you want to clear the schedule? (y/n): ")
            if x.lower() == "y":
                with open("schedule_text_file.txt", "w"):
                    print("Schedule has been cleared. \n")
            return None
        elif c.lower() == "/ show":
            with open("schedule_text_file.txt", "r") as show:
                for s in show:
                    print(s)
            return None
        elif c[:1] != "/":
            x = "normal"
            return x
        elif c[:1] == "/":
            print("Unknown command:", c)
    except AttributeError:
        pass


while True:
    while clock_in is None or get_command is None:
        try:
            clock_in = get_time(input("Clock in: "))
        except (TypeError, ValueError) as e:
            pass
        get_command = commands(clock_in)
    while clock_out is None and clock_in != "Off" and clock_in[0] != "/" or get_command is None:
        try:
            clock_out = get_time(input("Clock out: "))
        except (TypeError, ValueError) as e:
            pass
        get_command = commands(clock_out)

    if get_command == "normal":
        with open("schedule_text_file.txt", "a") as rf:
            day_count += 1
            end_date = date_ + datetime.timedelta(days=day_count)
            end_date = str(end_date)[:10].replace("-", "/")
            end_date = datetime.datetime.strptime(end_date, '%Y/%m/%d')
            end_date = str(end_date)[:10]
            shift = calculate_time()
            rf.write("\n")
            rf.write(shift.__add__(" -- " + end_date))

        with open("schedule_text_file.txt", "r") as r:
            for line in r:
                if line[:2].__contains__(":"):
                    n = 1
                else:
                    n = 2
                if line[:3] != "Off":
                    try:
                        total_hours += int(line[:n])
                        total_minutes += int(line[2:4])
                        total_hours, total_minutes = sixty_minutes(total_hours, total_minutes)
                        if total_minutes >= 60:
                            total_minutes -= 60
                            total_hours += 1
                    except ValueError:
                        pass
            print("Total is:", str(total_hours)+":"+str(add_zero(total_minutes)))

    with open("schedule_calculator_y-m-d.txt", "w") as w:
        if get_command[:5] == "/ set":
            end_date = get_command[6:]
        w.write(end_date)
        print("Date set for", end_date, "\n")

    clock_in = None
    clock_out = None
    total_hours = 0
    total_minutes = 0

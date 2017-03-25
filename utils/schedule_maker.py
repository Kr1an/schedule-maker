import random
import calendar
import time


def generate_schedule():
    masters = 8
    groups = 3
    days = 15
    subjects = 8
    max_lessons_per_day = 4
    average_lessons_of_one_subject = 8
    secs_to_work = 5

    masters_know_subjects = generate_masters_know_subjects(masters, subjects)
    schedule = generate_empty_schedule(max_lessons_per_day, groups, days)
    master_free_schedule = generate_master_free_schedule(max_lessons_per_day, masters, days)
    group_needed_subjects = generate_group_needed_subjects(average_lessons_of_one_subject, subjects, groups)

    start = get_cur_sec_time()
    last_sec_to_show = secs_to_work
    while get_cur_sec_time() - start <= secs_to_work:
        if secs_to_work - (get_cur_sec_time() - start) is not last_sec_to_show:
            last_sec_to_show = secs_to_work - (get_cur_sec_time() - start)
            print("Remains: %d" % last_sec_to_show)
        [i, j, k] = rand3d(days, groups, 4)     # i-days, j-groups, k-lesson
        if schedule[i][j][k] is not None:
            continue

        lesson = {'subject': None, 'master': None}
        subject_id = rand3d(subjects)[0]

        if group_needed_subjects[j][subject_id] is 0:
            continue

        free_masters_ids = [master_id for master_id in range(masters) if masters_know_subjects[master_id][subject_id] and master_free_schedule[i][master_id][k]]

        if len(free_masters_ids) is 0:
            continue

        master_id = sample(free_masters_ids)

        lesson['subject'] = subject_id
        lesson['master'] = master_id
        schedule[i][j][k] = lesson

        master_free_schedule[i][master_id][k] = 0
        group_needed_subjects[j][subject_id] -= 1



    print_info(master_free_schedule, schedule, masters_know_subjects, group_needed_subjects)


def print_info(master_free_schedule, schedule, masters_know_subjects, group_needed_subjects):
    print('\n\n', 'Masters/Subjects - every element shows if the master knows particular subject.')
    print('Masters - rows, Subjects - columns.')
    print('--------------------------------------------------------------------------------------')
    for x in masters_know_subjects:
        print(x)

    print('\n\n', 'Schedule for students - days/groups/lessons.')
    print('Days - rows. Each days element is Group and each element of the group is lesson. None stands for empty lesson.')
    print('---------------------------------------------------------------------------------------------------------')
    for x in schedule:
        print(x)

    print('\n\n', 'Masters schedule - 1 stands for free, 0 stands for busy.')
    print('Days - rows. Each days element is a master schedule for a day. Each element of the day shedule is a subject.')
    print('----------------------------------------------------------------')
    for x in master_free_schedule:
        print(x)

    print('\n\n', 'Num of lessons for every groups - groups/(num of every subject for particular group:')
    print('Groups - rows. every element is a left number of hours of particular subject to learn with particular group.')
    print('--------------------------------------------------------------------------------------------')
    for x in group_needed_subjects:
        print(x)


def generate_masters_know_subjects(masters, subjects):
    return [[random.randrange(0, 2) for i in range(subjects)] for j in range(masters)]


def generate_empty_schedule(max_lessons_per_day, groups, days):
    return [[[None for i in range(max_lessons_per_day)] for j in range(groups)] for k in range(days)]


def generate_master_free_schedule(max_lessons_per_day, masters, days):
    return [[[1 for i in range(max_lessons_per_day)] for j in range(masters)] for j in range(days)]


def generate_group_needed_subjects(average_lessons_of_one_subject, subjects, groups):
    return [[average_lessons_of_one_subject for i in range(subjects)] for j in range(groups)]


def get_cur_sec_time():
    return calendar.timegm(time.gmtime())


def sample(arr):
    return arr[random.randrange(0, len(arr))]


def rand3d(*args):
    rand_array = []
    for idx in range(len(args)):
        rand_array.append(random.randrange(args[idx]))
    return rand_array

from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# Custom function to check whether there isn't list out of box index error
def checkInboundIndex(index):

    #For the user the index start from 1 therefore subtracting a value from each index called
    global tasks

    valueReturn = {
        'success' : True,
        'data' : []
    }

    try:
        valueReturn['success'] = True
        valueReturn['data'] = tasks[index]
    except IndexError:
        valueReturn['success'] = False
        valueReturn['data'] = "List doesn't have that value on that index"
    
    return valueReturn

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def validate_insert(name: str, description: str, due: str):
    if name == "" or description == "" or due == "":
        print("Missing Information")
        return False
    try:
        str_to_datetime(due)
    except:
        print("Incorret date time format")
        return False
    return True

def lastActivity():
    return datetime.now().strftime("%m/%d/%y %H:%M:%S")

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # update lastActivity with the current datetime value
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    '''
    UCID    - dm767
    Date    - Feb 12
    Comment - Firstly striping the value of name and desciption and then verifyinh whether the values aren't null. 
              Once those test case are passed, checking whether the date is in proper format, if yes then
              storing the value in task and then appending it in global variable tasks and printing a success message,
              if the condition of validate_insert fails it will display out the proper error message and stop the functioning
    '''
    
    name = name.strip()
    description = description.strip()

    # Validating the data inserted is proper or not
    if validate_insert(name, description, due) == False:
        return False
    
    # Store the value in task dict
    task['name'] = name
    task['description'] = description
    task['due'] = due
    task['lastActivity'] = lastActivity()

    # Initializing the global tasks and then appending value in it
    global tasks
    tasks.append(task)

    # Printing a sucess method
    print("New Task added")

    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    '''
    UCID    - dm767
    Date    - Feb 12
    Comment - Taking all the input from users and passing it to another funciton for compute.
    '''

    name = input(f"What's the name of this task? (TODO name) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
    update_task(index, name=name, description=desc, due=due)

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    '''
    UCID    - dm767
    Date    - Feb 12
    Comment - Basically, the values which are taken input are from "def process_update(index)" fucntion, firstly removing all 
              the unnecassary spaces from name & description. Then checking whether the index is available in tasks, if not then
              displaying a proper output message for it and stoping the funciton or else it goes further and check if there is any 
              value which is empty then it would store the orignal value or else it would update it with new one. After this it see's
              whether there is any changes in new values over previous values if no changes found it will print a message with a 
              proper apporpriate message or else it would be printing success message and then finally save() is called.
    '''

    global tasks

    name = name.strip()
    description = description.strip()

    valuereturn = checkInboundIndex(index)

    if valuereturn['success'] == False:
        print(valuereturn['data'])
        return False
    
    task = valuereturn['data']

    flag = False

    if name != "" and task['name'] != name:
        task['name'] = name
        flag = True
    
    if description != "" and task['description'] != description:
        task['description'] = description
        flag = True
    
    if due != "" and task['due'] != due:
        try:
            str_to_datetime(due)
        except:
            return False
        task['description'] = description
        flag = True
    
    if flag == False:
        print("No new input were give to update the task")
        return False

    task['lastActivity'] = lastActivity()
    tasks[index] = task
    print("The task is updated with new values")

    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    '''
    UCID    - dm767
    Date    - Feb 13
    Comment - The index value is check whether that index is availble in global tasks, if no then it display appropriate message 
              according to it or else it goes further and store the data in local variable which then sees whether the task is 
              completed or not, if completed the print the message according to it or else it udpates the lastActivivty and change
              "done" key value to True, stating the task is completed and then print the success message.
    '''

    global tasks

    valuereturn = checkInboundIndex(index)

    if valuereturn['success'] == False:
        print(valuereturn['data'])
        return False
    
    task = valuereturn['data']

    if task['done'] == True:
        print("Task already completed")
        return True
    
    task['lastActivity'] = lastActivity()
    task['done'] = True

    tasks[index] = task

    print("Task Mark as Complted")

    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    '''
    UCID    - dm767
    Date    - Feb 13
    Comment - It takes a index value which user want's to watch, checks whether the index exists or not in the tasks if not then
              print message related to it or else will display the details of that index value to user
    '''
    valuereturn = checkInboundIndex(index)

    if valuereturn['success'] == False:
        print(valuereturn['data'])
        return False

    task = valuereturn['data']

    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    '''
    UCID    - dm767
    Date    - Feb 13
    Comment - If a user wants to delete the task they input a index value, firstly we check whether the index is available in tasks
              If Yes, we delete the task and display the appropritate message.
              If No, we display a message 
    '''

    global tasks

    valuereturn = checkInboundIndex(index)

    if valuereturn['success'] == False:
        print(valuereturn['data'])
        return False

    tasks.pop(index)
    
    print("Task Deleted")

    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''
    UCID    - dm767
    Date    - Feb 13
    Comment - We fetch all the tasks from global variable tasks and then loop it where we check the task which are not completed
              by using if conidtion to check whether the key "done" is True or False, if False we store that task in local variable
              in list. If the list is greater then 0 we list all the incompleted task or else we say "No Pending Task Available"
    '''

    global tasks
    _tasks = []

    for task in tasks:
        if not task['done']:
            _tasks.append(task)
  
    if len(_tasks) > 0:
        list_tasks(_tasks)
    else:
        print("No Pending Task Availble")

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    '''
    UCID    - dm767
    Date    - Feb 13
    Comment - We call the global tasks and declare a variable to store all the overdue tasks in it. We fetch current date & time
              using lastActivity() function and store it in a variable getCurrentTime. Then we rotate a loop taking an individual
              task and checking whether the currentTime is greater the due time and the task is not completed then we store it in 
              the local variable which we initialise before. Then we check whether the local variable _tasks lenght is more then
              0, if yes then we display all the over due tasks or else we print a message
    '''

    global tasks
    _tasks = []

    getCurrentTime = lastActivity()
    
    for task in tasks:
        if getCurrentTime > task['due'] and task['done'] == False:
            _tasks.append(task)

    if len(_tasks) > 0:
        list_tasks(_tasks)
    else:
        print("There are no task which are overdue as of now")

# Calculating date difference between two dates and returing the response in seconds
def find_diff_in_time(dt2, dt1):
  overall = dt2 - dt1
  return overall.days * 24 * 3600 + overall.seconds

# Calculating no. of days, hours, minutes, seconds from passing seconds
def calc_days_hrs_min_sec(sec):
	min, sec = divmod(sec, 60)
	hrs, min = divmod(min, 60)
	days, hrs = divmod(hrs, 24)
	return (days, hrs, min, sec)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    '''
    UCID    - dm767
    Date    - Feb 17
    Comment - We declare the global tasks to have access to all the task which are available, then we verify whether the index
              is available if yes we continue or else we show a proper error message and stop. If we continue then we convert
              the due date-time of the task to datetime type and get current datetime using datetime.now().
              Then we call two difference first find_diff_in_time() two subtract two dates and return total amount of seconds from it.
              Then we call calc_days_hrs_min_sec() to calculate days, hrs, minutes, seconds from seconds as a parameter.
              Then we check whether the days is negative or positive and display the appropriate message according to it to the 
              user.
    '''
    
    global tasks
    task = {}

    valuereturn = checkInboundIndex(index)

    if valuereturn['success'] == False:
        print(valuereturn['data'])
        return False
    
    task = tasks[index]

    if task['done']:
        print(f"Task Completed on {task['lastActivity']}")
        return True

    due_date = str_to_datetime(task['due'])
    current_date_time = datetime.now()

    days, hrs, min, sec = calc_days_hrs_min_sec(find_diff_in_time(due_date, current_date_time))
    if days > 0:
        print(f'The task needs to be completed in next {days} days, {hrs} hours, {min} minutes, {sec} seconds')
    else:
        days *= -1
        print(f'The task is overdue since {days} days, {hrs} hours, {min} minutes, {sec} seconds')

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()
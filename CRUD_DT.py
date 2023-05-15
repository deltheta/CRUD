# OUTLET OVERVIEW
# Simple and useful program for Sales Managers to do a monthly review and update

# README
# Program Testers should expand the terminal or command prompt window size to maximum before testing this program
# so that the table display shows clearly.
# Comments in Capital Letters indicate new feature or new section or important function.
# Due to project constraints of not allowing external libraries, the numerical data is limited to a maximum of 10 digits.
# Inputs are limited to 7 digits for floats and some inputs because this allows 2 decimal places (7 + .2f = 10).
# It also makes sense that if the numerical data exceeds this, the user should start using other database software.
# This is a simple but useful CRUD Program that is intended to be Pythonic in nature.


# DATABASE

# Each outlet data is stored in a dictionary nested in a list.
# Each dictionary should include the following 8 keys: id(ID), outlet(Name of Outlet), 
# sales_mth(Sales for Current Month), trns(Current Month Transactions), trns_avg(Value per Transaction), 
# mths(Months since Operational), sales_total(Cumulative Sales) and sales_avg(Average Monthly Sales).

data_outlets = [
    {
        'id': 1,
        'outlet': 'Galleria',
        'sales_mth': 49000.0,
        'trns': 700,
        'trns_avg': 70.0,
        'mths': 30,
        'sales_total': 1410000.0,
        'sales_avg': 47000.0
    },
    {
        'id': 2,
        'outlet': 'Emporium',
        'sales_mth': 37200.0,
        'trns': 600,
        'trns_avg': 62.0,
        'mths': 29,
        'sales_total': 1276000.0,
        'sales_avg': 44000.0
    },
    {
        'id': 3,
        'outlet': 'Promenade',
        'sales_mth': 42210.0,
        'trns': 630,
        'trns_avg': 67.0,
        'mths': 19,
        'sales_total': 722000.0,
        'sales_avg': 38000.0
    },
    {
        'id': 4,
        'outlet': 'Ecommerce',
        'sales_mth': 35770.0,
        'trns': 490,
        'trns_avg': 73.0,
        'mths': 7,
        'sales_total': 252000.0,
        'sales_avg': 36000.0
    },
    {
        'id': 5,
        'outlet': 'Other',
        'sales_mth': 21240.0,
        'trns': 360,
        'trns_avg': 59.0,
        'mths': 1,
        'sales_total': 21240.0,
        'sales_avg': 21240.0
    }
    ]

# DICTIONARY KEYS to COLUMN NAMES (data attributes)
# Required for update feature later, but placed at the top for better maintainability
keys_columns = {
               'outlet': 'name of outlet',
               'sales_mth': 'current month sales',
               'trns': 'current month transactions',
               'trns_avg': 'value per transaction',
               'mths': 'months since operational',
               'sales_total': 'cumulative sales',
               'sales_avg': 'average monthly sales'
               }


# PROMPT FUNCTION FOR RETURNING TO MAIN MENU
def back_main_menu():
    while True:
        prompt_main = input('Press 0 and Enter to return to Main Menu: ')
        if prompt_main == '0':
            print('Returning to Main Menu..')
            break
        else:
            print("You have entered an invalid option. Please press '0' and Enter to return to Main Menu: ")


# READ DATA - 3 Functions: read_menu() for submenu, read_all() for reading all data and read_single() for reading data of an outlet

# Sub-menu for Read Feature
def read_menu():
    while True:
        read_input = input('''
            What would you like to display?
            
            1. Data of all outlets
            2. Data of a chosen outlet
            3. Return to Main Menu

            Please input 1, 2 or 3: ''') 
        print('\n')
        if read_input == '1':
            read_all()
            break
        elif read_input == '2':
            read_single()
            break
        elif read_input == '3':
            print('Returning to Main Menu')
            break
        else:
            print('You have entered an invalid input. Please input 1, 2 or 3: ')

# Function for reading all rows
def read_all():
    try:
        print('Data of All Outlets\n')
        print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{'ID':<3}", f"{'Name of':<17}", f"{'Current Month':<10}", f"{'Current Month':<10}", 
                                                                f"{'Value per':<10}", f"{'Months since':<10}", 
                                                                f"{'Cumulative':<10}", f"{'Average':<10}"))
        print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|\n'.format(f"{'':<3}", f"{'Outlet':<17}", f"{'Sales':<10}", f"{'Transactions':<10}", 
                                                                f"{'Transaction':<10}", f"{'Operational':<10}", 
                                                                f"{'Sales':<10}", f"{'Monthly Sales':<10}"))
        for i in range(len(data_outlets)):
            print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{data_outlets[i]['id']:<3}", f"{data_outlets[i]['outlet']:<17}", 
                                                                    f"{data_outlets[i]['sales_mth']:<10}", f"{data_outlets[i]['trns']:<10}", 
                                                                    f"{data_outlets[i]['trns_avg']:<10}", f"{data_outlets[i]['mths']:<10}", 
                                                                    f"{data_outlets[i]['sales_total']:<10}", f"{data_outlets[i]['sales_avg']:<10}"))
        print('\n')
        back_main_menu()
    except:
        print('Data does not exist. Please return to Main Menu and create new data.')
        read_menu()

# Function for reading a single row
def read_single():
    while True:
        print('ID of Current Stores:')
        for i in range(len(data_outlets)):
            print('{}\t|{}\t|'.format(f"{data_outlets[i]['id']:<1}", f"{data_outlets[i]['outlet']:<17}"))
        try:
            read_id = int(input('Please input ID of outlet that you would like to display: '))-1
            print('\n{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{'ID':<3}", f"{'Name of':<17}", f"{'Current Month':<10}", f"{'Current Month':<10}", 
                                                                    f"{'Average per':<10}", f"{'Months since':<10}", f"{'Cumulative':<10}", 
                                                                    f"{'Average':<10}"))
            print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|\n'.format(f"{'':<3}", f"{'Outlet':<17}", f"{'Sales':<10}", f"{'Transactions':<10}", 
                                                                      f"{'Transaction':<10}", f"{'Operational':<10}", f"{'Sales':<10}", 
                                                                      f"{'Monthly Sales':<10}"))
            print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{data_outlets[read_id]['id']:<3}", f"{data_outlets[read_id]['outlet']:<17}", 
                                                                    f"{data_outlets[read_id]['sales_mth']:<10}", f"{data_outlets[read_id]['trns']:<10}", 
                                                                    f"{data_outlets[read_id]['trns_avg']:<10}", f"{data_outlets[read_id]['mths']:<10}", 
                                                                    f"{data_outlets[read_id]['sales_total']:<10}", f"{data_outlets[read_id]['sales_avg']:<10}"))
            break
        except:
            print('\nID is not found. Please input an ID from the following options..')
    print('\n')
    back_main_menu()
    

# CREATE DATA - 2 Functions: create_menu() for submenu and create_data() for creating data of new outlet

# Sub-menu for Create Feature
def create_menu():
    while True:
        create_input = input('''
            What would you like to do?
            
            1. Create data for a new outlet
            or
            2. Return to Main Menu

            Please input 1 or 2: ''')
        print('\n') 
        if create_input == '1':
            create_data()
            break
        elif create_input == '2':
            print('Returning to Main Menu..')
            break
        else:
            print('You have entered an invalid input. Please input 1 or 2: ')

# Things to note: check if ID and outlet name have duplicates in current data 
# and use try/except to ensure correct datatype for new data inputs
def create_data():    
    # Obtain ID that does not have a duplicate in existing data so primary value is unique
    duplicate_id = True
    while duplicate_id:    
        # First, Make sure that new_id is of the correct datatype
        try:
            new_id = int(input('Please input the ID of the new outlet (1-3 digits long): '))
        except:
            print('You have entered an invalid datatype. Please retry and input a number.')
            continue
        # Then, make sure that new_id is 1 to 3 digits long 
        if len(str(new_id)) > 3 or len(str(new_id)) < 1:
            print('Please make sure that the length of your input is 1 to 3 digits long and try again.')
            continue
        # Finally, make sure that ID does not have duplicate in existing data
        for i in range(len(data_outlets)):
            if (i==(len(data_outlets)-1)) and (data_outlets[i]['id'] != new_id): # If loop reached last iteration, stop while loop
                duplicate_id = False
                break
            elif data_outlets[i]['id'] != new_id:
                continue
            elif data_outlets[i]['id'] == new_id:
                print('Data already exists. Please choose another ID.')
                break

    # Obtain unique outlet name
    duplicate_outlet = True
    while duplicate_outlet:
        # No need try except because sometimes, outlet names do contain numbers
        # Just have to make sure it is string and capitalized to facilitate comparison with existing data    
        new_outlet = (str(input('Please input the name of the new outlet (1-17 characters long): '))).capitalize()
        # Then, make sure that new_outlet is 1 to 17 characters long
        if len(new_outlet) > 17 or len(new_outlet) < 1:
            print('Please make sure that the length of your input is 1 to 17 characters long and try again.')
            continue
        # Make sure that 'outlet' does not have duplicate in existing data
        for i in range(len(data_outlets)):
            if (i==(len(data_outlets)-1)) and (data_outlets[i]['outlet'] != new_outlet): # If loop reached last iteration, stop while loop
                duplicate_outlet = False
                break
            elif data_outlets[i]['outlet'] != new_outlet:
                continue
            elif data_outlets[i]['outlet'] == new_outlet:
                print('Data already exists. Please choose another name.')
                break
            # Can do if in list also, but if list is long, a lot of memory will be used to create that variable
            # So prefer to iterate

    # Input the other data attributes
    # Make sure that input for other data attributes are of the correct datatypes             
    while True:
        try:
            print('\nFor the following inputs, please make sure that your inputs are 1 to 7 digits long.\n')
            new_sales_mth = float(input('Please input the sales of the new outlet for the current month (number): '))
            new_trns = int(input('Please input the number of transactions of the new outlet for the current month (number): '))
            new_mths = int(input('Please input the number of months (number): '))
            new_sales_total = float(input('Please input the cumulative sales to date (number): '))
            new_sales_mth = float('{:.2f}'.format(new_sales_mth))
            new_sales_total = float('{:.2f}'.format(new_sales_total))
            # this guards against any potential errors from new decimal places being added, 7 + .2f = 10
            if len(str(new_sales_mth)) <= 7 and len(str(new_trns)) <= 7 and len(str(new_mths)) <= 7 and len(str(new_sales_total)) <= 7:
                break
            else:
                print('Please make sure that the length of your input is 1 to 7 digits long and try again.')
        except:
            print('You have entered an invalid datatype. Please retry and input a number.')
    
    # Make sure that transaction or months is not 0, otherwise, new value per transaction and new average monthly sales will be an error
    if new_trns >= 1 and new_mths >= 1:
        new_trns_avg = float("{:.2f}".format(new_sales_mth/new_trns))
        new_sales_avg = float("{:.2f}".format(new_sales_total/new_mths))
    # Otherwise, prepare manual input options so that the program still allows for inputs of 0 for months or transactions without any error
    else:
        while True:
            try:
                new_trns_avg = float(input('Please input the new average transaction value of the new outlet for the current month (number): '))
                new_trns_avg = float("{:.2f}".format(new_trns_avg))
                new_sales_avg = float(input('Please input the number of transactions of the new outlet for the current month (number): '))
                new_sales_avg = float("{:.2f}".format(new_sales_avg))
                break
            except:
                print('You have entered an invalid datatype. Please retry and input a number.')

    # Display the new data before confirmation
    print('\n{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{'ID':<3}", f"{'Name of':<17}", f"{'Current Month':<10}", f"{'Current Month':<10}", 
                                                            f"{'Average per':<10}", f"{'Months since':<10}", f"{'Cumulative':<10}", 
                                                            f"{'Average':<10}"))
    print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{'':<3}", f"{'Outlet':<17}", f"{'Sales':<10}", f"{'Transactions':<10}", 
                                                                f"{'Transaction':<10}", f"{'Operational':<10}", f"{'Sales':<10}", 
                                                                f"{'Monthly Sales':<10}"))
    print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{new_id:<3}", f"{new_outlet:<17}", f"{new_sales_mth:<10}", f"{new_trns:<10}", 
                                                            f"{new_trns_avg:<10}", f"{new_mths:<10}", f"{new_sales_total:<10}", f"{new_sales_avg:<10}"))

    # Confirm and save data, otherwise return to create menu
    while True:
        save_confirm = input('''
            Please confirm if you would like to proceed with the new entry:

            1. Confirm and save data
            2. Do not save data and return to Create Menu
            
            Please input 1 or 2: ''')
        if save_confirm == '1':
            data_outlets.append({
                'id': new_id,
                'outlet': new_outlet,
                'sales_mth': new_sales_mth,
                'trns': new_trns,
                'trns_avg': new_trns_avg,
                'mths': new_mths,
                'sales_total': new_sales_total,
                'sales_avg': new_sales_avg
                })
            break
        elif save_confirm == '2':
            create_menu()
            break
        else:
            print('You have entered an invalid input. Please input 1 or 2: ')
            

# UPDATE DATA - 2 Functions: update_menu() for submenu and update_data() for updating a single datapoint

# Sub-menu for Update Feature
def update_menu():
    while True:
        update_input = input('''
            What would you like to do?
            
            1. Update data of an outlet
            2. Return to Main Menu

            Please input 1 or 2: ''')
        print('\n')
        if update_input == '1':
            update_data()
            break
        elif update_input == '2':
            print('Returning to Main Menu..')
            break
        else:
            print('You have entered an invalid input. Please input 1 or 2: ')

# Function for updating a single data point
def update_data():
    # Input 'id' that the user wants to update and make sure that ID exists in data
    id_nonexistent = True
    while id_nonexistent:    
        # Display available choices for ID
        print('ID and Name of Current Stores:')
        print('{}\t|{}\t|\n'.format(f"{'ID':<3}", f"{'Outlet':<17}"))
        for i in range(len(data_outlets)):
            print('{}\t|{}\t|'.format(f"{data_outlets[i]['id']:<3}", f"{data_outlets[i]['outlet']:<17}"))
        id_input = int(input('Please input the ID of the outlet that you would like to update (number): '))
        # Search for index of selected ID (this function allows flexibility to create a custom ID for the primary key)
        for i in range(len(data_outlets)):
            if data_outlets[i]['id'] == id_input:
                i_update = i # Index of selected 'id' stored in i_update
                print('\n{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{'ID':<3}", f"{'Name of':<17}", f"{'Current Month':<10}", 
                                                                          f"{'Current Month':<10}", f"{'Average per':<10}", f"{'Months since':<10}", 
                                                                          f"{'Cumulative':<10}", f"{'Average':<10}"))
                print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{'':<3}", f"{'Outlet':<17}", f"{'Sales':<10}", 
                                                                        f"{'Transactions':<10}", f"{'Transaction':<10}", f"{'Operational':<10}", 
                                                                        f"{'Sales':<10}", f"{'Monthly Sales':<10}"))
                print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(f"{data_outlets[i_update]['id']:<3}", f"{data_outlets[i_update]['outlet']:<17}", 
                                                                        f"{data_outlets[i_update]['sales_mth']:<10}", f"{data_outlets[i_update]['trns']:<10}", 
                                                                        f"{data_outlets[i_update]['trns_avg']:<10}", f"{data_outlets[i_update]['mths']:<10}", 
                                                                        f"{data_outlets[i_update]['sales_total']:<10}", f"{data_outlets[i_update]['sales_avg']:<10}"))                
                id_nonexistent = False
                break
            elif (i==(len(data_outlets)-1)) and (data_outlets[i]['id'] != id_input): # If loop reached last iteration, stop while loop
                print('The data you are looking for does not exist. Please input a valid selection from the following ID: ')
                break

    # Input column name that the user wants to update
    while True:
        column_update = (str(input('''
                                    Please select a column name from the following choices:
                                    
                                    Input 'outlet' to update name of outlet.
                                    Input 'sales_mth' to update sales for current month.
                                    Input 'trns' to update transactions for current month.
                                    Input 'trns_avg' to update average transaction value for current month.
                                    Input 'mths' to update months since operational.
                                    Input 'sales_total' to update cumulative sales to date.
                                    Input 'sales_avg' to update average monthly sales.
                                    
                                    Your input here: '''))).lower()
        if column_update in keys_columns.keys():
            break
        else:
            print('The column name does not exist.\nPlease make sure that your input does not contain quotation marks.\nPlease try again.')
    
    # Now have Row Index(i_update) and Column Name(column_input), can specify which data point update
    # First, display the datapoint of the ID and Column Name 
    print('The {} for {} is {}.'.format(keys_columns[column_update], data_outlets[i_update]['outlet'], data_outlets[i_update][column_update]))
 
    # Then, request new value for the update and check if value is of the correct datatype using try/except
    
    # Filter out inappropriate input lengths and change input to correct datatype based on choice of column
    while True:
        try:
            update_value = str(input(f'Please input a new value for {keys_columns[column_update]}: '))
            if column_update == 'outlet':
                if len(update_value) <= 17:
                    break
                elif len(update_value) > 17 or len(update_value) < 1:
                    print('Please make sure the length of your input is 1 to 17 characters long and try again.')
                    continue
            elif len(update_value) > 10 or len(update_value) < 1: # Check that length of input is not more than 10
                print('Please make sure the length of your input is 1 to 10 characters long and try again.')
                continue
            elif column_update == 'trns' or column_update == 'mths':
                update_value = int(update_value)
            else:
                update_value = float(update_value)
            break
        except:
            print('You have entered an invalid datatype. Please retry and input the appropriate datatype: ')

    # Finally, confirm and update the datapoint
    while True:
        update_confirm = input('''
            Please confirm if you would like to proceed with the update:

            1. Confirm and update data
            2. Do not update data and return to Update Menu
            
            Please input 1 or 2: ''')
        if update_confirm == '1':
            data_outlets[i_update][column_update] = update_value
            break
        elif update_confirm == '2':
            update_menu()
            break
        else:
            print('You have entered an invalid input. Please input 1 or 2: ')


# DELETE DATA - 2 Functions: delete_menu() for submenu and delete_data() for deleting an outlet data

# Sub-menu for Delete Feature
def delete_menu():
    while True:
        delete_input = input('''
            What would you like to do?
            
            1. Delete Data of an outlet
            2. Return to Main Menu

            Please input 1 or 2: ''') 
        if delete_input == '1':
            delete_data()
            break
        elif delete_input == '2':
            print('Returning to Main Menu..')
            break
        else:
            print('You have entered an invalid input. Please input 1 or 2: ')

def delete_data():
    # Input 'id' that the user wants to update and make sure that ID exists in data
    id_nonexistent = True
    while id_nonexistent:    
        # Display available choices of ID and corresponding outlets
        print('ID and Name of Current Stores:')
        print('{}\t|{}\t|\n'.format(f"{'ID':<3}", f"{'Outlet':<17}"))
        for i in range(len(data_outlets)):
            print('{}\t|{}\t|'.format(f"{data_outlets[i]['id']:<3}", f"{data_outlets[i]['outlet']:<17}"))
        # Input ID and make sure that ID exists in data
        id_input = int(input('Please input the ID of the outlet that you would like to delete (number): '))
        for i in range(len(data_outlets)):
            if data_outlets[i]['id'] == id_input:
                id_nonexistent = False
                break
            elif (i==(len(data_outlets)-1)) and (data_outlets[i]['id'] != id_input):
                print('The data you are looking for does not exist. Please input a valid selection from the following ID: ')
                break
    
    # After obtaining 'id', confirm to delete data (Data Deletion Option Menu) of the chosen 'id'
    # Otherwise, provide another option to return to Delete submenu
    while True:
        delete_confirm = input('''
            Please confirm if you would like to proceed with the deletion:

            1. Confirm and delete data
            2. Do not delete data and return to Delete Menu
            
            Please input 1 or 2: ''')
        print('\n')
        if delete_confirm == '1':
            for i in range(len(data_outlets)):
                if data_outlets[i]['id'] == id_input:
                    del data_outlets[i]
                    print('Data successfully deleted.')
                    break
            break
        elif delete_confirm == '2':
            delete_menu()
            break
        else:
            print('You have entered an invalid input. Please input 1 or 2: ')


# Additional Features of Program Starts Here - MONTHLY UPDATE Feature, PERFORMANCE REPORT Feature

# MONTHLY UPDATE
# Create a list to store sales difference in list_performance
list_performance = [0, 0, 0, 0, 0, 0, 0, 0] 
# Later list elements will be replaced by sales difference calculated in the monthly update function
# Here, it is filled with 0 elements so that if the user just started using this program 
# and requested a performance report, the difference will show 0.

# This function prompts user to update sales_mth and trns columns for all outlets, to be done monthly
def monthly_update():
    for i in range(len(data_outlets)):
        print('Updating Data for', data_outlets[i]['outlet'])
        while True:    
            # Make sure that input is numerical and length is appropriate
            try:
                mthly_sales_mth = float(input('Please input sales for current month: '))
            except:
                print('You have entered an invalid input. Please retry and input a valid number.')
            if mthly_sales_mth > 0 and len(str(mthly_sales_mth)) <= 10:
                break
            else:
                print('Please input a number greater than 0 and 1 to 7 digits long.') # 7 digits to allow for decimal places
        while True:
            # Placed this into a different function for maintainability, 
            # For example, easier to change 'Sales' or 'Transactions' to other data attributes and other datatypes if desired
            try:
                mthly_trns = int(input('Please input number of transactions for current month: '))
            except:
                print('You have entered an invalid input. Please retry and input a valid number.')
            if mthly_trns >= 1 and len(str(mthly_trns)) <= 7:
                break
            else:
                print('Please input an integer greater than 0 and 1 to 7 digits long.')
        # Calculate new average transaction value
        mthly_trns_avg = float("{:.2f}".format(mthly_sales_mth/mthly_trns))
        # Increment number of months since operational by 1
        mthly_mths = int(data_outlets[i]['mths'] + 1)
        # Calculate new cumulative sales and new average monthly sales
        mthly_sales_total = float('{:.2f}'.format(data_outlets[i]['sales_total'] + mthly_sales_mth))
        mthly_sales_avg = float('{:.2f}'.format(mthly_sales_total/mthly_mths))
        
        # Fill in elements for performance update list
        list_performance[i] = mthly_sales_mth - data_outlets[i]['sales_mth']
        
        # Update data for data row of index i
        data_outlets[i]['sales_mth'] = mthly_sales_mth
        data_outlets[i]['trns'] = mthly_trns
        data_outlets[i]['trns_avg'] = mthly_trns_avg
        data_outlets[i]['mths'] = mthly_mths
        data_outlets[i]['sales_total'] = mthly_sales_total
        data_outlets[i]['sales_avg'] = mthly_sales_avg
    
    # Choose next action
    while True:
        monthly_complete = input('''
            What would you like to do?
            
            1. Display Data of all Outlets
            2. View Performance Report
            3. Return to Main Menu

            Please input 1, 2 or 3: ''')
        print('\n')
        if monthly_complete == '1':
            read_all()
            break
        elif monthly_complete == '2':
            performance_report()
            break
        elif monthly_complete == '3':
            print('Returning to Main Menu..')
            break
        else:
            print('You have entered an invalid input. Please input 1, 2 or 3: ')


# PERFORMANCE REPORT

def performance_report():
    print('Sales Performance of Outlets Compared to Previous Month\n')
    # If sales improved from previous month, show 'Sales improved.'
    # Else if difference is 0, show 'No change in sales.'
    # Else, show 'Sales declined.'
    for i in range(len(data_outlets)):
        if list_performance[i] > 0:
            check_diff = 'Sales improved.'
        elif list_performance[i] == 0:
            check_diff = 'No change in sales.'
        else:
            check_diff = 'Sales declined.'
        print('Performance of {}: {}\t| Difference is {}'.format(f"{data_outlets[i]['outlet']:<17}", 
        f"{check_diff:<12}", f"{list_performance[i]:<10}"))
    print('\n')
    back_main_menu()


# MAIN MENU / LOOP WHEN PROGRAM RUNS

while True:
    main_menu = input('''
        Welcome to Outlet Overview!

        Please select from the following options:

        1. Display Data for all Outlets or a chosen Outlet
        2. Create Data for New Outlet
        3. Update Data of an Outlet
        4. Delete Data of an Outlet
        5. Monthly Update
        6. Performance Report
        7. Exit Program
        
        Please choose an option from 1-7 and press Enter: ''')
    print('\n')
    # Choices direct to appropriate submenus or exiting the program
    if main_menu == '1':
        read_menu()
    elif main_menu == '2':
        create_menu()
    elif main_menu == '3':
        update_menu()
    elif main_menu == '4':
        delete_menu()
    elif main_menu == '5':
        monthly_update()
    elif main_menu == '6':
        performance_report()
    elif main_menu == '7':
        print('You have exited Outlet Overview. Thank you for using Outlet Overview.')
        break
    else:
        print('You have entered an invalid input. Please input a number from 1-7: ')
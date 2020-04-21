"""


"""


def big_data():
    print('\nbig data deals with collection, storage, processing and analysis of\nmassive-scale data.\n\nbig data has the potential to power next generation of smart applications.'.title())

def characteristics():
    print('\nbig data characteristics are: the 5vs.\nvolume | velocity | variety | veracity | variety | value'.title())

def examples():
    print('\nvarious applications used by big data.'.title())
    print('\n[0] Quit [1] web    [2] finance [3] healthcare [4] industry [5] environment\n[6] iot   [7] retail [8] transportation'.title())

def web():
    print('\nweb analytics deals with user visits related to online ad campaigns.\n\nperformance monitoring deals with vertical or horizintal scaling.\n\nad targeting deals with search and display advertisements.\n\ncontent recommendation deals with user search patterns, ratings, and\nbrowser histories.'.title())

def finance():
    print("\nbanking and financial institutions can predict if a borrower will default\nor not the future.\n\n- detecting credit card frauds\t- money laundering\n- insurance claim frauds\t- credit risk modeling.".title())

def healthcare():
    print('\nbig data can benefit the following healthcare applications:'.title())
    print('\n- epidemiological surveliance\t- patient-based decision intelligence application\n- adverse drug events prediction\t- real=time healt monitoring\n- evidence-based medicine\t- detecting claim anomalities'.title())

def industry():
    print('\nbig data can be useful in the following industrial fields:\n- machine diagnosis and prognosis\t- risk analysis of industrial operations\n- production planning and control'.title())

def iot():
    print('iot refers to thing that are connected to the internet:'.title())
    print('\n- intrusion detection\t- smart parking\t- smart roads\n- smart irrigation\t- structural healt monitoring'.title())

def retail():
    print('\nretail can use big data for boosting sales and improving customer satisfaction.\n- inventory management\t- customer recommendations\n- store layout optimization\t- forecasting demand'.title())

def transportation():
    print('\nlogistic and transportation:\n- real-time fleet tracking\t- remote vehicle diagnostics\n- shipment monitoring\t- route generation and scheduling\n- hper-local delivery\t- cab/taxi aggregators'.title())

def environment():
    print('\nhere are some environment monitoring applications frm big data:\n- weather monitoring\t- air pollution monitoring\t- noise pollution monitoring\n- forest fire detection\t- river floods detection\t- water quality monitoring'.title())

def main():
    big_data()
    characteristics()
    examples()
    x = int(input('\nEnter a number: '))
    while x:    
        if x == 1:
            web()
        elif x == 2:
            finance()
        elif x == 3:
            healthcare()
        elif x == 4:
            industry()
        elif x == 5:
            environment()
        elif x == 6:
            iot()
        elif x == 7:
            retail()
        elif x == 8:
            transportation()
        else:
            print('\ninvalid number...'.title())
        x = int(input('\nEnter a number: '))

    print('\nYou have exited the loop.')

main()
print()

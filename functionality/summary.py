def summary(args):
    '''
    Summary:
    Print all core information when starting a new timelapse.

    Inputs:
    ArgumentParser args: all args are used

    Outputs:
    None
    '''
    print('STARTING TIMELAPSE WITH THE FOLLOWING SETTINGS:')
    print('------------------------------')
    for arg in vars(args):
        print(' - {0:15} | {1}'.format(arg, getattr(args, arg)))
    print('------------------------------')


def concatenate_summary(args):
    print('------------------------------')
    print('CONCATENATING TIMELAPSES WITH THE FOLLOWING SETTINGS:')
    print('------------------------------')

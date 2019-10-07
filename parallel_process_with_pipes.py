""" file contains examples on Python MultiProcessing Pipe Connections """

import sys
import multiprocessing
import time
import os
import platform
from myprocessespackage import process_using_pipes

#==================================================================


# CHECK IF THE MODULE IS BEING EXECUTED AS THE MAIN SCRIPT BY THE INTERPRETER
# THIS SECTION IS VERY IMPORTANT FOR MULTIPROCESSING CODE
if __name__ == "__main__":

    #variable holds all the pipe connections created
    pipes_dict = {} 
    # print out program heading (using multi-line statement)
    programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                    sys.version[0:sys.\
                        version.index(" ")])
    print(programHeading)
    print('=' * len(programHeading))
    programHeading = "PYTHON MULTIPROCESSING PIPES"
    print(programHeading)
    print('=' * len(programHeading))
    
    # freeze the executable code (affects windows only)
    multiprocessing.freeze_support()

    # check the type for os the code is running on so 
    # we can set the default process type
    osname = platform.platform(aliased=True, terse=True).lower() # get the os name
    
    # check the os name
    if "window" in osname: # windows os
        multiprocessing.set_start_method("spawn")
    elif "linux" in osname: # linux distribution system
        multiprocessing.set_start_method("fork")
    elif "mac" in osname: # linux distribution system
        multiprocessing.set_start_method("fork")
    else:
        multiprocessing.set_start_method("fork")
    
    # get the multiprocessing contet to be used in creating the set of process
    multiprocess = multiprocessing.get_context()

    # create the process pool
    multiprocess_pool = multiprocess.Pool(processes=os.cpu_count() * 2, maxtasksperchild=2)
    # use a for loop to creating the process objects. Number of processes == number of cpus
    for(i) in range(1, os.cpu_count() + 1):
        # create name for the connection
        name = "connection" + str(i)
        pipes_dict[name] = {}
        # create a pipe connection for the process objects
        parentConn, childConn = multiprocess.Pipe(duplex=True) # allow for 2-way (duplex) connections
        parentConn.app_connection_name = name
        childConn.app_connection_name = name
        pipes_dict[name] = {"parent_connection": parentConn, "child_connection": childConn }

        # create the tasks for the process objects in the pool
        multiprocess_pool.apply_async(func=process_using_pipes.run_method, \
                                        kwds={"pipe_connection": pipes_dict[name]["child_connection"], \
                                            "process_count": i})
        
    # wait for any of the child processes to send a message 
    # create a list out of the available child connections
    parent_connections_list = [i["parent_connection"] for i in pipes_dict.values()]
    # make sure that list is NOT NONE and that the list has items in it
    while parent_connections_list is not None and len(parent_connections_list) > 0:
        # if so wait for any of the items to response. wait for 5 secs max
        parent_connections_list = multiprocessing.connection.wait(parent_connections_list)
        if parent_connections_list is not None and len(parent_connections_list) > 0:
            for parent_conn in parent_connections_list:
                print("Process {} says: {}". format(parent_conn.app_connection_name, \
                                    parent_conn.recv()))
                # remove the process that sent a message from the pipe_dicts
                del pipes_dict[parent_conn.app_connection_name]
            # get the new list of available child_conn connections
            parent_connections_list = [i["parent_connection"] for i in pipes_dict.values()] 

    # close the multiprocessing pool    
    multiprocess_pool.close()
    # wait for all process to exit
    multiprocess_pool.join()


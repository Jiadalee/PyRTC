# Some imports relevant to this script
from datetime import datetime
import pyswmm
import numpy as np
import matplotlib.pyplot as plt
from pyswmm import Simulation, Nodes, Links, Subcatchments

with Simulation("C:/Users/Jiada/2019 Spring Semester/Documents/PyRTC/Modeling/.INP files/gamma.inp") as sim:

    print("OWA-SWMM-{}".format(sim.engine_version))
    flow_unit = sim.flow_units
    print("Flow units: {}".format(flow_unit))
    print("System units: {}".format(sim.system_units))


    # storage_SU1 is now a handle to the "93-49743" storage in the model.
    # This object now has properties and allows you to
    # set different parameters depending on the type.
    storage_SU1 = Nodes(sim)["93-49743"]
    storage_SU2 = Nodes(sim)["93-49868"]
    storage_SU3 = Nodes(sim)["93-49919"]
    storage_SU4 = Nodes(sim)["93-49921"]
    storage_SU5 = Nodes(sim)["93-50074"]
    storage_SU6 = Nodes(sim)["93-50076"]
    storage_SU7 = Nodes(sim)["93-50077"]
    storage_SU8 = Nodes(sim)["93-50081"]
    storage_SU9 = Nodes(sim)["93-50225"]
    storage_SU10 = Nodes(sim)["93-90357"]
    storage_SU11 = Nodes(sim)["93-90358"]

    # OR39 is now a handle to the "OR39" link in the model.

    orifice_OR39 = Links(sim)["OR39"]
    orifice_OR34 = Links(sim)["OR34"]
    orifice_OR44 = Links(sim)["OR44"]
    orifice_OR45 = Links(sim)["OR45"]
    orifice_OR38 = Links(sim)["OR38"]
    orifice_OR46 = Links(sim)["OR46"]
    orifice_OR48 = Links(sim)["OR48"]
    orifice_OR47 = Links(sim)["OR47"]
    orifice_OR36 = Links(sim)["OR36"]
    orifice_OR43 = Links(sim)["OR43"]
    orifice_OR35 = Links(sim)["OR35"]

    sim.step_advance(300)  # Increased to 300 seconds

    ####################################################
    #### STARTING SIMULATION ###########################
    ####################################################

    # LET'S print OR48 setting, OR48 flow and SU7 depth for each step
    setting_OR48 = []
    flow_OR48 = []
    depth_SU7 = []
    inflow_SU7 = []
    overflow_SU7 = []
    outflow_SU7 = []
    TSS_SU7 = []
    # LET'S take an example: store OR39 setting, OR39 flow and SU1 depth for each step
    setting_OR39 = []
    flow_OR39 = []
    depth_SU1 = []
    inflow_SU1 = []
    overflow_SU1 = []
    outflow_SU1 = []
    TSS_SU1 = []
    # LET'S take an example: store OR34 setting, OR34 flow and SU2 depth for each step
    setting_OR34 = []
    flow_OR34 = []
    depth_SU2 = []
    inflow_SU2 = []
    overflow_SU2 = []
    outflow_SU2 = []
    TSS_SU2 = []
    # LET'S take an example: store OR44 setting, OR44 flow and SU3 depth for each step
    setting_OR44 = []
    flow_OR44 = []
    depth_SU3 = []
    inflow_SU3 = []
    overflow_SU3 = []
    outflow_SU3 = []
    TSS_SU3 = []
    # LET'S take an example: store OR45 setting, OR45 flow and SU4 depth for each step
    setting_OR45 = []
    flow_OR45 = []
    depth_SU4 = []
    inflow_SU4 = []
    overflow_SU4 = []
    outflow_SU4 = []
    TSS_SU4 = []
    # LET'S take an example: store OR38 setting, OR38 flow and SU5 depth for each step
    setting_OR38 = []
    flow_OR38 = []
    depth_SU5 = []
    inflow_SU5 = []
    overflow_SU5 = []
    outflow_SU5 = []
    TSS_SU5 = []
    # LET'S take an example: store OR46 setting, OR46 flow and SU6 depth for each step
    setting_OR46 = []
    flow_OR46 = []
    depth_SU6 = []
    inflow_SU6 = []
    overflow_SU6 = []
    outflow_SU6 = []
    TSS_SU6 = []

    # LET'S take an example: store OR47 setting, OR47 flow and SU8 depth for each step
    setting_OR47 = []
    flow_OR47 = []
    depth_SU8 = []
    inflow_SU8 = []
    overflow_SU8 = []
    outflow_SU8 = []
    TSS_SU8 = []
    # LET'S take an example: store OR36 setting, OR36 flow and SU9 depth for each step
    setting_OR36 = []
    flow_OR36 = []
    depth_SU9 = []
    inflow_SU9 = []
    overflow_SU9 = []
    outflow_SU9 = []
    TSS_SU9 = []
    # LET'S take an example: store OR43 setting, OR43 flow and SU10 depth for each step
    setting_OR43 = []
    flow_OR43 = []
    depth_SU10 = []
    inflow_SU10 = []
    overflow_SU10 = []
    outflow_SU10 = []
    TSS_SU10 = []
    # LET'S take an example: store OR35 setting, OR35 flow and SU11 depth for each step
    setting_OR35 = []
    flow_OR35 = []
    depth_SU11 = []
    inflow_SU11 = []
    overflow_SU11 = []
    outflow_SU11 = []
    TSS_SU11 = []

    # Create a empty list of current running step time
    step_time = []

    #### Loop the simulation for each eclipse step and get the output for each defined variable
    for step in enumerate(sim):
        #get the current sim time and append time to an array
        dt = sim.current_time
        timearray =dt.strftime('%Y.%m.%d.%H.%M')
        step_time.append(timearray)
        # Append the time-series data to orifice and storage
        #orifice_OR48.target_setting = controller_1(storage_SU7.depth)
        #setting_OR48.append(orifice_OR48.target_setting))
        #Get the link flow for orifice OR48
        flow_OR48.append(orifice_OR48.flow)
        #Get the nodal depth for  storage unit SU7
        depth_SU7.append(storage_SU7.depth)
        #Get the nodal inflow for each storage unit SU7
        inflow_SU7.append(storage_SU7.total_inflow)
        #Get nodal overflow the SU7 which is equal to flooding
        overflow_SU7.append(storage_SU7.flooding)
        #Get nodal outflow for SU7 which can be obtain by( j1.total_outflow )function.outflow equals to the sum of connected orifice flow and nodal overflow
        outflow_SU7.append(storage_SU7.total_outflow)
        #Get the nodal TSS for SU7
        TSS_SU7.append(storage_SU7.pollut_conc)
        #print("\t\t\t\torifice OR48 Setting:     {:.2f} {}".format( \
                #orifice_OR48.target_setting, " percentage"))
        #print("\t\t\t\torifice OR48 Flow:     {:.2f} {}".format( \
                #orifice_OR48.flow, flow_unit))
        #print("\t\t\t\tstorage SU7 Depth:     {:.2f} {}".format( \
                #storage_SU7.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR39.target_setting = controller_1(storage_SU1.depth)
        #setting_OR39.append(orifice_OR39.target_setting)
        #Get the link flow for orifice OR39
        flow_OR39.append(orifice_OR39.flow)
        #Get the nodal depth for  storage unit SU1
        depth_SU1.append(storage_SU1.depth)
        #Get the nodal inflow for each storage unit SU1
        inflow_SU1.append(storage_SU1.total_inflow)
        # Get nodal overflow the SU1 which is equal to flooding
        overflow_SU1.append(storage_SU1.flooding)
        # Get nodal outflow for SU1 which can be obtain by( j1.total_outflow )function.outflow equals to the sum of connected orifice flow and nodal overflow
        outflow_SU1.append(storage_SU1.total_outflow)
        #Get the nodal TSS for Storage unit SU1
        TSS_SU1.append(storage_SU1.pollut_conc)
        # print("\t\t\t\torifice OR39 Setting:     {:.2f} {}".format( \
        # orifice_OR39.target_setting, " percentage"))
        # print("\t\t\t\torifice OR39 Flow:     {:.2f} {}".format( \
        # orifice_OR39.flow, flow_unit))
        # print("\t\t\t\tstorage SU1 Depth:     {:.2f} {}".format( \
        # storage_SU1.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR34.target_setting = controller_3(storage_SU2.depth)
        #setting_OR34.append(orifice_OR34.target_setting)
        flow_OR34.append(orifice_OR34.flow)
        depth_SU2.append(storage_SU2.depth)
        inflow_SU2.append(storage_SU2.total_inflow)
        overflow_SU2.append(storage_SU2.flooding)
        outflow_SU2.append(storage_SU2.total_outflow)
        #Get the nodal TSS for Storage unit SU2
        TSS_SU2.append(storage_SU2.pollut_conc)
        # print("\t\t\t\torifice OR34 Setting:     {:.2f} {}".format( \
        # orifice_OR34.target_setting, " percentage"))
        # print("\t\t\t\torifice OR34 Flow:     {:.2f} {}".format( \
        # orifice_OR34.flow, flow_unit))
        # print("\t\t\t\tstorage SU2 Depth:     {:.2f} {}".format( \
        # storage_SU2.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR44.target_setting = controller_3(storage_SU3.depth)
        #setting_OR44.append(orifice_OR44.target_setting)
        flow_OR44.append(orifice_OR44.flow)
        depth_SU3.append(storage_SU3.depth)
        inflow_SU3.append(storage_SU3.total_inflow)
        overflow_SU3.append(storage_SU3.flooding)
        outflow_SU3.append(storage_SU3.total_outflow)
        #Get the nodal TSS for Storage unit SU3
        TSS_SU3.append(storage_SU3.pollut_conc)
        # print("\t\t\t\torifice OR44 Setting:     {:.2f} {}".format( \
        # orifice_OR44.target_setting, " percentage"))
        # print("\t\t\t\torifice OR44 Flow:     {:.2f} {}".format( \
        # orifice_OR44.flow, flow_unit))
        # print("\t\t\t\tstorage SU3 Depth:     {:.2f} {}".format( \
        # storage_SU3.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR45.target_setting = controller_4(storage_SU4.depth)
        #setting_OR45.append(orifice_OR45.target_setting)
        flow_OR45.append(orifice_OR45.flow)
        depth_SU4.append(storage_SU4.depth)
        inflow_SU4.append(storage_SU4.total_inflow)
        overflow_SU4.append(storage_SU4.flooding)
        outflow_SU4.append(storage_SU4.total_outflow)
        #Get the nodal TSS for Storage unit SU4
        TSS_SU4.append(storage_SU4.pollut_conc)
        # print("\t\t\t\torifice OR45 Setting:     {:.2f} {}".format( \
        # orifice_OR45.target_setting, " percentage"))
        # print("\t\t\t\torifice OR45 Flow:     {:.2f} {}".format( \
        # orifice_OR45.flow, flow_unit))
        # print("\t\t\t\tstorage SU4 Depth:     {:.2f} {}".format( \
        # storage_SU4.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR38.target_setting = controller_5(storage_SU5.depth)
        #setting_OR38.append(orifice_OR38.target_setting)
        flow_OR38.append(orifice_OR38.flow)
        depth_SU5.append(storage_SU5.depth)
        inflow_SU5.append(storage_SU5.total_inflow)
        overflow_SU5.append(storage_SU5.flooding)
        outflow_SU5.append(storage_SU5.total_outflow)
        #Get the nodal TSS for Storage unit SU5
        TSS_SU5.append(storage_SU5.pollut_conc)
        # print("\t\t\t\torifice OR38 Setting:     {:.2f} {}".format( \
        # orifice_OR38.target_setting, " percentage"))
        # print("\t\t\t\torifice OR38 Flow:     {:.2f} {}".format( \
        # orifice_OR38.flow, flow_unit))
        # print("\t\t\t\tstorage SU5 Depth:     {:.2f} {}".format( \
        # storage_SU5.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR46.target_setting = controller_6(storage_SU6.depth)
        #setting_OR46.append(orifice_OR46.target_setting)
        flow_OR46.append(orifice_OR46.flow)
        depth_SU6.append(storage_SU6.depth)
        inflow_SU6.append(storage_SU6.total_inflow)
        overflow_SU6.append(storage_SU6.flooding)
        outflow_SU6.append(storage_SU6.total_outflow)
        #Get the nodal TSS for Storage unit SU6
        TSS_SU6.append(storage_SU6.pollut_conc)
        # print("\t\t\t\torifice OR46 Setting:     {:.2f} {}".format( \
        # orifice_OR38.target_setting, " percentage"))
        # print("\t\t\t\torifice OR46 Flow:     {:.2f} {}".format( \
        # orifice_OR46.flow, flow_unit))
        # print("\t\t\t\tstorage SU6 Depth:     {:.2f} {}".format( \
        # storage_SU6.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR47.target_setting = controller_8(storage_SU8.depth)
        #setting_OR47.append(orifice_OR47.target_setting)
        flow_OR47.append(orifice_OR47.flow)
        depth_SU8.append(storage_SU8.depth)
        inflow_SU8.append(storage_SU8.total_inflow)
        overflow_SU8.append(storage_SU8.flooding)
        outflow_SU8.append(storage_SU8.total_outflow)
        #Get the nodal TSS for Storage unit SU8
        TSS_SU8.append(storage_SU8.pollut_conc)
        # print("\t\t\t\torifice OR47 Setting:     {:.2f} {}".format( \
        # orifice_OR47.target_setting, " percentage"))
        # print("\t\t\t\torifice OR47 Flow:     {:.2f} {}".format( \
        # orifice_OR47.flow, flow_unit))
        # print("\t\t\t\tstorage SU8 Depth:     {:.2f} {}".format( \
        # storage_SU8.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR36.target_setting = controller_9(storage_SU9.depth)
        #setting_OR36.append(orifice_OR36.target_setting)
        flow_OR36.append(orifice_OR36.flow)
        depth_SU9.append(storage_SU9.depth)
        inflow_SU9.append(storage_SU9.total_inflow)
        overflow_SU9.append(storage_SU9.flooding)
        outflow_SU9.append(storage_SU9.total_outflow)
        #Get the nodal TSS for Storage unit SU9
        TSS_SU9.append(storage_SU9.pollut_conc)
        # print("\t\t\t\torifice OR36 Setting:     {:.2f} {}".format( \
        # orifice_OR36.target_setting, " percentage"))
        # print("\t\t\t\torifice OR36 Flow:     {:.2f} {}".format( \
        # orifice_OR36.flow, flow_unit))
        # print("\t\t\t\tstorage SU9 Depth:     {:.2f} {}".format( \
        # storage_SU9.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR43.target_setting = controller_10(storage_SU10.depth)
        #setting_OR43.append(orifice_OR43.target_setting)
        flow_OR43.append(orifice_OR43.flow)
        depth_SU10.append(storage_SU10.depth)
        inflow_SU10.append(storage_SU10.total_inflow)
        overflow_SU10.append(storage_SU10.flooding)
        outflow_SU10.append(storage_SU10.total_outflow)
        #Get the nodal TSS for Storage unit SU10
        TSS_SU10.append(storage_SU10.pollut_conc)
        # print("\t\t\t\torifice OR43Setting:     {:.2f} {}".format( \
        # orifice_OR43.target_setting, " percentage"))
        # print("\t\t\t\torifice OR43 Flow:     {:.2f} {}".format( \
        # orifice_OR43.flow, flow_unit))
        # print("\t\t\t\tstorage SU10 Depth:     {:.2f} {}".format( \
        # storage_SU10.depth, " ft"))

        # Append the time-series data to orifice and storage
        #orifice_OR35.target_setting = controller_11(storage_SU11.depth)
        #setting_OR35.append(orifice_OR35.target_setting)
        flow_OR35.append(orifice_OR35.flow)
        depth_SU11.append(storage_SU11.depth)
        inflow_SU11.append(storage_SU11.total_inflow)
        overflow_SU11.append(storage_SU11.flooding)
        outflow_SU11.append(storage_SU11.total_outflow)
        #Get the nodal TSS for Storage unit SU11
        TSS_SU11.append(storage_SU1.pollut_conc)
        # print("\t\t\t\torifice OR35Setting:     {:.2f} {}".format( \
        # orifice_OR35.target_setting, " percentage"))
        # print("\t\t\t\torifice OR35 Flow:     {:.2f} {}".format( \
        # orifice_OR35.flow, flow_unit))
        # print("\t\t\t\tstorage SU11 Depth:     {:.2f} {}".format( \
        # storage_SU11.depth, " ft"))

    stats_SU1 = storage_SU1.statistics
    stats_SU2 = storage_SU2.statistics
    stats_SU3 = storage_SU3.statistics
    stats_SU4 = storage_SU4.statistics
    stats_SU5 = storage_SU5.statistics
    stats_SU6 = storage_SU6.statistics
    stats_SU7 = storage_SU7.statistics
    stats_SU8 = storage_SU8.statistics
    stats_SU9 = storage_SU9.statistics
    stats_SU10 = storage_SU10.statistics
    stats_SU11 = storage_SU11.statistics


    print("\n\n SU1 Max Depth reduced from 9.29ft to {:.2f}ft\n\n".format(stats_SU1["max_depth"]))
    print("\n\n SU2 Max Depth reduced from 10.0ft to {:.2f}ft\n\n".format(stats_SU2["max_depth"]))
    print("\n\n SU3 Max Depth reduced from 10.0ft to {:.2f}ft\n\n".format(stats_SU3["max_depth"]))
    print("\n\n SU4 Max Depth reduced from 10.0ft to {:.2f}ft\n\n".format(stats_SU4["max_depth"]))
    print("\n\n SU5 Max Depth reduced from 9.03ft to {:.2f}ft\n\n".format(stats_SU5["max_depth"]))
    print("\n\n SU6 Max Depth reduced from 9.00ft to {:.2f}ft\n\n".format(stats_SU6["max_depth"]))
    print("\n\n SU7 Max Depth reduced from 9.01ft to {:.2f}ft\n\n".format(stats_SU7["max_depth"]))
    print("\n\n SU8 Max Depth reduced from 9.74ft to {:.2f}ft\n\n".format(stats_SU8["max_depth"]))
    print("\n\n SU9 Max Depth reduced from 9.43ft to {:.2f}ft\n\n".format(stats_SU9["max_depth"]))
    print("\n\n SU10 Max Depth reduced from 9.38ft to {:.2f}ft\n\n".format(stats_SU10["max_depth"]))
    print("\n\n SU11 Max Depth reduced from 9.07ft to {:.2f}ft\n\n".format(stats_SU11["max_depth"]))

    #for key in stats_SU1:
        #print("{:}:{:.2f}".format(key, stats_SU1[key]))
    #for key in stats_SU7:
        #print("{:}:{:.2f}".format(key, stats_SU7[key]))
    #print("\nRouting Error: {:.2f}%, Continuity Error: {:.2f}%".format( \
        #sim.flow_routing_error * 100, sim.quality_error * 100))

    fig, (ax1,ax2,ax3,ax4,ax5,ax6,ax7) = plt.subplots(7, 1, figsize = [10,10], sharex = True)
    ax1.plot = (step_time,setting_OR48)
    ax1.set_xlabel('Timestep/(YYYY:MM:DD:MM)')
    ax1.set_ylabel('Open percentage/100%')
    ax1.set_title('Timeseries Orifice Setting')

    ax2.plot = (step_time,flow_OR48)
    ax2.set_xlabel('Timestep/(YYYY:MM:DD:MM)')
    ax2.set_ylabel('Flow/cfs')
    ax2.set_title('Timeseries Orifice Flow')

    ax3.plot = (step_time,depth_SU7)
    ax3.set_xlabel('Timestep/(YYYY:MM:DD:MM)')
    ax3.set_ylabel('Depth/cfs')
    ax3.set_title('Timeseries Storage Unit Depth')

    ax4.plot = (step_time,overflow_SU7)
    ax4.set_xlabel('Timestep/(YYYY:MM:DD:MM)')
    ax4.set_ylabel('Overflow/cfs')
    ax4.set_title('Timeseries Storage Unit Inflow')

    ax5.plot = (step_time,inflow_SU7)
    ax5.set_xlabel('Timestep/(YYYY:MM:DD:MM)')
    ax5.set_ylabel('Inflow/cfs')
    ax5.set_title('Timeseries Storage Unit Overflow')

    ax6.plot = (step_time,outflow_SU7)
    ax6.set_xlabel('Timestep/(YYYY:MM:DD:MM)')
    ax6.set_ylabel('Outflow/feet')
    ax6.set_title('Timeseries Storage Unit Outflow')

    ax7.plot = (step_time,TSS_SU7)
    ax7.set_xlabel('Timestep/(YYYY:MM:DD:MM)')
    ax7.set_ylabel('TSS/(mg/L)')
    ax7.set_title('Timeseries Storage Unit TSS')

    plt.tight_layout()

    #plt.subplot(2, 4, 1)
    #plt.plot(setting_OR48)
    #plt.title('Orifice Setting')
    #plt.xlabel('Timestep')
    #plt.ylabel('Open percentage/100%')
    #plt.subplot(2, 4, 2)
    #plt.plot(flow_OR48)
    #plt.title('Orifice Flow')
    #plt.xlabel('Timestep')
    #plt.ylabel('Flow/cfs')
    #plt.subplot(2, 4, 3)
    #plt.plot(depth_SU7)
    #plt.title('Storage Unit Depth')
    #plt.xlabel('Timestep')
    #plt.ylabel('Depth/feet')
    #plt.subplot(2,4,4)
    #plt.plot(inflow_SU7)
    #plt.title('Storage Unit Inflow')
    #plt.xlabel('Timestep')
    #plt.ylabel('Inflow/cfs')
    #plt.subplot(2,4,5)
    #plt.plot(overflow_SU7)
    #plt.title('Storage Unit Overflow')
    #plt.xlabel('Timestep')
    #plt.ylabel('Overflow/cfs')
    #plt.subplot(2,4,6)
    #plt.plot(outflow_SU7)
    #plt.title('Storage Unit Outflow')
    #plt.xlabel('Timestep')
    #plt.ylabel('Outflow/cfs')
    #plt.subplot(2,4,7)
    #plt.plot(TSS_SU7)
    #plt.title('Storage Unit TSS')
    #plt.xlabel('Timestep')
    #plt.ylabel('TSS/(mg/L)')
    #plt.show()
    ###


    # Finally, we can print the routing error and continuity errors.
    print("\nRouting Error: {:.2f}%, Continuity Error: {:.2f}%".format(\
        sim.flow_routing_error*100, sim.quality_error*100))


####################################################
#### SIMULATION CLOSED #############################
####################################################






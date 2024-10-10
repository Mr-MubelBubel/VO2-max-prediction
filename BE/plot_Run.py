import os
import numpy as np
import matplotlib.pyplot as plt
from flask import current_app

def plot_Run(VO2max: float, vLamax, bw, Ks1, Ks2, VolRel):

    RunningEco = 12.5
    Kel = 2
    # generate oxygen steady-states
    VO2ss = np.arange(1, VO2max, 0.01)

    # potentiate constants
    Ks1 = Ks1 ** 2
    Ks2 = Ks2 ** 3

    # calculate ADP corresponding to VO2ss (eq. 4b)
    ADP = np.sqrt((Ks1 * VO2ss) / (VO2max - VO2ss))

    # calculate steady state gross lactic acid (pyruvate) formation rate (eq. 3)
    vLass = 60 * vLamax / (1 + (Ks2 / ADP ** 3))

    # calculate lactate combustion (eq. 6)
    LaComb = (0.01576 / VolRel) * VO2ss

    # calculate net lactate formation
    vLanet = abs(vLass - LaComb)

    # Calculate overall demand in O2-equivalents and Intensity
    overall_demand = ((vLass * (VolRel * bw) * (5.5) / bw) + VO2ss)
    Intensity = overall_demand / RunningEco

    # calculate the crossing point (AT) between gross lactate production and combustion
    arg_sAT = np.argmin(vLanet)
    sAT = Intensity[arg_sAT]

    # speed at FatMax
    s_Fmx = Intensity[np.argmax(vLanet[0:arg_sAT])]

    # percentage of VO2max
    pcVO2maxAT = sAT * RunningEco / VO2max

    # print to console
    print(f'AT is at {round(sAT, 2)} m/s, {round(pcVO2maxAT * 100, 1)}% of VO2max, FatMax is at {round(s_Fmx, 2)} m/s')

    # Creating canvas for plots
    fig, ((ax1, ax2), (ax4, ax5)) = plt.subplots(2, 2, figsize=(20, 10))

    # Plotting vLanet
    ax1.plot(Intensity, vLanet, label='Lack of Pyruvate | Lactate Acummulation', color='purple')
    ax1.set_ylabel('mmol/L/min')
    ax1.set_xlabel('Velocity [m/s]')
    ax1.legend()
    ax1.set_ylim(0, 8)
    ax1.set_xlim(0, 6)

    # plotting O2-Deficit
    ax2.plot(Intensity, overall_demand, label="Oxygen Demand", color='red')
    ax2.plot(Intensity, VO2ss, label="Oxygen Uptake", color='blue')
    ax2.fill_between(Intensity, overall_demand, VO2ss, color="grey")
    ax2.set_xlabel('Velocity [m/s]')
    ax2.set_ylabel('Oxygen [ml/min/kg]')
    ax2.legend()

    # Plotting Macronutrient Utilization
    ## Plotting Carbohydrate Utilization
    CHO_util = vLass[:arg_sAT + 400] * (bw * VolRel) * 60 / 1000 / 2 * 162.14  # 162.14 molare masse glykogen
    Fat_util = (vLanet[
                :arg_sAT] * VolRel) / 0.01576 * bw * 60 * 4.65 / 9.5 / 1000  # 4.65 kcal/L VO2 stearinsäure, 9.5 g/kcal

    ax4.plot(Intensity[0:len(CHO_util)], CHO_util, label='Carbohydrates', color='darkgoldenrod')
    ax4.set_xlabel('Velocity [m/s]')
    ax4.set_ylabel('Carbohydrate g/h')
    ax4.legend()

    ## Plotting Fat Utilization
    ax3 = ax4.twinx()
    ax3.set_ylim(0, 100)
    ax3.plot(Intensity[0:len(Fat_util)], Fat_util, label='Fat', color='green')
    ax3.set_ylabel('Fat g/h')
    ax3.legend()

    # Plotting CLass
    Class = np.sqrt((vLamax * Kel * 60) / (((0.01576 / VolRel) * VO2ss[0:arg_sAT]) * (
            1 + (Ks2 / ((Ks1 * VO2ss[0:arg_sAT]) / (VO2max - VO2ss[0:arg_sAT])) ** (3 / 2))) - (vLamax * 60)))
    ax5.set_ylabel("mmol/L")
    ax5.set_xlabel("Velocity [m/s]")
    ax5.set_ylim(0, 10)
    ax5.plot(Intensity[0:len(Class)], Class, label='Steady-State Lactate')
    ax5.legend()

    # Calculating Carb. & Fat ultization
    CHO_util = vLass[:arg_sAT + 400] * (bw * VolRel) * 60 / 1000 / 2 * 162.14  # 162.14 molare masse glykogen
    Fat_util = (vLanet[
                :arg_sAT] * VolRel) / 0.01576 * bw * 60 * 4.65 / 9.5 / 1000  # 4.65 kcal/L VO2 stearinsäure, 9.5 g/kcal

    # indicating 90g/h of carb. utilization as CarbMax
    CarbMax = Intensity[np.min(np.where(CHO_util >= 90))]
    print(f'CarbMax is at {round(CarbMax, 2)} m/s')

    # Indicating lactate steady concentration at 2.5 mmol/L
    arg_25 = np.min(np.where(Class >= 2.5))
    La_25 = Intensity[arg_25]

    # Caculating predicted Marathon finish time as str in [h:mm]
    finish_time = str(int(42195 / La_25 / 3600)) + ":" + str(
        int(((42195 / La_25 / 3600) - int(42195 / La_25 / 3600)) * 60))

    # printing 2.5 mmol/L velocity to screen
    print(
        f'Velocity at 2.5 mmol/L steady state lactate is {round(La_25, 2)} m/s'
        f'\nPredicted Marathon finish: {finish_time} h'
    )

    # Set vars for output
    at = round(sAT, 2)
    per_vo2max = round(pcVO2maxAT * 100, 1)
    fatmax = round(s_Fmx, 2)
    carbmax = round(CarbMax, 2)
    lactate = round(La_25, 2)
    pred_t = finish_time

    # create dir for return
    values = {"CarbMax": carbmax, "Lactate": lactate, "Predicted Time": pred_t, "AT": at,
              "Percantage of VO2max": per_vo2max, "FatMax": fatmax}

    # cheack path or create a new one
    ## join flask-app for plot saving
    os.makedirs('../static/plots', exist_ok=True)
    save_path = os.path.join(current_app.root_path, 'static', 'plots', 'plot.png')

    # save plot and return values
    try:
        plt.savefig(save_path)
        print("Plot saved successfully!")
    except Exception as e:
        print(f"Error while saving plot: {e}")

    plt.close()

    return values


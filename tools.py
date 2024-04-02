import scipy.io as sio
import pandas as pd
import numpy as np
def get_events(filename):
    triggers = sio.loadmat(filename,
                      mat_dtype=True)
    names = [n[0] for n in triggers['names'][0]]
    trig_dict = {names[n]:triggers['onsets'][0][n][:] \
                 for n in range(len(triggers['onsets'][0]))}
    list_n = []
    list_o = []
    for n in trig_dict.keys():
        for z in range(len(trig_dict[n])):
            list_n.append(n)
            list_o.append(trig_dict[n][z][0])

    simple = [n.split('_')[0] for n in list_n]
    events = pd.DataFrame({'onset':list_o,
                           'duration':[15 for n in range(len(simple))],
                          'trial_type':simple})
    events = events.sort_values('onset').reset_index().drop('index',axis=1)
    return events
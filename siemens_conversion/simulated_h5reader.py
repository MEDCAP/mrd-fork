import numpy as np
import h5py
from matplotlib import pyplot as plt 

filepath = 'data/gre-hard.h5'

with h5py.File(filepath, 'r') as f:
    keys = []
    f.visit(lambda k : keys.append(k) if isinstance(f[k], h5py.Dataset) else None)

    # read B1
    B1x_V_packed = f['B1x_V'][()]
    B1x_min = f['B1x_V'].attrs['B1x_min']
    B1x_step = f['B1x_V'].attrs['B1x_step']
    B1x_V = (B1x_V_packed * B1x_step + B1x_min).astype(np.float32)

    B1y_V_packed = f['B1y_V'][()]
    B1y_min = f['B1y_V'].attrs['B1y_min']
    B1y_step = f['B1y_V'].attrs['B1y_step']
    B1y_V = (B1y_V_packed * B1y_step + B1y_min).astype(np.float32)

    # read 
    grad_packed = f['grad'][()]
    grad_min = f['grad'].attrs['grad_min']
    grad_step = f['grad'].attrs['grad_step']
    grad = (grad_packed * grad_step + grad_min).astype(np.float32)
    gx = grad[:, 0]
    gy = grad[:, 1]
    gz = grad[:, 2]

    datasize = f.attrs['datasize']
    dt = f.attrs['dt']
    t = np.linspace(0, datasize*dt, int(datasize))

    # figure plot setting 
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.85)
    ax.set_ylabel('gradients (T/m)')
    ax.yaxis.label.set_color('b')   # grad in blue
    ax.tick_params(axis='y', colors='b') 
    B1ax = ax.twinx()
    B1ax.set_ylabel('B1 (V)')   
    B1ax.yaxis.label.set_color('g')   # B1 in green
    B1ax.tick_params(axis='y', colors='g')
    # plot data
    B1ax.plot(t, B1x_V, color='g', linestyle='dashed', label='B1x_V')
    B1ax.plot(t, B1y_V, color='g', linestyle='dotted', label='B1y_V')
    ymax = 1.05*max(np.max(np.abs(B1x_V)), np.max(np.abs(B1y_V)))
    B1ax.set_ylim(bottom=-ymax,top=ymax)
    B1ax.legend(loc=4)
    ax.plot(t, grad[:, 0], color='b',linestyle='dashed', label='gx:readout')
    ax.plot(t, grad[:, 1], color='r',linestyle='dotted', label='gy:phase-encoding')
    ax.plot(t, grad[:, 2], color='y',linestyle='dashdot', label='gz:slice-selection')
    ymax = 1.05*max(np.max(np.abs(grad[:, 0])), np.max(np.abs(grad[:, 1])), np.max(np.abs(grad[:, 2])))
    ax.set_ylim(bottom=-ymax,top=ymax)
    ax.legend(loc=3)
    plt.show()

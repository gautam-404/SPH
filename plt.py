import numpy as np
import plotly.graph_objects as go

x = np.load('x.npy')
y = np.load('y.npy')
z = np.load('z.npy')
cval = np.load('cval.npy')


fig = go.Figure(data = [go.Scatter3d(x=[], y=[], z=[],
                                   mode='markers', marker=dict(size=1))])


frames = [go.Frame(
        data=[go.Scatter3d(
            x=x[k],
            y=y[k],
            z=z[k],
            mode="markers",
            marker=dict(size=1))], traces=[0], name=f'frame{k}' ) for k in range(len(x))]

fig.update(frames=frames)


def frame_args(duration):
    return {
            "frame": {"duration": duration},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
            }


sliders = [
    {"pad": {"b": 10, "t": 60},
     "len": 0.9,
     "x": 0.1,
     "y": 0,
     "steps": [
                 {"args": [[f.name], frame_args(100)],
                  "label": str(k),
                  "method": "animate",
                  } for k, f in enumerate(fig.frames)
              ]
     }
        ]

fig.update_layout(scene = dict(
                    xaxis = dict(nticks=4, range=[-2,2], autorange=False),
                    yaxis = dict(nticks=4, range=[-2,2], autorange=False),
                    zaxis = dict(nticks=4, range=[-2,2], autorange=False)),
            updatemenus=[dict(
                    type="buttons",
                    buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])],
            sliders = sliders
            )


fig.show()



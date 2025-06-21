import data_read as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# Dark mode color scheme
DARK_MODE = {
    'background': '#1a1a1a',
    'text': '#ffffff',
    'wave_color': 'yellow',
    'surface_color': 'black',
    'particle_color': '#ff3300',
    'grid_color': '#4d4d4d'
}

# Wave parameters
frequency = 1.0  # Hz
amplitude = 1.5   # meters
wavelength = 1.0  # meters

# Create spatial grid
x = np.linspace(0, 10, 100)

y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

# Time parameters
total_time = 7  # seconds
time_steps = 25
times = np.linspace(0, total_time, time_steps)

# 3D Wave function (circular wave with damping)
def wave_height(x, y, t):
    r = np.sqrt((x-5)**2 + (y-5)**2)  # Distance from center
    return amplitude * np.sin(2*np.pi*(r/wavelength - frequency*t)) * np.exp(-0.2*r)

# Create figure
fig = go.Figure()

# Initial surface plot
fig.add_trace(go.Surface(
    x=X, 
    y=Y, 
    z=wave_height(X, Y, 0),
    colorscale=[[0, DARK_MODE['surface_color']]], 
    showscale=False,
    name='Wave Surface'
))

# Add marker particle
particle_pos = [7.0, 7.0]
fig.add_trace(go.Scatter3d(
    x=[particle_pos[0]],
    y=[particle_pos[1]],
    z=[wave_height(particle_pos[0], particle_pos[1], 0)],
    mode='markers',
    marker=dict(
        color=DARK_MODE['particle_color'],
        size=8,
        line=dict(color='white', width=1)
    ),
    name='Particle'
))

# Create animation frames
frames = []
for i, t in enumerate(times):
    frames.append(go.Frame(
        data=[
            go.Surface(z=wave_height(X, Y, t)),
            go.Scatter3d(z=[wave_height(particle_pos[0], particle_pos[1], t)])
        ],
        name=f'Frame {i}'
    ))

fig.frames = frames

# Dark mode layout
fig.update_layout(
    title='3D Mechanical Wave Simulation',
    scene=dict(
        xaxis_title='X Position (m)',
        yaxis_title='Y Position (m)',
        zaxis_title='Displacement (m)',
        xaxis=dict(gridcolor=DARK_MODE['grid_color']),
        yaxis=dict(gridcolor=DARK_MODE['grid_color']),
        zaxis=dict(gridcolor=DARK_MODE['grid_color']),
        bgcolor=DARK_MODE['background']
    ),
    paper_bgcolor=DARK_MODE['background'],
    font_color=DARK_MODE['text'],
    updatemenus=[{
        'type': 'buttons',
        'buttons': [{
            'label': 'Play',
            'method': 'animate',
            'args': [None, {
                'frame': {'duration': 50, 'redraw': True},
                'fromcurrent': True
            }]
        }],
        'x': 0.1,
        'y': 0
    }],
    annotations=[{
        'text': f'Frequency: {frequency} Hz | Wavelength: {wavelength} m',
        'xref': 'paper',
        'yref': 'paper',
        'x': 0.5,
        'y': 1.1,
        'showarrow': False,
        'font': {'size': 12}
    }]
)

# Camera settings
fig.update_scenes(
    camera=dict(
        eye=dict(x=1.5, y=1.5, z=0.8)
    )
)

fig.show()
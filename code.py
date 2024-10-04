import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

# Function to diagnose the car
def diagnose(engine_light, strange_noise, smoke, car_starts):
    # Evaluate service need based on user input
    needs_service = any([
        engine_light, 
        (strange_noise and not car_starts), 
        smoke
    ])
    
    # Output result
    result = "The car needs service." if needs_service else "The car does not need service."
    
    # Clear previous output and display the result
    clear_output(wait=True)
    display(header, engine_light_checkbox, strange_noise_checkbox, smoke_checkbox, car_starts_checkbox, diagnose_button)
    print(result)

# Header with title and smaller image
header = HTML("""
    <h1 style='color: #0056b3; text-align: center;'>Car Diagnosis Expert System</h1>
    <img src='https://upload.wikimedia.org/wikipedia/commons/b/bb/2023_Lamborghini_Aventador_Ultimae.jpg' 
         style='display: block; margin-left: auto; margin-right: auto; width: 30%; border: 5px solid #0056b3;'>
""")

# Create checkboxes for user input with customized styles
engine_light_checkbox = widgets.Checkbox(value=False, description='Is the engine light on?', 
                                          style={'description_width': 'initial'}, 
                                          layout=widgets.Layout(width='50%', margin='10px 0'))
strange_noise_checkbox = widgets.Checkbox(value=False, description='Is there a strange noise?', 
                                           style={'description_width': 'initial'}, 
                                           layout=widgets.Layout(width='50%', margin='10px 0'))
smoke_checkbox = widgets.Checkbox(value=False, description='Is there smoke?', 
                                   style={'description_width': 'initial'}, 
                                   layout=widgets.Layout(width='50%', margin='10px 0'))
car_starts_checkbox = widgets.Checkbox(value=False, description='Does the car start?', 
                                        style={'description_width': 'initial'}, 
                                        layout=widgets.Layout(width='50%', margin='10px 0'))

# Create a button to diagnose with color
diagnose_button = widgets.Button(description='Diagnose', 
                                 button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
                                 layout=widgets.Layout(width='50%', margin='20px 0'))

# Set the button's click event to the diagnose function
diagnose_button.on_click(lambda x: diagnose(engine_light_checkbox.value, 
                                             strange_noise_checkbox.value, 
                                             smoke_checkbox.value, 
                                             car_starts_checkbox.value))

# Display the header, checkboxes, and button
display(header, engine_light_checkbox, strange_noise_checkbox, smoke_checkbox, car_starts_checkbox, diagnose_button)

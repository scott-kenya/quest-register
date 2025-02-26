import csv
import os
import hashlib
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window

class UniqueNumberGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super(UniqueNumberGenerator, self).__init__(**kwargs)

        # Create a label
        self.label = Label(text="Enter your name:")

        # Create a text input
        self.text_input = TextInput()
        
        # Create a text input for entering names (multiline)
        self.name_input = TextInput(hint_text="Enter Children Names", multiline=True)

        # Create a button
        self.button = Button(text="Generate Unique Number", on_press=self.generate_unique_number)

        # Add widgets to the layout
        self.add_widget(self.label)
        self.add_widget(self.text_input)
        self.add_widget(self.name_input)
        self.add_widget(self.button)

    def generate_unique_number(self, instance):
        # Get user input from TextInput widget
        name = self.text_input.text.strip()
        names_of_children = self.name_input.text.strip()
        
        if name:
            # Use hashlib to generate a unique hash based on the input name
            hashed_name = hashlib.sha256(name.encode()).hexdigest()
            unique_number = hashed_name[:5]
            current_datetime = datetime.now()

            self.label.text = "Unique Number: " + unique_number

            # Clear the text input
            self.text_input.text = ""
            self.name_input.text = ""

            # Save data to CSV file in the user's home directory
            csv_file_path = os.path.expanduser('~/OurData.csv')
            with open(csv_file_path, mode='a', newline='') as file:
                fieldnames = ["Name", "Names of Children", "Unique Number", "Date and Time"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                if os.stat(csv_file_path).st_size == 0:
                    writer.writeheader()
                
                writer.writerow({
                    "Name": name,
                    "Names of Children": names_of_children,
                    "Unique Number": unique_number,
                    "Date and Time": current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                })
                print("Data written to CSV file")


class CodeDisplay(BoxLayout):
    def __init__(self, **kwargs):
        super(CodeDisplay, self).__init__(**kwargs)
        
        # Create a label
        self.label = Label(text="Enter the generated code:")
        
        # Create a text input for the code
        self.code_input = TextInput()
        
        # Create a button
        self.button = Button(text="Display Details", on_press=self.display_details)
        
        # Create a label to display details
        self.details_label = Label(text="")
        
        # Add widgets to the layout
        self.add_widget(self.label)
        self.add_widget(self.code_input)
        self.add_widget(self.button)
        self.add_widget(self.details_label)

    def display_details(self, instance):
        # Get the entered code
        code = self.code_input.text.strip()
        
        # Read data from the CSV file
        csv_file_path = os.path.expanduser('~/OurData.csv')
        if os.path.exists(csv_file_path):
            with open(csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                
                # Debugging: print the fieldnames to verify column names
                print("CSV Fieldnames:", reader.fieldnames)
                
                for row in reader:
                    # Debugging: print each row to verify its contents
                    print("Row data:", row)
                    
                    # Check if 'Unique Number' exists in the row
                    unique_number = row.get("Unique Number")
                    if unique_number:
                        # Debugging: print the unique number and the entered code for comparison
                        print(f"Comparing {unique_number.strip()} with {code.strip()}")
                        
                        if unique_number.strip() == code.strip():
                            details = (f"Name: {row['Name']}\n"
                                       f"Names of Children: {row['Names of Children']}\n"
                                       f"Unique Number: {row['Unique Number']}\n"
                                       f"Date and Time: {row['Date and Time']}")
                            self.details_label.text = details
                            return
        
        # If no matching code is found
        self.details_label.text = "No details found for the entered code."


# Get the screen width
screen_width = Window.size[0]

# Set the minimum width of the window to the screen width
Window.minimum_width = screen_width

# Set the minimum height of the window to 200 pixels
Window.minimum_height = 200

class UniqueNumberApp(App):
    def build(self):
        self.title = "Nairobi Chapel GreenPark Sunday School Register"

        # Load the image
        image = Image(source='C:/Users/ADMIN/Documents/PYTHON POJECTS/header.png')
        image.size_hint = (1, 1)
        image.keep_ratio = False
        image.allow_stretch = True
        image.size_hint_y = None
        image.height = 300
        
        # Create a BoxLayout to hold the image
        image_layout = BoxLayout(orientation='vertical')
        image_layout.add_widget(image)

        # Create a footer Label
        footer_label = Label(text="Copyright © 2024 Nairobi Chapel GreenPark.  All rights reserved by Scott[code zena].",
                             size_hint_y=None, height=30)

        # Create a BoxLayout to hold the footer label
        footer_layout = BoxLayout(orientation='horizontal')
        footer_layout.add_widget(footer_label)
        
        # Create a BoxLayout to hold the UniqueNumberGenerator and footer layout
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(UniqueNumberGenerator())
        main_layout.add_widget(CodeDisplay())  # Add the CodeDisplay widget
        main_layout.add_widget(footer_layout)
        
        # Create a BoxLayout to hold the image layout and main layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(image_layout)
        layout.add_widget(main_layout)

        return layout

if __name__ == "__main__":
    UniqueNumberApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
from kivy.core.window import Window

import os
import shutil

class FileSeparatorUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"

        # Add blurred background image
        self.background = Image(source='zoro-pictures-8nv0c0nb7rijf6z2.jpg', allow_stretch=True, keep_ratio=False, pos_hint={'x':0, 'y':0}, size_hint=(1, 1))
        self.add_widget(self.background)

        # Create a vertical layout for file chooser and button
        file_layout = BoxLayout(orientation="vertical", spacing=10)

        self.label = Label(text="Select Folder:", color=(1, 1, 1, 1), font_size=20)  # Set font color to white and increase font size
        file_layout.add_widget(self.label)

        self.file_chooser = FileChooserListView()
        file_layout.add_widget(self.file_chooser)

        self.separator_button = Button(text="Separate Files", size_hint_y=None, height=50, background_color=(0, 0.7, 0.3, 1), color=(1, 1, 1, 1), font_size=20)  # Set button color to green and font color to white
        self.separator_button.bind(on_press=self.separate_files)
        file_layout.add_widget(self.separator_button)

        # Add file layout to main layout
        self.add_widget(file_layout)

    def separate_files(self, instance):
        folder_path = self.file_chooser.path
        print("Selected Folder:", folder_path)

        if not folder_path:
            print("Please select a folder first.")
            return
        
        print("Separating files in:", folder_path)

        try:
            # Iterate through files in the selected folder
            for filename in os.listdir(folder_path):
                src_file = os.path.join(folder_path, filename)
                if os.path.isfile(src_file):
                    _, ext = os.path.splitext(filename)
                    ext = ext[1:].lower()  # Remove the dot from extension and convert to lowercase

                    # Create a directory for the file type if it doesn't exist
                    dest_dir = os.path.join(folder_path, ext)
                    os.makedirs(dest_dir, exist_ok=True)

                    # Move the file to the corresponding directory
                    shutil.move(src_file, os.path.join(dest_dir, filename))

            print("File separation completed.")

        except Exception as e:
            print("An error occurred:", str(e))

class FileSeparatorApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)  # Set window background color to black
        self.title = "ZoroSlasher"
        return FileSeparatorUI()


if __name__ == "__main__":
    FileSeparatorApp().run()

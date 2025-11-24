import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk # You need pillow library

class SimpleDetectorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Disease Detector (Basic GUI Foundation)")
        self.geometry("600x400") # input the default size 
        self.img_label = None
        # use of call methods 
        self.create_widgets()

    def create_widgets(self):
        # 1. Title
        header_label = ttk.Label(self, text="Plant Leaf Disease Detection", font=('Arial', 18, 'bold'))
        header_label.pack(pady=20)
        # 2. Input
        upload_button = ttk.Button(self, text="Upload Leaf Image (Input)", command=self.upload_action)
        upload_button.pack(pady=10)
        # 3. Result 
        self.result_label = ttk.Label(self, text="Detection Result: Awaiting Input...", font=('Arial', 12))
        self.result_label.pack(pady=10)
        self.cure_text = tk.Text(self, height=8, width=60, state=tk.DISABLED)
        self.cure_text.pack(pady=10)

    def upload_action(self):
        # to select an image 
        file_path = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            # Main Source starts from here 
            print(f"File selected: {file_path}")
            # Place where we can dedect
            self.run_detection_and_cure(file_path)
            self.display_image(file_path)

    def run_detection_and_cure(self, image_path):
        # Used for detecting the names 
        detected_disease = "Example Disease (e.g., Apple Scab)" 
        cure_recommendation = "Example Cure: Apply copper fungicide and prune affected leaves."
        # Update the results 
        self.result_label.config(text=f"Disease Detected: {detected_disease}")
        self.cure_text.config(state=tk.NORMAL)
        self.cure_text.delete(1.0, tk.END)
        self.cure_text.insert(tk.END, f"Cure/Prevention:\n{cure_recommendation}")
        self.cure_text.config(state=tk.DISABLED)
    def display_image(self, file_path):
        # Simple image display 
        try:
            # Load the image 
            img = Image.open(file_path)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            if self.img_label:
                self.img_label.destroy() # Remove previous image
            self.img_label = tk.Label(self, image=photo)
            self.img_label.image = photo 
            self.img_label.pack(pady=5)
        except Exception as e:
             # Error Correction 
            print(f"Error loading image for display: {e}")

if __name__ == "__main__":
    app = SimpleDetectorGUI()
    app.mainloop()
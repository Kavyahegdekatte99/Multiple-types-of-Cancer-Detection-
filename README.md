# Multiple Types of Cancer Classification Using CT/MRI Images

This project presents a web-based model for classifying multiple types of cancer from CT and MRI images. It utilizes deep learning techniques to detect and classify tumors across five major types: **lung, brain, breast, oral, and kidney** cancers.

---

##  Project Workflow

1. **Input Data**  
   The system uses a Multi Disease CT/MRI Cancer Dataset. Input images are accepted in `.jpg` or `.png` format for the following cancer types:
   - Lung
   - Brain
   - Breast
   - Oral
   - Kidney

2. **Preprocessing**  
   - Image Resizing  
   - Noise Removal  
   - Histogram Equalization  
   - Grayscale Conversion  

3. **Segmentation**  
   - **Existing Method**: Threshold-based Segmentation  
   - **Proposed Method**: U-Net based Segmentation

4. **Data Splitting**  
   - 80% Training Data  
   - 20% Testing Data

5. **Classification Models**
   - **Existing Models**:  
     - DenseNet121  
     - VGG16  
   - **Proposed Model**:  
     - Hybrid of DenseNet121 and VGG19  

6. **Prediction Output**  
   The system classifies whether the image contains a tumor or not, and if a tumor is present, it predicts the type of cancer.

7. **Performance Metrics**
   - PSNR
   - SSIM
   - MSE & MAE
   - Accuracy
   - Precision
   - Recall
   - ROC Curve
   - Confusion Matrix
   - Error Rate
   - Classification Report

---

##  Technologies Used

- **Language**: Python  
- **Front End**: Flask, HTML, CSS  
- **Back End**: Anaconda Navigator (Spyder IDE)  
- **Libraries**: TensorFlow, Keras, OpenCV, NumPy, Matplotlib, Scikit-learn

---

##  Not a Real-Time Project

This project does **not** use a camera for real-time input. All inputs are taken as static images from the dataset.

---

##  Requesting Large Files

Due to GitHub file size restrictions, the following large files are **not included** in this repository:

- `Dataset.zip` (1.1 GB)
- `brainmodel.h5`
- `lungmodel.h5`
- `kidneymodel.h5`
- `breastmodel.h5`
- `oralmodel.h5`

To request access, please contact:

 **Email**: kavyahegdekatte@gmailcom

You will receive the dataset and model files.

---

## 🛠️ How to Use After Downloading Files

1. Place `Dataset.zip` in the project root directory and extract it.
2. Move all `.h5` files to the appropriate models directory (e.g., `models/`).
3. Update the Flask app routes to correctly load each `.h5` model using `load_model()` from Keras.

```python
from tensorflow.keras.models import load_model
model = load_model('models/brainmodel.h5')


Running the Application
# Step 1: Clone the repo
# Step 2: Navigate to project directory
# Step 3: Create a virtual environment (optional but recommended)
# Step 4: Install required libraries
# Step 5: Run the Flask app




